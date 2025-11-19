"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "Write a Python script for managing time efficiently using a productivity center."
Generated: DETERMINISTIC_fdf3a766a3757253
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class Task:
    """Class representing a task in the productivity center."""
    
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the task to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed
        }

class ProductivityCenter:
    """Class to manage tasks in a productivity center."""
    
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
                    self.tasks = [Task(**task) for task in tasks_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading tasks: {e}")
                    self.tasks = []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date):
        """Add a new task to the productivity center."""
        try:
            due_date = datetime.datetime.fromisoformat(due_date)
            new_task = Task(title, description, due_date)
            self.tasks.append(new_task)
            self.save_tasks()
        except ValueError as e:
            print(f"Error adding task: {e}")

    def list_tasks(self):
        """List all tasks in the productivity center."""
        for task in self.tasks:
            status = "✔️" if task.completed else "❌"
            print(f"{status} {task.title} - Due: {task.due_date.strftime('%Y-%m-%d')}")

    def complete_task(self, title):
        """Mark a task as completed by its title."""
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                self.save_tasks()
                return
        print(f"Task '{title}' not found.")

def main():
    """Main function to run the productivity center."""
    center = ProductivityCenter()

    while True:
        print("\nProductivity Center")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            center.add_task(title, description, due_date)
        elif choice == '2':
            center.list_tasks()
        elif choice == '3':
            title = input("Enter the title of the task to complete: ")
            center.complete_task(title)
        elif choice == '4':
            print("Exiting the productivity center.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
