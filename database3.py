import sqlite3


def StudentData():
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student1(id INTEGER PRIMARY KEY   ,StdID text   , Firstname text   , Surname text  ,Semester text  , Payment text  , Status text  )")
    con.commit()
    con.close()
    


def addStdRec(StdID, Firstname, Surname, Semester , Payment , Status ):
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student1 VALUES (NULL  ,   ?,   ?,   ?,   ?,   ?,   ?)",(StdID , Firstname, Surname, Semester , Payment , Status ))
    con.commit()
    con.close()


def viewData():
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student1 " )
    
    rows = cur.fetchall()
    con.close()
    return rows

    


def deleteRec(id):
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student1 WHERE id=?",(id,) )
    con.commit()
    con.close()


def searchData(StdID="", Firstname="", Surname="", Semester="", Payment="", Status=""):
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student1 WHERE StdID=? OR Firstname=? OR Surname=? OR Semester=? OR Payment=? OR Status=? ",(StdID, Firstname, Surname, Semester , Payment , Status )) 
    rows = cur.fetchall()
    con.close()
    return rows



def dataUpdate(id, StdID="", Firstname="", Surname="", Semester="", Payment="", Status=""):
    con=sqlite3.connect("student1.db")
    cur = con.cursor()
    cur.execute("UPDATE student1 SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?",(StdID, Firstname, Surname, Semester , Payment , Status , id)) 
    con.commit()
    con.close()
      


StudentData()
