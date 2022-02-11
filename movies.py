import mysql.connector

mydb= mysql.connector.connect(host="localhost", user="pooja", passwd="12345",auth_plugin='mysql_native_password',database="Movies")

mycurser= mydb.cursor()

mycurser.execute("select * from Movies")

result=mycurser.fetchall()

for i in result:
    print(i)