import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from assignmentnlp import getSuggestions


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Auto Filling program')
        self.init_ui()
        self.setFixedSize(700, 700)
        self.setStyleSheet("background-color: #152238;")


    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title = QLabel('Auto Filling')
        self.title.setFont(QFont('times new roman', 100))
        self.title.setStyleSheet("color:white;")


        self.search_input = QLineEdit()
        self.search_input.setFixedSize(400, 50)
        self.search_input.installEventFilter(self)
        self.search_input.setStyleSheet("QLineEdit{color: white; font-size: 30px;}")
        self.search_input.setFixedWidth(678)
        




        self.button = QPushButton('search')
        self.button.setFixedSize(90, 25)
        self.button.setStyleSheet("background-color : #ff9a44; color: #152238;")
        self.button.setFont(QFont('times new roman', 10))

        self.button.clicked.connect(self.get_results)
        self.button.setAutoDefault(True)
        self.search_input.returnPressed.connect(self.button.click)

        self.result = QLabel('')
        self.result.setStyleSheet("color: #EFEFEF; background-color: #23395d;")
        self.result.setFont(QFont('helvetica', 30))


        self.layout.addWidget(self.title)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)

        self.setLayout(self.layout)


        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyRelease and obj is self.search_input and self.search_input.hasFocus():
            self.get_results()
        return super().eventFilter(obj, event)


    def get_results(self):
        input = self.search_input.text()
        suggestion = getSuggestions(input)
        self.result.setText(suggestion)



if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = App()
        sys.exit(app.exec_())