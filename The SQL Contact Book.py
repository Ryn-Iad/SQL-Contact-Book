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
    def add_contact(self, name, phone):
        sql = "INSERT INTO contacts (name,phone) VALUES (%s,%s)"
        entry = (name,phone)
        self.mycursor.execute(sql,entry)
        self.mydb.commit()
    def get_all_contacts(self):
        sql = "SELECT * FROM contacts"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        return result
    
    def close(self):
        self.mycursor.close()
        self.mydb.close()




    