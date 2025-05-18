#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import sys
import os
# importing my modules 
# ?see at ./Modules and ./Data and ./Docs;
from Modules.modules import *
from Modules.SettingsGUI import *
from Data import Cache, Logs, UserData
from Docs import Fonts, Pics, HTML


class WebBrowser(QMainWindow):
    def __init__(self):
        global directory
        directory = os.path.dirname(os.path.realpath(sys.argv[0]))

        with open(f"{directory}/Data/UserData/Data.json", "r") as Data:
            UserData_dict: dict = json.load(Data)

        global searchEngineName
        searchEngineName = UserData_dict['UserSettings']['SearchEngine']

        global HomePage
        HomePage = UserData_dict['UserSettings']['Customisation']['HomePage']

        check_first_time_user(directory)

        super().__init__()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl.fromLocalFile(f"{directory}{HomePage}"))
        # ! this feature is still in developpement
        # self.browser.setPage(CustomWebEngineErrorPage(self.browser))

        self.setWindowTitle("Camaleont WebBrowser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.stacked_widget = QStackedWidget()
        self.browser_widget = QWidget()

        browser_layout = QVBoxLayout()
        browser_layout.addLayout(self.horizontal)
        self.scroll_area = SmoothScrollArea(self.browser)
        browser_layout.addWidget(self.scroll_area)
        self.browser_widget.setLayout(browser_layout)   

        self.stacked_widget.addWidget(self.browser_widget)       # index 0
        self.settings_menu = SettingsMenu()                      # index 1
        self.settings_menu.BackBtn.clicked.connect(self.goto_browser)
        self.stacked_widget.addWidget(self.settings_menu)

        self.setCentralWidget(self.stacked_widget)

        self.URLBar = QTextEdit()
        self.URLBar.setMaximumHeight(30)
        self.URLBar.setMinimumWidth(250)
        self.URLBar.setPlaceholderText(f"Search the Web with {searchEngineName}")

        self.NavBtn = QPushButton('', self)
        self.NavBtn.setIcon(QIcon(f'{directory}/Docs/icons/search.png'))
        self.NavBtn.setMaximumHeight(30)
        self.NavBtn.setMinimumWidth(30)

        self.BackBtn = QPushButton('', self)
        self.BackBtn.setIcon(QIcon(f'{directory}/Docs/icons/undo.png'))
        self.BackBtn.setMaximumHeight(30)
        self.BackBtn.setMaximumWidth(30)

        self.ForwardBtn = QPushButton('', self)
        self.ForwardBtn.setIcon(QIcon(f'{directory}/Docs/icons/redo.png'))
        self.ForwardBtn.setMaximumHeight(30)
        self.ForwardBtn.setMaximumWidth(30)

        self.ReloadBtn = QPushButton('', self)
        self.ReloadBtn.setIcon(QIcon(f'{directory}/Docs/icons/rotate-right.png'))
        self.ReloadBtn.setMaximumHeight(30)
        self.ReloadBtn.setMaximumWidth(30)

        self.delBtn = QPushButton('', self)
        self.delBtn.setIcon(QIcon(f'{directory}/Docs/icons/cross.png'))
        self.delBtn.setMaximumHeight(30)
        self.delBtn.setMaximumWidth(30)

        self.HomeBtn = QPushButton('', self)
        self.HomeBtn.setIcon(QIcon(f'{directory}/Docs/icons/home.png'))
        self.HomeBtn.setMaximumHeight(30)
        self.HomeBtn.setMaximumWidth(30)

        self.SettingsBtn = QPushButton('', self)
        self.SettingsBtn.setIcon(QIcon(f'{directory}/Docs/icons/settings.png'))
        self.SettingsBtn.setMaximumHeight(30)
        self.SettingsBtn.setMaximumWidth(30)

        self.horizontal.addWidget(self.BackBtn)
        self.horizontal.addWidget(self.ForwardBtn)
        self.horizontal.addWidget(self.ReloadBtn)
        self.horizontal.addWidget(self.HomeBtn)
        self.horizontal.addWidget(self.URLBar)
        self.horizontal.addWidget(self.delBtn)
        self.horizontal.addWidget(self.NavBtn)
        self.horizontal.addWidget(self.SettingsBtn)

        self.NavBtn.clicked.connect(lambda: self.Nav(self.URLBar.toPlainText()))
        self.BackBtn.clicked.connect(self.browser.back)
        self.ForwardBtn.clicked.connect(self.browser.forward)
        self.ReloadBtn.clicked.connect(self.browser.reload)
        self.delBtn.clicked.connect(self.del_searchBar)
        self.HomeBtn.clicked.connect(self.go_home)
        self.SettingsBtn.clicked.connect(self.goto_settings)

        self.browser.urlChanged.connect(self.update_url_bar)

        HTML_file_dir: str = f"{directory}{HomePage}"
        URLBar_content: str = self.URLBar.toPlainText()

        URLBar_reseter(URLBar_content, HTML_file_dir)

    def del_searchBar(self):
        self.URLBar.setText('')

    def update_url_bar(self, qurl):
        self.URLBar.setText(qurl.toString())

    def update_nav_bar(self, url):
        self.browser.setUrl(QUrl(url))
        self.URLBar.setText(url)

    def go_home(self):
        self.browser.setUrl(QUrl(f'file://{directory}{HomePage}'))
        self.URLBar.setText('')

    def goto_settings(self):
        self.stacked_widget.setCurrentWidget(self.settings_menu)

    def goto_browser(self):
        self.stacked_widget.setCurrentWidget(self.browser_widget)

    def Nav(self, url):
        searchEngineLink = check_searchengine(searchEngineName)

        tlds = [
            '.com', '.org', '.net', '.edu', '.gov', '.mil', '.int', '.ai', '.tv', '.ly', '.me', '.co', '.ma', '.it', '.ru', '.fr', '.us' 
        ]
        urlRep = url.replace(" ", "")
        if urlRep == "":
            return
        if " " not in url:
            if url.startswith("www.") or url.startswith("http://") or url.startswith("https://") or any(url.endswith(tld) for tld in tlds):
                if not url.startswith("http"):
                    url = f"https://{url}"
                    self.update_nav_bar(url)
                if not any(url.endswith(tld) for tld in tlds):
                    url = f"{url}.com"
                    self.update_nav_bar(url)
                if not url.endswith("/"):
                    url = f"{url}/"
                    self.update_nav_bar(url)
            else:
                searchQ = url
                url = f"{searchEngineLink}{searchQ}"
                self.update_nav_bar(url)
        elif " " in url:
            searchEngine = ['gs', 'bs', 'sofs', 'ddgs', 'wks']
            lowerCase_url = url.lower()
            url = url
            if not any(lowerCase_url.startswith(searchEng) for searchEng in searchEngine):
                url = replaceSearchEngine_abreviation(url)
                searchQ = url.replace(" ", "+")
                url = f"{searchEngineLink}{searchQ}"
                self.update_nav_bar(url)
            else:
                if lowerCase_url.startswith("gs"):
                    url = replaceSearchEngine_abreviation(url)
                    searchQ = url.replace(" ", "+")
                    url = f"https://www.google.com/search?q={searchQ}"
                    self.update_nav_bar(url)
                elif lowerCase_url.startswith("bs"):
                    url = replaceSearchEngine_abreviation(url)
                    searchQ = url.replace(" ", "+")
                    url = f"https://www.bing.com/search?q={searchQ}"
                    self.update_nav_bar(url)
                elif lowerCase_url.startswith("sofs"):
                    url = replaceSearchEngine_abreviation(url)
                    searchQ = url.replace(" ", "+")
                    url = f"https://stackoverflow.com/search?q={searchQ}"
                    self.update_nav_bar(url)
                elif lowerCase_url.startswith("ddgs"):
                    url = replaceSearchEngine_abreviation(url)
                    searchQ = url.replace(" ", "+")
                    url = f"https://duckduckgo.com/?q={searchQ}"
                    self.update_nav_bar(url)
                elif lowerCase_url.startswith("wks"):
                    url = replaceSearchEngine_abreviation(url)
                    searchQ = url.replace(" ", "+")
                    url = f"https://en.wikipedia.org/wiki/Special:Search?search={searchQ}"
                    self.update_nav_bar(url)

class SmoothScrollArea(QScrollArea):
    def __init__(self, widget, *args, **kwargs):
        super(SmoothScrollArea, self).__init__(*args, **kwargs)
        self.setWidget(widget)
        self.setWidgetResizable(True)
    def wheelEvent(self, event):
        delta = event.angleDelta().y() / 8  # Number of degrees
        steps = delta / 15  # Number of steps (15 degrees per step)
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() - steps * self.verticalScrollBar().singleStep())
        event.accept()

# ! this feature is still in developpement
# class CustomWebEngineErrorPage(QWebEnginePage):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#     def acceptNavigationRequest(self, url, _type, isMainFrame):
#         if _type == QWebEnginePage.NavigationTypeReload:
#             return super().acceptNavigationRequest(url, _type, isMainFrame)

#         # Attempt to load the URL
#         self.load(url)
#         self.loadFinished.connect(lambda success: self.handle_load_finished(success, url))
#         return False

#     def handle_load_finished(self, success, url):
#         if not success:
#             # Load the custom error page
#             error_page_path = os.path.join(os.path.dirname(__file__), f'{directory}/Docs/HTML/Page_Not_Found.html')
#             self.view().setUrl(QUrl.fromLocalFile(error_page_path))
#         else:
#             self.view().setUrl(url)

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(sys.argv[0]))
    app = QApplication(sys.argv)
    with open(f"{directory}/Docs/styles.qss", "r") as file:
        qss = file.read()
    # browser = QWebEngineView()
    # browser.setPage(CustomWebEngineErrorPage(browser))
    app.setStyleSheet(qss)
    window = WebBrowser()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())




