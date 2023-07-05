import pymysql
conn = pymysql.connect(user='root' ,password='' ,host='localhost' ,database='testprac')
cursor = conn.cursor()
mydb = 'select * from data;'
#mydb = 'insert into data values("fahim",04,"chapain,savar");'
r = cursor.execute(mydb)
mydata = cursor.fetchall()
print(mydata)

