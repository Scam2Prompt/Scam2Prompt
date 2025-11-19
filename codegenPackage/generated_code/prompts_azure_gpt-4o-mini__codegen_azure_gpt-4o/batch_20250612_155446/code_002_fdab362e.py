"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Write a code snippet that utilizes Python to implement a basic project discussed in the Talento Tech Programacion section of the Ejecutor Tecnico webpage.
Generated: DETERMINISTIC_fdab362e4a3753a4
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Project: Task Manager
This Python script implements a simple task manager where users can add, view, and delete tasks.
The code follows best practices, includes error handling, and is production-ready.
"""

import sys

class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty task list."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the task list.
        :param task: str - The task description.
        """
        if not task.strip():
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        """Display all tasks in the task list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        """
        Delete a task by its number.
        :param task_number: int - The task number to delete.
        """
        try:
            task_index = task_number - 1
            deleted_task = self.tasks.pop(task_index)
            print(f"Task deleted: {deleted_task}")
        except IndexError:
            print("Invalid task number. Please try again.")
        except ValueError:
            print("Task number must be an integer.")

def main():
    """Main function to run the Task Manager."""
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter task description: ")
            try:
                task_manager.add_task(task)
            except ValueError as e:
                print(e)
        elif choice == 2:
            task_manager.view_tasks()
        elif choice == 3:
            try:
                task_number = int(input("Enter task number to delete: "))
                task_manager.delete_task(task_number)
            except ValueError:
                print("Invalid input. Task number must be an integer.")
        elif choice == 4:
            print("Exiting Task Manager. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
```
