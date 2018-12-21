import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
 
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('random.ui',self)
        self.needrand.clicked.connect(self.run)
 
    def run(self):
        self.res.setText("OK")
 
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())