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
from threading import Thread

    
class vidFeed(QThread):
   ImgUpdate = pyqtSignal(QImage)
   def __init__(self):      
        # super(CameraThread,self).__init__()
        QThread.__init__(self, parent=None)

   def run(self):
        capture= cv2.VideoCapture(0)
        while True:
            ret,frame =capture.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                Flip = cv2.flip(Image,1)
                QtFormat = QImage(Flip.data,Flip.shape[1],Flip.shape[0],QImage.Format_RGB888)
                out =  QtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImgUpdate.emit(out)


class dispXY(QThread): 

    speak_x=pyqtSignal(str)
    speak_y=pyqtSignal(str)
    speak_z = pyqtSignal(str)
    def __init__(self):
        # super(CameraThread,self).__init__()
        QThread.__init__(self, parent=None)

    def run(self):
        while True:
            x = str(random.randint(1,1000)) 
            self.speak_x.emit(x)
            y = str(random.randint(1,1000)) 
            self.speak_y.emit(y)  
            z = str(random.randint(1,1000))
            self.speak_z.emit(z)
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
    
        self.zcord = QtWidgets.QTextEdit(self.centralwidget)
        self.zcord.move(10,93)
        self.zcord.resize(280,40)
        self.zcord.setReadOnly(True)
    
        self.ycord = QtWidgets.QTextEdit(self.centralwidget)
        self.ycord.move(10,51)
        self.ycord.resize(280,40)
        self.ycord.setReadOnly(True)

        self.button=QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(100, 400, 141, 41))
        self.button.clicked.connect(self.on_click)
        self.button.setText("Click")
        
        Window.setCentralWidget(self.centralwidget)  
        self.initUI()
        QtCore.QMetaObject.connectSlotsByName(Window)

    def on_click(self):
        self.textbox.setText("Button Pressed")    
   
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.CameraWindow.setPixmap(QPixmap.fromImage(image))
    
    pyqtSlot(str)
    def setX(self,x):        
        self.xcord.setText(x)
    pyqtSlot(str)
    def setY(self,y):
        self.ycord.setText(y)
    pyqtSlot
    def setZ(self,z):
        self.zcord.setText(z)
    def initUI(self):
        self.th =vidFeed()
        self.th.ImgUpdate.connect(self.setImage)
        self.th.start()
        self.th1=dispXY()
        self.th1.speak_x.connect(self.setX)
        self.th1.speak_y.connect(self.setY)
        self.th1.speak_z.connect(self.setZ)
        self.th1.start()
         
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainWindow()
    ui.uiSetup(Window)
    Window.show()
    app.exec_()  
