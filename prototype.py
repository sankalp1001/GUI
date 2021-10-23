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
#from threading import Thread
import threading
    
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



class dispXY():         
    def genX(): 
        while True:
            x = str(random.randint(1,1000)) 
            #mainWindow.xcord.setText(x)  
            sleep(1)
            return str(x)
    def genY():
        while True:    
            y = str(random.randint(1,1000)) 
            # mainWindow.ycord.setText(y)   
            sleep(1)
            return str(y)
 
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
        # self.xcord.setText(str (random.randint(1,100)))
    
        self.ycord = QtWidgets.QTextEdit(self.centralwidget)
        self.ycord.move(10,51)
        self.ycord.resize(280,40)
        self.ycord.setReadOnly(True)
        # self.ycord.setText(str(random.randint(1,100)))

        self.button=QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(100, 400, 141, 41))
        self.button.clicked.connect(self.on_click)
        self.button.setText("Click")
        
        Window.setCentralWidget(self.centralwidget)  
        self.initUI()
        QtCore.QMetaObject.connectSlotsByName(Window)
        #self.setXY()
    def on_click(self):
        self.textbox.setText("Button Pressed")    
   
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.CameraWindow.setPixmap(QPixmap.fromImage(image))
    
    def setXY(self):
        if (dispXY.genX() or dispXY.genY):
            self.xcord.setText(dispXY.genX())
            self.ycord.setText(dispXY.genY())
            #print(x,y)
            #sleep(1)
    def initUI(self):
        th =vidFeed(self)
        th.ImgUpdate.connect(self.setImage)
        th.start()
        th1 = threading.Thread(target=self.setXY())
        #th1.start()
        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainWindow()
    ui.uiSetup(Window)
    Window.show()
    app.exec_()  
    
