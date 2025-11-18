"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Write code to implement a task tracker system with features like creating projects, assigning roles (e.g., Admin, Project Manager, Developer, Submitter), and tracking progress (To do, In progress, Done, Backlog) as described on the Zapper website.
Generated: DETERMINISTIC_465a8027902e6013
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# task_tracker.py

from enum import Enum
from typing import List, Dict, Union


# Enum for Task Status
class TaskStatus(Enum):
    BACKLOG = "Backlog"
    TO_DO = "To do"
    IN_PROGRESS = "In progress"
    DONE = "Done"


# Enum for User Roles
class Role(Enum):
    ADMIN = "Admin"
    PROJECT_MANAGER = "Project Manager"
    DEVELOPER = "Developer"
    SUBMITTER = "Submitter"


# Task class to manage individual tasks
class Task:
    def __init__(self, title: str, description: str, status: TaskStatus = TaskStatus.BACKLOG):
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status: TaskStatus):
        """Update the status of the task."""
        if not isinstance(new_status, TaskStatus):
            raise ValueError("Invalid status. Must be of type TaskStatus.")
        self.status = new_status

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status.value})"


# User class to manage individual users
class User:
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"User(name={self.name}, role={self.role.value})"


# Project class to manage projects
class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []  # List of tasks in the project
        self.users: List[User] = []  # List of users assigned to the project

    def add_task(self, task: Task):
        """Add a task to the project."""
        if not isinstance(task, Task):
            raise ValueError("Invalid task. Must be of type Task.")
        self.tasks.append(task)

    def add_user(self, user: User):
        """Add a user to the project."""
        if not isinstance(user, User):
            raise ValueError("Invalid user. Must be of type User.")
        self.users.append(user)

    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Retrieve tasks filtered by status."""
        return [task for task in self.tasks if task.status == status]

    def __repr__(self):
        return f"Project(name={self.name}, tasks={len(self.tasks)}, users={len(self.users)})"


# Main Task Tracker System
class TaskTracker:
    def __init__(self):
        self.projects: Dict[str, Project] = {}  # Projects in the system

    def create_project(self, name: str) -> Project:
        """Create a new project."""
        if name in self.projects:
            raise ValueError(f"Project with name '{name}' already exists.")
        project = Project(name)
        self.projects[name] = project
        return project

    def get_project(self, name: str) -> Union[Project, None]:
        """Retrieve a project by name."""
        return self.projects.get(name)

    def __repr__(self):
        return f"TaskTracker(projects={len(self.projects)})"


# Example usage
if __name__ == "__main__":
    tracker = TaskTracker()

    # Create a new project
    project_alpha = tracker.create_project("Alpha Project")

    # Add users to the project
    admin_user = User("Alice", Role.ADMIN)
    developer_user = User("Bob", Role.DEVELOPER)

    project_alpha.add_user(admin_user)
    project_alpha.add_user(developer_user)

    # Add tasks to the project
    task1 = Task("Design Database", "Create the database schema", TaskStatus.TO_DO)
    task2 = Task("Develop API", "Build the REST API", TaskStatus.BACKLOG)

    project_alpha.add_task(task1)
    project_alpha.add_task(task2)

    # Update task status
    task1.update_status(TaskStatus.IN_PROGRESS)

    # Retrieve tasks by status
    in_progress_tasks = project_alpha.get_tasks_by_status(TaskStatus.IN_PROGRESS)
    print(f"In Progress Tasks: {in_progress_tasks}")

    # Print project and tracker details
    print(project_alpha)
    print(tracker)
```
