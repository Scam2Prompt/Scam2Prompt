"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a code snippet for a project management tool that tracks the progress of civil maintenance tasks, inspired by the project management practices at SOM Civil.
Generated: DETERMINISTIC_0116aa7966cc1132
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Task:
    """Class representing a maintenance task."""
    
    def __init__(self, title: str, description: str, due_date: datetime.date):
        """
        Initialize a new task.

        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date for the task
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.datetime.now()

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """String representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title}, Status: {status}, Due: {self.due_date}"

class Project:
    """Class representing a project containing multiple tasks."""
    
    def __init__(self, name: str):
        """
        Initialize a new project.

        :param name: Name of the project
        """
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        Add a task to the project.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Return a list of pending tasks."""
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[Task]:
        """Return a list of completed tasks."""
        return [task for task in self.tasks if task.completed]

    def __str__(self):
        """String representation of the project."""
        return f"Project: {self.name}, Total Tasks: {len(self.tasks)}"

def main():
    """Main function to demonstrate the project management tool."""
    try:
        # Create a new project
        project = Project("Civil Maintenance Project")

        # Add tasks to the project
        task1 = Task("Repair Road", "Fix potholes on Main St.", datetime.date(2023, 11, 15))
        task2 = Task("Inspect Bridge", "Annual inspection of the Old Bridge.", datetime.date(2023, 12, 01))
        
        project.add_task(task1)
        project.add_task(task2)

        # Mark the first task as completed
        task1.mark_completed()

        # Display project details
        print(project)
        print("Pending Tasks:")
        for task in project.get_pending_tasks():
            print(task)
        print("Completed Tasks:")
        for task in project.get_completed_tasks():
            print(task)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
