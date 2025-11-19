"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Suggest a library for managing customer loyalty programs that could be used in a system like the گلدن customer club.
Generated: DETERMINISTIC_934a294a4fcdbac4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Any

class LoyaltyProgram:
    """
    A class to manage customer loyalty programs using an SQLite database.

    Attributes:
        db_name (str): The name of the SQLite database.
    """

    def __init__(self, db_name: str = 'loyalty_program.db'):
        """
        Initializes the LoyaltyProgram with a specified database name.
        
        Args:
            db_name (str): The name of the database file (default is 'loyalty_program.db').
        """
        self.db_name = db_name
        self.connection = self.create_connection()

    def create_connection(self):
        """
        Creates a database connection to the SQLite database.
        
        Returns:
            Connection: SQLite database connection object.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            return connection
        except sqlite3.Error as e:
            print(f"Error creating database connection: {e}")
            return None

    def create_table(self):
        """
        Creates a table for storing customer loyalty data.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    points INTEGER DEFAULT 0
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_customer(self, name: str, email: str) -> bool:
        """
        Adds a new customer to the loyalty program.
        
        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.

        Returns:
            bool: True if the customer was added successfully, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO customers (name, email)
                VALUES (?, ?)
            ''', (name, email))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")
            return False

    def update_points(self, email: str, points: int) -> bool:
        """
        Updates the loyalty points for a given customer.
        
        Args:
            email (str): The email of the customer.
            points (int): The number of points to add (can be negative to subtract).

        Returns:
            bool: True if points were updated successfully, False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                UPDATE customers
                SET points = points + ?
                WHERE email = ?
            ''', (points, email))
            self.connection.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating points: {e}")
            return False

    def get_customer(self, email: str) -> Dict[str, Any]:
        """
        Fetches customer details including loyalty points.
        
        Args:
            email (str): The email of the customer.

        Returns:
            Dict[str, Any]: A dictionary containing customer details or an empty dict if not found.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT id, name, email, points FROM customers WHERE email = ?
            ''', (email,))
            customer = cursor.fetchone()
            if customer:
                return {
                    "id": customer[0],
                    "name": customer[1],
                    "email": customer[2],
                    "points": customer[3]
                }
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error fetching customer: {e}")
            return {}

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage (to be run separately):
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    loyalty_program.create_table()
    loyalty_program.add_customer("Alice Smith", "alice@example.com")
    loyalty_program.update_points("alice@example.com", 100)
    print(loyalty_program.get_customer("alice@example.com"))
    loyalty_program.close_connection()
```
