"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: Develop a task management tool using ChatGPT's capabilities for organizing tasks and managing time, tailored for individuals in reconversion or those seeking to improve productivity.
Generated: DETERMINISTIC_2e0fd88d27875d61
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Task:
    """Class representing a single task."""
    
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else datetime.now() + timedelta(days=7)  # Default to one week from now
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the task to a dictionary for easy serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed
        }

class TaskManager:
    """Class to manage a collection of tasks."""
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if file not found or invalid JSON

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date=None):
        """Add a new task to the task manager."""
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def complete_task(self, title):
        """Mark a task as completed by its title."""
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.mark_completed()
                self.save_tasks()
                return
        raise ValueError(f"Task '{title}' not found or already completed.")

    def list_tasks(self):
        """List all tasks."""
        return [task.to_dict() for task in self.tasks]

    def list_pending_tasks(self):
        """List all pending tasks."""
        return [task.to_dict() for task in self.tasks if not task.completed]

def main():
    """Main function to run the task management tool."""
    task_manager = TaskManager()

    # Example usage
    task_manager.add_task("Learn Python", "Complete the Python course on Codecademy.")
    task_manager.add_task("Build a project", "Create a task management tool using Python.")
    
    print("All Tasks:")
    print(task_manager.list_tasks())

    print("\nPending Tasks:")
    print(task_manager.list_pending_tasks())

    try:
        task_manager.complete_task("Learn Python")
        print("\nAfter completing 'Learn Python':")
        print(task_manager.list_pending_tasks())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
