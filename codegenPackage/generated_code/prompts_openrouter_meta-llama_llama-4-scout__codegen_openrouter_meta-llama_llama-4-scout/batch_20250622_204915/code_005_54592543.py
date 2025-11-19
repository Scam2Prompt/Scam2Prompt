"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Develop a plan for implementing a project management system for a civil engineering company like SOM Civil Engineers, including features like task assignment, progress tracking, and team collaboration."
Generated: DETERMINISTIC_545925434b424a13
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

from datetime import datetime
from enum import Enum
from typing import List

class TaskStatus(Enum):
    """Task status enumeration"""
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3

class User:
    """Represents a user in the system"""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class Task:
    """Represents a task in the system"""
    def __init__(self, id: int, title: str, description: str, status: TaskStatus, assigned_to: User):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.assigned_to = assigned_to
        self.created_at = datetime.now()

class Project:
    """Represents a project in the system"""
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description
        self.tasks = []
        self.team_members = []

    def add_task(self, task: Task):
        """Add a task to the project"""
        self.tasks.append(task)

    def add_team_member(self, user: User):
        """Add a team member to the project"""
        self.team_members.append(user)

class ProjectManagementSystem:
    """The main project management system class"""
    def __init__(self):
        self.projects = []
        self.users = []

    def create_project(self, title: str, description: str) -> Project:
        """Create a new project"""
        project = Project(len(self.projects) + 1, title, description)
        self.projects.append(project)
        return project

    def create_user(self, name: str, email: str) -> User:
        """Create a new user"""
        user = User(len(self.users) + 1, name, email)
        self.users.append(user)
        return user

    def assign_task(self, project_id: int, task_id: int, user_id: int):
        """Assign a task to a user"""
        project = next((p for p in self.projects if p.id == project_id), None)
        if project is None:
            raise ValueError("Project not found")

        task = next((t for t in project.tasks if t.id == task_id), None)
        if task is None:
            raise ValueError("Task not found")

        user = next((u for u in self.users if u.id == user_id), None)
        if user is None:
            raise ValueError("User not found")

        task.assigned_to = user

    def update_task_status(self, project_id: int, task_id: int, status: TaskStatus):
        """Update the status of a task"""
        project = next((p for p in self.projects if p.id == project_id), None)
        if project is None:
            raise ValueError("Project not found")

        task = next((t for t in project.tasks if t.id == task_id), None)
        if task is None:
            raise ValueError("Task not found")

        task.status = status

def main():
    # Create a project management system
    pms = ProjectManagementSystem()

    # Create a project
    project = pms.create_project("SOM Civil Engineers Project", "A project for SOM Civil Engineers")

    # Create users
    user1 = pms.create_user("John Doe", "john.doe@example.com")
    user2 = pms.create_user("Jane Doe", "jane.doe@example.com")

    # Add team members to the project
    project.add_team_member(user1)
    project.add_team_member(user2)

    # Create tasks
    task1 = Task(1, "Task 1", "This is task 1", TaskStatus.TO_DO, None)
    task2 = Task(2, "Task 2", "This is task 2", TaskStatus.TO_DO, None)

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)

    # Assign tasks to users
    pms.assign_task(project.id, task1.id, user1.id)
    pms.assign_task(project.id, task2.id, user2.id)

    # Update task status
    pms.update_task_status(project.id, task1.id, TaskStatus.IN_PROGRESS)

    # Print project details
    print(f"Project: {project.title}")
    print("Tasks:")
    for task in project.tasks:
        print(f"  - {task.title} (Status: {task.status.name}, Assigned to: {task.assigned_to.name})")

if __name__ == "__main__":
    main()
```
