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



my_db = DatabaseManager()
while True:
    print("\n1. Add a new contact")
    print("2. View all contacts")
    print("3. Exit\n")
    choice = int(input("Enter your choice (1-3):"))
    if choice == 1 :
        name = input("please enter the name : ")
        phone = input("please enter the phone number : ")
        my_db.add_contact(name,phone)
        print("information added with success ")
    elif choice == 2:
        result = my_db.get_all_contacts()
        print("")
        for x in result:
            print(x)
    elif choice == 3:
        print("Goodbye")
        my_db.close()
        break
    else:
        print("Invalid choice")