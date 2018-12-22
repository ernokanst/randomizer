import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random
 
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('random.ui',self)
        self.needrand.clicked.connect(self.run)
 
    def run(self):
        if self.neednums.isChecked():
            for i in range(int(self.resquant.text())):
                self.res.setText(str(random.randInt(int(self.fromn.text()),
                                                    int(self.ton.text()))) + 
                                 '\n')
 
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())