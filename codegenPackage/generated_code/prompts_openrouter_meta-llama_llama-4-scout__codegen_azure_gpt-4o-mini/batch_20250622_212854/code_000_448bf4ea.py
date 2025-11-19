"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Write a Python script to manage a brick and stone restoration project, including tasks for repointing, tuckpointing, and lintel replacement."
Generated: DETERMINISTIC_448bf4eacc319af0
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class RestorationTask:
    """Class to represent a restoration task."""
    
    def __init__(self, task_name: str, description: str, due_date: str):
        self.task_name = task_name
        self.description = description
        self.due_date = self.validate_due_date(due_date)
        self.completed = False

    @staticmethod
    def validate_due_date(due_date: str) -> str:
        """Validate the due date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert the task to a dictionary for JSON serialization."""
        return {
            "task_name": self.task_name,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

class RestorationProject:
    """Class to manage a restoration project."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.tasks: List[RestorationTask] = []

    def add_task(self, task: RestorationTask):
        """Add a new task to the project."""
        self.tasks.append(task)

    def complete_task(self, task_name: str):
        """Mark a task as completed by its name."""
        for task in self.tasks:
            if task.task_name == task_name:
                task.mark_completed()
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def save_to_file(self, filename: str):
        """Save the project tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load project tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [RestorationTask(**task) for task in tasks_data]
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading from file: {e}")

    def list_tasks(self) -> List[Dict[str, Any]]:
        """List all tasks in the project."""
        return [task.to_dict() for task in self.tasks]

def main():
    """Main function to demonstrate the restoration project management."""
    project = RestorationProject("Brick and Stone Restoration")

    # Adding tasks
    project.add_task(RestorationTask("Repointing", "Repoint the brickwork on the east wall.", "2023-12-01"))
    project.add_task(RestorationTask("Tuckpointing", "Tuckpoint the south wall.", "2023-12-15"))
    project.add_task(RestorationTask("Lintel Replacement", "Replace the lintel above the front door.", "2023-12-20"))

    # Marking a task as completed
    try:
        project.complete_task("Repointing")
    except ValueError as e:
        print(e)

    # Saving the project to a file
    try:
        project.save_to_file("restoration_project.json")
    except IOError as e:
        print(e)

    # Loading the project from a file
    try:
        project.load_from_file("restoration_project.json")
    except ValueError as e:
        print(e)

    # Listing all tasks
    tasks = project.list_tasks()
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
```
