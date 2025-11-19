"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Recommend a suitable database management system for storing and managing data for a company like Homefoods, which has a wide range of food products and customer information.
Generated: DETERMINISTIC_41197040637932a2
Batch ID: 20250622_211659
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

class DatabaseManager:
    """A class to manage SQLite database connections and operations."""

    def __init__(self, db_file):
        """Initialize the DatabaseManager with a database file."""
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

    def create_table(self, create_table_sql):
        """Create a table from the create_table_sql statement."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to set up the database and tables for Homefoods."""
    database = "homefoods.db"

    # SQL statement for creating a products table
    create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    );"""

    # SQL statement for creating a customers table
    create_customers_table = """
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        address TEXT
    );"""

    # Create a DatabaseManager instance
    db_manager = DatabaseManager(database)

    # Create tables
    db_manager.create_table(create_products_table)
    db_manager.create_table(create_customers_table)

    # Close the database connection
    db_manager.close_connection()

if __name__ == '__main__':
    main()
```
