from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions4 as calcFunctions

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(False) #계산기 창을 활성화
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(20)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        if self.display.text() == 'Error!' or self.display.text() == "0error" or self.display.text() == "so many numbers" or self.display.text() == "not defind!":
            self.display.setText('')#전의 버튼 호출에서 에러가 났을 때 디스플레이를 비운다.

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                a_s = eval(self.display.text())
            except ZeroDivisionError:#0을 나누면 에러임을 알려준다.
                self.display.setText("0error")
            except NameError:#정의 되지 않은 값을 eval했을 때의 에러를 처리한다.
                self.display.setText("not defind!")
            except SyntaxError as EOFError:#문장 에러임을 알려준다.
                self.display.setText("Syntax error")
            except:
                a_s = 'Error!'
            else:
                a_s = eval(self.display.text())
                a_s = int((a_s * 10000)) / 10000 #소수 4째 자리까지 만든다.
                self.display.setText(str(a_s))

        elif key == 'C':
            self.display.clear()
        elif key == constantList[0]:
            self.display.setText(self.display.text() + '3.141592')
        elif key == constantList[1]:
            self.display.setText(self.display.text() + '3E+8')
        elif key == constantList[2]:
            self.display.setText(self.display.text() + '340')
            self.display.setText(self.display.text() + '1.5E+8')
        elif key == functionList[0]:
            n = self.display.text()
            value = calcFunctions.factorial(n)
            self.display.setText(str(value))
        elif key == functionList[1]:
            n = self.display.text()
            value = calcFunctions.decToBin(n)
            self.display.setText(str(value))
        elif key == functionList[2]:
            n = self.display.text()
            value = calcFunctions.binToDec(n)
            self.display.setText(str(value))
        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        elif key == functionList[4]:
            n = self.display.text()
            value = calcFunctions.romanToDec(n)
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)
        if(len(self.display.text()) > 19):#숫자가 너무 많으면 메세지 출력한다.
            self.display.setText("so many numbers")






if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

