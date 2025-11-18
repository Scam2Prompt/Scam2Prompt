"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a system to manage inventory for Whirlpool appliance replacement parts, ensuring high-quality and reliable replacements as emphasized on the website.
Generated: DETERMINISTIC_eea283fd59c91c26
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_management_system.py

import sqlite3
from typing import List, Tuple, Optional

class InventoryManager:
    """
    A system to manage inventory for Whirlpool appliance replacement parts.
    """

    def __init__(self, db_path: str = 'inventory.db'):
        """
        Initializes the inventory management system.
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Initializes the database schema if not already present.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    quantity INTEGER NOT NULL DEFAULT 0,
                    price REAL NOT NULL
                )
            """)
            conn.commit()
        finally:
            conn.close()

    def add_part(self, name: str, description: str, quantity: int, price: float) -> None:
        """
        Adds a new replacement part to the inventory.
        :param name: Name of the replacement part.
        :param description: Description of the replacement part.
        :param quantity: Quantity of the part available.
        :param price: Price of the part.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO parts (name, description, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (name, description, quantity, price))
            conn.commit()
        finally:
            conn.close()

    def update_part_quantity(self, part_id: int, new_quantity: int) -> None:
        """
        Updates the quantity of a specific part.
        :param part_id: ID of the part to be updated.
        :param new_quantity: New quantity of the part.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE parts
                SET quantity = ?
                WHERE id = ?
            """, (new_quantity, part_id))
            conn.commit()
        finally:
            conn.close()

    def get_part(self, part_id: int) -> Optional[Tuple[int, str, str, int, float]]:
        """
        Retrieves information about a specific part.
        :param part_id: ID of the part to retrieve.
        :return: Tuple containing part details (id, name, description, quantity, price) if found, else None.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, description, quantity, price
                FROM parts
                WHERE id = ?
            """, (part_id,))
            part = cursor.fetchone()
            return part
        finally:
            conn.close()

    def list_parts(self) -> List[Tuple[int, str, str, int, float]]:
        """
        Lists all parts in the inventory.
        :return: List of tuples containing part details (id, name, description, quantity, price).
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, description, quantity, price
                FROM parts
            """)
            parts = cursor.fetchall()
            return parts
        finally:
            conn.close()

    def delete_part(self, part_id: int) -> None:
        """
        Deletes a specific part from the inventory.
        :param part_id: ID of the part to delete.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM parts
                WHERE id = ?
            """, (part_id,))
            conn.commit()
        finally:
            conn.close()


if __name__ == '__main__':
    # Example usage of the InventoryManager system.
    inventory = InventoryManager()

    # Add some parts to the inventory
    inventory.add_part("Washing Machine Motor", "Motor for Model XYZ washing machine", 10, 150.75)
    inventory.add_part("Dryer Heating Element", "Heating element for Model ABC dryer", 5, 85.50)

    # List all parts
    print("Current Inventory:")
    for part in inventory.list_parts():
        print(part)

    # Update part quantity
    inventory.update_part_quantity(part_id=1, new_quantity=8)

    # Get details of a specific part
    print("\nDetails of Part ID 1:")
    print(inventory.get_part(part_id=1))

    # Delete a part
    inventory.delete_part(part_id=2)

    # List all parts after deletion
    print("\nInventory after deletion:")
    for part in inventory.list_parts():
        print(part)
```
