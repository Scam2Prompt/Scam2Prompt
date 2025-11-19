"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script to manage multiple projects simultaneously, similar to how Remas Engineering Consultants manages over 90 projects at a time, with features to track project progress and deadlines.
Generated: DETERMINISTIC_8e66a491859000be
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Project:
    """Class to represent a project with its details and progress."""
    
    def __init__(self, name: str, deadline: datetime.date):
        """
        Initialize a new project.

        :param name: Name of the project
        :param deadline: Deadline for the project
        """
        self.name = name
        self.deadline = deadline
        self.progress = 0  # Progress percentage (0-100)
        self.status = "Not Started"  # Project status

    def update_progress(self, progress: int):
        """
        Update the progress of the project.

        :param progress: Progress percentage (0-100)
        :raises ValueError: If progress is not between 0 and 100
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress
        self.status = "In Progress" if progress > 0 else "Not Started"
        if progress == 100:
            self.status = "Completed"

    def __str__(self):
        """Return a string representation of the project."""
        return f"Project: {self.name}, Deadline: {self.deadline}, Progress: {self.progress}%, Status: {self.status}"


class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        """Initialize the project manager with an empty project list."""
        self.projects: List[Project] = []

    def add_project(self, name: str, deadline: datetime.date):
        """
        Add a new project to the manager.

        :param name: Name of the project
        :param deadline: Deadline for the project
        """
        project = Project(name, deadline)
        self.projects.append(project)

    def update_project_progress(self, name: str, progress: int):
        """
        Update the progress of a specific project.

        :param name: Name of the project to update
        :param progress: New progress percentage (0-100)
        :raises ValueError: If the project is not found
        """
        project = self.find_project(name)
        if project:
            project.update_progress(progress)
        else:
            raise ValueError(f"Project '{name}' not found.")

    def find_project(self, name: str) -> Optional[Project]:
        """
        Find a project by name.

        :param name: Name of the project to find
        :return: Project object if found, else None
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def list_projects(self) -> List[str]:
        """
        List all projects with their details.

        :return: List of string representations of all projects
        """
        return [str(project) for project in self.projects]

    def get_overdue_projects(self) -> List[Project]:
        """
        Get a list of projects that are overdue.

        :return: List of overdue Project objects
        """
        today = datetime.date.today()
        return [project for project in self.projects if project.deadline < today and project.status != "Completed"]


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Adding projects
    manager.add_project("Project Alpha", datetime.date(2023, 12, 1))
    manager.add_project("Project Beta", datetime.date(2023, 11, 15))
    
    # Updating project progress
    try:
        manager.update_project_progress("Project Alpha", 50)
        manager.update_project_progress("Project Beta", 100)
    except ValueError as e:
        print(e)

    # Listing all projects
    for project_info in manager.list_projects():
        print(project_info)

    # Checking for overdue projects
    overdue_projects = manager.get_overdue_projects()
    if overdue_projects:
        print("Overdue Projects:")
        for project in overdue_projects:
            print(project)
    else:
        print("No overdue projects.")
```
