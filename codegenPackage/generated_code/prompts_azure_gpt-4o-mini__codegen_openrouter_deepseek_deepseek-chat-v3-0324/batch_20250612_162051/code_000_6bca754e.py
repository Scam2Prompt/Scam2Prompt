"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate a code snippet for an Agile project management tool that incorporates interactive learning features as described on the CrestAgile website.
Generated: DETERMINISTIC_6bca754ef7c11569
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Optional
from datetime import datetime
import json
import uuid
from enum import Enum

# Define enums for task status and priority
class TaskStatus(Enum):
    """Enum representing the status of a task."""
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    REVIEW = "Review"
    DONE = "Done"

class Priority(Enum):
    """Enum representing the priority of a task."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

# Define data models
class User:
    """Class representing a user in the system."""
    def __init__(self, user_id: str, name: str, email: str, role: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

class Task:
    """Class representing a task in the system."""
    def __init__(self, task_id: str, title: str, description: str, status: TaskStatus, 
                 priority: Priority, assignee: Optional[User] = None, 
                 due_date: Optional[datetime] = None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.assignee = assignee
        self.due_date = due_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Project:
    """Class representing a project in the system."""
    def __init__(self, project_id: str, name: str, description: str):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks: List[Task] = []
        self.members: List[User] = []
        self.created_at = datetime.now()

class LearningModule:
    """Class representing an interactive learning module."""
    def __init__(self, module_id: str, title: str, content: str, 
                 related_tasks: List[Task] = None):
        self.module_id = module_id
        self.title = title
        self.content = content
        self.related_tasks = related_tasks if related_tasks else []
        self.completed_by: List[User] = []

# Agile Project Management Tool
class AgileProjectManager:
    """Main class for the Agile Project Management Tool with interactive learning features."""
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.users: Dict[str, User] = {}
        self.learning_modules: Dict[str, LearningModule] = {}

    def create_project(self, name: str, description: str) -> Project:
        """Create a new project."""
        project_id = str(uuid.uuid4())
        project = Project(project_id, name, description)
        self.projects[project_id] = project
        return project

    def add_user(self, name: str, email: str, role: str) -> User:
        """Add a new user to the system."""
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, role)
        self.users[user_id] = user
        return user

    def create_task(self, project_id: str, title: str, description: str, 
                    status: TaskStatus, priority: Priority, 
                    assignee_id: Optional[str] = None, 
                    due_date: Optional[datetime] = None) -> Task:
        """Create a new task in a project."""
        if project_id not in self.projects:
            raise ValueError("Project not found")
        
        assignee = None
        if assignee_id:
            if assignee_id not in self.users:
                raise ValueError("Assignee not found")
            assignee = self.users[assignee_id]
        
        task_id = str(uuid.uuid4())
        task = Task(task_id, title, description, status, priority, assignee, due_date)
        self.projects[project_id].tasks.append(task)
        return task

    def update_task_status(self, project_id: str, task_id: str, new_status: TaskStatus) -> Task:
        """Update the status of a task."""
        project = self.projects.get(project_id)
        if not project:
            raise ValueError("Project not found")
        
        task = next((t for t in project.tasks if t.task_id == task_id), None)
        if not task:
            raise ValueError("Task not found")
        
        task.status = new_status
        task.updated_at = datetime.now()
        return task

    def add_learning_module(self, title: str, content: str, 
                           related_task_ids: List[str] = None) -> LearningModule:
        """Add a new interactive learning module."""
        module_id = str(uuid.uuid4())
        related_tasks = []
        
        if related_task_ids:
            for project in self.projects.values():
                for task in project.tasks:
                    if task.task_id in related_task_ids:
                        related_tasks.append(task)
        
        module = LearningModule(module_id, title, content, related_tasks)
        self.learning_modules[module_id] = module
        return module

    def complete_learning_module(self, user_id: str, module_id: str) -> LearningModule:
        """Mark a learning module as completed by a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if module_id not in self.learning_modules:
            raise ValueError("Learning module not found")
        
        module = self.learning_modules[module_id]
        user = self.users[user_id]
        
        if user not in module.completed_by:
            module.completed_by.append(user)
        
        return module

    def get_recommended_modules(self, user_id: str) -> List[LearningModule]:
        """Get recommended learning modules based on user's tasks."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        recommended = []
        
        for module in self.learning_modules.values():
            # Recommend modules related to user's tasks
            for task in module.related_tasks:
                if task.assignee and task.assignee.user_id == user_id:
                    if module not in recommended:
                        recommended.append(module)
        
        return recommended

    def to_json(self) -> str:
        """Serialize the project manager data to JSON."""
        data = {
            "projects": [
                {
                    "project_id": p.project_id,
                    "name": p.name,
                    "description": p.description,
                    "tasks": [
                        {
                            "task_id": t.task_id,
                            "title": t.title,
                            "description": t.description,
                            "status": t.status.value,
                            "priority": t.priority.value,
                            "assignee": t.assignee.user_id if t.assignee else None,
                            "due_date": t.due_date.isoformat() if t.due_date else None,
                            "created_at": t.created_at.isoformat(),
                            "updated_at": t.updated_at.isoformat()
                        } for t in p.tasks
                    ],
                    "members": [m.user_id for m in p.members],
                    "created_at": p.created_at.isoformat()
                } for p in self.projects.values()
            ],
            "users": [
                {
                    "user_id": u.user_id,
                    "name": u.name,
                    "email": u.email,
                    "role": u.role
                } for u in self.users.values()
            ],
            "learning_modules": [
                {
                    "module_id": m.module_id,
                    "title": m.title,
                    "content": m.content,
                    "related_tasks": [t.task_id for t in m.related_tasks],
                    "completed_by": [u.user_id for u in m.completed_by]
                } for m in self.learning_modules.values()
            ]
        }
        return json.dumps(data, indent=2)

# Example usage
if __name__ == "__main__":
    manager = AgileProjectManager()
    
    # Create users
    product_owner = manager.add_user("Alice", "alice@example.com", "Product Owner")
    developer = manager.add_user("Bob", "bob@example.com", "Developer")
    
    # Create project
    project = manager.create_project("E-commerce Platform", "Build a new online store")
    
    # Create tasks
    task1 = manager.create_task(
        project.project_id, 
        "Implement shopping cart", 
        "Create the shopping cart functionality", 
        TaskStatus.TODO, 
        Priority.HIGH, 
        developer.user_id,
        datetime(2023, 12, 31)
    )
    
    task2 = manager.create_task(
        project.project_id, 
        "Design homepage", 
        "Create wireframes for the homepage", 
        TaskStatus.IN_PROGRESS, 
        Priority.MEDIUM
    )
    
    # Create learning module
    module = manager.add_learning_module(
        "Agile Development Basics", 
        "Learn the fundamentals of Agile methodology",
        [task1.task_id]
    )
    
    # Complete learning module
    manager.complete_learning_module(developer.user_id, module.module_id)
