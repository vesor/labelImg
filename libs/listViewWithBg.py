from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ListViewWithBg(QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.emptyBgColor = None
        self.emptyText = None

    # def setEmptyBgColor(self, color):
    #     self.emptyBgColor = color
    #     self.update()

    def setEmptyText(self, text):
        self.emptyText = text
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.count() == 0 and self.emptyText:
            painter = QPainter(self.viewport())
            painter.save()
            col = self.palette().color(QPalette.Foreground)
            painter.setPen(col)
            fm = self.fontMetrics()
            elided_text = fm.elidedText(
                self.emptyText, Qt.ElideRight, self.viewport().width()
            )
            painter.drawText(self.viewport().rect(), Qt.AlignCenter, elided_text)

            bgcolor = self.palette().color(QPalette.Button)
            painter.setPen(bgcolor)

            painter.restore()
