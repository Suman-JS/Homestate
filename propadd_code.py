#!C:\Python38-32\python.exe
#print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
form=cgi.FieldStorage()
a=form.getvalue('a1')
b=form.getvalue('a2')
c=form.getvalue('a3')

db=mysql.connector.connect(host="localhost",user="root",passwd="",db="prop_sdf")
cur=db.cursor()
cur.execute("insert into prop_detail (area,loc,price) values ('%s','%s','%s')"%(a,b,c))
db.commit()
db.close()
print("location:./adwelcome.html?msg=done\r\n\r\n")