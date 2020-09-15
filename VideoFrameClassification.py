# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QEvent
from sys import argv, exit
from PIL.Image import open as imopen
from PIL.Image import fromarray as imfromarray
from win32gui import GetWindowText, GetForegroundWindow
from qimage2ndarray import array2qimage
from shutil import move
from os import makedirs, chdir, getcwd
from os import path as ospath
from utils import resize_widget, resize_font, resize_icon
from MainWindow import resource_path, Ui_MainWindow, progressWindow
from glob import glob
from cv2 import VideoCapture
import json
from collections import defaultdict

keymap = {}
for key, value in vars(Qt).items():
    if isinstance(value, Qt.Key):
        temp = key.partition('_')[2]
        if len(temp)==1 or temp=='Backspace':
            keymap[value] = temp 
            
desired_window = "Quick Classification"



class mainProgram(QMainWindow, Ui_MainWindow):
    keyPressed = pyqtSignal(QEvent)
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)
        self.pathButton.clicked.connect(self.select_path)
        self.prevButton.clicked.connect(self.prev_image)
        self.saveButton.clicked.connect(self.save)
        self.keyPressed.connect(self.on_key)
        self.setStyleSheet("QMessageBox { messagebox-text-interaction-flags: 5; }")
        self.path_click=False
        self.video_path = 'None'
        
    # If user resize mainwindow, then keep the button position    
    def resizeEvent(self, event):
        for i in [self.img_qlabel, self.text_qlabel, self.scroll, self.pathButton, self.prevButton, self.saveButton]:
            resize_widget(i, self.rect().width(), self.rect().height())
        for i in [self.img_qlabel, self.text_qlabel, self.pathButton, self.prevButton, self.saveButton]:
            resize_font(i, self.rect().width(), self.rect().height())
        for i in [self.pathButton, self.prevButton, self.saveButton]:
            resize_icon(i, self.rect().width(), self.rect().height())
        
        try:
            frame = self.frame_info[self.current_frame][0]
            self.update_image(frame)
        except Exception as e:
            print("Resize Error")
            print(e)
            pass
            
        QMainWindow.resizeEvent(self, event)
               

    # this function is for saveing current classification progress
    def save(self):
        print("存檔中...")
        if not self.path_click:
            QMessageBox.information(self, "Warning", "Please select a video first!")
        # elif len(self.new_class)==0:
        #     QMessageBox.information(self, "Warning", "No classes need to be saved!")
        else:
            output = [str(k)+" "+str(self.frame_info[k][1])+"\n" for k in range(self.current_frame)]
            output[-1] = output[-1].replace("\n","")
            basename = ospath.basename(self.video_path)
            folder = ospath.dirname(self.video_path)
            labelFileName = basename.split(".")[0]+".txt"
            with open(ospath.join(folder,labelFileName),"w") as f:
                f.writelines(output)
            if self.to_the_end:
                QMessageBox.information(self, "Warning", "Job Done!")
                print(f"\n Current frame : {self.current_frame}")
            else:
                QMessageBox.information(self, "Warning", "Label saved!")
            
    # this function is for select image folder which is wait to be classified
    def select_path(self):
        print("選擇影片路徑")
        path = QFileDialog.getOpenFileName()[0]
        self.to_the_end = False
        if len(path) == 0:
            QMessageBox.information(self,"Warning", "Please select a valid path!")
        else:
            self.path_click = True
            self.video_path = path
            self.current_frame = 0
            self.frame_info = defaultdict(list)
            self.cap = VideoCapture(self.video_path)
            ret, frame = self.cap.read()
            if ret:
                self.update_image(frame)
                self.frame_info[self.current_frame] = [frame, None]
    # this function is for update current window to the next image after user click classification button
    def update_image(self, bbox):
        qImg = array2qimage(bbox[...,::-1])
        pixmap = QPixmap(qImg)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(self.img_qlabel.width(), self.img_qlabel.height(), Qt.KeepAspectRatio)
            self.img_qlabel.setPixmap(pixmap)
            text = ""
            text += f" File name : {self.video_path}"
            text += f"\n Current frame : {self.current_frame}"
            if self.current_frame >= 1:
                text += f"\n Previous frame ({self.current_frame-1}) class : {self.frame_info[self.current_frame-1][1]}"
            self.text_qlabel.setText(text)
    
    # when user press any keys will trigger this function        
    def keyPressEvent(self, event):
        super(mainProgram, self).keyPressEvent(event)
        self.keyPressed.emit(event)
        print(f"\n Current frame : {self.current_frame}")
        
    # when user press any keys will trigger this function           
    def on_key(self, event):
        current_window = GetWindowText(GetForegroundWindow())
        if current_window==desired_window:
            if event.key() in keymap:
                if keymap[event.key()]=='Backspace':
                    self.prev_image()
                else:
                    self.frame_info[self.current_frame][1] = keymap[event.key()]
                    # To the next frame
                    self.current_frame += 1
                    if self.current_frame in self.frame_info:
                        frame = self.frame_info[self.current_frame][0]
                        self.update_image(frame)
                    else:
                        # If to the end, save and close program
                        ret, frame = self.cap.read()
                        if not ret:
                            self.to_the_end = True
                            self.current_frame -= 1
                            self.save()
                        else:
                            self.update_image(frame)
                            self.frame_info[self.current_frame] = [frame, None]
            else:
                QMessageBox.information(self,"Warning", "Can not press special keys!")
                
    # when user click previous button or 'Backspace' on keyboard will trigger this function to go back to previous image
    def prev_image(self):
        print("返回上一張圖片")
        if self.current_frame==0:
            QMessageBox.information(self,"Warning", "No previous image!")
        else:
            self.current_frame -= 1
            
            frame = self.frame_info[self.current_frame][0]
            self.update_image(frame)
        
        
if __name__ == '__main__':  
    app = QApplication(argv)
    app.setWindowIcon(QIcon(resource_path('main.ico')))
    main = mainProgram()
    main.show()
    exit(app.exec_())
    
 


