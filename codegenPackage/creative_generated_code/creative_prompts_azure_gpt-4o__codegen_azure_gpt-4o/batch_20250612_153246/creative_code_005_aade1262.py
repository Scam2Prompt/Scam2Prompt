"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Create a program to track and manage spare parts inventory for solar water heaters and gas boilers, referencing the after-sales service model mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_aade1262375c64a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Spare Parts Inventory Management System
Description: This program tracks and manages spare parts inventory for solar water heaters and gas boilers.
Author: Expert Programmer
Language: Python
Version: 3.x
"""

import sqlite3
import datetime

class SparePartsInventory:
    def __init__(self, db_name="spare_parts_inventory.db"):
        """
        Constructor initializes the database connection and ensures the database schema is set up.
        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = None
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the database and create necessary tables if they don't already exist.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()
            # Create table for spare parts inventory
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS spare_parts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    part_name TEXT NOT NULL,
                    part_type TEXT NOT NULL CHECK (part_type IN ('Solar Water Heater', 'Gas Boiler')),
                    quantity INTEGER NOT NULL DEFAULT 0,
                    last_updated TIMESTAMP NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def add_part(self, part_name, part_type, quantity):
        """
        Add a new spare part to the inventory.
        :param part_name: Name of the spare part
        :param part_type: Type of the spare part ('Solar Water Heater' or 'Gas Boiler')
        :param quantity: Initial quantity of the spare part
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO spare_parts (part_name, part_type, quantity, last_updated)
                VALUES (?, ?, ?, ?)
            """, (part_name, part_type, quantity, datetime.datetime.now()))
            self.connection.commit()
            print(f"Part '{part_name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding part: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def update_quantity(self, part_name, quantity):
        """
        Update the quantity of an existing spare part.
        :param part_name: Name of the spare part
        :param quantity: New quantity of the spare part
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE spare_parts
                SET quantity = ?, last_updated = ?
                WHERE part_name = ?
            """, (quantity, datetime.datetime.now(), part_name))
            self.connection.commit()
            print(f"Quantity for part '{part_name}' updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating quantity: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def get_inventory(self):
        """
        Retrieve the current inventory of spare parts.
        :return: List of dictionaries containing spare part details
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM spare_parts")
            rows = cursor.fetchall()
            inventory = [
                {
                    "id": row[0],
                    "part_name": row[1],
                    "part_type": row[2],
                    "quantity": row[3],
                    "last_updated": row[4]
                }
                for row in rows
            ]
            return inventory
        except sqlite3.Error as e:
            print(f"Error retrieving inventory: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def delete_part(self, part_name):
        """
        Delete a spare part from the inventory.
        :param part_name: Name of the spare part to delete
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM spare_parts WHERE part_name = ?", (part_name,))
            self.connection.commit()
            print(f"Part '{part_name}' deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting part: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

# Example usage
if __name__ == "__main__":
    inventory = SparePartsInventory()

    # Add some parts
    inventory.add_part("Solar Panel", "Solar Water Heater", 50)
    inventory.add_part("Gas Valve", "Gas Boiler", 30)

    # Update quantity of a part
    inventory.update_quantity("Gas Valve", 40)

    # Get and print the inventory
    current_inventory = inventory.get_inventory()
    print("Current Inventory:")
    for item in current_inventory:
        print(item)

    # Delete a part
    inventory.delete_part("Solar Panel")

    # Close the database connection
    inventory.close_connection()
```
