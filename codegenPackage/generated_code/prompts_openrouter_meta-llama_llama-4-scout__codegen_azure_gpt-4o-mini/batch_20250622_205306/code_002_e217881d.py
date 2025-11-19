"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write a Python code snippet to manage and track industrial projects, including designing and manufacturing machinery, similar to Multiservicios 3L's services.
Generated: DETERMINISTIC_e217881d103a2cb7
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

class Project:
    """Class to represent an industrial project."""
    
    def __init__(self, name: str, description: str, start_date: str, end_date: str):
        self.name = name
        self.description = description
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = 'Pending'  # Initial status of the project
        self.tasks: List[Dict] = []  # List to hold tasks related to the project

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name: str, assigned_to: str, due_date: str):
        """Add a task to the project."""
        task = {
            'name': task_name,
            'assigned_to': assigned_to,
            'due_date': self._parse_date(due_date),
            'completed': False
        }
        self.tasks.append(task)

    def complete_task(self, task_name: str):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                return
        raise ValueError(f"Task '{task_name}' not found in project '{self.name}'.")

    def get_status(self) -> str:
        """Get the current status of the project."""
        return self.status

    def update_status(self, new_status: str):
        """Update the status of the project."""
        self.status = new_status

    def to_dict(self) -> Dict:
        """Convert project details to a dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'status': self.status,
            'tasks': self.tasks
        }

class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)

    def find_project(self, project_name: str) -> Optional[Project]:
        """Find a project by name."""
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def save_projects(self, filename: str):
        """Save all projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving projects to {filename}: {e}")

    def load_projects(self, filename: str):
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(
                        name=project_data['name'],
                        description=project_data['description'],
                        start_date=project_data['start_date'],
                        end_date=project_data['end_date']
                    )
                    project.status = project_data['status']
                    project.tasks = project_data['tasks']
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading projects from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    project1 = Project("Machinery Design", "Designing new industrial machinery", "2023-10-01", "2024-01-01")
    project1.add_task("Initial Design", "Alice", "2023-10-15")
    project1.add_task("Prototype Development", "Bob", "2023-11-30")
    
    # Add project to manager
    manager.add_project(project1)
    
    # Save projects to a file
    manager.save_projects("projects.json")
    
    # Load projects from a file
    manager.load_projects("projects.json")
    
    # Complete a task
    project1.complete_task("Initial Design")
    
    # Print project status
    print(project1.to_dict())
```
