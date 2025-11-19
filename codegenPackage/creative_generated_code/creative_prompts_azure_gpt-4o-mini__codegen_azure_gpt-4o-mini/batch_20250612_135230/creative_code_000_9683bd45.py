"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Generate a code snippet for a construction management application that includes features for managing concrete pole installation and electrical civil engineering projects.
Generated: DETERMINISTIC_9683bd4530fa9be1
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

# Define a class to manage the construction projects
class ConstructionManagement:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error occurred while connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for managing projects."""
        try:
            sql_create_projects_table = """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_name TEXT NOT NULL,
                project_type TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_projects_table)
        except Error as e:
            print(f"Error occurred while creating table: {e}")

    def add_project(self, project_name, project_type, status):
        """Add a new project to the database."""
        try:
            sql = """INSERT INTO projects(project_name, project_type, status) 
                     VALUES(?, ?, ?)"""
            cursor = self.connection.cursor()
            cursor.execute(sql, (project_name, project_type, status))
            self.connection.commit()
            print(f"Project '{project_name}' added successfully.")
        except Error as e:
            print(f"Error occurred while adding project: {e}")
    
    def update_project_status(self, project_id, new_status):
        """Update the status of an existing project."""
        try:
            sql = """UPDATE projects SET status = ? WHERE id = ?"""
            cursor = self.connection.cursor()
            cursor.execute(sql, (new_status, project_id))
            self.connection.commit()
            print(f"Project ID {project_id} status updated to '{new_status}'.")
        except Error as e:
            print(f"Error occurred while updating project status: {e}")
    
    def get_projects(self):
        """Retrieve all projects from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM projects")
            projects = cursor.fetchall()
            return projects
        except Error as e:
            print(f"Error occurred while fetching projects: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Usage example:
if __name__ == "__main__":
    # Initialize the construction management system
    db_file = "construction_management.db"
    cm_system = ConstructionManagement(db_file)

    # Create the projects table
    cm_system.create_table()

    # Add some projects
    cm_system.add_project("Concrete Pole Installation - Site A", "Concrete", "In Progress")
    cm_system.add_project("Electrical Installation - Site B", "Electrical", "Planning")

    # Update a project's status
    cm_system.update_project_status(1, "Completed")

    # Fetch and display all projects
    projects = cm_system.get_projects()
    for project in projects:
        print(project)

    # Close the connection
    cm_system.close_connection()
```
