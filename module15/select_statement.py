import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password",
    database = "hr"
)

mycursor = mydb.cursor()

# insert Data into a table  
sql_command = """
        select * 
        from employees
        where salary > 100
        limit 10
"""
mycursor.execute( sql_command )
data = mycursor.fetchall()

for i in data:
    print(i)
