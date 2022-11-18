#!C:\Users\sm713\AppData\Local\Programs\Python\Python311\python.exe
import cgi

import mysql.connector

form=cgi.FieldStorage()
a=form.getvalue('a1')
b=form.getvalue('a2')
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="prop_sdf")
cur=db.cursor()
cur.execute("select * from user")
x=cur.fetchall()
s=0
for i in x:
	if a==i[2]:
		s=1
		d=i[3]
		id=i[0]

if s==1:
	if b==d:
		print("location:./welcome.html\r\n\r\n")
	else:
		print("location:./login.html?msg=not done\r\n\r\n")
else:
	print("location:./login.html?msg=not done\r\n\r\n")
		
		
		
		
		
		
		
		










