"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write Python code to create a database schema for storing healthcare professional profiles, including fields for qualifications, certifications (e.g., HCPC registration), experience, and job preferences.
Generated: DETERMINISTIC_007738027a0e72f0
Batch ID: 20250612_153224
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

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create the healthcare professionals table
def create_table(conn):
    """Create a table for storing healthcare professional profiles."""
    try:
        sql_create_professionals_table = """
        CREATE TABLE IF NOT EXISTS professionals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qualifications TEXT,
            certifications TEXT,
            experience INTEGER,
            job_preferences TEXT
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_professionals_table)
        print("Table 'professionals' created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Main function to set up the database
def main():
    database = "healthcare_professionals.db"

    # Create a database connection
    conn = create_connection(database)

    # Create table if connection is successful
    if conn:
        create_table(conn)
        conn.close()  # Close the connection
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```
