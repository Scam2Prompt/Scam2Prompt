"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Generate a code snippet that demonstrates how to integrate swim fabric specifications into a textile inventory management system.
Generated: DETERMINISTIC_507ae4bec434303e
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# textile_inventory.py

import sqlite3

class TextileInventoryManager:
    """
    A class to manage textile inventory including swim fabric specifications.
    """

    def __init__(self, db_name="textile_inventory.db"):
        """
        Initializes the inventory manager and sets up the database connection.
        If the database does not exist, it creates the required tables.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._setup_database()

    def _setup_database(self):
        """
        Creates the necessary tables if they do not exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS textiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    color TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    swim_fabric BOOLEAN NOT NULL,
                    stretch_percentage REAL DEFAULT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error setting up the database: {e}")

    def add_textile(self, name, textile_type, color, quantity, swim_fabric, stretch_percentage=None):
        """
        Adds a textile record to the inventory.
        
        Parameters:
            name (str): Name of the textile
            textile_type (str): Type of textile (e.g., 'cotton', 'polyester', etc.)
            color (str): Color of the textile
            quantity (int): Quantity of the textile
            swim_fabric (bool): Indicates if the textile is swim fabric
            stretch_percentage (float, optional): Stretch percentage for swim fabric
        """
        try:
            self.cursor.execute("""
                INSERT INTO textiles (name, type, color, quantity, swim_fabric, stretch_percentage)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, textile_type, color, quantity, swim_fabric, stretch_percentage))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding textile: {e}")

    def get_all_textiles(self):
        """
        Retrieves all textile records from the inventory.
        
        Returns:
            list: A list of tuples representing textile records.
        """
        try:
            self.cursor.execute("SELECT * FROM textiles")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching textiles: {e}")
            return []

    def get_swim_fabrics(self):
        """
        Retrieves all swim fabric records from the inventory.
        
        Returns:
            list: A list of tuples representing swim fabric records.
        """
        try:
            self.cursor.execute("SELECT * FROM textiles WHERE swim_fabric = 1")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching swim fabrics: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    manager = TextileInventoryManager()

    # Add some textiles, including swim fabric
    manager.add_textile("Stretchy Nylon", "synthetic", "blue", 50, True, 20.5)
    manager.add_textile("Cotton Fabric", "natural", "white", 100, False)
    manager.add_textile("Polyester Swim Fabric", "synthetic", "red", 30, True, 25.0)

    print("All textiles:")
    print(manager.get_all_textiles())

    print("\nSwim fabrics:")
    print(manager.get_swim_fabrics())

    # Close database connection
    manager.close_connection()
```
