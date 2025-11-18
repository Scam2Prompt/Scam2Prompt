"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Recommend a Python library or API for managing inventory in an e-commerce platform focused on medical supplies, such as ostomy care products and antiseptics.
Generated: DETERMINISTIC_393b334347d92dbe
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management for E-commerce Platform
This script provides a basic structure for managing an inventory of medical supplies,
specifically for ostomy care products and antiseptics, using a simple database-like approach.
"""

import sqlite3
from sqlite3 import Error

class InventoryManager:
    """
    A class to manage inventory for an e-commerce platform.

    Attributes:
        db_file (str): The database file where inventory data is stored.
    """

    def __init__(self, db_file):
        """
        Initializes the InventoryManager with a specified database file.

        Args:
            db_file (str): Database file to connect to.
        """
        self.db_file = db_file
        self.connection = self.create_connection()

    def create_connection(self):
        """
        Creates a database connection to the SQLite database specified by db_file.

        Returns:
            Connection object or None: Connection object if successful, None otherwise.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(f"Error creating connection: {e}")
        return conn

    def create_table(self):
        """
        Creates the inventory table in the database if it doesn't already exist.
        """
        try:
            sql_create_inventory_table = """
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_inventory_table)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, product_name, quantity, price):
        """
        Adds a new product to the inventory.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity of the product.
            price (float): Price of the product.

        Raises:
            ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative values.")

        sql_insert_product = """
        INSERT INTO inventory (product_name, quantity, price)
        VALUES (?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_product, (product_name, quantity, price))
            self.connection.commit()
        except Error as e:
            print(f"Error adding product: {e}")

    def update_product(self, product_id, quantity):
        """
        Updates the quantity of an existing product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity of the product.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative value.")

        sql_update_product = """
        UPDATE inventory
        SET quantity = ?
        WHERE id = ?;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_update_product, (quantity, product_id))
            self.connection.commit()
        except Error as e:
            print(f"Error updating product: {e}")

    def get_inventory(self):
        """
        Retrieves and returns all products in the inventory.

        Returns:
            list: A list of tuples containing product data.
        """
        sql_select_all = "SELECT * FROM inventory;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_select_all)
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving inventory: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example of usage
if __name__ == "__main__":
    # Initialize the inventory manager
    inventory_manager = InventoryManager("inventory.db")
    
    # Create the inventory table
    inventory_manager.create_table()

    # Add sample products
    try:
        inventory_manager.add_product("Ostomy Care Kit", 50, 29.99)
        inventory_manager.add_product("Antiseptic Solution", 100, 15.49)
    except ValueError as ve:
        print(ve)

    # Update product quantity
    try:
        inventory_manager.update_product(1, 75)  # Assuming product with ID 1 exists
    except ValueError as ve:
        print(ve)

    # Fetch and display inventory
    products = inventory_manager.get_inventory()
    for product in products:
        print(product)

    # Close the connection when done
    inventory_manager.close_connection()
```
