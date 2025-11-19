"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: How can I apply the programming techniques from the Ejecutor Tecnico's "Presentaciones de Python" in a real-world project?
Generated: DETERMINISTIC_81da5285d62f7773
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean and well-structured Python code example that applies common programming techniques discussed in "Presentaciones de Python." This example demonstrates a simple task manager application that allows users to create, view, and delete tasks.

```python
import json
import os

# Constants
TASKS_FILE = 'tasks.json'

# Task Manager Class
class TaskManager:
    def __init__(self):
        """Initialize the TaskManager and load existing tasks."""
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error reading tasks file. Returning empty task list.")
                    return []
        return []

    def save_tasks(self):
        """Save the current list of tasks to a JSON file."""
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}: {task}")

    def delete_task(self, task_index):
        """Delete a task by its index."""
        try:
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f'Task "{removed_task}" deleted successfully.')
        except IndexError:
            print("Error: Invalid task index.")

# Main function
def main():
    """Main entry point of the task manager application."""
    manager = TaskManager()

    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to delete: "))
            manager.delete_task(task_index)
        elif choice == '4':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

### Notes:
- The code follows best practices, including encapsulation via a class, error handling for file operations and user inputs, and clear separation of concerns.
- It uses JSON for persistent storage of tasks, which is a common technique for lightweight data storage.
- Each function and class method is well-documented with docstrings explaining their purpose.
