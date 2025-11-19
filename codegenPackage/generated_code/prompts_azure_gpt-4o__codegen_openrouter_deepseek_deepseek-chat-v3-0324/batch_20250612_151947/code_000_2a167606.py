"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write Python code to create a database schema for storing information about "Social Impact Heroes," including categories like "Stars Making a Social Impact," "Young Social Impact Heroes," and "Social Impact Investors."
Generated: DETERMINISTIC_2a167606054ea92c
Batch ID: 20250612_151947
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

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """Create tables for Social Impact Heroes database."""
    sql_create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    );
    """

    sql_create_heroes_table = """
    CREATE TABLE IF NOT EXISTS heroes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bio TEXT,
        achievements TEXT,
        category_id INTEGER NOT NULL,
        year_recognized INTEGER,
        website_url TEXT,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    );
    """

    sql_create_investors_table = """
    CREATE TABLE IF NOT EXISTS investors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        organization TEXT,
        investment_focus TEXT,
        notable_investments TEXT,
        website_url TEXT,
        year_recognized INTEGER
    );
    """

    try:
        c = conn.cursor()
        c.execute(sql_create_categories_table)
        c.execute(sql_create_heroes_table)
        c.execute(sql_create_investors_table)
        conn.commit()
    except Error as e:
        print(e)

def insert_initial_categories(conn):
    """Insert initial category data."""
    categories = [
        ("Stars Making a Social Impact", "Celebrities using their platform for social good"),
        ("Young Social Impact Heroes", "Youth making significant contributions to society"),
        ("Social Impact Investors", "Individuals investing in social causes and enterprises")
    ]

    try:
        c = conn.cursor()
        c.executemany("INSERT OR IGNORE INTO categories(name, description) VALUES(?, ?)", categories)
        conn.commit()
    except Error as e:
        print(e)

def main():
    database = "social_impact_heroes.db"

    # Create database connection
    conn = create_connection(database)

    if conn is not None:
        # Create tables
        create_tables(conn)

        # Insert initial categories
        insert_initial_categories(conn)

        # Close connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
