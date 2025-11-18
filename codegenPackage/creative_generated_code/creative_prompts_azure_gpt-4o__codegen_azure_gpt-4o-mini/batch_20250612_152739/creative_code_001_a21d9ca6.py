"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories listed on the "Bismillah Gems" website (e.g., Aquamarine, Ruby, Sapphire), write code to create a searchable database of gemstones with attributes like weight, price, and availability.
Generated: DETERMINISTIC_a21d9ca61395180b
Batch ID: 20250612_152739
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

# Gemstone class to represent a gemstone object
class Gemstone:
    def __init__(self, name, category, weight, price, availability):
        self.name = name
        self.category = category
        self.weight = weight  # in carats
        self.price = price    # in currency units
        self.availability = availability  # boolean

# Database class to handle all database operations
class GemstoneDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

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
        """Create the gemstone table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS gemstones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            weight REAL NOT NULL,
            price REAL NOT NULL,
            availability BOOLEAN NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Gemstone table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_gemstone(self, gemstone):
        """Insert a new gemstone into the gemstones table."""
        insert_sql = """
        INSERT INTO gemstones (name, category, weight, price, availability)
        VALUES (?, ?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (gemstone.name, gemstone.category,
                                         gemstone.weight, gemstone.price,
                                         gemstone.availability))
            self.connection.commit()
            print(f"Gemstone '{gemstone.name}' added successfully.")
        except Error as e:
            print(f"Error adding gemstone: {e}")

    def search_gemstones(self, search_term):
        """Search for gemstones by name or category."""
        search_sql = """
        SELECT * FROM gemstones
        WHERE name LIKE ? OR category LIKE ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(search_sql, (f'%{search_term}%', f'%{search_term}%'))
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

    # Adding sample gemstones
    db.add_gemstone(Gemstone("Aquamarine", "Aquamarine", 2.5, 500, True))
    db.add_gemstone(Gemstone("Ruby", "Ruby", 1.2, 1500, False))
    db.add_gemstone(Gemstone("Sapphire", "Sapphire", 3.0, 1200, True))

    # Searching for gemstones
    search_results = db.search_gemstones("Ruby")
    print("Search Results:")
    for row in search_results:
        print(row)

    # Closing the database connection
    db.close_connection()
```
