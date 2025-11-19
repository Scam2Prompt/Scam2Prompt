"""
Generated Code Metadata:
========================
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Write code to implement a task tracker system with features like creating projects, assigning roles (e.g., Admin, Project Manager, Developer, Submitter), and tracking progress (To do, In progress, Done, Backlog) as described on the Zapper website.
Generated: DETERMINISTIC_465a8027902e6013
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional
from uuid import uuid4
from pydantic import BaseModel, validator


class Role(str, Enum):
    ADMIN = "Admin"
    PROJECT_MANAGER = "Project Manager"
    DEVELOPER = "Developer"
    SUBMITTER = "Submitter"


class Status(str, Enum):
    TODO = "To do"
    IN_PROGRESS = "In progress"
    DONE = "Done"
    BACKLOG = "Backlog"


class User(BaseModel):
    id: str
    name: str
    email: str
    role: Role

    class Config:
        use_enum_values = True


class Task(BaseModel):
    id: str
    title: str
    description: str
    status: Status
    assignee: Optional[User] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        use_enum_values = True


class Project(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    tasks: List[Task] = []
    members: List[User] = []

    def add_member(self, user: User) -> None:
        if user not in self.members:
            self.members.append(user)
            self.updated_at = datetime.now()

    def remove_member(self, user_id: str) -> None:
        self.members = [member for member in self.members if member.id != user_id]
        self.updated_at = datetime.now()

    def create_task(self, title: str, description: str, assignee: Optional[User] = None) -> Task:
        task = Task(
            id=str(uuid4()),
            title=title,
            description=description,
            status=Status.BACKLOG,
            assignee=assignee,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.tasks.append(task)
        self.updated_at = datetime.now()
        return task

    def update_task_status(self, task_id: str, status: Status) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                task.updated_at = datetime.now()
                self.updated_at = datetime.now()
                return task
        return None

    def assign_task(self, task_id: str, assignee: User) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.assignee = assignee
                task.updated_at = datetime.now()
                self.updated_at = datetime.now()
                return task
        return None


class TaskTracker:
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.users: Dict[str, User] = {}

    def create_user(self, name: str, email: str, role: Role) -> User:
        user = User(
            id=str(uuid4()),
            name=name,
            email=email,
            role=role
        )
        self.users[user.id] = user
        return user

    def create_project(self, name: str, description: str, creator: User) -> Project:
        project = Project(
            id=str(uuid4()),
            name=name,
            description=description,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            members=[creator]
        )
        self.projects[project.id] = project
        return project

    def get_project(self, project_id: str) -> Optional[Project]:
        return self.projects.get(project_id)

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def delete_project(self, project_id: str) -> bool:
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def get_all_projects(self) -> List[Project]:
        return list(self.projects.values())

    def get_projects_by_user(self, user_id: str) -> List[Project]:
        return [project for project in self.projects.values() if user_id in [member.id for member in project.members]]

    def get_tasks_by_user(self, user_id: str) -> List[Task]:
        tasks = []
        for project in self.projects.values():
            for task in project.tasks:
                if task.assignee and task.assignee.id == user_id:
                    tasks.append(task)
        return tasks
```
