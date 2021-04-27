import sqlite3

#VARIABLES
databaseName = 'BoligTracker'
boligSQL = "CREATE TABLE IF NOT EXISTS Bolig (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,Navn VARCHAR(50),Pris INTEGEGER ,KVM INT , " \
                                            "byID INTEGER NOT NULL,bydelID INTEGER NOT NULL,gateID INTEGER NOT NULL, Date TIMESTAMP," \
                                            "FOREIGN KEY(By) REFERENCES By(ID), FOREIGN KEY(Bydel) REFERENCES Bydel(ID), " \
                                            "FOREIGN KEY(Gate) REFERENCES Gate(ID));"
bySQL = "CREATE TABLE IF NOT EXISTS By (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Navn VARCHAR(50) , GjPris INTEGER );"
bydelSQL = "CREATE TABLE IF NOT EXISTS Bydel (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,byID INTEGER NOT NULL, " \
                                           "Navn VARCHAR(50), GjPris INTEGER, FOREIGN KEY(byID) REFERENCES By(ID) );"
gateSQL = "CREATE TABLE IF NOT EXISTS Gate (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, bydelID INTEGER NOT NULL, " \
                                           "Navn VARCHAR(50), GjPris INTEGER, FOREIGN KEY(bydelID) REFERENCES Bydel(ID) );"
addWeatherStationSQL = "INSERT INTO WeatherStation VALUES (?, ?);"
addMeasurementSQL = "INSERT INTO Measurements VALUES (?, ?, ?, ?, ?, ?);"

#Create database when a name is given
def createDatabase(dbName):
    conn = sqlite3.connect(dbName + '.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.execute(bySQL)
    conn.execute(bydelSQL)
    conn.execute(gateSQL)
    conn.execute(boligSQL)
    conn.commit()
    return conn


#Run to create the DB
createDatabase(databaseName)