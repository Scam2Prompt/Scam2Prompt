"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Suggest tools or APIs to manage and track community development projects, ensuring alignment with the association's strategic goals of improving work behavior, personal development, and community participation.
Generated: DETERMINISTIC_13027c980c0be433
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Management and Tracking System

import datetime
from enum import Enum
from typing import List, Dict

class ProjectStatus(str, Enum):
    """Project status enumeration"""
    TO_DO = "To-Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, description: str, status: ProjectStatus):
        """
        Initialize a project

        Args:
        id (int): Unique project ID
        name (str): Project name
        description (str): Project description
        status (ProjectStatus): Project status
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.tasks = []

    def add_task(self, task: str):
        """Add a task to the project"""
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus):
        """Update project status"""
        self.status = status

class Task:
    """Task class"""
    def __init__(self, id: int, description: str, due_date: datetime.date):
        """
        Initialize a task

        Args:
        id (int): Unique task ID
        description (str): Task description
        due_date (datetime.date): Task due date
        """
        self.id = id
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        """Mark task as completed"""
        self.completed = True

class CommunityDevelopmentProjectManager:
    """Community development project manager class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def create_project(self, id: int, name: str, description: str, status: ProjectStatus):
        """
        Create a new project

        Args:
        id (int): Unique project ID
        name (str): Project name
        description (str): Project description
        status (ProjectStatus): Project status

        Returns:
        Project: Created project
        """
        if id in self.projects:
            raise ValueError("Project with given ID already exists")

        project = Project(id, name, description, status)
        self.projects[id] = project
        return project

    def get_project(self, id: int) -> Project:
        """
        Get a project by ID

        Args:
        id (int): Unique project ID

        Returns:
        Project: Project with given ID

        Raises:
        ValueError: If project with given ID does not exist
        """
        project = self.projects.get(id)
        if project is None:
            raise ValueError("Project with given ID does not exist")
        return project

def main():
    # Example usage
    manager = CommunityDevelopmentProjectManager()

    project1 = manager.create_project(1, "Improve Work Behavior", "Conduct workshops and training sessions", ProjectStatus.TO_DO)
    project1.add_task("Research potential trainers")
    project1.add_task("Book a venue")

    project2 = manager.create_project(2, "Personal Development", "Provide resources and support for personal growth", ProjectStatus.IN_PROGRESS)
    task1 = Task(1, "Create a resource library", datetime.date(2024, 9, 30))
    # task1.mark_as_completed()  # Uncomment to mark task as completed

    try:
        print(manager.get_project(1).name)  # Improve Work Behavior
        print(manager.get_project(2).description)  # Personal Development
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
