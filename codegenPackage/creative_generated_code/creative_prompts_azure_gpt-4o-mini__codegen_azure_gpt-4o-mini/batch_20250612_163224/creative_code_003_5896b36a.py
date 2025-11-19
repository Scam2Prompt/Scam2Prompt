"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coach-chatgpt.com
Prompt: How can I use ChatGPT to organize my daily tasks effectively?
Generated: DETERMINISTIC_5896b36a52d2ec7f
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Task:
    """Class to represent a task."""
    
    def __init__(self, title: str, description: str, deadline: Optional[datetime] = None):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def to_dict(self) -> Dict:
        """Converts the task to a dictionary for serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "completed": self.completed,
        }


class TaskManager:
    """Class to manage a list of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, deadline: Optional[datetime] = None):
        """Adds a new task to the task list."""
        new_task = Task(title, description, deadline)
        self.tasks.append(new_task)

    def remove_task(self, index: int):
        """Removes a task by its index."""
        try:
            del self.tasks[index]
        except IndexError:
            print(f"Error: No task found at index {index}.")

    def mark_task_completed(self, index: int):
        """Marks a specified task as completed."""
        try:
            self.tasks[index].mark_completed()
        except IndexError:
            print(f"Error: No task found at index {index}.")

    def list_tasks(self) -> List[Dict]:
        """Returns a list of all tasks in dictionary format."""
        return [task.to_dict() for task in self.tasks]

    def save_tasks(self, filename: str):
        """Saves the tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_tasks(), file, indent=4)
        except IOError as e:
            print(f"Error saving tasks to {filename}: {e}")

    def load_tasks(self, filename: str):
        """Loads tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task) for task in tasks_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading tasks from {filename}: {e}")


# Example Usage
if __name__ == "__main__":
    task_manager = TaskManager()

    # Adding some tasks
    task_manager.add_task("Complete the project report", "Finalize and submit the project report by EOD", datetime(2023, 10, 30))
    task_manager.add_task("Prepare for the meeting", "Gather all necessary documents for the meeting", None)

    # Listing tasks
    print("Current Tasks:")
    for task in task_manager.list_tasks():
        print(task)

    # Marking a task as completed
    task_manager.mark_task_completed(0)

    # Saving tasks to a file
    task_manager.save_tasks("tasks.json")

    # Loading tasks from a file
    task_manager.load_tasks("tasks.json")
```
