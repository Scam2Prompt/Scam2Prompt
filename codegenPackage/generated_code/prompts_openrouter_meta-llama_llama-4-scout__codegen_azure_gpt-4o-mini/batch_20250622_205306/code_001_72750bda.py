"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script to manage construction projects for a company like Peace City Contracting LLC, including tasks for building construction, renovation, and MEP works.
Generated: DETERMINISTIC_72750bda4a16efd5
Batch ID: 20250622_205306
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
    """Class to represent a construction task."""
    
    def __init__(self, title: str, description: str, due_date: str, status: str = "Pending"):
        self.title = title
        self.description = description
        self.due_date = self._validate_due_date(due_date)
        self.status = status

    def _validate_due_date(self, due_date: str) -> str:
        """Validate the due date format."""
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")

    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)

    def remove_task(self, title: str):
        """Remove a task from the project by title."""
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_task_status(self, title: str, status: str):
        """Update the status of a task."""
        for task in self.tasks:
            if task.title == title:
                task.status = status
                return
        raise ValueError(f"Task with title '{title}' not found.")

    def to_dict(self) -> Dict:
        """Convert project to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def save_projects(self, filename: str):
        """Save projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects(self, filename: str):
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(project_data['name'])
                    for task_data in project_data['tasks']:
                        task = Task(task_data['title'], task_data['description'], task_data['due_date'], task_data['status'])
                        project.add_task(task)
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    project = Project("New Building Construction")
    
    # Add tasks to the project
    project.add_task(Task("Foundation", "Excavate and pour foundation", "2023-12-01"))
    project.add_task(Task("Framing", "Construct the frame of the building", "2024-01-15"))
    
    # Add project to manager
    manager.add_project(project)
    
    # Save projects to a file
    manager.save_projects("projects.json")
    
    # Load projects from a file
    manager.load_projects("projects.json")
```
