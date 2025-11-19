"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a database schema to store information about Chile Horse Riding's tours, guides, and horses, and provide a simple Python script to interact with the database.
Generated: DETERMINISTIC_256dbbf248a7bd5c
Batch ID: 20250622_210655
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

# Database schema creation
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    """ Create tables for tours, guides, and horses in the database """
    try:
        cursor = conn.cursor()
        
        # Create table for guides
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                experience_years INTEGER NOT NULL,
                bio TEXT
            );
        ''')
        
        # Create table for horses
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS horses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                breed TEXT NOT NULL,
                age INTEGER NOT NULL
            );
        ''')
        
        # Create table for tours
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tours (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                guide_id INTEGER,
                horse_id INTEGER,
                duration INTEGER NOT NULL,  -- Duration in hours
                FOREIGN KEY (guide_id) REFERENCES guides (id),
                FOREIGN KEY (horse_id) REFERENCES horses (id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

def main():
    database = "chile_horse_riding.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create tables
    if conn:
        create_tables(conn)
        conn.close()

if __name__ == '__main__':
    main()
```

This script creates a SQLite database with tables for guides, horses, and tours, including foreign key relationships. It handles errors during database connection and table creation.
