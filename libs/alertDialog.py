try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from libs.lib import newIcon

BB = QDialogButtonBox


class AlertDialog(QDialog):

    def __init__(self, text="", parent=None):
        super(AlertDialog, self).__init__(parent)

        self.label = QLabel()
        self.label.setText(text)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.buttonBox = bb = BB(BB.Ok | BB.Cancel, Qt.Horizontal, self)
        bb.button(BB.Ok).setIcon(newIcon('done'))
        bb.button(BB.Cancel).setIcon(newIcon('undo'))
        bb.accepted.connect(self.accept)
        bb.rejected.connect(self.reject)
        layout.addWidget(bb)

        self.setLayout(layout)

    def popUp(self, text=''):
        self.label.setText(text)
        self.exec()

