import sqlite3
import sys
from random import randint

class Cart:
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        try:
            self.connection = sqlite3.connect(self.databaseName)
        except:
            print("Could not open database.")
            sys.exit()

        self.cursor = self.connection.cursor()

    def viewCart(self, userID):
        query = "SELECT * FROM Cart WHERE UserID=?"
        self.cursor.execute(query, (userID,))
        cart_items = self.cursor.fetchall()
        print("Cart Items:")
        for item in cart_items:
            print(item)

    def addToCart(self, userID, ISBN, quantity):
        query = "INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, ?)"
        self.cursor.execute(query, (userID, ISBN, quantity))
        self.connection.commit()
        print("Item added to cart.")

    def removeFromCart(self, userID, ISBN):
        query = "DELETE FROM Cart WHERE UserID=? AND ISBN=?"
        self.cursor.execute(query, (userID, ISBN))
        self.connection.commit()
        print("Item removed from cart.")

    def clearCart(self, userID):
        query = "DELETE FROM Cart WHERE UserID=?"
        self.cursor.execute(query, (userID,))
        self.connection.commit()
        print("Cart cleared.")

# Testing the Cart class
if __name__ == "__main__":
    cart = Cart()

    # Example usage
    userID = "12-3456"  # Assuming a valid user ID
    ISBN = "978-0451524935"  # Example ISBN
    quantity = 2  # Example quantity

    cart.viewCart(userID)
    cart.addToCart(userID, ISBN, quantity)
    cart.viewCart(userID)
    cart.removeFromCart(userID, ISBN)
    cart.viewCart(userID)
    cart.clearCart(userID)
    cart.viewCart(userID)