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

Below is Python code leveraging `SQLite` for the inventory management system. SQLite is cost-effective, easy to use, and doesn't require a separate server.

```python
import sqlite3

# Inventory Management System
class InventoryManagementSystem:
    def __init__(self, db_name="inventory.db"):
        """
        Initialize the InventoryManagementSystem with a database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the SQLite database and create necessary tables.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create the inventory table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price_per_unit REAL NOT NULL
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_item(self, name, quantity, price_per_unit):
        """
        Add an item to the inventory.
        :param name: Name of the item.
        :param quantity: Quantity of the item.
        :param price_per_unit: Price per unit of the item.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO inventory (name, quantity, price_per_unit)
                VALUES (?, ?, ?)
            """, (name, quantity, price_per_unit))

            conn.commit()
            print(f"Item '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding item: {e}")
        finally:
            conn.close()

    def update_item(self, item_id, name=None, quantity=None, price_per_unit=None):
        """
        Update an item's details in the inventory.
        :param item_id: ID of the item to update.
        :param name: New name of the item (optional).
        :param quantity: New quantity of the item (optional).
        :param price_per_unit: New price per unit of the item (optional).
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Build the SQL query based on the provided arguments
            updates = []
            params = []
            if name:
                updates.append("name = ?")
                params.append(name)
            if quantity:
                updates.append("quantity = ?")
                params.append(quantity)
            if price_per_unit:
                updates.append("price_per_unit = ?")
                params.append(price_per_unit)

            params.append(item_id)
            query = f"UPDATE inventory SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)

            conn.commit()
            print(f"Item ID '{item_id}' updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating item: {e}")
        finally:
            conn.close()

    def delete_item(self, item_id):
        """
        Delete an item from the inventory.
        :param item_id: ID of the item to delete.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
            conn.commit()
            print(f"Item ID '{item_id}' deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting item: {e}")
        finally:
            conn.close()

    def list_items(self):
        """
        List all items in the inventory.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM inventory")
            items = cursor.fetchall()

            print("Current Inventory:")
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price/Unit: ${item[3]:.2f}")
        except sqlite3.Error as e:
            print(f"Error fetching items: {e}")
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    # Initialize the inventory system
    inventory_system = InventoryManagementSystem()

    # Add items to the inventory
    inventory_system.add_item("Widget", 100, 2.50)
    inventory_system.add_item("Gadget", 50, 5.75)

    # List all items
    inventory_system.list_items()

    # Update an item
    inventory_system.update_item(item_id=1, name="Super Widget", quantity=150)

    # Delete an item
    inventory_system.delete_item(item_id=2)

    # List items again
    inventory_system.list_items()
```

This code defines a simple inventory management system using SQLite as the database backend. It includes operations for adding, updating, deleting, and listing inventory items.
