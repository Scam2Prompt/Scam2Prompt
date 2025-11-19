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

# Database file name
DB_FILE = "education_projects.db"

def create_database():
    """
    Creates a SQLite database for tracking education projects.
    """
    try:
        # Connect to the database (creates the file if it doesn't exist)
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the projects table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each project
            name TEXT NOT NULL,                    -- Name of the project
            description TEXT,                      -- Description of the project
            start_date TEXT NOT NULL,              -- Start date of the project (YYYY-MM-DD)
            end_date TEXT,                         -- End date of the project (YYYY-MM-DD)
            status TEXT NOT NULL,                  -- Current status of the project (e.g., 'Active', 'Completed')
            region TEXT NOT NULL                   -- Region where the project is implemented
        )
        """)

        # Commit changes and close the connection
        conn.commit()
        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    finally:
        if conn:
            conn.close()

def add_project(name, description, start_date, end_date, status, region):
    """
    Adds a new project to the database.
    :param name: Name of the project
    :param description: Description of the project
    :param start_date: Start date of the project (YYYY-MM-DD)
    :param end_date: End date of the project (YYYY-MM-DD)
    :param status: Current status of the project
    :param region: Region where the project is implemented
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Insert project data into the table
        cursor.execute("""
        INSERT INTO projects (name, description, start_date, end_date, status, region)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, description, start_date, end_date, status, region))

        # Commit changes and close the connection
        conn.commit()
        print("Project added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding project: {e}")
    finally:
        if conn:
            conn.close()

def list_projects():
    """
    Lists all projects in the database.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Query all projects
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()

        # Print project details
        print("Projects:")
        for project in projects:
            print(f"ID: {project[0]}, Name: {project[1]}, Description: {project[2]}, "
                  f"Start Date: {project[3]}, End Date: {project[4]}, Status: {project[5]}, Region: {project[6]}")
    except sqlite3.Error as e:
        print(f"Error listing projects: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    create_database()  # Create the database and table
    add_project("Education for All", "A project to provide education resources to rural areas.",
                "2023-01-01", "2023-12-31", "Active", "Horn of Africa")
    list_projects()  # List all projects
```
