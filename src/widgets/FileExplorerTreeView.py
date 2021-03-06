from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeView


class FileExplorerTreeView(QTreeView):
    def __init__(self, parent=None):
        super(FileExplorerTreeView, self).__init__(parent)

        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header().setVisible(True)
