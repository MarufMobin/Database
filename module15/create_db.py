import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password",
)

# print( mydb )

# Create a database 
mycursor = mydb.cursor()

db_name = "mydatabase"
sql_command = "create database " + db_name

mycursor.execute( sql_command )