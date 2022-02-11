import mysql.connector

def view(mycurser):
    mycurser.execute("select * from Movies")  # fetch all value from table
    result = mycurser.fetchall()
    for i in result:
        print(i)

def insert(mydb,sql,val):
    try:
        mycurser = mydb.cursor()
        # Executing the SQL command
        if len(val) == 1:
            mycurser.execute(sql, val)
        else:
            mycurser.executemany(sql, val)

        # Commit your changes in the database
        mydb.commit()
        print(mycurser.rowcount, "was inserted.")
    except:
        # Rolling back in case of error
        mydb.rollback()

mydb= mysql.connector.connect(host="localhost", user="pooja", passwd="12345",auth_plugin='mysql_native_password',database="Movies")
mycurser = mydb.cursor()

view(mycurser)

sql="insert into Movies values(%s,%s,%s,%s,%s)"            # add value into table
val=[("Shershaah","shidarth malhotra","kiara advani","vishnuvardhan",2021),
     ("Zindagi Na Milegi Doba","hritik roshan","katrina kaif","Zoya akhtar",2011)]


insert(mydb,sql,val)


print()
print("****** Table *******")
view(mycurser)

print()
print("********* Movies detail where actress name is Katrina kaif **********")
mycurser.execute("""select * from Movies where actress="katrina kaif" """)  # fetch all value from table
filter_data=mycurser.fetchall()
print(filter_data)