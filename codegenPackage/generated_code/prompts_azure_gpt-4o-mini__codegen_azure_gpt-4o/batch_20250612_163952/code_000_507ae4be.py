"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Generate a code snippet that demonstrates how to integrate swim fabric specifications into a textile inventory management system.
Generated: DETERMINISTIC_507ae4bec434303e
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# textile_inventory.py

import sqlite3

class TextileInventoryManager:
    """
    A class to manage textile inventory, including swim fabric specifications.
    """

    def __init__(self, db_name="textile_inventory.db"):
        """
        Initialize the TextileInventoryManager with a SQLite database connection.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None
        self._connect_to_db()
        self._initialize_tables()

    def _connect_to_db(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def _initialize_tables(self):
        """
        Create the necessary tables for textile inventory management.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS swim_fabric (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    material TEXT NOT NULL,
                    stretch_percentage REAL NOT NULL,
                    uv_protection BOOLEAN NOT NULL,
                    color TEXT NOT NULL,
                    stock_quantity INTEGER NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing tables: {e}")
            raise

    def add_swim_fabric(self, name, material, stretch_percentage, uv_protection, color, stock_quantity):
        """
        Add a new swim fabric specification to the inventory.

        :param name: Name of the swim fabric.
        :param material: Material of the swim fabric (e.g., polyester, spandex).
        :param stretch_percentage: Stretch percentage of the fabric.
        :param uv_protection: Whether the fabric has UV protection (True/False).
        :param color: Color of the fabric.
        :param stock_quantity: Quantity of the fabric in stock.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO swim_fabric (name, material, stretch_percentage, uv_protection, color, stock_quantity)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, material, stretch_percentage, uv_protection, color, stock_quantity))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding swim fabric: {e}")
            raise

    def get_swim_fabric(self, fabric_id):
        """
        Retrieve swim fabric details by ID.

        :param fabric_id: ID of the swim fabric.
        :return: Dictionary containing swim fabric details or None if not found.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM swim_fabric WHERE id = ?", (fabric_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "material": row[2],
                    "stretch_percentage": row[3],
                    "uv_protection": bool(row[4]),
                    "color": row[5],
                    "stock_quantity": row[6]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving swim fabric: {e}")
            raise

    def update_stock_quantity(self, fabric_id, new_quantity):
        """
        Update the stock quantity of a swim fabric.

        :param fabric_id: ID of the swim fabric.
        :param new_quantity: New stock quantity.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE swim_fabric
                SET stock_quantity = ?
                WHERE id = ?
            """, (new_quantity, fabric_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating stock quantity: {e}")
            raise

    def delete_swim_fabric(self, fabric_id):
        """
        Delete a swim fabric from the inventory.

        :param fabric_id: ID of the swim fabric.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM swim_fabric WHERE id = ?", (fabric_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting swim fabric: {e}")
            raise

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    manager = TextileInventoryManager()

    # Add a swim fabric
    manager.add_swim_fabric(
        name="Ocean Blue Swim Fabric",
        material="Polyester-Spandex",
        stretch_percentage=20.5,
        uv_protection=True,
        color="Blue",
        stock_quantity=100
    )

    # Retrieve swim fabric details
    fabric = manager.get_swim_fabric(1)
    print(fabric)

    # Update stock quantity
    manager.update_stock_quantity(1, 120)

    # Delete swim fabric
    manager.delete_swim_fabric(1)

    # Close the connection
    manager.close_connection()
```
