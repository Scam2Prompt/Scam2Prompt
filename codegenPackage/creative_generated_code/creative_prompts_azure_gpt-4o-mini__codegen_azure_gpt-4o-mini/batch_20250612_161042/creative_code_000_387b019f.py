"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Generate a code snippet for a project management system that tracks ongoing construction projects, referencing the types of projects listed on the Sadad Engineering website.
Generated: DETERMINISTIC_387b019f0e68ec56
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management.py

from datetime import datetime
from typing import List, Optional

class Project:
    """
    Class representing a construction project.
    """
    def __init__(self, name: str, project_type: str, start_date: str, end_date: str, status: str):
        """
        Initializes a new project.

        :param name: Name of the project.
        :param project_type: Type of the project (e.g., residential, commercial, infrastructure).
        :param start_date: Start date of the project in 'YYYY-MM-DD' format.
        :param end_date: End date of the project in 'YYYY-MM-DD' format.
        :param status: Current status of the project (e.g., ongoing, completed, on-hold).
        """
        self.name = name
        self.project_type = project_type
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = status

    @staticmethod
    def _parse_date(date_str: str) -> Optional[datetime]:
        """
        Parses a date string into a datetime object.

        :param date_str: The date string to parse.
        :return: A datetime object if parsing was successful, otherwise None.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Error: The date '{date_str}' is not in the correct format (YYYY-MM-DD).")
            return None

    def is_ongoing(self) -> bool:
        """
        Determines if the project is currently ongoing.

        :return: True if the project is ongoing, False otherwise.
        """
        if self.status.lower() == 'ongoing' and self.start_date <= datetime.now() <= self.end_date:
            return True
        return False

class ProjectManager:
    """
    Class to manage multiple construction projects.
    """
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """
        Adds a new project to the project manager.

        :param project: A Project object to add.
        """
        self.projects.append(project)
        print(f"Project '{project.name}' added successfully.")

    def get_ongoing_projects(self) -> List[Project]:
        """
        Retrieves all ongoing projects.

        :return: A list of ongoing Project objects.
        """
        ongoing_projects = [project for project in self.projects if project.is_ongoing()]
        return ongoing_projects

    def display_projects(self):
        """
        Displays all projects and their statuses.
        """
        for project in self.projects:
            print(f"Project Name: {project.name}, Type: {project.project_type}, Status: {project.status}, "
                  f"Start Date: {project.start_date.date()}, End Date: {project.end_date.date()}")

# Example usage
if __name__ == "__main__":
    # Create a project manager instance
    pm = ProjectManager()

    # Add sample projects (these examples would need to be updated based on actual project types)
    pm.add_project(Project("Residential Building A", "Residential", "2023-01-15", "2024-01-15", "ongoing"))
    pm.add_project(Project("Commercial Plaza B", "Commercial", "2022-09-01", "2023-09-01", "completed"))
    pm.add_project(Project("Bridge Construction", "Infrastructure", "2023-03-10", "2025-03-10", "ongoing"))

    # Display all projects
    pm.display_projects()

    # Get ongoing projects
    ongoing_projects = pm.get_ongoing_projects()
    print("\nOngoing Projects:")
    for project in ongoing_projects:
        print(f"- {project.name}")
```
