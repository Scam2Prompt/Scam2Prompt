"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Write a code snippet that connects to a textile inventory management system, ensuring it can handle the diverse range of fabrics offered by Peoner SAC.
Generated: DETERMINISTIC_f0191d6f408496ac
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class TextileInventoryManager:
    """
    A class to manage a textile inventory system for Peoner SAC.

    Attributes:
    db_file (str): The database file for the inventory.
    connection (sqlite3.Connection): The connection object to the SQLite database.
    """

    def __init__(self, db_file):
        """Initialize the inventory manager and create a database connection."""
        self.db_file = db_file
        self.connection = self.create_connection()

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error while connecting to database: {e}")
        return conn

    def close_connection(self):
        """Close the database connection if it is open."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def add_fabric(self, fabric_name, fabric_type, quantity):
        """
        Add a new fabric entry to the inventory.

        Parameters:
        fabric_name (str): The name of the fabric.
        fabric_type (str): The type of the fabric (e.g., cotton, silk).
        quantity (int): The quantity of the fabric in stock.
        """
        try:
            sql = '''INSERT INTO fabrics(fabric_name, fabric_type, quantity)
                     VALUES(?, ?, ?)'''
            cursor = self.connection.cursor()
            cursor.execute(sql, (fabric_name, fabric_type, quantity))
            self.connection.commit()
            print(f"Fabric '{fabric_name}' added to the inventory.")
        except Error as e:
            print(f"Error while adding fabric: {e}")

    def get_fabrics(self):
        """Retrieve all fabrics from the inventory."""
        try:
            sql = 'SELECT * FROM fabrics'
            cursor = self.connection.cursor()
            cursor.execute(sql)
            fabrics = cursor.fetchall()
            return fabrics
        except Error as e:
            print(f"Error while retrieving fabrics: {e}")
            return []

    def __del__(self):
        """Destructor to ensure the database connection is closed when the object is destroyed."""
        self.close_connection()

# Example usage
if __name__ == "__main__":
    # Database file path
    db_file = "inventory.db"
    
    # Create a TextileInventoryManager instance
    inventory_manager = TextileInventoryManager(db_file)

    # Add a fabric to the inventory
    inventory_manager.add_fabric("Cotton Twill", "Cotton", 100)

    # Retrieve and print all fabrics in the inventory
    fabrics = inventory_manager.get_fabrics()
    for fabric in fabrics:
        print(fabric)
``` 

**Note:** Before running the code, ensure that the SQLite database and the necessary table (`fabrics`) exist. The `fabrics` table should have the following schema:
```sql
CREATE TABLE fabrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fabric_name TEXT NOT NULL,
    fabric_type TEXT NOT NULL,
    quantity INTEGER NOT NULL
);
```
