"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Create a program to track the progress of over 30,000 completed construction projects, as highlighted on the Bismillah Traders website.
Generated: DETERMINISTIC_1e262140d1705050
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
from typing import List, Tuple, Optional

# Database handler class to manage construction project records
class ConstructionProjectDB:
    def __init__(self, db_file: str):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file: str) -> Optional[sqlite3.Connection]:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create the projects table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL,
            completion_date TEXT,
            budget REAL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Projects table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_project(self, name: str, location: str, status: str, completion_date: str, budget: float):
        """Insert a new project into the projects table."""
        sql = '''INSERT INTO projects(name, location, status, completion_date, budget)
                 VALUES(?,?,?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, location, status, completion_date, budget))
            self.connection.commit()
            print(f"Project '{name}' added successfully.")
        except Error as e:
            print(f"Error adding project: {e}")

    def get_projects(self) -> List[Tuple]:
        """Fetch all projects from the database."""
        sql = 'SELECT * FROM projects'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching projects: {e}")
            return []

    def update_project(self, project_id: int, status: str, completion_date: str):
        """Update the status and completion date of a project."""
        sql = '''UPDATE projects
                 SET status = ?, completion_date = ?
                 WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (status, completion_date, project_id))
            self.connection.commit()
            print(f"Project ID {project_id} updated successfully.")
        except Error as e:
            print(f"Error updating project: {e}")

    def delete_project(self, project_id: int):
        """Delete a project from the database."""
        sql = 'DELETE FROM projects WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (project_id,))
            self.connection.commit()
            print(f"Project ID {project_id} deleted successfully.")
        except Error as e:
            print(f"Error deleting project: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage of the ConstructionProjectDB class
if __name__ == '__main__':
    db = ConstructionProjectDB('construction_projects.db')
    db.create_table()

    # Adding sample projects
    db.add_project('Project Alpha', 'Location A', 'Completed', '2023-01-15', 150000.00)
    db.add_project('Project Beta', 'Location B', 'In Progress', None, 200000.00)

    # Fetching and displaying all projects
    projects = db.get_projects()
    for project in projects:
        print(project)

    # Updating a project
    db.update_project(1, 'Archived', '2023-01-20')

    # Deleting a project
    db.delete_project(2)

    # Closing the database connection
    db.close_connection()
```
