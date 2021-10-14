from time import sleep
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
import cv2
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, Qt, pyqtSignal,pyqtSlot
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
import random
from threading import *

class vidFeed(QThread):
   ImgUpdate = pyqtSignal(QImage)
   def run(self):
        capture= cv2.VideoCapture(2)
        while True:
           ret,frame =capture.read()
           if ret:
               Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
               Flip = cv2.flip(Image,1)
               QtFormat = QImage(Flip.data,Flip.shape[1],Flip.shape[0],QImage.Format_RGB888)
               out =  QtFormat.scaled(640, 480, Qt.KeepAspectRatio)
               self.ImgUpdate.emit(out)


class dispXY(QThread):
    def genX(): 
        while True: 
            x = random.randint(1,1000)    
            sleep(1)
            return str(x)

    def genY():
        while True: 
            y = random.randint(1,1000)    
            sleep(1)
            return str(y)  
    
    def click_x(self):
        while True:
            #print("in x while")
            y = self.genY()
            self.xcord.setText(y)
            sleep(1)
    def click_y(self):
        while True:
            y = self.genX()
            self.ycord.setText(y)
            sleep(1)    
 
class mainWindow(QWidget):
   

    def uiSetup(self,Window):
        Window.setObjectName("MainWindow")
        Window.resize(800,640)

        self.centralwidget = QtWidgets.QWidget(Window)


        self.CameraWindow = QtWidgets.QLabel(self.centralwidget)
        self.CameraWindow.setGeometry(QtCore.QRect(300, 40, 271, 311))
        self.CameraWindow.resize(480,480)

        self.textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.textbox.move(10,300)
        self.textbox.resize(280,40)
        self.textbox.setText("Button not pressed yet")
        self.textbox.setReadOnly(True)

        self.xcord = QtWidgets.QTextEdit(self.centralwidget)
        self.xcord.move(10,10)
        self.xcord.resize(280,40)
        self.xcord.setReadOnly(True)
        #self.xcord.setText(str(dispXY.genY()))
    
        self.ycord = QtWidgets.QTextEdit(self.centralwidget)
        self.ycord.move(10,51)
        self.ycord.resize(280,40)
        self.ycord.setReadOnly(True)
        #self.ycord.setText(str(dispXY.genY()))

        self.button=QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(100, 400, 141, 41))
        self.button.clicked.connect(self.on_click)
        self.button.setText("Click")

        '''self.xBut=QtWidgets.QPushButton(self.centralwidget)
        self.xBut.setGeometry(QtCore.QRect(152, 250, 100, 21))
        self.xBut.clicked.connect(self.click_x)
        self.xBut.setText("y")

        self.yBut=QtWidgets.QPushButton(self.centralwidget)
        self.yBut.setGeometry(QtCore.QRect(10, 250, 100, 21))
        self.yBut.clicked.connect(self.click_y)
        self.yBut.setText("x")'''

        Window.setCentralWidget(self.centralwidget)  
        self.initUI(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        self.setXY(dispXY.genX(),dispXY.genY())
        #self.click_y()

        #self.xyThre()
    def on_click(self):
        self.textbox.setText("Button Pressed")    
   
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.CameraWindow.setPixmap(QPixmap.fromImage(image))
    #def setXY(sef):
    def setXY(self,x,y):
        while True:
            self.xcord.setText(x)
            self.ycord.setText(y) 
            sleep(1)
    def initUI(self,mainWindow):
        th =vidFeed(self)
        th.ImgUpdate.connect(self.setImage)
        th.start()
        ''' th1 = dispXY(self)
        th1.genX()
        th1 = dispXY(self)
        th1.start()'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainWindow()
    ui.uiSetup(Window)
    Window.show()
    sys.exit(app.exec_())   
