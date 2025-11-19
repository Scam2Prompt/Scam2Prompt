"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    """Task status enum"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class Task:
    """Task class"""
    def __init__(self, task_id, name, description, phase, status=TaskStatus.PENDING):
        """
        Initialize a task

        Args:
            task_id (int): Unique task ID
            name (str): Task name
            description (str): Task description
            phase (str): Task phase (design or execution)
            status (TaskStatus, optional): Task status. Defaults to TaskStatus.PENDING.
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.phase = phase
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, status):
        """
        Update task status

        Args:
            status (TaskStatus): New task status
        """
        self.status = status
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Task {self.task_id}: {self.name} ({self.phase}) - {self.status.name}"

class Project:
    """Project class"""
    def __init__(self, project_id, name):
        """
        Initialize a project

        Args:
            project_id (int): Unique project ID
            name (str): Project name
        """
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project

        Args:
            task (Task): Task to add
        """
        self.tasks.append(task)

    def get_tasks(self, phase=None):
        """
        Get tasks for the project

        Args:
            phase (str, optional): Phase to filter tasks by. Defaults to None.

        Returns:
            list[Task]: List of tasks
        """
        if phase:
            return [task for task in self.tasks if task.phase == phase]
        return self.tasks

def main():
    try:
        # Create a project
        project = Project(1, "Vivek Enterprises Interior Turnkey Contracting")

        # Create tasks
        task1 = Task(1, "Design Concept", "Create design concept for the project", "design")
        task2 = Task(2, "Execution Planning", "Plan execution for the project", "execution")
        task3 = Task(3, "Material Procurement", "Procure materials for the project", "execution")

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # Print project tasks
        print("Project Tasks:")
        for task in project.get_tasks():
            print(task)

        # Update task status
        task1.update_status(TaskStatus.IN_PROGRESS)
        print(f"\nUpdated Task {task1.task_id} Status: {task1.status.name}")

        # Print design phase tasks
        print("\nDesign Phase Tasks:")
        for task in project.get_tasks("design"):
            print(task)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
