"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Suggest a library for managing client projects in a digital branding agency and provide a code example for its implementation.
Generated: DETERMINISTIC_d855e05ce647b3c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
import sqlite3
from sqlite3 import Error

# Class for managing client projects
class ClientProjectManager:
    def __init__(self, db_file):
        """Initialize the project manager with a SQLite database."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error while connecting to SQLite: {e}")
        return conn

    def create_table(self):
        """Create a table for storing client projects."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            name text NOT NULL,
            client_name text NOT NULL,
            status text NOT NULL,
            start_date text,
            end_date text
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Table created successfully")
        except Error as e:
            print(f"Error while creating table: {e}")

    def add_project(self, name, client_name, status, start_date, end_date):
        """Add a new project to the database."""
        sql = """INSERT INTO projects (name, client_name, status, start_date, end_date)
                 VALUES (?, ?, ?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, client_name, status, start_date, end_date))
            self.connection.commit()
            print("Project added successfully")
        except Error as e:
            print(f"Error while adding project: {e}")

    def get_projects(self):
        """Fetch all projects from the database."""
        sql = "SELECT * FROM projects"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error while fetching projects: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed")

# Example usage
if __name__ == "__main__":
    db_file = "client_projects.db"
    project_manager = ClientProjectManager(db_file)

    project_manager.create_table()

    # Adding projects
    project_manager.add_project("Website Redesign", "Client A", "In Progress", "2023-01-10", "2023-03-10")
    project_manager.add_project("Social Media Campaign", "Client B", "Completed", "2023-02-01", "2023-02-15")

    # Fetching all projects
    projects = project_manager.get_projects()
    for project in projects:
        print(project)

    # Closing the connection
    project_manager.close_connection()
```
