from PySide2 import QtCore, QtGui, QtWidgets
from random import randint as random
import sys

class UI_window(object):
    def setup(self, window):
        window.setObjectName("window")
        window.resize(182, 280)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(30, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.enterButton.setFont(font)
        self.enterButton.setAutoDefault(False)
        self.enterButton.setDefault(False)
        self.enterButton.setFlat(False)
        self.enterButton.setObjectName("enterButton")
        self.inputLine = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLine.setGeometry(QtCore.QRect(40, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.inputLine.setFont(font)
        self.inputLine.setObjectName("inputLine")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(40, 145, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.scoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.scoreLabel.setGeometry(QtCore.QRect(10, 210, 165, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setObjectName("scoreLabel")
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(window)
        window.setWindowTitle(QtWidgets.QApplication.translate("window", "Guess number", None, -1))
        self.enterButton.setText(QtWidgets.QApplication.translate("window", "Enter", None, -1))
        self.resultLabel.setText(QtWidgets.QApplication.translate("window", "N/A", None, -1))
        self.scoreLabel.setText(QtWidgets.QApplication.translate("window", "Score: " + str(score), None, -1))

score = 0

def play():
    global score
    inputNumber = UI.inputLine.text()
    UI.inputLine.setText("")
    if inputNumber != "":
        try:
            inputNumber = int(inputNumber)
        except:
            UI.resultLabel.setText(":(")
            return
        if inputNumber > 10 or inputNumber < 0:
            UI.resultLabel.setText(":(")
            return
        guessedNumber = random(0,10)
        UI.resultLabel.setText(str(guessedNumber))
        if inputNumber == guessedNumber:
            score += 1
        UI.scoreLabel.setText("Score: " + str(score))
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
UI = UI_window()
UI.setup(window)
UI.enterButton.clicked.connect(play)
window.show()
sys.exit(app.exec_())