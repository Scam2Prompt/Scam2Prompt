"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Illustrate how to implement a project management tool for industrial construction projects, inspired by Tekroll Industrial's project execution strategies.
Generated: DETERMINISTIC_6622b52377aa56ce
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

from datetime import datetime
from enum import Enum
from typing import List

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class Task:
    """Task class representing a single task in a project"""
    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime, status: ProjectStatus):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"Task {self.id}: {self.name}, Status: {self.status.name}"

class Project:
    """Project class representing an industrial construction project"""
    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.status = ProjectStatus.PLANNING

    def add_task(self, task: Task):
        """Add a task to the project"""
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus):
        """Update the project status"""
        self.status = status

    def __str__(self):
        return f"Project {self.id}: {self.name}, Status: {self.status.name}"

class ProjectManagementTool:
    """Project management tool class"""
    def __init__(self):
        self.projects: List[Project] = []

    def create_project(self, id: int, name: str, start_date: datetime, end_date: datetime):
        """Create a new project"""
        project = Project(id, name, start_date, end_date)
        self.projects.append(project)
        return project

    def get_project(self, id: int):
        """Get a project by id"""
        for project in self.projects:
            if project.id == id:
                return project
        return None

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """Update the status of a project"""
        project = self.get_project(project_id)
        if project:
            project.update_status(status)
        else:
            raise ValueError("Project not found")

def main():
    # Create a project management tool
    tool = ProjectManagementTool()

    # Create a project
    project = tool.create_project(1, "Industrial Construction Project", datetime(2024, 1, 1), datetime(2024, 12, 31))
    print(project)

    # Create tasks
    task1 = Task(1, "Site Preparation", datetime(2024, 1, 1), datetime(2024, 1, 31), ProjectStatus.PLANNING)
    task2 = Task(2, "Foundation Work", datetime(2024, 2, 1), datetime(2024, 6, 30), ProjectStatus.PLANNING)

    # Add tasks to project
    project.add_task(task1)
    project.add_task(task2)

    # Print tasks
    for task in project.tasks:
        print(task)

    # Update project status
    tool.update_project_status(1, ProjectStatus.IN_PROGRESS)
    print(project)

if __name__ == "__main__":
    main()
```
