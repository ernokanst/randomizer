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
        self.answer = []
        if self.neednums.isChecked():
            for i in range(self.resquant.value()):
                self.answer.append(str(random.randint(self.fromn.value(), 
                                                  self.ton.value())))
        self.res.setPlainText('\n'.join(self.answer))
 
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())