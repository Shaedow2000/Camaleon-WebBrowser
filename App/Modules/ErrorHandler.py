#!/usr/bin/env python3

# ! feature comming soon

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QScrollArea, QTextEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5 import QtCore
import sys
import os

try:
    pass
except Exception as error:
    directory: str = os.path.dirname(os.path.realpath(sys.argv[0]))

    log_file_dir: str = f"{directory}/Data/Logs/Errors/error-log-file.txt"

    numb_error_file_dir: str = f"{directory}/Data/Cache/error_number.txt"

    error_number_file = open(numb_error_file_dir, "r")
    error_number: int = int(error_number_file.readline())
    error_number_file = open(numb_error_file_dir, "w")
    error_number_write: int = error_number + 1
    error_number_file.write(f"{error_number_write}")
    error_number_file.close()

    log_file = open(log_file_dir, "a")
    error_str = str(error)
    log_file.write(f"Error number {error_number} at directory: {directory}/main.py:\n\t{error_str}\n\n")
    log_file.close()
