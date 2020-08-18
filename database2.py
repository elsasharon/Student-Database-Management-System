import sqlite3


def student1Data():
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student2(id INTEGER PRIMARY KEY   ,StdID text   , Firstname text   , Surname text  ,DoB text    , Gender text  , Address text   , Mobile text  )")
    con.commit()
    con.close()
    


def addStdRec(StdID, Firstname, Surname, DoB,  Gender, Address, Mobile ):
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student2 VALUES (NULL  ,   ?,   ?,   ?,   ?,   ?,   ?,   ?)",(StdID , Firstname, Surname, DoB,  Gender, Address, Mobile))
    con.commit()
    con.close()


def viewData():
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student2 " )
    
    rows = cur.fetchall()
    con.close()
    return rows

    


def deleteRec(id):
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student2 WHERE id=?",(id,) )
    con.commit()
    con.close()


def searchData(StdID="", Firstname="", Surname="", DoB="",  Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student2 WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Gender=? OR Address=? OR Mobile=?",(StdID, Firstname, Surname, DoB,  Gender, Address, Mobile)) 
    rows = cur.fetchall()
    con.close()
    return rows



def dataUpdate(id, StdID="", Firstname="", Surname="", DoB="",  Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student2.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoB=?, Gender=?, Address=?, Mobile=?, WHERE id=?",(StdID, Firstname, Surname, DoB, Gender, Address, Mobile, id)) 
    con.commit()
    con.close()
      


student1Data()
