"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frontiersistem.ro
Prompt: Suggest a library for building a cost-effective inventory management system, taking cues from the import solutions provided by FRONTIER SISTEM.
Generated: DETERMINISTIC_e29a77ef55ecbbfc
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for inventory management system
import sqlite3
from sqlite3 import Error

class InventoryManager:
    """Class to manage inventory items in a SQLite database."""

    def __init__(self, db_file):
        """Initialize the InventoryManager with a database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the items table in the database if it doesn't exist."""
        try:
            sql_create_items_table = """
            CREATE TABLE IF NOT EXISTS items (
                id integer PRIMARY KEY,
                name text NOT NULL,
                quantity integer NOT NULL,
                price real NOT NULL
            );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_items_table)
            print("Items table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_item(self, name, quantity, price):
        """Add a new item to the inventory."""
        sql = '''INSERT INTO items(name, quantity, price) VALUES(?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, quantity, price))
            self.connection.commit()
            print(f"Item '{name}' added successfully.")
        except Error as e:
            print(f"Error adding item: {e}")

    def update_item(self, item_id, quantity, price):
        """Update an existing item's quantity and price."""
        sql = '''UPDATE items SET quantity = ?, price = ? WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (quantity, price, item_id))
            self.connection.commit()
            print(f"Item with id '{item_id}' updated successfully.")
        except Error as e:
            print(f"Error updating item: {e}")

    def delete_item(self, item_id):
        """Delete an item from the inventory."""
        sql = 'DELETE FROM items WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (item_id,))
            self.connection.commit()
            print(f"Item with id '{item_id}' deleted successfully.")
        except Error as e:
            print(f"Error deleting item: {e}")

    def fetch_items(self):
        """Fetch all items from the inventory."""
        sql = 'SELECT * FROM items'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching items: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = "inventory.db"
    manager = InventoryManager(db)
    manager.create_table()
    
    # Example operations
    manager.add_item("Widget", 10, 2.99)
    manager.update_item(1, 15, 3.49)
    print(manager.fetch_items())
    manager.delete_item(1)
    manager.close_connection()
```
