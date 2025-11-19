"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Suggest a library for managing inventory of construction materials, specifically for products like compensados and doors, as highlighted by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_59a3bb272d4b3a38
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation using Python. It leverages the popular `sqlite3` library to manage inventory data in a database, ensuring reliability and scalability.

```python
import sqlite3
from typing import List, Dict

class InventoryManager:
    """
    A class to manage inventory for construction materials like compensados and doors.
    Uses SQLite for persistent storage.
    """

    def __init__(self, db_name: str = "inventory.db"):
        """
        Initializes the InventoryManager and creates a database connection.
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None
        self._initialize_database()

    def _initialize_database(self):
        """
        Initializes the database and creates necessary tables if they do not exist.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            # Create the inventory table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL
                )
            """)
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def add_item(self, product_name: str, category: str, quantity: int, unit_price: float):
        """
        Adds a new item to the inventory.
        Args:
            product_name (str): Name of the product.
            category (str): Category of the product (e.g., "compensados", "doors").
            quantity (int): Quantity in stock.
            unit_price (float): Price per unit.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            cursor.execute("""
                INSERT INTO inventory (product_name, category, quantity, unit_price)
                VALUES (?, ?, ?, ?)
            """, (product_name, category, quantity, unit_price))
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding item to inventory: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def update_quantity(self, product_id: int, new_quantity: int):
        """
        Updates the quantity of a specific product in the inventory.
        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity in stock.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            cursor.execute("""
                UPDATE inventory
                SET quantity = ?
                WHERE id = ?
            """, (new_quantity, product_id))
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating item quantity: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def delete_item(self, product_id: int):
        """
        Deletes an item from the inventory by its ID.
        Args:
            product_id (int): ID of the product to delete.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            cursor.execute("""
                DELETE FROM inventory
                WHERE id = ?
            """, (product_id,))
            
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting item from inventory: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def get_all_items(self) -> List[Dict]:
        """
        Retrieves all items from the inventory.
        Returns:
            List[Dict]: A list of dictionaries containing inventory data.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            
            items = [
                {
                    "id": row[0],
                    "product_name": row[1],
                    "category": row[2],
                    "quantity": row[3],
                    "unit_price": row[4]
                }
                for row in rows
            ]
            
            return items
        except sqlite3.Error as e:
            print(f"Error retrieving inventory items: {e}")
            return []
        finally:
            if self.connection:
                self.connection.close()

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add sample items
    manager.add_item("Compensado A", "compensados", 50, 25.5)
    manager.add_item("Wooden Door", "doors", 20, 120.0)

    # Retrieve and print all items
    items = manager.get_all_items()
    print("Inventory:")
    for item in items:
        print(item)

    # Update quantity
    manager.update_quantity(product_id=1, new_quantity=60)

    # Delete an item
    manager.delete_item(product_id=2)

    # Final inventory state
    print("Updated Inventory:")
    items = manager.get_all_items()
    for item in items:
        print(item)
```

This code provides full functionality for managing an inventory of construction materials, including adding, updating, deleting, and retrieving items. It adheres to best practices with proper error handling and documentation.
