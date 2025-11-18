"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Write Python code to integrate an inventory management system for tracking the availability of stainless steel, aluminum, copper, and other metals, using a database schema tailored for Meta+ product categories.
Generated: DETERMINISTIC_9965ca47193440db
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

# Database class to handle database operations
class InventoryDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Create the inventory table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metal_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_per_unit REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_metal(self, metal_type, quantity, price_per_unit):
        """Add new metal item to the inventory."""
        sql = '''INSERT INTO inventory(metal_type, quantity, price_per_unit)
                 VALUES(?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (metal_type, quantity, price_per_unit))
            self.connection.commit()
        except Error as e:
            print(f"Error adding metal to inventory: {e}")

    def get_inventory(self):
        """Retrieve all metal items from the inventory."""
        sql = 'SELECT * FROM inventory'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving inventory: {e}")
            return []

    def update_quantity(self, metal_type, quantity):
        """Update the quantity of a specific metal in the inventory."""
        sql = '''UPDATE inventory
                 SET quantity = ?
                 WHERE metal_type = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (quantity, metal_type))
            self.connection.commit()
        except Error as e:
            print(f"Error updating quantity for {metal_type}: {e}")

    def delete_metal(self, metal_type):
        """Delete a metal item from the inventory."""
        sql = 'DELETE FROM inventory WHERE metal_type = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (metal_type,))
            self.connection.commit()
        except Error as e:
            print(f"Error deleting metal {metal_type}: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    db = InventoryDatabase("inventory.db")
    
    # Adding some metals to inventory
    db.add_metal("Stainless Steel", 100, 1.50)
    db.add_metal("Aluminum", 200, 0.80)
    db.add_metal("Copper", 50, 3.00)

    # Retrieving and displaying inventory
    inventory = db.get_inventory()
    print("Current Inventory:")
    for item in inventory:
        print(item)

    # Updating quantity
    db.update_quantity("Aluminum", 150)

    # Deleting a metal
    db.delete_metal("Copper")

    # Final inventory output
    print("Updated Inventory:")
    print(db.get_inventory())

    db.close()
```
