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