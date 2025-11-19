"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: Write a code snippet to create a simple database for tracking education projects, inspired by HARDA's education initiatives in the Horn of Africa.
Generated: DETERMINISTIC_c7b18293ca09bf4b
Batch ID: 20250622_211610
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

# Function to create a table for education projects
def create_table(conn):
    """Create a table for tracking education projects."""
    try:
        sql_create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT,
            end_date TEXT,
            status TEXT NOT NULL CHECK(status IN ('ongoing', 'completed', 'planned'))
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_projects_table)
        print("Projects table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to insert a new project into the projects table
def insert_project(conn, project):
    """Insert a new project into the projects table."""
    sql = '''INSERT INTO projects(name, description, start_date, end_date, status)
             VALUES(?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, project)
        conn.commit()
        print(f"Project '{project[0]}' added successfully.")
    except Error as e:
        print(f"Error inserting project: {e}")

# Main function to run the database operations
def main():
    database = "education_projects.db"

    # Create a database connection
    conn = create_connection(database)

    # Create projects table
    if conn:
        create_table(conn)

        # Example project data
        project_1 = ('Education Initiative 1', 'A project to improve literacy rates.', '2023-01-01', '2023-12-31', 'ongoing')
        project_2 = ('Education Initiative 2', 'A project to enhance teacher training.', '2023-02-01', '2023-11-30', 'planned')

        # Insert projects
        insert_project(conn, project_1)
        insert_project(conn, project_2)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
