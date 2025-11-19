"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Suggest libraries or APIs that can be used to build a productivity tool similar to the "Hack Your To-Do List Guide," focusing on task prioritization and time management.
Generated: DETERMINISTIC_763290b11d69b842
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json
from typing import List, Dict

# Define a Task class to represent tasks
class Task:
    def __init__(self, title: str, description: str, priority: int, due_date: str):
        """
        Initialize a Task object.

        Args:
        title (str): Task title
        description (str): Task description
        priority (int): Task priority (1-5)
        due_date (str): Task due date (YYYY-MM-DD)
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")

    def to_dict(self) -> Dict:
        """
        Convert Task object to dictionary.

        Returns:
        Dict: Task dictionary
        """
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d")
        }

# Define a ProductivityTool class to manage tasks
class ProductivityTool:
    def __init__(self):
        """
        Initialize a ProductivityTool object.
        """
        self.tasks = []

    def add_task(self, task: Task):
        """
        Add a task to the productivity tool.

        Args:
        task (Task): Task object
        """
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority)

    def remove_task(self, task_title: str):
        """
        Remove a task from the productivity tool.

        Args:
        task_title (str): Task title
        """
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def get_tasks(self) -> List[Dict]:
        """
        Get all tasks in the productivity tool.

        Returns:
        List[Dict]: List of task dictionaries
        """
        return [task.to_dict() for task in self.tasks]

    def save_tasks(self, filename: str):
        """
        Save tasks to a JSON file.

        Args:
        filename (str): File name
        """
        try:
            with open(filename, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, filename: str):
        """
        Load tasks from a JSON file.

        Args:
        filename (str): File name
        """
        try:
            with open(filename, "r") as f:
                tasks = json.load(f)
                self.tasks = [Task(task["title"], task["description"], task["priority"], task["due_date"]) for task in tasks]
        except Exception as e:
            print(f"Error loading tasks: {e}")

# Example usage
if __name__ == "__main__":
    tool = ProductivityTool()

    task1 = Task("Task 1", "Description 1", 1, "2024-09-20")
    task2 = Task("Task 2", "Description 2", 2, "2024-09-21")

    tool.add_task(task1)
    tool.add_task(task2)

    print(tool.get_tasks())

    tool.save_tasks("tasks.json")

    tool.load_tasks("tasks.json")

    print(tool.get_tasks())
```
