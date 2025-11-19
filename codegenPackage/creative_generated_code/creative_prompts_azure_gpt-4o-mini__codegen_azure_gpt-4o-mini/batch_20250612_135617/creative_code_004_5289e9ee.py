"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Illustrate how to implement a warehouse management system that aligns with the logistics and warehousing services provided by Portline Shipping.
Generated: DETERMINISTIC_5289e9ee2d1e06c8
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Optional

class WarehouseManagementSystem:
    """
    A class to manage warehouse operations such as adding items, retrieving inventory,
    and processing shipments.
    """

    def __init__(self, db_name: str):
        """
        Initialize the WarehouseManagementSystem with a SQLite database.
        
        :param db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables in the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY,
                        item_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        location TEXT NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_item(self, item_name: str, quantity: int, location: str) -> None:
        """
        Add an item to the inventory.

        :param item_name: Name of the item.
        :param quantity: Quantity of the item.
        :param location: Storage location of the item in the warehouse.
        """
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO inventory (item_name, quantity, location)
                    VALUES (?, ?, ?)
                ''', (item_name, quantity, location))
        except sqlite3.Error as e:
            print(f"Error adding item: {e}")

    def retrieve_inventory(self) -> List[Dict[str, Optional[str]]]:
        """
        Retrieve the list of items in the inventory.

        :return: A list of dictionaries containing inventory items.
        """
        try:
            cursor = self.conn.execute('SELECT * FROM inventory')
            items = cursor.fetchall()
            return [{'id': row[0], 'item_name': row[1], 'quantity': row[2], 'location': row[3]} for row in items]
        except sqlite3.Error as e:
            print(f"Error retrieving inventory: {e}")
            return []

    def process_shipment(self, item_id: int, quantity: int) -> None:
        """
        Process a shipment by updating the quantity of an item.

        :param item_id: The ID of the item to be shipped.
        :param quantity: The quantity to be shipped.
        """
        try:
            with self.conn:
                cur = self.conn.execute('SELECT quantity FROM inventory WHERE id = ?', (item_id,))
                current_quantity = cur.fetchone()
                
                if current_quantity is None:
                    print(f"Item ID {item_id} not found.")
                    return

                if current_quantity[0] < quantity:
                    print(f"Insufficient quantity for item ID {item_id}. Current quantity is {current_quantity[0]}.")
                    return

                self.conn.execute('''
                    UPDATE inventory
                    SET quantity = quantity - ?
                    WHERE id = ?
                ''', (quantity, item_id))

        except sqlite3.Error as e:
            print(f"Error processing shipment: {e}")

    def close(self):
        """Close the database connection."""
        self.conn.close()

if __name__ == "__main__":
    # Example usage of the WarehouseManagementSystem
    wms = WarehouseManagementSystem('warehouse.db')

    # Add items to the inventory
    wms.add_item('Widget A', 100, 'Shelf 1')
    wms.add_item('Widget B', 50, 'Shelf 2')

    # Retrieve and print the inventory
    inventory = wms.retrieve_inventory()
    print(f"Current Inventory: {inventory}")

    # Process a shipment
    wms.process_shipment(item_id=1, quantity=20)

    # Retrieve and print the inventory again
    updated_inventory = wms.retrieve_inventory()
    print(f"Updated Inventory: {updated_inventory}")

    # Close the database connection
    wms.close()
```
