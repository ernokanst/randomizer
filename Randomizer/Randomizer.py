import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random #самое важное
import string


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('random.ui',self)
        self.needrand.clicked.connect(self.run)

    def run(self):
        self.answer = [] #формирование ответа

        if self.neednums.isChecked(): #генерация числа
            for i in range(self.resquant.value()):
                self.answer.append(str(random.randint(self.fromn.value(), 
                                                  self.ton.value())))

        elif self.needobj.isChecked(): #элемент последовательности
            for i in range(self.resquant.value()):
                if self.sequence.toPlainText() != '': #проверка
                    self.answer.append(random.choice(
                        self.sequence.toPlainText().split()))
                else: #иначе – ошибка
                    self.answer.append('Не выбраны необходимые символы')

        elif self.needpass.isChecked(): #генерация пароля
            self.whattouse = [] #что необходимо использовать в пароле
            if self.upletters.isChecked():
                self.whattouse.append('U')
            if self.lowletters.isChecked():
                self.whattouse.append('L')
            if self.numbers.isChecked():
                self.whattouse.append('N')
            if self.symbols.isChecked():
                self.whattouse.append('S')

            for i in range(self.resquant.value()):
                self.password = '' #формирование пароля
                for j in range(self.lenpass.value()):
                    if self.whattouse != []: #проверка, что параметры заданы
                        self.using = random.choice(self.whattouse)
                        if self.using == 'U':
                            self.password += random.choice(string.ascii_uppercase)
                        elif self.using == 'L':
                            self.password += random.choice(string.ascii_lowercase)
                        elif self.using == 'N':
                            self.password += random.choice(string.digits)
                        elif self.using == 'S':
                            self.password += random.choice(string.punctuation)
                    else: #иначе – вывести ошибку
                        self.password = 'Не выбраны необходимые символы'
                self.answer.append(self.password)

        self.res.setPlainText('\n'.join(self.answer)) #вывод ответа


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())