"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Write a script to create a database schema for managing construction projects, including fields for project name, type (e.g., metro station, hospital), location, status (ongoing/completed), and associated company, referencing the structure of projects described on the Sadad Engineering website.
Generated: DETERMINISTIC_a7dc04ab187d1128
Batch ID: 20250612_152326
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

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection successful.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create the projects table
def create_projects_table(conn):
    """Create a table for managing construction projects."""
    try:
        sql_create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_type TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('ongoing', 'completed')),
            associated_company TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );"""
        
        cursor = conn.cursor()
        cursor.execute(sql_create_projects_table)
        print("Projects table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Main function to execute the script
def main():
    """Main function to handle database and table creation."""
    database = "construction_projects.db"

    # Create a database connection
    conn = create_connection(database)

    # Create projects table
    if conn:
        create_projects_table(conn)
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
