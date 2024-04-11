import mysql.connector

mydb = mysql.connector.connect(
    host="mysql_container",
    user="root",
    password="contraseña",
    database="db_test"
)
##
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")

for row in mycursor.fetchall():
    print(row)
mydb.close()


