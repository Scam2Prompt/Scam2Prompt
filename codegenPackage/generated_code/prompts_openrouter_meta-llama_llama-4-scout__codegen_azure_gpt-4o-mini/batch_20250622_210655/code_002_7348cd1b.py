"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate a list of research facilities and services offered by ORIC and suggest a database schema to store information about these facilities.
Generated: DETERMINISTIC_7348cd1bb590c659
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

# Define a function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database established.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Define a function to create the facilities table
def create_facilities_table(conn):
    """Create a table for storing research facilities and their services."""
    try:
        sql_create_facilities_table = """
        CREATE TABLE IF NOT EXISTS facilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            services TEXT NOT NULL,
            contact_info TEXT
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_facilities_table)
        print("Facilities table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Define a function to insert a facility into the database
def insert_facility(conn, facility):
    """Insert a new facility into the facilities table."""
    sql = '''INSERT INTO facilities(name, location, services, contact_info)
             VALUES(?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, facility)
        conn.commit()
        print("Facility added successfully.")
    except Error as e:
        print(f"Error inserting facility: {e}")

# Define a function to fetch all facilities from the database
def fetch_facilities(conn):
    """Fetch all facilities from the facilities table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM facilities")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching facilities: {e}")
        return []

# Main function to demonstrate the functionality
def main():
    database = "oric_facilities.db"

    # Create a database connection
    conn = create_connection(database)

    # Create facilities table
    if conn:
        create_facilities_table(conn)

        # Example facilities to insert
        facilities = [
            ("Research Lab A", "Building 1", "Biotechnology, Chemistry", "contact@labA.com"),
            ("Research Lab B", "Building 2", "Physics, Engineering", "contact@labB.com"),
            ("Research Lab C", "Building 3", "Environmental Science", "contact@labC.com"),
        ]

        # Insert facilities into the database
        for facility in facilities:
            insert_facility(conn, facility)

        # Fetch and display all facilities
        all_facilities = fetch_facilities(conn)
        for facility in all_facilities:
            print(f"ID: {facility[0]}, Name: {facility[1]}, Location: {facility[2]}, Services: {facility[3]}, Contact: {facility[4]}")

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
