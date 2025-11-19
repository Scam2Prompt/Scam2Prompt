"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Write Python code to integrate an inventory management system for tracking the availability of stainless steel, aluminum, copper, and other metals, using a database schema tailored for Meta+ product categories.
Generated: DETERMINISTIC_9965ca47193440db
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from enum import Enum
from typing import Dict, List

# Define an Enum for metal types
class MetalType(str, Enum):
    STAINLESS_STEEL = "stainless steel"
    ALUMINUM = "aluminum"
    COPPER = "copper"
    OTHER = "other"

# Define a class for Metal Inventory
class MetalInventory:
    def __init__(self, db_name: str):
        """
        Initialize the MetalInventory class.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the metal inventory table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS metal_inventory
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             metal_type TEXT NOT NULL,
             quantity REAL NOT NULL,
             unit_price REAL NOT NULL,
             product_category TEXT NOT NULL)
        ''')
        self.conn.commit()

    def add_metal(self, metal_type: MetalType, quantity: float, unit_price: float, product_category: str):
        """
        Add a new metal inventory entry.

        Args:
        metal_type (MetalType): The type of metal.
        quantity (float): The quantity of metal in stock.
        unit_price (float): The unit price of the metal.
        product_category (str): The Meta+ product category.

        Raises:
        ValueError: If quantity or unit_price is negative.
        """
        if quantity < 0 or unit_price < 0:
            raise ValueError("Quantity and unit price must be non-negative.")

        self.cursor.execute('''
            INSERT INTO metal_inventory (metal_type, quantity, unit_price, product_category)
            VALUES (?, ?, ?, ?)
        ''', (metal_type.value, quantity, unit_price, product_category))
        self.conn.commit()

    def update_metal(self, id: int, quantity: float = None, unit_price: float = None):
        """
        Update an existing metal inventory entry.

        Args:
        id (int): The ID of the metal inventory entry.
        quantity (float, optional): The new quantity of metal in stock. Defaults to None.
        unit_price (float, optional): The new unit price of the metal. Defaults to None.

        Raises:
        ValueError: If quantity or unit_price is negative.
        """
        if quantity is not None and quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        if unit_price is not None and unit_price < 0:
            raise ValueError("Unit price must be non-negative.")

        update_query = "UPDATE metal_inventory SET "
        params = []
        if quantity is not None:
            update_query += "quantity = ?, "
            params.append(quantity)
        if unit_price is not None:
            update_query += "unit_price = ?, "
            params.append(unit_price)
        update_query = update_query.rstrip(", ") + " WHERE id = ?"
        params.append(id)

        self.cursor.execute(update_query, params)
        self.conn.commit()

    def get_metal(self, id: int) -> Dict:
        """
        Get a metal inventory entry by ID.

        Args:
        id (int): The ID of the metal inventory entry.

        Returns:
        Dict: A dictionary containing the metal inventory entry details.
        """
        self.cursor.execute('''
            SELECT * FROM metal_inventory
            WHERE id = ?
        ''', (id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "metal_type": row[1],
                "quantity": row[2],
                "unit_price": row[3],
                "product_category": row[4]
            }
        else:
            return {}

    def get_all_metals(self) -> List[Dict]:
        """
        Get all metal inventory entries.

        Returns:
        List[Dict]: A list of dictionaries containing the metal inventory entry details.
        """
        self.cursor.execute('''
            SELECT * FROM metal_inventory
        ''')
        rows = self.cursor.fetchall()
        return [
            {
                "id": row[0],
                "metal_type": row[1],
                "quantity": row[2],
                "unit_price": row[3],
                "product_category": row[4]
            } for row in rows
        ]

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    inventory = MetalInventory("metal_inventory.db")

    # Add metals
    inventory.add_metal(MetalType.STAINLESS_STEEL, 1000, 10.99, "Meta+ Category 1")
    inventory.add_metal(MetalType.ALUMINUM, 500, 5.99, "Meta+ Category 2")

    # Get all metals
    metals = inventory.get_all_metals()
    for metal in metals:
        print(metal)

    # Update metal
    inventory.update_metal(1, quantity=800)

    # Get metal by ID
    metal = inventory.get_metal(1)
    print(metal)

    # Close connection
    inventory.close_connection()
```
