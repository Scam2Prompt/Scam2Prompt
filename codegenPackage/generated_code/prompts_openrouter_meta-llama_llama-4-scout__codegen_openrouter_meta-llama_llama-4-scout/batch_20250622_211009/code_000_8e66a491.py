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
# project_manager.py

import datetime
from typing import Dict, List

class Project:
    """Represents a project with a name, deadline, and progress."""

    def __init__(self, name: str, deadline: datetime.date):
        """
        Initializes a Project.

        Args:
            name (str): The project's name.
            deadline (datetime.date): The project's deadline.
        """
        self.name = name
        self.deadline = deadline
        self.progress = 0  # Initial progress is 0%

    def update_progress(self, progress: int):
        """
        Updates the project's progress.

        Args:
            progress (int): The new progress percentage.

        Raises:
            ValueError: If progress is not between 0 and 100.
        """
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        self.progress = progress

    def __str__(self):
        return f"{self.name} - Deadline: {self.deadline}, Progress: {self.progress}%"


class ProjectManager:
    """Manages multiple projects."""

    def __init__(self):
        """Initializes a ProjectManager."""
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project):
        """
        Adds a project to the manager.

        Args:
            project (Project): The project to add.

        Raises:
            ValueError: If a project with the same name already exists.
        """
        if project.name in self.projects:
            raise ValueError("Project with the same name already exists")
        self.projects[project.name] = project

    def remove_project(self, project_name: str):
        """
        Removes a project from the manager.

        Args:
            project_name (str): The name of the project to remove.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_name not in self.projects:
            raise KeyError("Project does not exist")
        del self.projects[project_name]

    def update_project_progress(self, project_name: str, progress: int):
        """
        Updates a project's progress.

        Args:
            project_name (str): The name of the project to update.
            progress (int): The new progress percentage.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_name not in self.projects:
            raise KeyError("Project does not exist")
        self.projects[project_name].update_progress(progress)

    def get_project(self, project_name: str) -> Project:
        """
        Gets a project by name.

        Args:
            project_name (str): The name of the project to get.

        Returns:
            Project: The project with the given name.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_name not in self.projects:
            raise KeyError("Project does not exist")
        return self.projects[project_name]

    def list_projects(self) -> List[Project]:
        """
        Lists all projects.

        Returns:
            List[Project]: A list of all projects.
        """
        return list(self.projects.values())


def main():
    # Create a project manager
    manager = ProjectManager()

    while True:
        print("\n1. Add project")
        print("2. Remove project")
        print("3. Update project progress")
        print("4. Get project")
        print("5. List projects")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter project name: ")
            deadline = datetime.datetime.strptime(input("Enter project deadline (YYYY-MM-DD): "), "%Y-%m-%d").date()
            project = Project(name, deadline)
            try:
                manager.add_project(project)
                print(f"Project '{name}' added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            project_name = input("Enter project name: ")
            try:
                manager.remove_project(project_name)
                print(f"Project '{project_name}' removed successfully.")
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            project_name = input("Enter project name: ")
            progress = int(input("Enter new progress percentage: "))
            try:
                manager.update_project_progress(project_name, progress)
                print(f"Project '{project_name}' progress updated successfully.")
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "4":
            project_name = input("Enter project name: ")
            try:
                project = manager.get_project(project_name)
                print(project)
            except KeyError as e:
                print(str(e))
        elif choice == "5":
            projects = manager.list_projects()
            for project in projects:
                print(project)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
