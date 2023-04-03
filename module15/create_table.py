import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "password",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# Create a table 
sql_command = """
                            CREATE TABLE Student( 
                                roll  int,
                                first_name VARCHAR(20),
                                last_name VARCHAR(20)
                            );
                        """

mycursor.execute(sql_command) 
