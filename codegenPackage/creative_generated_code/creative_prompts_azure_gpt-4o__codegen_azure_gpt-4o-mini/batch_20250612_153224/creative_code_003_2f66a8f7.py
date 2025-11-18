"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to manage warehousing operations, including inventory tracking and packaging, inspired by Alexa Shipping's logistics solutions.
Generated: DETERMINISTIC_2f66a8f74ab710c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WarehouseManager:
    def __init__(self, db_name='warehouse.db'):
        """Initialize the WarehouseManager with a database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables in the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    packaging_type TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            logging.info('Inventory table created successfully.')
        except sqlite3.Error as e:
            logging.error(f"Error creating tables: {e}")

    def add_item(self, item_name, quantity, packaging_type):
        """Add a new item to the inventory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO inventory (item_name, quantity, packaging_type)
                VALUES (?, ?, ?)
            ''', (item_name, quantity, packaging_type))
            self.connection.commit()
            logging.info(f"Added item: {item_name}, Quantity: {quantity}, Packaging: {packaging_type}")
        except sqlite3.Error as e:
            logging.error(f"Error adding item: {e}")

    def update_item(self, item_id, quantity):
        """Update the quantity of an existing item in the inventory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                UPDATE inventory
                SET quantity = ?
                WHERE id = ?
            ''', (quantity, item_id))
            self.connection.commit()
            logging.info(f"Updated item ID: {item_id}, New Quantity: {quantity}")
        except sqlite3.Error as e:
            logging.error(f"Error updating item: {e}")

    def delete_item(self, item_id):
        """Delete an item from the inventory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                DELETE FROM inventory
                WHERE id = ?
            ''', (item_id,))
            self.connection.commit()
            logging.info(f"Deleted item ID: {item_id}")
        except sqlite3.Error as e:
            logging.error(f"Error deleting item: {e}")

    def view_inventory(self):
        """Retrieve and display all items in the inventory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM inventory')
            items = cursor.fetchall()
            logging.info("Current inventory:")
            for item in items:
                logging.info(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Packaging: {item[3]}")
            return items
        except sqlite3.Error as e:
            logging.error(f"Error retrieving inventory: {e}")

    def __del__(self):
        """Close the database connection when the instance is deleted."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

# Example usage
if __name__ == "__main__":
    manager = WarehouseManager()
    manager.add_item('Box', 100, 'Cardboard')
    manager.add_item('Bubble Wrap', 200, 'Plastic')
    manager.view_inventory()
    manager.update_item(1, 150)
    manager.view_inventory()
    manager.delete_item(2)
    manager.view_inventory()
```
