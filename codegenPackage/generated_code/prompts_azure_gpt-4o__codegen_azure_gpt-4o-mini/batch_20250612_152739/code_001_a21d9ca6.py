"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories listed on the "Bismillah Gems" website (e.g., Aquamarine, Ruby, Sapphire), write code to create a searchable database of gemstones with attributes like weight, price, and availability.
Generated: DETERMINISTIC_a21d9ca61395180b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

# Define a class to manage the gemstone database
class GemstoneDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for gemstones if it doesn't exist."""
        try:
            sql_create_gemstones_table = """
            CREATE TABLE IF NOT EXISTS gemstones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                price REAL NOT NULL,
                availability INTEGER NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_gemstones_table)
            print("Gemstones table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_gemstone(self, name, weight, price, availability):
        """Insert a new gemstone into the gemstones table."""
        sql = '''INSERT INTO gemstones(name, weight, price, availability)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, weight, price, availability))
            self.connection.commit()
            print(f"Gemstone '{name}' added successfully.")
        except Error as e:
            print(f"Error adding gemstone: {e}")

    def search_gemstones(self, name=None, min_price=None, max_price=None):
        """Search for gemstones based on name and price range."""
        query = "SELECT * FROM gemstones WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if min_price is not None:
            query += " AND price >= ?"
            params.append(min_price)
        if max_price is not None:
            query += " AND price <= ?"
            params.append(max_price)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error searching gemstones: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = GemstoneDatabase("gemstones.db")
    db.create_table()
    
    # Adding sample gemstones
    db.add_gemstone("Aquamarine", 1.5, 200.0, 10)
    db.add_gemstone("Ruby", 2.0, 500.0, 5)
    db.add_gemstone("Sapphire", 1.2, 300.0, 8)

    # Searching for gemstones
    results = db.search_gemstones(name="Ruby", min_price=100)
    print("Search Results:", results)

    # Close the database connection
    db.close_connection()
```
