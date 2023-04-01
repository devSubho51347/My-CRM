import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Subhadeep12121@'
)


## prepare a cursor object
cursorObject = database.cursor()

## Create a database

cursorObject.execute("CREATE DATABASE crm")

print("Successfully created database")