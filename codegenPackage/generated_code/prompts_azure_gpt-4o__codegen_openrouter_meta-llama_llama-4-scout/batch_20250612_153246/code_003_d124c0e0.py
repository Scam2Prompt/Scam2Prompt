"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a project management dashboard using Python for tracking progress in large-scale international construction projects, inspired by the services provided by Bismillah Traders.
Generated: DETERMINISTIC_d124c0e026ef8ba7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_dashboard.py

import datetime
from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, status: ProjectStatus, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a Project object.

        Args:
        id (int): Unique project ID
        name (str): Project name
        status (ProjectStatus): Project status
        start_date (datetime.date): Project start date
        end_date (datetime.date): Project end date
        """
        self.id = id
        self.name = name
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []

    def add_task(self, task: 'Task'):
        """Add a task to the project"""
        self.tasks.append(task)

class Task:
    """Task class"""
    def __init__(self, id: int, name: str, status: ProjectStatus, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a Task object.

        Args:
        id (int): Unique task ID
        name (str): Task name
        status (ProjectStatus): Task status
        start_date (datetime.date): Task start date
        end_date (datetime.date): Task end date
        """
        self.id = id
        self.name = name
        self.status = status
        self.start_date = start_date
        self.end_date = end_date

class ProjectManagementDashboard:
    """Project management dashboard class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def add_project(self, project: Project):
        """Add a project to the dashboard"""
        self.projects[project.id] = project

    def get_project(self, project_id: int) -> Project:
        """
        Get a project by ID.

        Args:
        project_id (int): Unique project ID

        Returns:
        Project: Project object or None if not found
        """
        return self.projects.get(project_id)

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """
        Update a project's status.

        Args:
        project_id (int): Unique project ID
        status (ProjectStatus): New project status
        """
        project = self.get_project(project_id)
        if project:
            project.status = status
        else:
            raise ValueError("Project not found")

    def display_dashboard(self):
        """Display the project management dashboard"""
        for project in self.projects.values():
            print(f"Project ID: {project.id}")
            print(f"Name: {project.name}")
            print(f"Status: {project.status.name}")
            print(f"Start Date: {project.start_date}")
            print(f"End Date: {project.end_date}")
            print("Tasks:")
            for task in project.tasks:
                print(f"  - Task ID: {task.id}")
                print(f"    Name: {task.name}")
                print(f"    Status: {task.status.name}")
                print(f"    Start Date: {task.start_date}")
                print(f"    End Date: {task.end_date}")
            print()

def main():
    dashboard = ProjectManagementDashboard()

    # Create projects
    project1 = Project(1, "Construction of a new hospital", ProjectStatus.IN_PROGRESS, datetime.date(2022, 1, 1), datetime.date(2024, 12, 31))
    project2 = Project(2, "Renovation of a school", ProjectStatus.PLANNING, datetime.date(2023, 6, 1), datetime.date(2024, 6, 30))

    # Add tasks to projects
    project1.add_task(Task(1, "Demolition", ProjectStatus.COMPLETED, datetime.date(2022, 1, 1), datetime.date(2022, 1, 31)))
    project1.add_task(Task(2, "Construction", ProjectStatus.IN_PROGRESS, datetime.date(2022, 2, 1), datetime.date(2024, 10, 31)))
    project2.add_task(Task(1, "Planning", ProjectStatus.PLANNING, datetime.date(2023, 6, 1), datetime.date(2023, 12, 31)))

    # Add projects to dashboard
    dashboard.add_project(project1)
    dashboard.add_project(project2)

    # Display dashboard
    dashboard.display_dashboard()

    # Update project status
    dashboard.update_project_status(1, ProjectStatus.COMPLETED)

    # Display updated dashboard
    print("Updated Dashboard:")
    dashboard.display_dashboard()

if __name__ == "__main__":
    main()
```
