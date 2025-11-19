"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Illustrate how to implement a project management tool for tracking construction timelines and materials, inspired by the project management practices of ExpertStroy.
Generated: DETERMINISTIC_00db890fa2721dda
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python implementation for a project management tool for tracking construction timelines and materials:

```python
import sqlite3
from datetime import datetime


class ProjectManagementTool:
    def __init__(self, db_name="construction_projects.db"):
        """
        Initialization of the project management tool.
        Creates a SQLite database and sets up the schema if it doesn't exist.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the database schema for storing project, timeline, 
        and materials information.
        """
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    client_name TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    status TEXT NOT NULL
                );
            """)

            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS materials (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL,
                    FOREIGN KEY(project_id) REFERENCES projects(id)
                );
            """)

    def add_project(self, name, client_name, start_date, end_date, status="Pending"):
        """
        Adds a new construction project to the database.
        
        :param name: Name of the project
        :param client_name: Name of the client
        :param start_date: Start date of the project (format: YYYY-MM-DD)
        :param end_date: End date of the project (format: YYYY-MM-DD)
        :param status: Status of the project (default: "Pending")
        """
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO projects (name, client_name, start_date, end_date, status)
                    VALUES (?, ?, ?, ?, ?);
                """, (name, client_name, start_date, end_date, status))
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")

    def add_material(self, project_id, name, quantity, unit_price):
        """
        Adds materials to a specific project.
        
        :param project_id: ID of the project
        :param name: Name of the material
        :param quantity: Quantity of the material
        :param unit_price: Unit price of the material
        """
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO materials (project_id, name, quantity, unit_price)
                    VALUES (?, ?, ?, ?);
                """, (project_id, name, quantity, unit_price))
        except sqlite3.Error as e:
            print(f"Error adding material: {e}")

    def update_project_status(self, project_id, status):
        """
        Updates the status of a project.
        
        :param project_id: ID of the project
        :param status: New status of the project
        """
        try:
            with self.connection:
                self.connection.execute("""
                    UPDATE projects
                    SET status = ?
                    WHERE id = ?;
                """, (status, project_id))
        except sqlite3.Error as e:
            print(f"Error updating project status: {e}")

    def get_projects(self):
        """
        Retrieves all projects from the database.
        
        :return: List of projects
        """
        try:
            with self.connection:
                return self.connection.execute("SELECT * FROM projects;").fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving projects: {e}")
            return []

    def get_materials_by_project(self, project_id):
        """
        Retrieves all materials associated with a specific project.
        
        :param project_id: ID of the project
        :return: List of materials
        """
        try:
            with self.connection:
                return self.connection.execute("""
                    SELECT * FROM materials WHERE project_id = ?;
                """, (project_id,)).fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving materials: {e}")
            return []

    def delete_project(self, project_id):
        """
        Deletes a project and its associated materials from the database.
        
        :param project_id: ID of the project
        """
        try:
            with self.connection:
                self.connection.execute("DELETE FROM materials WHERE project_id = ?;", (project_id,))
                self.connection.execute("DELETE FROM projects WHERE id = ?;", (project_id,))
        except sqlite3.Error as e:
            print(f"Error deleting project: {e}")

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()


# Example usage
if __name__ == "__main__":
    tool = ProjectManagementTool()

    # Add a project
    tool.add_project(name="Residential Apartment", client_name="John Doe", start_date="2023-01-01", end_date="2023-12-31")

    # Add materials to the project
    tool.add_material(project_id=1, name="Cement", quantity=500, unit_price=7.5)
    tool.add_material(project_id=1, name="Steel", quantity=300, unit_price=25.0)

    # Update project status
    tool.update_project_status(project_id=1, status="In Progress")

    # Retrieve and print all projects
    projects = tool.get_projects()
    print("Projects:")
    for project in projects:
        print(project)

    # Retrieve and print materials for a specific project
    materials = tool.get_materials_by_project(project_id=1)
    print("\nMaterials for Project 1:")
    for material in materials:
        print(material)

    # Delete a project
    tool.delete_project(project_id=1)

    # Close the tool
    tool.close()
```

This code demonstrates how to implement a project management tool for tracking timelines and materials in a construction project using Python and SQLite.
