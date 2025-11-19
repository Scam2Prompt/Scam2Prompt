"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Generate code to create a searchable database for automotive parts, including categories such as "filtrations," "amortisseurs," and "courroie," based on the inventory structure mentioned on the Distribution Pièces Service website.
Generated: DETERMINISTIC_56dcefffc9408da9
Batch ID: 20250612_151752
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

# Define the database file
DATABASE_FILE = 'automotive_parts.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table for automotive parts if it doesn't already exist."""
    try:
        sql_create_parts_table = """
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_parts_table)
        print("Parts table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_part(conn, part):
    """Insert a new part into the parts table."""
    sql = '''INSERT INTO parts(name, category, description, price, stock)
             VALUES(?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, part)
        conn.commit()
        print(f"Part added: {part[0]}")
    except Error as e:
        print(f"Error adding part: {e}")

def search_parts(conn, search_term):
    """Search for parts by name or category."""
    sql = '''SELECT * FROM parts WHERE name LIKE ? OR category LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{search_term}%', f'%{search_term}%'))
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error searching parts: {e}")
        return []

def main():
    # Create a database connection
    conn = create_connection(DATABASE_FILE)

    if conn:
        # Create the parts table
        create_table(conn)

        # Example parts to add
        parts_to_add = [
            ('Oil Filter', 'Filtrations', 'High-quality oil filter', 15.99, 100),
            ('Air Filter', 'Filtrations', 'Premium air filter', 25.50, 50),
            ('Shock Absorber', 'Amortisseurs', 'Durable shock absorber', 75.00, 30),
            ('Timing Belt', 'Courroie', 'Timing belt for various models', 45.00, 20)
        ]

        # Add parts to the database
        for part in parts_to_add:
            add_part(conn, part)

        # Search for parts
        search_term = input("Enter part name or category to search: ")
        results = search_parts(conn, search_term)

        # Display search results
        if results:
            print("Search Results:")
            for row in results:
                print(row)
        else:
            print("No parts found.")

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
