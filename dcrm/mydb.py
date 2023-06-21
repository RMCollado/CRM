import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create the database
cursorObject.execute("CREATE DATABASE CRM_DB")

print("database created")
