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
"""
This script demonstrates the use of pandas and sqlite3 for managing construction project data specifically
for projects involving StoTherm EIFS systems and textured designs.

Pandas is chosen for data manipulation and analysis.
SQLite is chosen for lightweight database management.

Ensure you have pandas and sqlite3 installed in your environment before running this script:
pip install pandas
"""

import pandas as pd
import sqlite3


class ConstructionProjectManager:
    """
    A class to manage construction project data using Pandas and SQLite.
    Specifically designed for projects involving StoTherm EIFS systems and textured designs.
    """

    def __init__(self, db_name="construction_projects.db"):
        """
        Initialize the manager with a database file.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name

        # Create a connection to the SQLite database
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

        # Create a table for construction project data if it doesn't exist
        self._create_table()

    def _create_table(self):
        """
        Create a table for construction projects if it doesn't already exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    eifs_system TEXT,
                    textured_design BOOLEAN,
                    start_date DATE,
                    end_date DATE
                )
            """)
            self.connection.commit()
            print("Table 'projects' created or already exists.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_project(self, name, description, eifs_system, textured_design, start_date, end_date):
        """
        Add a new construction project to the database.
        :param name: Name of the project.
        :param description: Description of the project.
        :param eifs_system: Type of EIFS system used.
        :param textured_design: Whether the project involves textured designs (True/False).
        :param start_date: Project start date (YYYY-MM-DD).
        :param end_date: Project end date (YYYY-MM-DD).
        """
        try:
            self.cursor.execute("""
                INSERT INTO projects (name, description, eifs_system, textured_design, start_date, end_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, description, eifs_system, textured_design, start_date, end_date))
            self.connection.commit()
            print(f"Project '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")
            raise

    def fetch_projects(self):
        """
        Fetch all projects from the database.
        Returns a Pandas DataFrame for easy manipulation.
        """
        try:
            query = "SELECT * FROM projects"
            df = pd.read_sql_query(query, self.connection)
            return df
        except sqlite3.Error as e:
            print(f"Error fetching projects: {e}")
            raise

    def close_connection(self):
        """
        Close the connection to the SQLite database.
        """
        try:
            self.connection.close()
            print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
            raise


# Example usage
if __name__ == "__main__":
    manager = ConstructionProjectManager()

    # Add new projects
    manager.add_project(
        name="StoTherm EIFS Project 1",
        description="High-performance EIFS system with textured design.",
        eifs_system="StoTherm Classic",
        textured_design=True,
        start_date="2023-01-01",
        end_date="2023-06-01"
    )
    manager.add_project(
        name="StoTherm EIFS Project 2",
        description="Energy-efficient EIFS system without textured design.",
        eifs_system="StoTherm Lotusan",
        textured_design=False,
        start_date="2023-03-01",
        end_date="2023-10-01"
    )

    # Fetch and display all projects
    projects = manager.fetch_projects()
    print("All Projects:")
    print(projects)

    # Close the database connection
    manager.close_connection()
```
