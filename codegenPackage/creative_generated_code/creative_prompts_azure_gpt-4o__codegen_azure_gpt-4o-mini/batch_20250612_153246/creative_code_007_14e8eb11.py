"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Recommend a Python library for managing construction project data, specifically for projects involving StoTherm EIFS systems and textured designs, as highlighted on Engenharia WPJ.
Generated: DETERMINISTIC_14e8eb118a49eec0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import sqlite3

class ConstructionProjectManager:
    """
    A class to manage construction project data, specifically for projects involving
    StoTherm EIFS systems and textured designs.
    """

    def __init__(self, db_name='projects.db'):
        """
        Initializes the ConstructionProjectManager with a SQLite database.
        
        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.conn = self.create_connection()
        self.create_table()

    def create_connection(self):
        """
        Creates a connection to the SQLite database.

        :return: SQLite connection object
        """
        try:
            conn = sqlite3.connect(self.db_name)
            print("SQLite connection successful.")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """
        Creates a table for storing project data if it doesn't exist.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_name TEXT NOT NULL,
                    project_location TEXT NOT NULL,
                    system_type TEXT NOT NULL,
                    design_type TEXT NOT NULL
                )
            ''')
            self.conn.commit()
            print("Table 'projects' is ready.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_project(self, project_name, project_location, system_type, design_type):
        """
        Adds a new project to the database.

        :param project_name: Name of the project
        :param project_location: Location of the project
        :param system_type: Type of system used (e.g., StoTherm EIFS)
        :param design_type: Type of design (e.g., textured)
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO projects (project_name, project_location, system_type, design_type)
                VALUES (?, ?, ?, ?)
            ''', (project_name, project_location, system_type, design_type))
            self.conn.commit()
            print(f"Project '{project_name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")

    def fetch_projects(self):
        """
        Fetches all projects from the database.

        :return: DataFrame containing all project data
        """
        try:
            return pd.read_sql_query("SELECT * FROM projects", self.conn)
        except sqlite3.Error as e:
            print(f"Error fetching projects: {e}")
            return pd.DataFrame()

    def __del__(self):
        """
        Ensures that the database connection is closed when the object is deleted.
        """
        if self.conn:
            self.conn.close()
            print("SQLite connection closed.")

# Example usage
if __name__ == "__main__":
    # Create an instance of the project manager
    project_manager = ConstructionProjectManager()

    # Add a sample project
    project_manager.add_project(
        project_name='Sample EIFS Project',
        project_location='123 Main St, Anytown, USA',
        system_type='StoTherm EIFS',
        design_type='Textured'
    )

    # Fetch and display all projects
    projects_df = project_manager.fetch_projects()
    print(projects_df)
```
