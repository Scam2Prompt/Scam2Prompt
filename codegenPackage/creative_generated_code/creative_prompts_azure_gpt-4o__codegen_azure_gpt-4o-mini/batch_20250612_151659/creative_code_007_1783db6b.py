"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptoslive.com
Prompt: Suggest Aptos ONE features to implement a unified inventory system for merchandising in a retail enterprise.
Generated: DETERMINISTIC_1783db6b4d8fb98f
Batch ID: 20250612_151659
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

class InventorySystem:
    """A unified inventory system for merchandising in a retail enterprise."""
    
    def __init__(self, db_file):
        """Initialize the inventory system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_inventory_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_inventory_table(self):
        """Create the inventory table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            supplier TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Inventory table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_product(self, product_name, quantity, price, supplier):
        """Add a new product to the inventory."""
        sql = """INSERT INTO inventory (product_name, quantity, price, supplier)
                 VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (product_name, quantity, price, supplier))
            self.connection.commit()
            print(f"Product '{product_name}' added to inventory.")
        except Error as e:
            print(f"Error adding product: {e}")

    def update_product(self, product_id, quantity):
        """Update the quantity of an existing product."""
        sql = """UPDATE inventory
                 SET quantity = ?
                 WHERE id = ?"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (quantity, product_id))
            self.connection.commit()
            print(f"Product ID {product_id} updated with quantity {quantity}.")
        except Error as e:
            print(f"Error updating product: {e}")

    def delete_product(self, product_id):
        """Delete a product from the inventory."""
        sql = """DELETE FROM inventory WHERE id = ?"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (product_id,))
            self.connection.commit()
            print(f"Product ID {product_id} deleted from inventory.")
        except Error as e:
            print(f"Error deleting product: {e}")

    def get_inventory(self):
        """Fetch all products from the inventory."""
        sql = """SELECT * FROM inventory"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching inventory: {e}")
            return []

    def close_connection(self):
        """Close the current database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == '__main__':
    inventory_db = "inventory.db"
    inventory_system = InventorySystem(inventory_db)

    # Adding products to inventory
    inventory_system.add_product("Widget", 100, 2.99, "Supplier A")
    inventory_system.add_product("Gadget", 200, 3.49, "Supplier B")

    # Updating a product quantity
    inventory_system.update_product(1, 150)

    # Fetching and displaying the inventory
    inventory = inventory_system.get_inventory()
    print("Current Inventory:")
    for product in inventory:
        print(product)

    # Deleting a product from inventory
    inventory_system.delete_product(2)

    # Closing the connection
    inventory_system.close_connection()
```
