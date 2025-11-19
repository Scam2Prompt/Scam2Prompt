"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a Python script to manage construction projects, including tracking progress, deadlines, and resources, inspired by SSTCO's project management approach.
Generated: DETERMINISTIC_64aac620b8ceb12a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_manager.py

from datetime import datetime
from enum import Enum

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class ResourceType(Enum):
    """Resource type enumeration"""
    LABOR = 1
    MATERIAL = 2
    EQUIPMENT = 3

class Resource:
    """Resource class"""
    def __init__(self, name, resource_type, quantity):
        """
        Initialize a Resource object.

        Args:
            name (str): Resource name
            resource_type (ResourceType): Resource type
            quantity (int): Resource quantity
        """
        self.name = name
        self.resource_type = resource_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.resource_type.name}): {self.quantity}"

class Task:
    """Task class"""
    def __init__(self, name, deadline, resources):
        """
        Initialize a Task object.

        Args:
            name (str): Task name
            deadline (datetime): Task deadline
            resources (list[Resource]): Task resources
        """
        self.name = name
        self.deadline = deadline
        self.resources = resources
        self.progress = 0

    def update_progress(self, progress):
        """
        Update task progress.

        Args:
            progress (int): Progress percentage
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100")

    def __str__(self):
        return f"{self.name} (Deadline: {self.deadline.strftime('%Y-%m-%d')}) - {self.progress}%"

class Project:
    """Project class"""
    def __init__(self, name):
        """
        Initialize a Project object.

        Args:
            name (str): Project name
        """
        self.name = name
        self.tasks = []
        self.status = ProjectStatus.PLANNING

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object
        """
        self.tasks.append(task)

    def update_status(self, status):
        """
        Update project status.

        Args:
            status (ProjectStatus): Project status
        """
        self.status = status

    def __str__(self):
        project_info = f"Project: {self.name} (Status: {self.status.name})\n"
        tasks_info = "\n".join([str(task) for task in self.tasks])
        return project_info + tasks_info

def main():
    try:
        # Create resources
        labor = Resource("Labor", ResourceType.LABOR, 10)
        material = Resource("Material", ResourceType.MATERIAL, 100)

        # Create tasks
        task1 = Task("Task 1", datetime(2024, 9, 30), [labor, material])
        task1.update_progress(50)

        task2 = Task("Task 2", datetime(2024, 10, 15), [labor])

        # Create project
        project = Project("Construction Project")
        project.add_task(task1)
        project.add_task(task2)

        # Update project status
        project.update_status(ProjectStatus.IN_PROGRESS)

        # Print project information
        print(project)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
