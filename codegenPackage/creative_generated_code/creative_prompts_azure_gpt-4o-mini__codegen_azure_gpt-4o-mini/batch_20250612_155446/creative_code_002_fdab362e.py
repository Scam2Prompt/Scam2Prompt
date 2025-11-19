"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Write a code snippet that utilizes Python to implement a basic project discussed in the Talento Tech Programacion section of the Ejecutor Tecnico webpage.
Generated: DETERMINISTIC_fdab362e4a3753a4
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Task:
    """
    A class to represent a task in a to-do list.
    """

    def __init__(self, title, description):
        """
        Initializes a new task with title and description.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
        """
        self.title = title
        self.description = description
        self.completed = False

    def complete_task(self):
        """Marks the task as completed."""
        self.completed = True

    def __repr__(self):
        """Returns a string representation of the task."""
        return f"Task(title={self.title}, completed={self.completed})"


class TaskManager:
    """
    A class to manage a list of tasks.
    """

    def __init__(self):
        """Initializes an empty task list."""
        self.tasks = []

    def add_task(self, title, description):
        """
        Adds a new task to the task list.

        Args:
            title (str): The title of the new task.
            description (str): The description of the new task.
        """
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def complete_task(self, title):
        """
        Marks a task as completed by title.

        Args:
            title (str): The title of the task to be completed.
        """
        for task in self.tasks:
            if task.title == title:
                task.complete_task()
                return
        raise ValueError(f"Task with title '{title}' not found.")

    def list_tasks(self):
        """Returns a list of all tasks."""
        return self.tasks

    def save_to_file(self, filename):
        """
        Saves the current tasks to a JSON file.

        Args:
            filename (str): The name of the file to save tasks to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file)
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def load_from_file(self, filename):
        """
        Loads tasks from a JSON file.

        Args:
            filename (str): The name of the file to load tasks from.
        """
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task) for task in tasks_data]
        except IOError as e:
            print(f"Error loading tasks from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


if __name__ == "__main__":
    # Example usage of the TaskManager class
    manager = TaskManager()
    manager.add_task("Learn Python", "Complete the Python course.")
    manager.add_task("Build a project", "Develop a simple project using Python.")

    # Mark a task as completed
    try:
        manager.complete_task("Learn Python")
    except ValueError as e:
        print(e)

    # List all tasks
    for task in manager.list_tasks():
        print(task)

    # Save tasks to a file
    manager.save_to_file("tasks.json")

    # Load tasks from a file
    manager.load_from_file("tasks.json")
```
