import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.dr = False
        self.pushButton.clicked.connect(self.on_click)

    def paintEvent(self, e):
        super().paintEvent(e)
        if self.dr:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        pos = [random.randint(0, 300) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)
        pos = [random.randint(100, 300) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)
        pos = [random.randint(200, 300) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)

    def on_click(self):
        self.pushButton.setVisible(False)
        self.dr = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
