import sqlite3

"""
Functions that sends a variety
of queries to the database. These queries are 
adding, altering and removing data from the
different tables of the database.
"""


#Conn is the database
def addBolig(pris:int,by:int,bydel:int,gate:int,conn):
    query = "INSERT INTO Bolig VALUES (?, ?, ?, ?);"
    data_tuple = (pris,by,bydel,gate)
    conn.execute(query,data_tuple)


def addBy(navn:str,conn):
    query = "INSERT INTO By VALUES (?, ?, ?);"
    data_tuple = (navn,0)
    conn.execute(query,data_tuple)

def addBydel(navn:str,by:int,conn):
    query = "INSERT INTO Bydel VALUES (?, ?, ?);"
    data_tuple = (by,navn,0)
    conn.execute(query,data_tuple)

def addGate(navn:str,bydel:int,conn):
    query = "INSERT INTO Gate VALUES (?, ?, ?);"
    data_tuple = (bydel,navn,0)
    conn.execute(query,data_tuple)


#Meant to be called in regular time intervals, every day for example
#Takes table name as argument
def updateGjPris(table:str,conn):
    query = f"UPDATE {table}" \
            f"FROM Bolig ,{table}" \
            f"SET GjPris = SUM(Bolig.Pris)" \
            f"WHERE {table}.ID = Bolig.{table}"
    conn.execute(query)


