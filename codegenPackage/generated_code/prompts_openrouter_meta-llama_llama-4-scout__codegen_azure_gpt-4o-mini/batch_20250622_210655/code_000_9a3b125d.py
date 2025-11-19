"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Write a Python script to manage construction projects for a company like URANPRES, s.r.o. that handles underground construction, including tunnel boring projects like the Ovčiarsko tunnel."
Generated: DETERMINISTIC_9a3b125d373e8efc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, name: str, start_date: str, end_date: str, budget: float):
        """
        Initialize a new construction project.

        :param name: Name of the project
        :param start_date: Start date of the project in 'YYYY-MM-DD' format
        :param end_date: End date of the project in 'YYYY-MM-DD' format
        :param budget: Budget allocated for the project
        """
        self.name = name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.budget = budget
        self.tasks: List[Dict[str, Any]] = []

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            logging.error(f"Date parsing error: {e}")
            raise

    def add_task(self, task_name: str, assigned_to: str, due_date: str):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date of the task in 'YYYY-MM-DD' format
        """
        due_date_parsed = self._parse_date(due_date)
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date_parsed,
            'completed': False
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.name}'.")

    def complete_task(self, task_name: str):
        """
        Mark a task as completed.

        :param task_name: Name of the task to complete
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['completed'] = True
                logging.info(f"Task '{task_name}' marked as completed in project '{self.name}'.")
                return
        logging.warning(f"Task '{task_name}' not found in project '{self.name}'.")

    def to_dict(self) -> Dict[str, Any]:
        """Convert project details to a dictionary."""
        return {
            'name': self.name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'budget': self.budget,
            'tasks': self.tasks
        }

class ProjectManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        """Initialize the project manager with an empty project list."""
        self.projects: List[Project] = []

    def add_project(self, project: Project):
        """Add a new project to the manager."""
        self.projects.append(project)
        logging.info(f"Project '{project.name}' added.")

    def save_projects(self, filename: str):
        """
        Save all projects to a JSON file.

        :param filename: Name of the file to save projects
        """
        try:
            with open(filename, 'w') as f:
                json.dump([project.to_dict() for project in self.projects], f, indent=4)
            logging.info(f"Projects saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Error saving projects to file: {e}")

    def load_projects(self, filename: str):
        """
        Load projects from a JSON file.

        :param filename: Name of the file to load projects from
        """
        try:
            with open(filename, 'r') as f:
                projects_data = json.load(f)
                for project_data in projects_data:
                    project = Project(
                        name=project_data['name'],
                        start_date=project_data['start_date'],
                        end_date=project_data['end_date'],
                        budget=project_data['budget']
                    )
                    for task in project_data['tasks']:
                        project.add_task(task['task_name'], task['assigned_to'], task['due_date'])
                    self.add_project(project)
            logging.info(f"Projects loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading projects from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    project = Project(name="Ovčiarsko Tunnel", start_date="2023-01-01", end_date="2024-12-31", budget=5000000.0)
    project.add_task("Excavation", "John Doe", "2023-06-01")
    project.add_task("Tunnel Boring", "Jane Smith", "2024-06-01")
    
    # Add project to manager
    manager.add_project(project)
    
    # Save projects to a file
    manager.save_projects("projects.json")
    
    # Load projects from a file
    manager.load_projects("projects.json")
```
