"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Generate code to create a searchable database for automotive parts, including categories such as "filtrations," "amortisseurs," and "courroie," based on the inventory structure mentioned on the Distribution Pièces Service website.
Generated: DETERMINISTIC_56dcefffc9408da9
Batch ID: 20250612_151752
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

class Database:
    """A class to manage a SQLite database for automotive parts."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for automotive parts if it doesn't already exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
            print("Table 'parts' created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_part(self, name, category, price, stock):
        """Add a new part to the database."""
        sql = ''' INSERT INTO parts(name, category, price, stock) VALUES(?,?,?,?) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, category, price, stock))
            self.connection.commit()
            print(f"Part '{name}' added successfully.")
        except Error as e:
            print(f"Error adding part: {e}")

    def search_parts(self, query):
        """Search for parts in the database by name or category."""
        cursor = self.connection.cursor()
        sql = ''' SELECT * FROM parts WHERE name LIKE ? OR category LIKE ? '''
        try:
            cursor.execute(sql, (f'%{query}%', f'%{query}%'))
            results = cursor.fetchall()
            if results:
                print("Search Results:")
                for row in results:
                    print(row)
            else:
                print("No parts found.")
        except Error as e:
            print(f"Error searching parts: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Example usage of the Database class

    # Initialize the database
    db = Database("automotive_parts.db")

    # Create the parts table
    db.create_table()

    # Add some parts
    db.add_part("Oil Filter", "filtrations", 15.99, 100)
    db.add_part("Air Filter", "filtrations", 22.49, 50)
    db.add_part("Shock Absorber", "amortisseurs", 75.00, 20)
    db.add_part("Timing Belt", "courroie", 35.00, 10)

    # Search for parts
    db.search_parts("filtrations")

    # Close the database connection
    db.close_connection()
```
