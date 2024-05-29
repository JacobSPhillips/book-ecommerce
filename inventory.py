import sqlite3
import sys





class Inventory:

    def __init__(self, databaseName: str = "methods.db"):
        self.databaseName = databaseName
        try:
            self.connection = sqlite3.connect(self.databaseName)
        except:
            print("Could not open database.")
            sys.exit()

        self.cursor = self.connection.cursor()

    def Inventory(self, databaseName):
        self.databaseName = databaseName
        try:
            self.connection = sqlite3.connect(self.databaseName)
        except:
            print("Could not open database.")
            sys.exit()

        self.cursor = self.connection.cursor()

    def viewInventory(self):
        self.cursor.execute("SELECT * FROM Inventory")
        inventory = self.cursor.fetchall()
        if inventory:
            print("Inventory:")
            print(f"{'ISBN':<20}{'Title':<25}{'Author':<30}{'Genre':<35}{'Page Number':<40}{'Release Date':<45}{'Price':<50}{'Stock':<55}")
            separatory = "-" * 200
            print(separatory)
            for item in inventory:
                print(f"{item[0]:<20}{item[1]:<25}{item[2]:<30}{item[3]:<35}{item[4]:<40}{item[5]:<45}{item[6]:<50}{item[7]:<55}")
                print(separatory)
        #print("Inventory: ", inventory, sep="\n", end="\n\n\n")

    def searchInventory(self):
        title = str(input("What title would you like to search for: "))
        self.cursor.execute("SELECT * FROM Inventory WHERE Title = ?", (title,))
        results = self.cursor.fetchall()
        if results:
            print("Search results: ")
            for items in results:
                print(items)
        else:
            print("No results found for ", title)

    def decreaseStock(self, ISBN, quantity=1):
        self.cursor.execute("UPDATE Inventory SET Stock = Stock - ? WHERE ISBN = ?", (quantity, ISBN,))
        self.connection.commit()
