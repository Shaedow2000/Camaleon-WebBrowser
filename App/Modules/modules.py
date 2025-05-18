#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QScrollArea, QTextEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage # type: ignore
from PyQt5.QtCore import QUrl, Qt
from PyQt5 import QtCore
import json
import sys
import os

class PopUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the main window
        self.setWindowTitle('Camaleont Web-Browser first start')
        self.setMaximumHeight(350)
        self.setMaximumWidth(800)
        # Show the pop-up message box
        self.show_popup()

    def show_popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Welcome To Camaleont Web-Browser!')
        msg.setText('Hello & Welcome To The Camaleont Web-Browser.\n\tThis project is opensource and fully free of charge!\n\n-We hope you enjoy our browser, and Thank you for your support!!\n\n\tMessage from Amir Saliola, Maintainer of the project.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # def feature_in_developpement_popup(self): 
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setWindowTitle('Quick Message!')
    #     msg.setText('The Settings Menu is still in developpement, and it will be implemented in futur versions!\n\n-We hope you enjoy our browser, and Thank you for your support!!\n\n\tMessage from Amir Saliola, Maintainer of the project.')
    #     msg.setStandardButtons(QMessageBox.Ok)
    #     msg.exec_()

def URLBar_reseter(URLBar_content, HTML_file_dir):
    if URLBar_content == f"{HTML_file_dir}":
        URLBar_content.setText("")
    else:
        pass
    
def replaceSearchEngine_abreviation(url):
    if url.lower().startswith("gs") or url.lower().startswith("bs"):
        url = url[2:]
        if url.startswith(" "):
            url = url[1:]
            return url
        else:
            return url
    elif url.lower().startswith("wks"):
        url = url[3:]
        if url.startswith(" "):
            url = url[1:]
            return url
        else:
            return url
    elif url.lower().startswith("sofs") or url.lower().startswith("ddgs"):
        url = url[4:]
        if url.startswith(" "):
            url = url[1:]
            return url
        else:
            return url
    else:
        return url

def check_first_time_user(directory):
    with open(f"{directory}/Data/UserData/Data.json", "r") as Data:
        UserData_dict: dict = json.load(Data)

    firstTimeUser: str = UserData_dict["User"]["firstTimeUser"]

    if firstTimeUser == "Yes":
        mainWin = PopUpWindow()
        mainWin.show()
        mainWin.close()
        # ! updating firstTimeUser to be No;
        NotfrstTimeUser = UserData_dict["User"]["firstTimeUser"]
        NotfrstTimeUser = "No"
        UserData_dict["User"]["firstTimeUser"] = NotfrstTimeUser

        with open(f"{directory}/Data/UserData/Data.json", "w") as Data:
            json.dump(UserData_dict, Data)
    else:
        pass

def check_searchengine(jsonData_searchengine):
    if jsonData_searchengine == 'Google':
        return 'https://www.google.com/search?q='
    elif jsonData_searchengine == 'DuckDuckGo': 
        return 'https://duckduckgo.com/?q='
    elif jsonData_searchengine == 'Bing':
        return 'https://www.bing.com/search?q='
    elif jsonData_searchengine == 'StackOverflow':
        return 'https://stackoverflow.com/search?q='
    elif jsonData_searchengine == 'Wikipedia':
        return 'https://en.wikipedia.org/wiki/Special:Search?search='
    else:
        print('No search engine name in json file.\nDefaulting to "DuckDuckgo search engine"')
        return 'https://duckduckgo.com/?q='

