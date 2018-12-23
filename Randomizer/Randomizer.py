import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random
import string


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

        elif self.needobj.isChecked():
            for i in range(self.resquant.value()):
                self.answer.append(random.choice(
                    self.sequence.toPlainText().split()))

        elif self.needpass.isChecked():
            self.whattouse = []
            if self.upletters.isChecked():
                self.whattouse.append('U')
            if self.lowletters.isChecked():
                self.whattouse.append('L')
            if self.numbers.isChecked():
                self.whattouse.append('N')
            if self.symbols.isChecked():
                self.whattouse.append('S')

            for i in range(self.resquant.value()):
                self.password = ''
                for j in range(self.lenpass.value()):
                    if self.whattouse != []:
                        self.using = random.choice(self.whattouse)
                        if self.using == 'U':
                            self.password += random.choice(string.ascii_uppercase)
                        elif self.using == 'L':
                            self.password += random.choice(string.ascii_lowercase)
                        elif self.using == 'N':
                            self.password += random.choice(string.digits)
                        elif self.using == 'S':
                            self.password += random.choice(string.punctuation)
                    else:
                        self.password = 'Не выбраны необходимые символы'
                self.answer.append(self.password)

        self.res.setPlainText('\n'.join(self.answer))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())