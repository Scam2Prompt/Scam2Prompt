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
from typing import List, Dict, Optional


class Role(Enum):
    ADMIN = "Admin"
    PROJECT_MANAGER = "Project Manager"
    DEVELOPER = "Developer"
    SUBMITTER = "Submitter"


class TaskStatus(Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    BACKLOG = "Backlog"


class Task:
    def __init__(self, title: str, description: str, status: TaskStatus):
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def __repr__(self):
        return f"Project(name={self.name}, tasks={self.tasks})"


class User:
    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"


class TaskTracker:
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.users: Dict[str, User] = {}

    def create_project(self, project_name: str):
        if project_name in self.projects:
            raise ValueError("Project with this name already exists.")
        self.projects[project_name] = Project(project_name)

    def add_user(self, username: str, role: Role):
        if username in self.users:
            raise ValueError("User with this username already exists.")
        self.users[username] = User(username, role)

    def assign_task(self, project_name: str, task: Task):
        if project_name not in self.projects:
            raise ValueError("Project does not exist.")
        self.projects[project_name].add_task(task)

    def get_project_status(self, project_name: str) -> Dict[str, List[Task]]:
        if project_name not in self.projects:
            raise ValueError("Project does not exist.")
        status_dict = {status.value: [] for status in TaskStatus}
        for task in self.projects[project_name].get_tasks():
            status_dict[task.status.value].append(task)
        return status_dict

    def __repr__(self):
        return f"TaskTracker(projects={self.projects}, users={self.users})"


# Example usage:
if __name__ == "__main__":
    tracker = TaskTracker()

    # Create users
    tracker.add_user("alice", Role.ADMIN)
    tracker.add_user("bob", Role.PROJECT_MANAGER)
    tracker.add_user("charlie", Role.DEVELOPER)

    # Create a project
    tracker.create_project("Project Alpha")

    # Add tasks to the project
    tracker.assign_task("Project Alpha", Task("Setup Environment", "Set up the development environment.", TaskStatus.TO_DO))
    tracker.assign_task("Project Alpha", Task("Implement Feature X", "Implement the core feature X.", TaskStatus.IN_PROGRESS))

    # Check project status
    status = tracker.get_project_status("Project Alpha")
    print(status)
```
