"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Write a Python script to manage a civil engineering project, including tasks such as structural audit, waterproofing, and building construction, for a company like SOM Civil Engineers."
Generated: DETERMINISTIC_7906d8f8b9809c3a
Batch ID: 20250622_204915
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

class Task:
    """Class representing a task in the civil engineering project."""
    
    def __init__(self, name: str, description: str, due_date: str):
        self.name = name
        self.description = description
        self.due_date = self._parse_due_date(due_date)
        self.completed = False

    def _parse_due_date(self, due_date: str) -> datetime:
        """Parse the due date string into a datetime object."""
        try:
            return datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {due_date}. Expected format: YYYY-MM-DD") from e

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert the task to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "completed": self.completed
        }

class Project:
    """Class representing a civil engineering project."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a new task to the project."""
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Retrieve a list of pending tasks."""
        return [task for task in self.tasks if not task.completed]

    def save_to_file(self, filename: str):
        """Save the project data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "project_name": self.project_name,
                    "tasks": [task.to_dict() for task in self.tasks]
                }, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving project to file: {filename}") from e

    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load project data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                project = cls(data["project_name"])
                for task_data in data["tasks"]:
                    task = Task(task_data["name"], task_data["description"], task_data["due_date"])
                    if task_data["completed"]:
                        task.mark_completed()
                    project.add_task(task)
                return project
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading project from file: {filename}") from e

def main():
    """Main function to manage the civil engineering project."""
    project = Project("SOM Civil Engineers Project")

    # Adding tasks to the project
    project.add_task(Task("Structural Audit", "Conduct a thorough structural audit of the building.", "2023-12-01"))
    project.add_task(Task("Waterproofing", "Implement waterproofing measures for the basement.", "2024-01-15"))
    project.add_task(Task("Building Construction", "Start the construction of the main building.", "2024-03-01"))

    # Save the project to a file
    project.save_to_file("project_data.json")

    # Load the project from a file
    loaded_project = Project.load_from_file("project_data.json")
    print(f"Loaded project: {loaded_project.project_name}")
    for task in loaded_project.get_pending_tasks():
        print(f"Pending Task: {task.name} - Due: {task.due_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
```
