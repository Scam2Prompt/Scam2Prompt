"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a code snippet for an inventory management system that tracks computer hardware and accessories like SSDs and projectors, similar to the offerings on mixpelinfobrazz.
Generated: DETERMINISTIC_f60f03bf7ef5e141
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Inventory Management System for Computer Hardware and Accessories

class InventoryManager:
    def __init__(self, db_name="inventory.db"):
        """
        Initialize the InventoryManager with a SQLite database.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the necessary tables in the database if they don't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Create table for inventory items
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    added_date TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_item(self, name, category, quantity, price):
        """
        Add a new item to the inventory.
        :param name: Name of the item
        :param category: Category of the item (e.g., SSD, Projector)
        :param quantity: Quantity of the item
        :param price: Price of the item
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO inventory (name, category, quantity, price, added_date)
                VALUES (?, ?, ?, ?, ?)
            """, (name, category, quantity, price, added_date))
            conn.commit()
            print(f"Item '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding item: {e}")
        finally:
            conn.close()

    def view_inventory(self):
        """
        View all items in the inventory.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory")
            items = cursor.fetchall()
            print("Inventory:")
            print("ID | Name | Category | Quantity | Price | Added Date")
            print("-" * 60)
            for item in items:
                print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | ${item[4]:.2f} | {item[5]}")
        except sqlite3.Error as e:
            print(f"Error viewing inventory: {e}")
        finally:
            conn.close()

    def update_item(self, item_id, name=None, category=None, quantity=None, price=None):
        """
        Update an existing item in the inventory.
        :param item_id: ID of the item to update
        :param name: New name of the item (optional)
        :param category: New category of the item (optional)
        :param quantity: New quantity of the item (optional)
        :param price: New price of the item (optional)
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Build the update query dynamically based on provided parameters
            updates = []
            params = []
            if name:
                updates.append("name = ?")
                params.append(name)
            if category:
                updates.append("category = ?")
                params.append(category)
            if quantity is not None:
                updates.append("quantity = ?")
                params.append(quantity)
            if price is not None:
                updates.append("price = ?")
                params.append(price)
            params.append(item_id)
            query = f"UPDATE inventory SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            conn.commit()
            print(f"Item with ID {item_id} updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating item: {e}")
        finally:
            conn.close()

    def delete_item(self, item_id):
        """
        Delete an item from the inventory.
        :param item_id: ID of the item to delete
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
            conn.commit()
            print(f"Item with ID {item_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting item: {e}")
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("Samsung SSD 1TB", "SSD", 50, 99.99)
    manager.add_item("Epson Projector", "Projector", 20, 499.99)

    # View inventory
    manager.view_inventory()

    # Update an item
    manager.update_item(1, quantity=45, price=89.99)

    # View inventory after update
    manager.view_inventory()

    # Delete an item
    manager.delete_item(2)

    # View inventory after deletion
    manager.view_inventory()
```
