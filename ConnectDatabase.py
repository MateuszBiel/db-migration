import mysql.connector

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

    def findNextTable(self, name):
        for x in self._instances:
            if name == x[0]:
                return x
        

    def createInsertString(self):
        print("called createInsertString")
        print(self._dbData)
        print(self._instances)
        print(self._constarinTable)
        print(self.dbSchema)
        _tmpData = []

        insertArray = []
        insertArraySchema = []
        valueList=""
        insertString=""

        for x in self._instances:
            for y in self.dbSchema:
                # print("1 "+x+" "+y[0])
                if x == y[0]:
                    insertArraySchema.append(y)
        print('s')            
        print(insertArraySchema)
        for y in self._dbData:
           
            insertString2=""
            for x in insertArraySchema:
                print(x)
                insertString=""
                insertValues=""
                for z in y:
                    #print(z[0]+ "== "+x[1])
                    if z[0] in x[1]:
                        # print("weszlo")
                        insertValues = insertValues+z[0]+"',"
                        insertString=insertString+z[1]+"',"

                insertValues=insertValues[0:-2]
                insertString=insertString[0:-2]
                # if :
                #     insertString2 = "INSERT INTO "+x[0]+" ('"+insertValues+"') VALUES ('"+insertString+"')"
                # else:
                fkData = self.findNextTable(x[0])
                if fkData is not None:
                    insertString2 = "INSERT INTO "+x[0]+" ('"+insertValues+"','"+fkData[1]+"') VALUES ('"+insertString+"','(SELECT (SELECT `COLUMN_NAME` FROM `information_schema`.`COLUMNS` WHERE (`TABLE_NAME` = '"+fkData[2]+"') AND (`COLUMN_KEY` = 'PRI')  FROM "+fkData[2]+") where ')"
                else:
                    insertString2 = "INSERT INTO "+x[0]+" ('"+insertValues+"') VALUES ('"+insertString+"')"
                # print(insertString2)
                insertArray.append(insertString2)
                prevTable
        self._insertSchemaArray = insertArray
        today = datetime.date.today()
        print('z')
        print(self._insertSchemaArray)
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
        # cursor.execute("SELECT distinct table_name as selected_table,(SELECT GROUP_CONCAT(column_name) from information_schema.columns where table_schema = 'technologycupdb' and COLUMN_KEY != 'PRI' and table_name=selected_table order by table_name,ordinal_position ) from information_schema.columns where table_schema = 'technologycupdb' order by table_name,ordinal_position")
        cursor.execute("SELECT distinct table_name as selected_table,(SELECT GROUP_CONCAT(column_name) from information_schema.columns where table_schema = 'technologycupdb'  and table_name=selected_table order by table_name,ordinal_position ) from information_schema.columns where table_schema = 'technologycupdb' order by table_name,ordinal_position")
        self.dbSchema = cursor.fetchall()
        cursor.execute("SELECT  table_name,  column_name, referenced_table_name FROM INFORMATION_SCHEMA.key_column_usage WHERE referenced_table_schema = 'technologycupdb'   AND referenced_table_name IS NOT NULL ORDER BY table_name, column_name")
        self._constarinTable = cursor.fetchall()

    def getTableName(self,name):
        for x in self.dbSchema:
            if name in x[1]:
                return  x[0]
