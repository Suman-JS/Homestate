#!C:\Users\sm713\AppData\Local\Programs\Python\Python311\python.exe
#print("Content-type:text/html\r\n\r\n")
import cgi

import mysql.connector

form=cgi.FieldStorage()
a=form.getvalue('a1')
b=form.getvalue('a2')
c=form.getvalue('a3')
d=form.getvalue('a4')
e=form.getvalue('a5')
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="prop_sdf")
cur=db.cursor()
cur.execute("insert into user (name,email,pwd,phno,addr) values ('%s','%s','%s','%s','%s')"%(a,b,c,d,e))
db.commit()
db.close()
print("location:./login.html?msg=done\r\n\r\n")