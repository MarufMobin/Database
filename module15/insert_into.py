import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# insert Data into a table  
sql_command = """
        insert into Student( roll, first_name , last_name )
        values ( 1, "Maruf", "Mobin" ),
        ( 2, "Munna", "Mahmud" ),
        ( 3, "Abdul", "jabbar" ),
        ( 4, "Masum", "Mollah" );
"""
mycursor.execute( sql_command )
mydb.commit()