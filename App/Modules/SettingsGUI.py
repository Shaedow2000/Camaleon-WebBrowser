#!/usr/bin/env python3

from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import sys
import os

# * pages ui functions
class openAccountSection(QWidget):
    def __init__(self):
        super().__init__()

        with open(f"{directory}/Data/UserData/Data.json", "r") as Data:
            UserData_dict: dict = json.load(Data)
        
        # * account Img
        accountIcon = QPixmap(f'{directory}/Docs/Pics/user.png')
        accountIcon = accountIcon.scaled(100, 100)

        # ? account icon
        self.accountImg = QLabel('image', self)
        self.accountImg.resize(100, 100)
        self.accountImg.setPixmap(accountIcon)

        # ? account info
        users_name = UserData_dict['UserAccountInfo']['Name']
        self.name = QLabel(f"\\033[1mName:\\033[0m", self)

class openCustomisationSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('label 2'))
        layout.addWidget(QLabel('label 2'))
        layout.addWidget(QLabel('label 2'))
        layout.addWidget(QLabel('label 2'))
        self.setLayout(layout)

class openPrivacySection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('label 3'))
        self.setLayout(layout)

class openLanguageSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('label 4'))
        self.setLayout(layout)


class SettingsMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camaleont WebBrowser - Settings")
        self.setGeometry(100, 100, 500, 300)

        global directory
        directory = os.path.dirname(os.path.realpath(sys.argv[0])).replace('Modules/', '')

        # ? sidebar buttons
        self.TitleBar = QLabel('Settings', self)
        self.BackBtn = QPushButton('', self)
        self.BackBtn.setIcon(QIcon(f'{directory}/Docs/icons/cross.png'))
        self.AccountBtn = QPushButton('Account Info', self)
        self.CustomisationBtn = QPushButton('Customisation Settings', self)
        self.PrivacyBtn = QPushButton('Privacy and Protection', self)
        self.LanguageBtn = QPushButton('Language', self)

        for btn in [self.AccountBtn, self.CustomisationBtn, self.PrivacyBtn, self.LanguageBtn]:
            btn.setFixedHeight(40)
            btn.setMinimumWidth(160)
            btn.setMaximumWidth(200)

        self.BackBtn.setFixedHeight(30)
        self.BackBtn.setFixedWidth(30)

        # * Left: Sidebar
        sidebarWidget = QWidget()
        sidebarLayout = QVBoxLayout(sidebarWidget)
        sidebarLayout.setSpacing(20)
        sidebarLayout.setAlignment(Qt.AlignTop)
        sidebarLayout.addWidget(self.TitleBar)
        sidebarLayout.addSpacing(10)
        sidebarLayout.addWidget(self.AccountBtn)
        sidebarLayout.addWidget(self.CustomisationBtn)
        sidebarLayout.addWidget(self.PrivacyBtn)
        sidebarLayout.addWidget(self.LanguageBtn)
        sidebarLayout.addStretch()

        # * Adding pages to QStackedWidgets
        self.stack = QStackedWidget()
        self.AccountSection = openAccountSection()
        self.CustomisationSection = openCustomisationSection()
        self.PrivacySection = openPrivacySection()
        self.LanguageSection = openLanguageSection()
        self.stack.addWidget(self.AccountSection)
        self.stack.addWidget(self.CustomisationSection)
        self.stack.addWidget(self.PrivacySection)
        self.stack.addWidget(self.LanguageSection)

        # * buton click
        self.AccountBtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.AccountSection))
        self.CustomisationBtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.CustomisationSection))
        self.PrivacyBtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.PrivacySection))
        self.LanguageBtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.LanguageSection))

        # * Right: Stack and Back Button at top-right
        rightWidget = QWidget()
        rightLayout = QVBoxLayout(rightWidget)
        rightLayout.setContentsMargins(0, 0, 0, 0)

        topBar = QHBoxLayout()
        topBar.setAlignment(Qt.AlignRight)
        topBar.addWidget(self.BackBtn)
        rightLayout.addLayout(topBar)
        rightLayout.addWidget(self.stack)

        # * Main layout
        mainWindow = QHBoxLayout()
        mainWindow.addWidget(sidebarWidget)
        mainWindow.addWidget(rightWidget)

        container = QWidget()
        container.setLayout(mainWindow)
        self.setCentralWidget(container)

