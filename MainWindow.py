# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QStatusBar, QScrollArea, QDialog,QProgressBar
from PyQt5.QtCore import QRect, Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys
from os.path import join, abspath

default_width = 800
default_height = 600

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)
     
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(default_width, default_height)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.img_qlabel = QLabel(self.centralwidget)
        self.img_qlabel.x_, self.img_qlabel.y_, self.img_qlabel.width_, self.img_qlabel.height_ = 50, 50, 345, 500
        self.img_qlabel.setGeometry(QRect(self.img_qlabel.x_, self.img_qlabel.y_, self.img_qlabel.width_, self.img_qlabel.height_))
        self.img_qlabel.setStyleSheet("QLabel{color: gray;border: 1px solid gray}")
        self.img_qlabel.setAlignment(Qt.AlignLeading|Qt.AlignCenter|Qt.AlignCenter)
        self.img_qlabel.setObjectName("img_qlabel")
        self.img_qlabel.setFont(QFont("Roman times",12,QFont.Bold))
        
        self.text_qlabel = QLabel(self.centralwidget)
        self.text_qlabel.x_, self.text_qlabel.y_, self.text_qlabel.width_, self.text_qlabel.height_ = 0, 0, 800, 190
        self.text_qlabel.setGeometry(QRect(self.text_qlabel.x_, self.text_qlabel.y_, self.text_qlabel.width_, self.text_qlabel.height_))
        self.text_qlabel.setStyleSheet("background: white; color: rgb(121, 121, 121)")
        self.text_qlabel.setObjectName("text_qlabel")
        self.text_qlabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.text_qlabel.setFont(QFont("Roman times",12,QFont.Bold))
        
        self.scroll = QScrollArea(self.centralwidget)
        self.scroll.x_, self.scroll.y_, self.scroll.width_, self.scroll.height_ = 440, 20, 350, 190
        self.scroll.setGeometry(QRect(self.scroll.x_, self.scroll.y_, self.scroll.width_, self.scroll.height_))
        self.scroll.setWidget(self.text_qlabel)

        self.pathButton = QPushButton(self.centralwidget)
        self.pathButton.x_, self.pathButton.y_, self.pathButton.width_, self.pathButton.height_ = 450, 325, 331, 75
        self.pathButton.setGeometry(QRect(self.pathButton.x_, self.pathButton.y_, self.pathButton.width_, self.pathButton.height_))
        self.pathButton.setObjectName("pathButton")
        self.pathButton.setIcon(QIcon(QPixmap(resource_path('folder.png'))))
        self.pathButton.setIconSize(QSize(40, 40))   
        self.pathButton.setFont(QFont("Roman times",12,QFont.Bold))
        
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.x_, self.prevButton.y_, self.prevButton.width_, self.prevButton.height_ = 450, 415, 331, 75
        self.prevButton.setGeometry(QRect(self.prevButton.x_, self.prevButton.y_, self.prevButton.width_, self.prevButton.height_))
        self.prevButton.setObjectName("prevButton")
        self.prevButton.setIcon(QIcon(QPixmap(resource_path('back.png'))))
        self.prevButton.setIconSize(QSize(40, 40))   
        self.prevButton.setFont(QFont("Roman times",12,QFont.Bold))
        
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.x_, self.saveButton.y_, self.saveButton.width_, self.saveButton.height_ = 450, 505, 331, 75
        self.saveButton.setGeometry(QRect(self.saveButton.x_, self.saveButton.y_, self.saveButton.width_, self.saveButton.height_))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setIcon(QIcon(QPixmap(resource_path('download.png'))))
        self.saveButton.setIconSize(QSize(40, 40))
        self.saveButton.setFont(QFont("Roman times",12,QFont.Bold))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Classification"))
        self.img_qlabel.setText(_translate("MainWindow", "Image Display"))
        self.text_qlabel.setText(_translate("MainWindow", " Please select a folder"))
        self.pathButton.setText(_translate("MainWindow", "Open Video"))
        self.prevButton.setText(_translate("MainWindow", "Previous"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

class progressWindow(QDialog):
    def __init__(self,bar_len,title):
        super().__init__()
        self.bar_len = bar_len
        self.initUI()
        self.setWindowTitle(title)
        
    def initUI(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(self.bar_len)
        self.show()
        
    def set_progress_value(self,value):
        self.progress.setValue(value)
        
        
        