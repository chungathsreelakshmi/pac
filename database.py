
import mysql.connector

def select(q):
    cnx=mysql.connector.connect(user="root",password="",host="localhost",database="pacs")
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    result=cur.fetchall()
    cnx.close()
    cur.close()
    return result

def insert(q):
    cnx=mysql.connector.connect(user="root",password="",host="localhost",database="pacs")
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    cnx.commit()
    id=cur.lastrowid
    cnx.close()
    cur.close()
    return id

def update(q):
    cnx=mysql.connector.connect(user="root",password="",host="localhost",database="pacs")
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    cnx.commit()
    count=cur.rowcount
    cnx.close()
    cur.close()
    return count
