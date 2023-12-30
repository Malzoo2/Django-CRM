import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root@123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE DCRM_DB")

print("all done!")

