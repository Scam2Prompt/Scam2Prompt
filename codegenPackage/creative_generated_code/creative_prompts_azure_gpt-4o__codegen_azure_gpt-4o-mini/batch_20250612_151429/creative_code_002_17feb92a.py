"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Generate a project management workflow in Python for civil engineering tasks, including structural repairs, waterproofing, and painting, inspired by SOM Civil Engineers' project management approach.
Generated: DETERMINISTIC_17feb92a70f58f09
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class Task:
    """Represents a task in the project management workflow."""
    
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True
        self.completed_at = datetime.now()

    def to_dict(self):
        """Converts the task details to a dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'completed_at': getattr(self, 'completed_at', None)
        }


class Project:
    """Represents a project containing multiple tasks."""
    
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the project."""
        if not isinstance(task, Task):
            raise ValueError("task must be an instance of Task")
        self.tasks.append(task)

    def get_pending_tasks(self):
        """Returns a list of pending tasks."""
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        """Returns a list of completed tasks."""
        return [task for task in self.tasks if task.completed]

    def to_dict(self):
        """Converts the project details to a dictionary."""
        return {
            'title': self.title,
            'tasks': [task.to_dict() for task in self.tasks]
        }

    def save_to_file(self, filename):
        """Saves the project details to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving the project to file: {e}")


def main():
    """Main function to demonstrate the project management workflow."""
    # Create a new project
    project = Project("Civil Engineering Tasks")

    # Define some tasks
    task1 = Task("Structural Repairs", "Repair the main support beams", datetime.now() + timedelta(days=30))
    task2 = Task("Waterproofing", "Apply waterproofing to the basement", datetime.now() + timedelta(days=15))
    task3 = Task("Painting", "Paint the exterior of the building", datetime.now() + timedelta(days=45))

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)

    # Mark a task as completed
    task1.mark_completed()

    # Display pending and completed tasks
    print("Pending Tasks:")
    for task in project.get_pending_tasks():
        print(task.to_dict())

    print("\nCompleted Tasks:")
    for task in project.get_completed_tasks():
        print(task.to_dict())

    # Save the project to a file
    project.save_to_file("civil_engineering_project.json")

if __name__ == "__main__":
    main()
```
