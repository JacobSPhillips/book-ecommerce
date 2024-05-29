import sqlite3
import sys
from random import randint


class OrderHistory:

    def __init__(self, databaseName: str = "method.db"):
        self.databaseName = databaseName
        try:
            self.connection = sqlite3.connect(self.databaseName)
        except:
            print("Could not open database.")
            sys.exit()

        self.cursor = self.connection.cursor()

    def OrderHistory(self, databaseName):
        self.databaseName = databaseName
        try:
            self.connection = sqlite3.connect(self.databaseName)
        except:
            print("Could not open database.")
            sys.exit()

        self.cursor = self.connection.cursor()

    def viewHistory(self, userID):
        query = ("SELECT * FROM Orders WHERE UserID=?")
        self.cursor.execute(query, (userID,))
        orders = self.cursor.fetchall()
        print("Order History: ", orders, sep="\n", end="\n\n\n")

    def viewOrder(self, userID, orderID):
        query = ("SELECT * FROM Orders WHERE UserID = ? AND OrderID = ?")
        self.cursor.execute(query, (userID, orderID))
        order = self.cursor.fetchone()
        ## If both ID's match order it will print out
        ## If not an error message will
        if order:
            print("Past Order: ", order, sep="\n", end="\n\n\n")
        else:
            print("This Order does not belong to current User!", end="\n\n\n")

    def createOrder(self, userID, quantity, cost, date):
        while True:
            ## Random number with 6 digits
            newID = randint(100000, 999999)
            query = "SELECT OrderNumber FROM Orders WHERE OrderNumber = ?"
            self.cursor.execute(query, (newID,))
            existingOrder = self.cursor.fetchone()
            if not existingOrder:
                break

        query = "INSERT INTO Orders (OrderNumber, UserID, Quantity, Cost, Date) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (newID, userID, quantity, cost, date))
        self.connection.commit
        return (str(newID))

    def addOrderItems(self, userID, orderID):
        query = "SELECT * FROM Cart WHERE UserID = ?"
        self.cursor.execute(query, (userID))
        cartItems = self.cursor.fetchall()
        for item in cartItems:
            ISBN = item[1]
            quantity = item[2]
            query = "INSERT INTO OrderItems (OrderNumber, ISBN, Quantity) VALUES (?,?,?)"
            self.cursor.execute(query, (orderID, ISBN, quantity))
        self.connection.commit()