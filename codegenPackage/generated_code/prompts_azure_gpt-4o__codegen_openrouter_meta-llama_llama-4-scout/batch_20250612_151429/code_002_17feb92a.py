"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a project management workflow in Python for civil engineering tasks, including structural repairs, waterproofing, and painting, inspired by SOM Civil Engineers' project management approach.
Generated: DETERMINISTIC_17feb92a70f58f09
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_workflow.py

from enum import Enum
from typing import List, Dict

class TaskStatus(Enum):
    """Task status enum"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Task:
    """Task class"""
    def __init__(self, id: int, name: str, description: str, status: TaskStatus = TaskStatus.PENDING):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def update_status(self, status: TaskStatus):
        """Update task status"""
        self.status = status

    def __str__(self):
        return f"Task {self.id}: {self.name} - {self.status.name}"

class Project:
    """Project class"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add task to project"""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Get all tasks in project"""
        return self.tasks

    def __str__(self):
        return f"Project {self.id}: {self.name}"

class Workflow:
    """Workflow class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def create_project(self, project: Project):
        """Create a new project"""
        self.projects[project.id] = project

    def get_project(self, project_id: int) -> Project:
        """Get project by id"""
        try:
            return self.projects[project_id]
        except KeyError:
            raise ValueError(f"Project {project_id} not found")

    def add_task_to_project(self, project_id: int, task: Task):
        """Add task to project"""
        project = self.get_project(project_id)
        project.add_task(task)

def main():
    # Create workflow
    workflow = Workflow()

    # Create projects
    project1 = Project(1, "Structural Repairs")
    project2 = Project(2, "Waterproofing")
    project3 = Project(3, "Painting")

    # Add projects to workflow
    workflow.create_project(project1)
    workflow.create_project(project2)
    workflow.create_project(project3)

    # Create tasks
    task1 = Task(1, "Repair Column", "Repair damaged column")
    task2 = Task(2, "Apply Waterproofing Coating", "Apply waterproofing coating to roof")
    task3 = Task(3, "Paint Walls", "Paint walls with new color")

    # Add tasks to projects
    workflow.add_task_to_project(1, task1)
    workflow.add_task_to_project(2, task2)
    workflow.add_task_to_project(3, task3)

    # Update task status
    task1.update_status(TaskStatus.IN_PROGRESS)
    task2.update_status(TaskStatus.COMPLETED)

    # Print project tasks
    for project in workflow.projects.values():
        print(project)
        for task in project.get_tasks():
            print(task)

if __name__ == "__main__":
    main()
```
