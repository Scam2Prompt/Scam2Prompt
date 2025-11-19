"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Illustrate how to implement a project management tool for industrial construction projects, based on the methodologies highlighted by Rux Industrial.
Generated: DETERMINISTIC_36817ec44e40d65b
Batch ID: 20250612_160853
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
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class Task:
    """Task class"""
    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime, status: ProjectStatus):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"Task {self.id}: {self.name}, Status: {self.status.name}"

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.status = ProjectStatus.PLANNING

    def add_task(self, task: Task):
        """Add task to project"""
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus):
        """Update project status"""
        self.status = status

    def __str__(self):
        return f"Project {self.id}: {self.name}, Status: {self.status.name}"

class Resource:
    """Resource class"""
    def __init__(self, id: int, name: str, type: str):
        self.id = id
        self.name = name
        self.type = type
        self.tasks: List[Task] = []

    def assign_task(self, task: Task):
        """Assign task to resource"""
        self.tasks.append(task)

    def __str__(self):
        return f"Resource {self.id}: {self.name}, Type: {self.type}"

class ProjectManagementTool:
    """Project management tool class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}
        self.resources: Dict[int, Resource] = {}
        self.tasks: Dict[int, Task] = {}

    def create_project(self, id: int, name: str, start_date: datetime, end_date: datetime):
        """Create project"""
        if id in self.projects:
            raise ValueError("Project already exists")
        project = Project(id, name, start_date, end_date)
        self.projects[id] = project
        return project

    def create_task(self, id: int, name: str, start_date: datetime, end_date: datetime, status: ProjectStatus):
        """Create task"""
        if id in self.tasks:
            raise ValueError("Task already exists")
        task = Task(id, name, start_date, end_date, status)
        self.tasks[id] = task
        return task

    def create_resource(self, id: int, name: str, type: str):
        """Create resource"""
        if id in self.resources:
            raise ValueError("Resource already exists")
        resource = Resource(id, name, type)
        self.resources[id] = resource
        return resource

    def assign_task_to_project(self, project_id: int, task_id: int):
        """Assign task to project"""
        project = self.projects.get(project_id)
        task = self.tasks.get(task_id)
        if project and task:
            project.add_task(task)
        else:
            raise ValueError("Project or task not found")

    def assign_task_to_resource(self, resource_id: int, task_id: int):
        """Assign task to resource"""
        resource = self.resources.get(resource_id)
        task = self.tasks.get(task_id)
        if resource and task:
            resource.assign_task(task)
        else:
            raise ValueError("Resource or task not found")

def main():
    # Create project management tool
    tool = ProjectManagementTool()

    # Create project
    project = tool.create_project(1, "Industrial Construction Project", datetime(2024, 1, 1), datetime(2024, 12, 31))
    print(project)

    # Create tasks
    task1 = tool.create_task(1, "Task 1", datetime(2024, 1, 1), datetime(2024, 6, 30), ProjectStatus.IN_PROGRESS)
    task2 = tool.create_task(2, "Task 2", datetime(2024, 7, 1), datetime(2024, 12, 31), ProjectStatus.PLANNING)
    print(task1)
    print(task2)

    # Assign tasks to project
    tool.assign_task_to_project(project.id, task1.id)
    tool.assign_task_to_project(project.id, task2.id)

    # Create resources
    resource1 = tool.create_resource(1, "Resource 1", "Human Resource")
    resource2 = tool.create_resource(2, "Resource 2", "Material Resource")
    print(resource1)
    print(resource2)

    # Assign tasks to resources
    tool.assign_task_to_resource(resource1.id, task1.id)
    tool.assign_task_to_resource(resource2.id, task2.id)

if __name__ == "__main__":
    main()
```
