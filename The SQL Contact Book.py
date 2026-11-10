import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "your user name (usually root)",
            password = "your password",
            database = "name of database"
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255) , phone VARCHAR(10) )")
    