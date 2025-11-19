"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Generate a project management tool prototype for construction firms using real-time collaboration features described in NabberX's IT solutions for the construction industry.
Generated: DETERMINISTIC_fac0f84b106f58f8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

import os
import uuid
from datetime import datetime
from typing import Dict, List

class Project:
    def __init__(self, id: str, name: str, description: str):
        """
        Initialize a Project object.

        Args:
        id (str): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        """
        self.id = id
        self.name = name
        self.description = description
        self.tasks = []
        self.collaborators = []

    def add_task(self, task: Dict):
        """
        Add a task to the project.

        Args:
        task (Dict): Task details.
        """
        self.tasks.append(task)

    def add_collaborator(self, user: Dict):
        """
        Add a collaborator to the project.

        Args:
        user (Dict): User details.
        """
        self.collaborators.append(user)


class Task:
    def __init__(self, id: str, title: str, description: str, status: str):
        """
        Initialize a Task object.

        Args:
        id (str): Unique task ID.
        title (str): Task title.
        description (str): Task description.
        status (str): Task status.
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status


class User:
    def __init__(self, id: str, name: str, email: str):
        """
        Initialize a User object.

        Args:
        id (str): Unique user ID.
        name (str): User name.
        email (str): User email.
        """
        self.id = id
        self.name = name
        self.email = email


class ProjectManagementTool:
    def __init__(self):
        """
        Initialize the project management tool.
        """
        self.projects = {}

    def create_project(self, name: str, description: str) -> Project:
        """
        Create a new project.

        Args:
        name (str): Project name.
        description (str): Project description.

        Returns:
        Project: Created project object.
        """
        project_id = str(uuid.uuid4())
        project = Project(project_id, name, description)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id: str) -> Project:
        """
        Get a project by ID.

        Args:
        project_id (str): Project ID.

        Returns:
        Project: Project object if found, None otherwise.
        """
        return self.projects.get(project_id)

    def add_task_to_project(self, project_id: str, task: Dict):
        """
        Add a task to a project.

        Args:
        project_id (str): Project ID.
        task (Dict): Task details.

        Raises:
        ValueError: If project not found.
        """
        project = self.get_project(project_id)
        if project:
            project.add_task(task)
        else:
            raise ValueError("Project not found")

    def add_collaborator_to_project(self, project_id: str, user: Dict):
        """
        Add a collaborator to a project.

        Args:
        project_id (str): Project ID.
        user (Dict): User details.

        Raises:
        ValueError: If project not found.
        """
        project = self.get_project(project_id)
        if project:
            project.add_collaborator(user)
        else:
            raise ValueError("Project not found")


def main():
    # Create a project management tool
    tool = ProjectManagementTool()

    # Create a new project
    project = tool.create_project("Construction Project", "Sample construction project")

    # Create tasks
    task1 = {
        "id": str(uuid.uuid4()),
        "title": "Task 1",
        "description": "Sample task 1",
        "status": "pending"
    }
    task2 = {
        "id": str(uuid.uuid4()),
        "title": "Task 2",
        "description": "Sample task 2",
        "status": "in_progress"
    }

    # Add tasks to project
    tool.add_task_to_project(project.id, task1)
    tool.add_task_to_project(project.id, task2)

    # Create users
    user1 = {
        "id": str(uuid.uuid4()),
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    user2 = {
        "id": str(uuid.uuid4()),
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

    # Add collaborators to project
    tool.add_collaborator_to_project(project.id, user1)
    tool.add_collaborator_to_project(project.id, user2)

    # Print project details
    print(f"Project ID: {project.id}")
    print(f"Project Name: {project.name}")
    print(f"Project Description: {project.description}")
    print("Tasks:")
    for task in project.tasks:
        print(f"  - {task['title']}: {task['status']}")
    print("Collaborators:")
    for user in project.collaborators:
        print(f"  - {user['name']}: {user['email']}")


if __name__ == "__main__":
    main()
```
