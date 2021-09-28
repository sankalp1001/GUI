import PyQt5 
from PyQt5 import QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
import sys

class window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window")
    self.setGeometry(700,450,500,500)
    self.label=QtWidgets.QLabel(self)
    self.label.setText("Button not pressed yet")
    self.UpdateSize()
    self.label.move(150,50)
    self.pushButton()
    self.show()
  def pushButton(self):
      button=QPushButton("Click",self)
      button.setGeometry(200,250,100,30)
      button.clicked.connect(self.clicked)
  def clicked(self):
     self.label.setText("Button pressed")
     self.UpdateSize()
  def UpdateSize(self):
      self.label.adjustSize()   

App = QApplication(sys.argv)
  
window = window()
  
sys.exit(App.exec())
