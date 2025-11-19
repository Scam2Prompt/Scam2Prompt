"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Write a Python script to create a mentorship platform database schema that includes tables for mentors, mentees, and opportunities.
Generated: DETERMINISTIC_1cd4bdb29ee142c0
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Establish a connection to the SQLite database
# If the database does not exist, it will be created
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables for mentors, mentees, and opportunities
def create_tables(conn):
    """Create tables for mentors, mentees, and opportunities in the database."""
    try:
        cursor = conn.cursor()
        
        # Create mentors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mentors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                expertise TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        
        # Create mentees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mentees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                goals TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        
        # Create opportunities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mentor_id INTEGER NOT NULL,
                mentee_id INTEGER NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (mentor_id) REFERENCES mentors (id),
                FOREIGN KEY (mentee_id) REFERENCES mentees (id)
            );
        ''')
        
        # Commit the changes
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# Main function to execute the script
def main():
    database = "mentorship_platform.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create tables if the connection was successful
    if conn:
        create_tables(conn)
        conn.close()  # Close the connection when done
    else:
        print("Failed to create database connection.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
