import sys 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import cv2

class MainWindow(QWidget):
    def __init__(self):
       super(MainWindow,self).__init__()

       self.WIN = QVBoxLayout()

       self.FeedLabel = QLabel()
       self.WIN.addWidget(self.FeedLabel)

       self.worker1 = worker1()

       self.worker1.start()
       self.worker1.ImgUpdate.connect(self.ImageUpdateSlot)
       self.setLayout(self.WIN)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

class worker1(QThread):
   ImgUpdate = pyqtSignal(QImage)
   def run(self):
        self.Thread = True
        capture= cv2.VideoCapture(0)
        while self.Thread:
           ret,frame =capture.read()
           if ret:
               Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
               Flip = cv2.flip(Image,1)
               QtFormat = QImage(Flip.data,Flip.shape[1],Flip.shape[0],QImage.Format_RGB888)
               out =  QtFormat.scaled(640, 480, Qt.KeepAspectRatio)
               self.ImgUpdate.emit(out)
   def stop(self):
        self.ThreadActive = False
        self.quit()
if __name__ == "__main__":
    App= QApplication(sys.argv)
    Root =MainWindow()
    Root.show()
    sys.exit(App.exec())
