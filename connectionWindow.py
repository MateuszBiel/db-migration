from PyQt4 import QtGui,QtCore,uic
from model.ConnectDatabase import *
import mysql.connector
class connectionWindow(QtGui.QDialog):
    def __init__(self):
        super(connectionWindow , self).__init__()
        uic.loadUi('view/form2.ui', self)
        self.cancelButton.clicked.connect(self.close)
        self.connectButton.clicked.connect(self.setConnection)

    def setConnection(self):
        print("called setConnection")
        dbHostName  = self.dbHostText.text()
        dbLogin     = self.dbLoginText.text()
        dbPassowrd  = self.dbPasswordText.text()
        dbDatabase  = self.dbNameText.text()
        connectDatabase.setDbConnection(self,dbHostName, dbLogin, dbPassowrd, dbDatabase)
        connectDatabase.getDbConnection(self)
        connectDatabase.getDataTables(self)
        self.close()