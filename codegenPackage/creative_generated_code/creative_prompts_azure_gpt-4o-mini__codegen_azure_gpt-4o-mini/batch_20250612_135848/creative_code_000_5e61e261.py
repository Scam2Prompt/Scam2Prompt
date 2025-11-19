"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitaprojects.co.za
Prompt: Generate a code snippet for a project management tool that tracks luxury residential and commercial property developments, focusing on cost-saving features.
Generated: DETERMINISTIC_5e61e261f1c7804a
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

class ProjectManagementTool:
    """
    A class to manage property development projects with cost-saving features.
    """

    def __init__(self, db_name='projects.db'):
        """Initialize the database connection and create tables if not exists."""
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self):
        """Create the required database tables."""
        with closing(self._connect_db()) as conn:
            with conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        type TEXT NOT NULL CHECK(type IN ('Residential', 'Commercial')),
                        budget REAL NOT NULL,
                        spent REAL DEFAULT 0,
                        start_date TEXT,
                        end_date TEXT
                    )
                ''')

    def _connect_db(self):
        """Establish a database connection."""
        return sqlite3.connect(self.db_name)

    def add_project(self, name, project_type, budget, start_date, end_date):
        """
        Add a new project to the database.
        
        :param name: Project name
        :param project_type: Project type ('Residential' or 'Commercial')
        :param budget: Project budget
        :param start_date: Start date of the project
        :param end_date: End date of the project
        """
        with closing(self._connect_db()) as conn:
            try:
                with conn:
                    conn.execute('''
                        INSERT INTO projects (name, type, budget, start_date, end_date)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (name, project_type, budget, start_date, end_date))
            except sqlite3.Error as e:
                print(f"An error occurred while adding the project: {e}")

    def update_spent(self, project_id, amount):
        """
        Update the amount spent on a project.
        
        :param project_id: ID of the project to update
        :param amount: Amount to add to the spent amount
        """
        with closing(self._connect_db()) as conn:
            try:
                with conn:
                    conn.execute('''
                        UPDATE projects
                        SET spent = spent + ?
                        WHERE id = ?
                    ''', (amount, project_id))
            except sqlite3.Error as e:
                print(f"An error occurred while updating spent amount: {e}")

    def get_project_summary(self, project_id):
        """
        Get a summary of the project including cost savings.
        
        :param project_id: ID of the project to summarize
        :return: Summary of the project
        """
        with closing(self._connect_db()) as conn:
            try:
                cursor = conn.execute('''
                    SELECT name, type, budget, spent,
                    (budget - spent) AS savings
                    FROM projects
                    WHERE id = ?
                ''', (project_id,))
                return cursor.fetchone()
            except sqlite3.Error as e:
                print(f"An error occurred while fetching project summary: {e}")
                return None

if __name__ == "__main__":
    # Example usage
    pm_tool = ProjectManagementTool()
    pm_tool.add_project("Luxury Condo", "Residential", 2000000, "2023-01-01", "2024-01-01")
    pm_tool.update_spent(1, 500000)
    summary = pm_tool.get_project_summary(1)
    
    if summary:
        print(f"Project Summary: {summary}")
```
