"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Write a script to convert the "آیین نامه مرخصی" (leave regulations) into a searchable database, allowing users to query specific rules based on keywords or categories.
Generated: DETERMINISTIC_64dfec06d3e68641
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import os

# Define the path for the SQLite database
DB_PATH = 'leave_regulations.db'

# Establish a connection to the SQLite database
def create_connection(db_path):
    """Create a new database connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to the database successfully.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create a table for leave regulations
def create_table(conn):
    """Create a table for storing leave regulations."""
    try:
        sql_create_regulations_table = '''
        CREATE TABLE IF NOT EXISTS regulations (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL
        );
        '''
        cursor = conn.cursor()
        cursor.execute(sql_create_regulations_table)
        print("Regulations table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Insert leave regulations into the database
def insert_regulation(conn, title, content, category):
    """Insert a regulation into the regulations table."""
    try:
        sql_insert_regulation = '''
        INSERT INTO regulations (title, content, category)
        VALUES (?, ?, ?);
        '''
        cursor = conn.cursor()
        cursor.execute(sql_insert_regulation, (title, content, category))
        conn.commit()
        print(f"Inserted regulation: {title}")
    except sqlite3.Error as e:
        print(f"Error inserting regulation: {e}")

# Search regulations based on keywords or categories
def search_regulations(conn, keyword=None, category=None):
    """Search for regulations based on a keyword or category."""
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM regulations WHERE 1=1"
        params = []
        
        if keyword:
            query += " AND (title LIKE ? OR content LIKE ?)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        if category:
            query += " AND category = ?"
            params.append(category)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        if results:
            print("Regulations found:")
            for row in results:
                print(f"ID: {row[0]}, Title: {row[1]}, Category: {row[3]}")
        else:
            print("No regulations found.")
    except sqlite3.Error as e:
        print(f"Error searching regulations: {e}")

# Main function to run the script
def main():
    # Create database and table
    conn = create_connection(DB_PATH)
    if conn is not None:
        create_table(conn)

    # Sample data insertion (for demonstration purposes)
    insert_regulation(conn, "Leave for Family Reasons", "Employees are entitled to leave for family emergencies.", "Family")
    insert_regulation(conn, "Annual Leave", "Employees can take annual leave as per company policy.", "Annual")

    # Example search queries
    search_regulations(conn, keyword="Family")
    search_regulations(conn, category="Annual")

    # Close the database connection
    if conn:
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
