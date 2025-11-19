"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: "Create a Python script to manage game development projects, including tasks such as design, development, and advertisement, using Agile methodologies."
Generated: DETERMINISTIC_b1629e8827e329fd
Batch ID: 20250622_212440
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
from typing import List, Dict, Optional

class Task:
    """Class representing a task in the game development project."""
    
    def __init__(self, title: str, description: str, status: str, assignee: str, due_date: str):
        self.title = title
        self.description = description
        self.status = status  # e.g., 'To Do', 'In Progress', 'Done'
        self.assignee = assignee
        self.due_date = self.validate_due_date(due_date)

    @staticmethod
    def validate_due_date(due_date: str) -> str:
        """Validates the due date format."""
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")

    def to_dict(self) -> Dict:
        """Converts the task to a dictionary for JSON serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "assignee": self.assignee,
            "due_date": self.due_date
        }

class Project:
    """Class representing a game development project."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the project."""
        self.tasks.append(task)

    def update_task(self, title: str, status: Optional[str] = None, assignee: Optional[str] = None) -> None:
        """Updates the status or assignee of a task."""
        for task in self.tasks:
            if task.title == title:
                if status:
                    task.status = status
                if assignee:
                    task.assignee = assignee
                return
        raise ValueError(f"Task with title '{title}' not found.")

    def remove_task(self, title: str) -> None:
        """Removes a task from the project."""
        self.tasks = [task for task in self.tasks if task.title != title]

    def save_to_file(self, filename: str) -> None:
        """Saves the project tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Loads tasks from a JSON file into the project."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(**task_data)
                    self.add_task(task)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate project management."""
    project = Project("Game Development Project")

    # Example tasks
    try:
        task1 = Task("Design Game Mechanics", "Define the core mechanics of the game.", "To Do", "Alice", "2023-12-01")
        task2 = Task("Develop Level 1", "Create the first level of the game.", "In Progress", "Bob", "2023-12-15")
        
        project.add_task(task1)
        project.add_task(task2)

        # Update a task
        project.update_task("Design Game Mechanics", status="In Progress")

        # Save project to file
        project.save_to_file("project_tasks.json")

        # Load project from file
        new_project = Project("New Game Project")
        new_project.load_from_file("project_tasks.json")
        
        print(f"Loaded tasks: {[task.title for task in new_project.tasks]}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
