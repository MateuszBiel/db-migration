from PyQt4 import QtGui,QtCore,uic
from PyQt4.QtCore import QVariant
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QVariant

class chooseTables(QtGui.QDialog):
    chosedValue=""
    ID = ""
    currentColumn = ""
    currentRow = ""
    width = 0
    height = 0
    def __init__(self):
        super(chooseTables , self).__init__()
        uic.loadUi('form3.ui', self)
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.chooseData)
        self.dbTables.cellClicked.connect(self.cell_was_clicked)
        self.fillData()


    def setCurrentCell(self,column=0, row=0):
        print("called setCurrentCell")
        currentColumn = column
        currentRow = row

    def fillData(self):
        print("called fillData")
        self.width = len(connection.dbSchema)

        self.maxLen=0
        for x in connection.dbSchema:
            if self.maxLen<len(x[1].split(",")):
                self.maxLen=len(x[1].split(","))
        self.dbTables.setRowCount(self.maxLen+1)
        self.dbTables.setColumnCount(self.width )
        last_Table =""
        last_id = 0

        for data in enumerate(connection.dbSchema):
            splitedData = data[1][1].split(",")
            self.dbTables.setItem(0,data[0],QtGui.QTableWidgetItem(data[1][0]))
            for oneEntity in enumerate(splitedData):
                self.dbTables.setItem(oneEntity[0] ,data[0],QtGui.QTableWidgetItem(oneEntity[1]))

    def cell_was_clicked(self, row, column):
        print("called cell_was_clicked")
        item = self.dbTables.item(row, column)
        self.ID = item.text()
        self.chosedValue.setText(self.ID)
        self.closeWindow()

    def closeWindow(self):
        self.close()

    def chooseData(self):
        return self.ID