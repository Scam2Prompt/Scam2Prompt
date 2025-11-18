"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate code to integrate a discount system for psychological tests, as mentioned in the Colegio de Psicólogos de Oruro's partnership with AMI-Bolivia, using Python and a database management system.
Generated: DETERMINISTIC_dc09cf18a56fad9e
Batch ID: 20250612_154010
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

class DiscountSystem:
    def __init__(self, db_file):
        """Initialize the DiscountSystem with a database file."""
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_discount_table(self):
        """Create a discounts table in the database if it does not exist."""
        try:
            sql_create_discounts_table = """ 
            CREATE TABLE IF NOT EXISTS discounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                discount_percentage REAL NOT NULL,
                min_tests INTEGER NOT NULL,
                max_tests INTEGER NOT NULL
            ); """
            cursor = self.conn.cursor()
            cursor.execute(sql_create_discounts_table)
        except Error as e:
            print(f"Error creating table: {e}")

    def add_discount(self, name, discount_percentage, min_tests, max_tests):
        """Add a new discount to the database."""
        try:
            sql_insert_discount = """ INSERT INTO discounts (name, discount_percentage, min_tests, max_tests)
                                    VALUES (?, ?, ?, ?) """
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_discount, (name, discount_percentage, min_tests, max_tests))
            self.conn.commit()
        except Error as e:
            print(f"Error inserting discount: {e}")

    def get_discount(self, num_tests):
        """Retrieve applicable discount based on the number of tests."""
        try:
            sql_select_discount = """ SELECT name, discount_percentage FROM discounts
                                    WHERE min_tests <= ? AND max_tests >= ? """
            cursor = self.conn.cursor()
            cursor.execute(sql_select_discount, (num_tests, num_tests))
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching discount: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    # Example usage of the DiscountSystem
    discount_system = DiscountSystem("psychology_tests.db")
    discount_system.create_discount_table()

    # Add some sample discounts
    discount_system.add_discount("Student Discount", 10.0, 1, 5)
    discount_system.add_discount("Bulk Discount", 20.0, 6, 10)

    # Fetch discount for a specific number of tests
    num_tests = 7
    discounts = discount_system.get_discount(num_tests)
    
    if discounts:
        print("Applicable Discounts:")
        for discount in discounts:
            print(f"Name: {discount[0]}, Discount: {discount[1]}%")
    else:
        print("No applicable discounts found.")

    # Close the database connection
    discount_system.close_connection()
```
