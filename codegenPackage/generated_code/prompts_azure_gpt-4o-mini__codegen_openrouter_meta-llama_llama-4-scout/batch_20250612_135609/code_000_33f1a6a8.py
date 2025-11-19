"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Generate a code snippet for a construction project management application that includes features for building construction, renovation works, and fit-out works.
Generated: DETERMINISTIC_33f1a6a8923932a9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management.py

from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class ProjectType(Enum):
    """Project type enumeration"""
    BUILDING_CONSTRUCTION = 1
    RENOVATION_WORKS = 2
    FIT_OUT_WORKS = 3

class Project:
    """Project class"""
    def __init__(self, project_id: int, project_name: str, project_type: ProjectType, status: ProjectStatus):
        self.project_id = project_id
        self.project_name = project_name
        self.project_type = project_type
        self.status = status
        self.tasks: List[Task] = []

    def add_task(self, task: 'Task'):
        """Add task to project"""
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus):
        """Update project status"""
        self.status = status

class Task:
    """Task class"""
    def __init__(self, task_id: int, task_name: str, task_type: str, start_date: str, end_date: str):
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type
        self.start_date = start_date
        self.end_date = end_date
        self.status: TaskStatus = TaskStatus.PENDING

    def update_status(self, status: TaskStatus):
        """Update task status"""
        self.status = status

class TaskStatus(Enum):
    """Task status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class ConstructionProjectManagement:
    """Construction project management class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def create_project(self, project_id: int, project_name: str, project_type: ProjectType):
        """Create project"""
        if project_id in self.projects:
            raise ValueError("Project already exists")
        project = Project(project_id, project_name, project_type, ProjectStatus.PLANNING)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id: int) -> Project:
        """Get project by ID"""
        return self.projects.get(project_id)

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """Update project status"""
        project = self.get_project(project_id)
        if project:
            project.update_status(status)
        else:
            raise ValueError("Project not found")

def main():
    # Example usage
    management = ConstructionProjectManagement()

    project1 = management.create_project(1, "Building Construction Project", ProjectType.BUILDING_CONSTRUCTION)
    project2 = management.create_project(2, "Renovation Works Project", ProjectType.RENOVATION_WORKS)

    task1 = Task(1, "Site preparation", "Site preparation", "2024-01-01", "2024-01-31")
    task2 = Task(2, "Foundation works", "Foundation works", "2024-02-01", "2024-04-30")

    project1.add_task(task1)
    project1.add_task(task2)

    management.update_project_status(1, ProjectStatus.IN_PROGRESS)

    print("Project 1 Name:", project1.project_name)
    print("Project 1 Status:", project1.status.name)
    for task in project1.tasks:
        print("Task Name:", task.task_name)
        print("Task Status:", task.status.name)

if __name__ == "__main__":
    main()
```
