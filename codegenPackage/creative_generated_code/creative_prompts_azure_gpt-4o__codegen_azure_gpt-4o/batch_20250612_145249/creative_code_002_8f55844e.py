"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Generate a script to automate scheduling and tracking of scaffolding services for multi-story building restoration projects, referencing Premier Pointing's scaffolding offerings.
Generated: DETERMINISTIC_8f55844ef2c4b4b8
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
from typing import List, Tuple


class ScaffoldingScheduler:
    """
    A class to manage scheduling and tracking of scaffolding services.
    Uses an SQLite database to store project and scheduling information.
    """

    def __init__(self, db_name: str = "scaffolding_services.db"):
        """
        Initialize the scheduler and create the necessary database schema.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Create the database schema if it doesn't already exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_name TEXT NOT NULL,
                    client_name TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    status TEXT DEFAULT 'Scheduled'
                )
            """)
            conn.commit()

    def add_project(
        self, project_name: str, client_name: str, start_date: str, end_date: str
    ):
        """
        Add a new scaffolding project to the schedule.

        :param project_name: Name of the restoration project.
        :param client_name: Name of the client.
        :param start_date: Project start date in YYYY-MM-DD format.
        :param end_date: Project end date in YYYY-MM-DD format.
        """
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Dates must be in YYYY-MM-DD format.") from e

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO projects (project_name, client_name, start_date, end_date)
                VALUES (?, ?, ?, ?)
            """, (project_name, client_name, start_date, end_date))
            conn.commit()

    def update_project_status(self, project_id: int, status: str):
        """
        Update the status of an existing project.

        :param project_id: ID of the project to be updated.
        :param status: New status of the project (e.g., "In Progress", "Completed").
        """
        if status not in ("Scheduled", "In Progress", "Completed", "Cancelled"):
            raise ValueError("Invalid status value.")

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE projects
                SET status = ?
                WHERE id = ?
            """, (status, project_id))
            if cursor.rowcount == 0:
                raise ValueError(f"Project with ID {project_id} not found.")
            conn.commit()

    def get_all_projects(self) -> List[Tuple]:
        """
        Retrieve all projects from the schedule.

        :return: A list of tuples containing project data.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects")
            return cursor.fetchall()

    def delete_project(self, project_id: int):
        """
        Delete a project from the schedule by its ID.

        :param project_id: ID of the project to be deleted.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
            if cursor.rowcount == 0:
                raise ValueError(f"Project with ID {project_id} not found.")
            conn.commit()


# Example usage
if __name__ == "__main__":
    scheduler = ScaffoldingScheduler()

    # Add sample projects
    try:
        scheduler.add_project(
            project_name="Building A Restoration",
            client_name="Premier Pointing",
            start_date="2023-11-01",
            end_date="2023-12-15"
        )

        scheduler.add_project(
            project_name="Building B Scaffolding",
            client_name="John's Construction",
            start_date="2023-12-01",
            end_date="2024-01-30"
        )

        # Update project status
        scheduler.update_project_status(1, "In Progress")

        # List all projects
        projects = scheduler.get_all_projects()
        for project in projects:
            print(project)

        # Delete a project
        scheduler.delete_project(2)

    except ValueError as e:
        print(f"Error: {e}")
```
