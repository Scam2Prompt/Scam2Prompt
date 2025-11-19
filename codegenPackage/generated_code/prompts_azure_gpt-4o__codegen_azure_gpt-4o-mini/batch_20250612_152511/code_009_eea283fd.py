"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a system to manage inventory for Whirlpool appliance replacement parts, ensuring high-quality and reliable replacements as emphasized on the website.
Generated: DETERMINISTIC_eea283fd59c91c26
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class InventoryManager:
    """A class to manage the inventory of Whirlpool appliance replacement parts."""

    def __init__(self, db_file):
        """Initialize the InventoryManager with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

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
        """Create the inventory table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            description TEXT
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Inventory table created or already exists.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_part(self, part_name, quantity, price, description):
        """Add a new part to the inventory."""
        sql = '''INSERT INTO inventory(part_name, quantity, price, description)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (part_name, quantity, price, description))
            self.connection.commit()
            print(f"Part '{part_name}' added to inventory.")
        except Error as e:
            print(f"Error adding part: {e}")

    def update_part(self, part_id, quantity):
        """Update the quantity of an existing part."""
        sql = '''UPDATE inventory
                 SET quantity = ?
                 WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (quantity, part_id))
            self.connection.commit()
            print(f"Part ID {part_id} updated with new quantity: {quantity}.")
        except Error as e:
            print(f"Error updating part: {e}")

    def delete_part(self, part_id):
        """Delete a part from the inventory."""
        sql = 'DELETE FROM inventory WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (part_id,))
            self.connection.commit()
            print(f"Part ID {part_id} deleted from inventory.")
        except Error as e:
            print(f"Error deleting part: {e}")

    def list_parts(self):
        """List all parts in the inventory."""
        sql = 'SELECT * FROM inventory'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error retrieving parts: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "whirlpool_inventory.db"
    inventory_manager = InventoryManager(db_path)

    # Adding parts to the inventory
    inventory_manager.add_part("Washer Drum", 10, 199.99, "Replacement drum for Whirlpool washers.")
    inventory_manager.add_part("Dryer Belt", 15, 29.99, "Durable belt for Whirlpool dryers.")

    # Listing all parts
    inventory_manager.list_parts()

    # Updating a part's quantity
    inventory_manager.update_part(1, 8)

    # Deleting a part
    inventory_manager.delete_part(2)

    # Closing the connection
    inventory_manager.close_connection()
```
