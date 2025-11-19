"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Create a Python script to track and manage municipal and traffic-related tasks, such as vehicle licensing updates and traffic fine monitoring, as described in Alphamor’s property management services.
Generated: DETERMINISTIC_9303e2cc843cb55b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class Task:
    """Class to represent a municipal or traffic-related task."""
    
    def __init__(self, task_id, description, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        """Convert the task to a dictionary for JSON serialization."""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create a Task instance from a dictionary."""
        return Task(
            task_id=data['task_id'],
            description=data['description'],
            due_date=datetime.fromisoformat(data['due_date']),
            completed=data['completed']
        )

class TaskManager:
    """Class to manage a collection of tasks."""
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    tasks_data = json.load(file)
                    self.tasks = [Task.from_dict(task) for task in tasks_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading tasks: {e}")
                    self.tasks = []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description, due_date):
        """Add a new task to the task manager."""
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                self.save_tasks()
                return
        print(f"Task with ID {task_id} not found.")

    def list_tasks(self):
        """List all tasks."""
        for task in self.tasks:
            status = "✔️" if task.completed else "❌"
            print(f"ID: {task.task_id}, Description: {task.description}, Due: {task.due_date.date()}, Status: {status}")

def main():
    """Main function to run the task manager."""
    manager = TaskManager()

    # Example usage
    while True:
        print("\nMunicipal and Traffic Task Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                manager.add_task(description, due_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '2':
            task_id = int(input("Enter task ID to complete: "))
            manager.complete_task(task_id)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
