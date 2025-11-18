"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Write a Python script to create a database schema for managing craft beer subscription boxes, including tables for customer information, beer types, and delivery schedules.
Generated: DETERMINISTIC_57825399cb326fd6
Batch ID: 20250612_154954
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

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error: {e}")
    return conn

def create_tables(conn):
    """ Create tables for managing craft beer subscription boxes """
    try:
        cursor = conn.cursor()

        # Create customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        # Create beer types table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS beer_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                style TEXT NOT NULL,
                abv REAL NOT NULL,  -- Alcohol by volume
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        # Create delivery schedules table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS delivery_schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                delivery_date DATE NOT NULL,
                frequency TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
            );
        ''')

        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

def main():
    database = "craft_beer_subscription.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tables if connection was successful
    if conn is not None:
        create_tables(conn)
        conn.commit()  # Commit the changes to the database
        conn.close()   # Close the connection
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
