"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Recommend tools or libraries for implementing a project management system to coordinate renovation tasks, as described in the webpage's "6 steps to ideal renovation" process.
Generated: DETERMINISTIC_e897c14e0c0392c6
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# renovation_project_management.py

import datetime
from enum import Enum
from typing import List

class RenovationTaskStatus(Enum):
    """Task status enum"""
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3

class RenovationTask:
    """Represents a renovation task"""
    def __init__(self, id: int, name: str, description: str, status: RenovationTaskStatus = RenovationTaskStatus.TO_DO):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.assigned_to = None
        self.due_date = None

    def assign_task(self, assignee: str, due_date: datetime.date):
        """Assign task to a person with a due date"""
        self.assigned_to = assignee
        self.due_date = due_date

    def update_status(self, status: RenovationTaskStatus):
        """Update task status"""
        self.status = status

class RenovationProject:
    """Represents a renovation project"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.tasks = []

    def add_task(self, task: RenovationTask):
        """Add task to project"""
        self.tasks.append(task)

    def get_tasks(self, status: RenovationTaskStatus = None):
        """Get tasks by status"""
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

class RenovationProjectManagementSystem:
    """Manages renovation projects"""
    def __init__(self):
        self.projects = []

    def create_project(self, id: int, name: str):
        """Create a new project"""
        project = RenovationProject(id, name)
        self.projects.append(project)
        return project

    def get_project(self, id: int):
        """Get project by id"""
        for project in self.projects:
            if project.id == id:
                return project
        return None

def main():
    # Create a project management system
    system = RenovationProjectManagementSystem()

    # Create a new project
    project = system.create_project(1, "My Renovation Project")

    # Create tasks
    task1 = RenovationTask(1, "Demolition", "Demolish the old kitchen")
    task2 = RenovationTask(2, "Installation", "Install new kitchen cabinets")

    # Add tasks to project
    project.add_task(task1)
    project.add_task(task2)

    # Assign tasks
    task1.assign_task("John Doe", datetime.date(2024, 9, 20))
    task2.assign_task("Jane Doe", datetime.date(2024, 9, 25))

    # Update task status
    task1.update_status(RenovationTaskStatus.IN_PROGRESS)

    # Get tasks
    tasks = project.get_tasks()
    for task in tasks:
        print(f"Task {task.id}: {task.name} - Status: {task.status.name}")

if __name__ == "__main__":
    main()
```
