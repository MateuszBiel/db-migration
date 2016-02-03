from PyQt4 import QtGui,QtCore,uic

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from view.connectionWindow import *

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.tableDBChoose = QtGui.QTableWidget ()
        self.tableDBChoose.setRowCount(1)
        self.tableDBChoose.setColumnCount(5)
        self.tableDBChoose.doubleClicked.connect(lambda: self.fillData())

        self.textEdit = QtGui.QTableWidget ()
        self.textEdit.setMinimumSize(400,300)
        self.textEdit.setRowCount(5)
        self.textEdit.setColumnCount(5)
        self.textEdit.setSortingEnabled(1)

        self.layout.addWidget(self.tableDBChoose)

        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)

    def fillData(self):
        print("called fillData")
        if not (connection.dbSchema is None):
            s = chooseTables()
            s.setCurrentCell(self.tableDBChoose.currentColumn(),self.tableDBChoose.currentRow())
            s.exec_()
            dataw= s.chooseData()
            self.tableDBChoose.setItem(self.tableDBChoose.currentRow(),self.tableDBChoose.currentColumn(),QtGui.QTableWidgetItem(dataw))