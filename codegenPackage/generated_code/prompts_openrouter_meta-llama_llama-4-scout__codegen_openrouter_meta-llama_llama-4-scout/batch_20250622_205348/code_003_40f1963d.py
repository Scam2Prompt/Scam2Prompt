"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Generate a code template for creating a construction project management system with features similar to those described on the MGEL website.
Generated: DETERMINISTIC_40f1963d98465b1b
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management_system.py

"""
Construction Project Management System

This system provides features for managing construction projects, including
project creation, task assignment, and progress tracking.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
from enum import Enum
from typing import List

class ProjectStatus(Enum):
    """Project status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class TaskStatus(Enum):
    """Task status enumeration"""
    ASSIGNED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, description: str):
        """
        Initialize a project

        Args:
            id (int): Project ID
            name (str): Project name
            description (str): Project description
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = ProjectStatus.PENDING
        self.tasks = []

    def add_task(self, task):
        """Add a task to the project"""
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus):
        """Update the project status"""
        self.status = status

class Task:
    """Task class"""
    def __init__(self, id: int, name: str, description: str, assigned_to: str):
        """
        Initialize a task

        Args:
            id (int): Task ID
            name (str): Task name
            description (str): Task description
            assigned_to (str): Task assignee
        """
        self.id = id
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.status = TaskStatus.ASSIGNED

    def update_status(self, status: TaskStatus):
        """Update the task status"""
        self.status = status

class ConstructionProjectManagementSystem:
    """Construction project management system class"""
    def __init__(self):
        self.projects = []

    def create_project(self, id: int, name: str, description: str):
        """
        Create a new project

        Args:
            id (int): Project ID
            name (str): Project name
            description (str): Project description

        Returns:
            Project: Created project
        """
        project = Project(id, name, description)
        self.projects.append(project)
        return project

    def get_project(self, id: int):
        """
        Get a project by ID

        Args:
            id (int): Project ID

        Returns:
            Project: Project with the given ID, or None if not found
        """
        for project in self.projects:
            if project.id == id:
                return project
        return None

    def create_task(self, project_id: int, id: int, name: str, description: str, assigned_to: str):
        """
        Create a new task for a project

        Args:
            project_id (int): Project ID
            id (int): Task ID
            name (str): Task name
            description (str): Task description
            assigned_to (str): Task assignee

        Returns:
            Task: Created task, or None if project not found
        """
        project = self.get_project(project_id)
        if project:
            task = Task(id, name, description, assigned_to)
            project.add_task(task)
            return task
        return None

def main():
    try:
        # Create a construction project management system
        system = ConstructionProjectManagementSystem()

        # Create a project
        project = system.create_project(1, "Construction Project", "This is a construction project")

        # Create tasks for the project
        task1 = system.create_task(1, 1, "Task 1", "This is task 1", "John Doe")
        task2 = system.create_task(1, 2, "Task 2", "This is task 2", "Jane Doe")

        # Update task status
        task1.update_status(TaskStatus.IN_PROGRESS)
        task2.update_status(TaskStatus.COMPLETED)

        # Update project status
        project.update_status(ProjectStatus.IN_PROGRESS)

        # Print project and task information
        print(f"Project {project.id}: {project.name}")
        print(f"Status: {project.status.name}")
        for task in project.tasks:
            print(f"Task {task.id}: {task.name}")
            print(f"Status: {task.status.name}")
            print(f"Assigned to: {task.assigned_to}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
