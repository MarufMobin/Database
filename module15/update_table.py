import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_statement = """
    update student
    set first_name = "Ruku", last_name = "haidari"
    where roll = 4;
"""
mycursor.execute( sql_statement )
mydb.commit()
