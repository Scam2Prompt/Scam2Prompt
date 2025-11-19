"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script that automates the tracking of special paint works and renovation tasks for a contracting business.
Generated: DETERMINISTIC_e0ae03a36bfba924
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class Task:
    """Class representing a renovation task or special paint work."""

    def __init__(self, title, description, due_date, status='Pending'):
        """Initialize a new task with title, description, due date, and status."""
        self.title = title
        self.description = description
        self.due_date = self._validate_due_date(due_date)
        self.status = status

    def _validate_due_date(self, due_date):
        """Validate and return due date in YYYY-MM-DD format."""
        try:
            return datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")

    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'due_date': str(self.due_date),
            'status': self.status
        }

class TaskManager:
    """Class to manage tasks for special paint works and renovations."""

    def __init__(self, data_file='tasks.json'):
        """Initialize the TaskManager with a data file."""
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return [Task(**task) for task in json.load(file)]
                except json.JSONDecodeError:
                    print("Error in loading tasks: Invalid JSON format.")
                    return []
        return []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date):
        """Add a new task and save to file."""
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        """List all tasks."""
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, "
                  f"Due Date: {task.due_date}, Status: {task.status}")

    def update_task_status(self, title, status):
        """Update the status of a task by title."""
        for task in self.tasks:
            if task.title == title:
                task.status = status
                self.save_tasks()
                return
        print(f"Task with title '{title}' not found.")

def main():
    """Main function to run the task manager."""
    manager = TaskManager()

    # Example usage
    try:
        manager.add_task('Paint Living Room', 'Use eco-friendly paint', '2023-10-31')
        manager.add_task('Renovate Kitchen', 'Install new cabinets', '2023-11-15')

        print("Current tasks:")
        manager.list_tasks()

        manager.update_task_status('Paint Living Room', 'Completed')
        print("\nUpdated tasks:")
        manager.list_tasks()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
