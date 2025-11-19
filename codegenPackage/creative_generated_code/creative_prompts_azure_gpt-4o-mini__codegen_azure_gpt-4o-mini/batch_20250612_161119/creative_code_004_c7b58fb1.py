"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeclaiming.site
Prompt: How do I create a database schema for storing meme claims and user data?
Generated: DETERMINISTIC_c7b58fb1f7b4d2d3
Batch ID: 20250612_161119
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

# Function to create a connection to the SQLite database
def create_connection(db_file):
    """ Create a database connection to a SQLite database. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables in the database
def create_tables(conn):
    """ Create tables for users and meme claims. """
    try:
        cursor = conn.cursor()
        
        # Create user table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Create meme claims table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS meme_claims (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                meme_url TEXT NOT NULL,
                claim TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
        """)

        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to close the database connection
def close_connection(conn):
    """ Close the database connection. """
    if conn:
        conn.close()
        print("Database connection closed.")

# Main function to orchestrate the database setup
def main():
    database = "meme_claims.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create tables
        create_tables(conn)

        # Close the connection
        close_connection(conn)

if __name__ == '__main__':
    main()
```
