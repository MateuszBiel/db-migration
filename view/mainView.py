import sys
from PyQt4 import QtGui,QtCore,uic
from PyQt4.QtCore import QVariant
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QVariant
import mysql.connector
import csv
import json
import itertools
import datetime
from collections import OrderedDict

class connectDatabase():
    _instances = []
    _constarinTable= []
    dbHostName = ""
    dbLogin = ""
    dbPassowrd = ""
    dbDatabase =""
    dbSchema= []
    endArray= []
    _dbData = []
    _insertSchemaArray = []

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(connectDatabase, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def fillTAble(self):
        print("called fillTAble")
        for row in connection._constarinTable:
            tmpArray=[]
            tmpArray.append(row[0])
            tmpArray.append(row[2])
            self.endArray.append(tmpArray)
        for row in enumerate(self.endArray):
            self.findID(row[1][0])
        self._instances=list(OrderedDict.fromkeys(self._instances))


    def createInsertString(self):
        print("called createInsertString")
        print(self._dbData)
        print(self._instances)
        print(self._constarinTable)
        _tmpData = []

        insertArray = []
        insertArraySchema = []
        valueList=""
        insertString=""

        for x in self._instances:
            for y in self._constarinTable:
                if x is y[0]:
                    insertArraySchema.append(y)

        for y in self._dbData:
            insertString2=""
            for x in insertArraySchema:
                insertString=""
                insertValues=""
                for z in y:
                    # print(z[0]+ "== "+x[1])
                    if z[0] in x[1]:
                        # print("weszlo")
                        insertValues = insertValues+z[0]+"',"
                        insertString=insertString+z[1]+"',"

                insertValues=insertValues[0:-2]
                insertString=insertString[0:-2]
                insertString2 = "INSERT INTO "+x[0]+" ('"+insertValues+"') VALUES ('"+insertString+"')"
                insertArray.append(insertString2)
        self._insertSchemaArray = insertArray
        today = datetime.date.today()
        with open('insertData'+today.strftime('%d-%b-%Y')+'_insertString.txt', 'w') as outfile:
            json.dump(self._insertSchemaArray, outfile)
        # for x in insertArray:
        #     print(x)


    def findID(self, id):
        print("called findID")
        found=""
        newArray = []
        for row in self.endArray:

            if row[0] is id:
                # newArray.append(row[0])
                self.findID(row[1])
            else:

                self._instances.append(id)
        self._instances=list(OrderedDict.fromkeys(self._instances))
        self.createInsertString()


    def filterTable(self):
        print("called filterTable")
        newArray = []
        for row in enumerate(self.endArray):

            actualRow = row[1]
            isEmpty =0


            for row2 in self.endArray:

                if (row2[1] is not row[1]) and (  ):
                    isEmpty =1
                else:
                    isEmpty =0
            if isEmpty is  0:
                newArray.append(actualRow)
            else:
                newArray.insert(0,actualRow)
                # newArray.insert(0,actualRow) if isEmpty==1 else newArray.append(actualRow)
        self._insertSchemaArray = newArray



    def setDbConnection(self,_dbHostName="localhost" , _dbLogin="newUser" , _dbPassowrd="zaq" , _dbDatabase="super-crm"):
        print("called setDbConnection")
        self.dbHostName = _dbHostName
        self.dbLogin    = _dbLogin
        self.dbPassowrd = _dbPassowrd
        self.dbDatabase = _dbDatabase

    def getDbConnection(self):
        print("called getDbConnection")
        print(self.dbHostName)
        print(self.dbLogin)
        print(self.dbPassowrd)
        print(self.dbDatabase)

    def getDataTables(self):
        print("called getDataTables")
        print("login: "+self.dbLogin)
        print("pass: "+self.dbPassowrd)
        print("dbHostName: "+self.dbHostName)
        print("dbDatabase: "+self.dbDatabase)
        # config = {
        #     'user':     self.dbLogin,
        #     'password': self.dbPassowrd,
        #     'host':     self.dbHostName,
        #     'port': '3306',
        #     'database': self.dbDatabase}
        config = {
            'user':     "newUser",
            'password': "zaq",
            'host':     "localhost",
            'port': '3306',
            'database': "technologycupdb"}

        db = mysql.connector.connect( **config)
        cursor = db.cursor()
        # cursor.execute("select * from information_schema.columns where table_schema = '"+self.dbDatabase+"' order by table_name,ordinal_position")
        cursor.execute("select distinct table_name as selected_table,(SELECT GROUP_CONCAT(column_name) from information_schema.columns where table_schema = 'technologycupdb' and table_name=selected_table order by table_name,ordinal_position) from information_schema.columns where table_schema = 'technologycupdb' order by table_name,ordinal_position")
        self.dbSchema = cursor.fetchall()
        cursor.execute("SELECT  table_name,  column_name, referenced_table_name FROM INFORMATION_SCHEMA.key_column_usage WHERE referenced_table_schema = 'technologycupdb'   AND referenced_table_name IS NOT NULL ORDER BY table_name, column_name")
        self._constarinTable = cursor.fetchall()



    def getTableName(self,name):
        for x in self.dbSchema:
            if name in x[1]:
                return  x[0]


class dataAppliacation():
    print("called dataAppliacation")
    dataArray = []
    dataColumnName = []
    def __init__(self):
        self.dataArray= [['00','01','02'],
            ['10','11','12'],
            ['20','21','22']]

    def getDataArray(self):
        return self.dataArray

    def setDataArray(self,newArray):

        self.dataArray=newArray

    def getColumnCount(self):
        return len(self.dataArray[0][0].split(";"))

    def getRownCount(self):
        return len(self.dataArray
)


class connectionWindow(QtGui.QDialog):
    def __init__(self):
        super(connectionWindow , self).__init__()
        uic.loadUi('form2.ui', self)
        self.cancelButton.clicked.connect(self.close)
        self.connectButton.clicked.connect(self.setConnection)

    def setConnection(self):
        print("called setConnection")
        dbHostName  = self.dbHostText.text()
        dbLogin     = self.dbLoginText.text()
        dbPassowrd  = self.dbPasswordText.text()
        dbDatabase  = self.dbNameText.text()
        connectDatabase.setDbConnection(connection,dbHostName, dbLogin, dbPassowrd, dbDatabase)
        connectDatabase.getDbConnection(connection)
        connectDatabase.getDataTables(connection)
        self.close()


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

class mainView(QtGui.QMainWindow):
    connection = connectDatabase()
    def __init__(self):
        self.dataAppliacations =dataAppliacation()
        super(mainView, self).__init__()
        self.initUI()
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

    def splitData(self):
        print("called splitData")
        col = self.form_widget.textEdit.selectionModel().selectedColumns()
        #col = self.textEdit.currentItem().column()
        listSize = 0
        startListCount=self.form_widget.textEdit.columnCount()
        for index in sorted(col):
            for item in range(0, self.form_widget.textEdit.rowCount()):
                newlist = self.form_widget.textEdit.item(item, index.column()).text().split()
                if len(newlist)>listSize:
                    listSize = len(newlist)


        self.form_widget.textEdit.setColumnCount(self.form_widget.textEdit.columnCount()+listSize)
        self.form_widget.tableDBChoose.setColumnCount(self.form_widget.tableDBChoose.columnCount()+listSize)
        for index in sorted(col):
            for item in range(0, self.form_widget.textEdit.rowCount()):
                print(str(item)+ " "+str(self.form_widget.textEdit.rowCount()))
                #print(self.textEdit.item(item, index.column()).text().encode('UTF8'))
                newlist = self.form_widget.textEdit.item(item, index.column()).text().split()
                #print(newlist.encode('UTF8'))
                self.form_widget.textEdit.item(item, index.column()).setBackground(QtGui.QColor(238,55,55))
                for splitListElement in enumerate(newlist):
                    print(self.form_widget.textEdit.columnCount()+splitListElement[0])

                    self.form_widget.textEdit.setItem(item,(startListCount+splitListElement[0]),QtGui.QTableWidgetItem(splitListElement[1]))
                #print(newlist)
        model = self.form_widget.textEdit.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(str(model.data(index)))

        #print(data)
        self.dataAppliacations.setDataArray(data)
        for x in data:
            print(x.encode('UTF8'))

    def sendDataToDatabase(self):
        print("called sendDataToDatabase")
        columnCount = self.form_widget.tableDBChoose.columnCount()
        rowCount = self.form_widget.textEdit.rowCount()
        print(str(columnCount)+" "+str(rowCount))
        insertString = ""
        insertArray = []
        topArray= []
        for x in range(0,columnCount):
            if self.form_widget.tableDBChoose.item(0, x) is not None:
                tableName=[]
                tableName.append(connection.getTableName(self.form_widget.tableDBChoose.item(0, x).text()))
                topArray.append(tableName)

        topArray.sort()
        topArray=list(topArray for topArray,_ in itertools.groupby(topArray))
        print(topArray)
        # for z in range(0,rowCount):
        #     insertArray.append(topArray)
        print(columnCount)
        print(insertArray)
        for z in range(0,rowCount):
            insertArray.append([])
            for x in range(0,columnCount):
                if self.form_widget.tableDBChoose.item(0, x) is not None:
                    tmpArray=[]
                    tmpArray.append(self.form_widget.tableDBChoose.item(0, x).text())
                    if self.form_widget.textEdit.item(z, x).type() is not None:
                        tmpArray.append(self.form_widget.textEdit.item(z, x).text())

                    curElement = connection.getTableName(self.form_widget.tableDBChoose.item(0, x).text())
                    insertArray[z].append(tmpArray)
        print(insertArray)
        today = datetime.date.today()
        with open('insertData'+today.strftime('%d-%b-%Y')+'.txt', 'w') as outfile:
            json.dump(insertArray, outfile)
        connection._dbData = insertArray
        connection.fillTAble()

    def moveLeft(self):
        print("called moveLeft")
        print(self.form_widget.textEdit.columnCount())
        col = self.form_widget.textEdit.selectedItems()
        for x in col:
            row= x.row()
            tmpArray=[]
            for y in range(x.column()+1,self.form_widget.textEdit.columnCount()):
                # print(self.form_widget.textEdit.tifeam(1,y))
                print(y)
                print(self.form_widget.textEdit.item(row,y-1).text())
                tmpArray.append(self.form_widget.textEdit.item(row,y-1).text())
                # self.form_widget.textEdit.setItem(x.row(),y-2,QtGui.QTableWidgetItem('a'))

                self.form_widget.textEdit.setItem(row,y-2,QtGui.QTableWidgetItem(self.form_widget.textEdit.item(row,y-1).text()))
            print('tutaj')
            print(tmpArray)


    def moveRight(self):
        print("called moveRight")
        col = self.form_widget.textEdit.selectedItems()
        for x in col:
            for y in reversed(range(x.column(),self.form_widget.textEdit.columnCount())):
                # print(self.form_widget.textEdit.tifeam(1,y))
                if self.form_widget.textEdit.item(x.row(),y) !=None:
                    print(str(self.form_widget.textEdit.columnCount())+ " "+ str(y))
                    if y+1 == self.form_widget.textEdit.columnCount():
                        print("powiekszono")
                        self.form_widget.textEdit.setColumnCount(self.form_widget.textEdit.columnCount()+1)     
                    itmBefore= self.form_widget.textEdit.item(x.row(),y).text()
                    print(itmBefore)
                    # self.form_widget.textEdit.setItem(1,5,QtGui.QTableWidgetItem(itmBefore))
                    self.form_widget.textEdit.setItem(x.row(),y+1,QtGui.QTableWidgetItem(itmBefore))

    def initUI(self):

        openFile = QtGui.QAction(QtGui.QIcon('folder265.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        exitAction = QtGui.QAction(QtGui.QIcon('cross108.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        startApp = QtGui.QAction(QtGui.QIcon('arrow16.png'), 'Start', self)
        startApp.setStatusTip('Start application')
        startApp.triggered.connect(self.sendDataToDatabase)

        newConnection = QtGui.QAction(QtGui.QIcon('computers3.png'), 'New connection', self)
        newConnection.triggered.connect(self.connectionView)

        moveLeft = QtGui.QAction(QtGui.QIcon('left224.png'), 'move left', self)
        moveLeft.triggered.connect(self.moveLeft)

        moveRight = QtGui.QAction(QtGui.QIcon('right224.png'), 'move right', self)
        moveRight.triggered.connect(self.moveRight)

        self.statusBar()

        splitColumn = QtGui.QAction(QtGui.QIcon('split4.png'), 'Open', self)
        splitColumn.setShortcut('Ctrl+O')
        splitColumn.setStatusTip('Open new File')
        splitColumn.triggered.connect(self.splitData)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(newConnection)
        fileMenu.addAction(startApp)
        fileMenu.addAction(exitAction)


        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(openFile)
        self.toolbar.addAction(newConnection)
        self.toolbar.addAction(splitColumn)
        self.toolbar.addAction(startApp)
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(moveLeft)
        self.toolbar.addAction(moveRight)

        self.setGeometry(300, 300, 650, 550)
        self.setWindowTitle('Main window')
        self.show()

    def connectionView(sefl):
        s = connectionWindow()
        s.exec_()

    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')
        data = ""
        with open(fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            csvList = list(reader)
            self.dataAppliacations.setDataArray(csvList)
        print(self.dataAppliacations.dataArray)
        print(self.dataAppliacations.getColumnCount())
        self.form_widget.textEdit.setRowCount(self.dataAppliacations.getRownCount())
        self.form_widget.textEdit.setColumnCount(self.dataAppliacations.getColumnCount())
        self.form_widget.tableDBChoose.setColumnCount(self.dataAppliacations.getColumnCount())
        for rows in enumerate(self.dataAppliacations.getDataArray()):
            listOfElements=rows[1][0].split(";")
            counter= rows[0]
            for element in enumerate(listOfElements):
                print(element)
                self.form_widget.textEdit.setItem(counter,element[0],QtGui.QTableWidgetItem(element[1]))



connection = connectDatabase()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = mainView()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
