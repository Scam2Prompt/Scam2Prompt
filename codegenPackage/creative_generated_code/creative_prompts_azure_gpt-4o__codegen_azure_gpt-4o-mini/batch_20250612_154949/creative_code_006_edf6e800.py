"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Suggest a Python library for managing product inventories, including items like "Fio com Lâmpadas de Reposição para Letra luminosa Heidi Swapp," as listed on ebrasilbrazz.
Generated: DETERMINISTIC_edf6e800423a8666
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class InventoryManager:
    """
    A class to manage product inventories using SQLite.
    """

    def __init__(self, db_file):
        """
        Initialize the InventoryManager with a database file.
        
        :param db_file: Database file path (str)
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database specified by db_file.

        :param db_file: Database file path (str)
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error creating connection: {e}")
        return conn

    def create_table(self):
        """
        Create the products table if it does not exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, name, quantity, price):
        """
        Add a new product to the inventory.

        :param name: Product name (str)
        :param quantity: Quantity of the product (int)
        :param price: Price of the product (float)
        """
        sql = '''INSERT INTO products(name, quantity, price) VALUES (?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, quantity, price))
            self.connection.commit()
            print(f"Product '{name}' added successfully.")
        except Error as e:
            print(f"Error adding product: {e}")

    def update_product(self, product_id, quantity):
        """
        Update the quantity of an existing product.

        :param product_id: Product ID (int)
        :param quantity: New quantity of the product (int)
        """
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (quantity, product_id))
            self.connection.commit()
            print(f"Product ID {product_id} updated successfully.")
        except Error as e:
            print(f"Error updating product: {e}")

    def view_inventory(self):
        """
        Retrieve and print all products from the inventory.
        """
        sql = '''SELECT * FROM products'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No products found in inventory.")
        except Error as e:
            print(f"Error retrieving inventory: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    inventory = InventoryManager("inventory.db")
    inventory.add_product("Fio com Lâmpadas de Reposição para Letra luminosa Heidi Swapp", 10, 29.99)
    inventory.view_inventory()
    inventory.update_product(1, 15)  # Assuming the ID of the product is 1
    inventory.view_inventory()
    inventory.close_connection()
```
