"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Write Python code to simulate a project management system for housing developments and retirement living, incorporating health and safety guidelines as outlined by Westpoint Construction.
Generated: DETERMINISTIC_d79ce1087e45216f
Batch ID: 20250612_152410
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

class Project:
    """
    Represents a housing development or retirement living project.
    """

    def __init__(self, name: str, start_date: str, end_date: str):
        """
        Initializes a new project.

        Args:
            name (str): The name of the project.
            start_date (str): The start date of the project in YYYY-MM-DD format.
            end_date (str): The end date of the project in YYYY-MM-DD format.
        """
        self.name = name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.tasks: List[Task] = []
        self.health_and_safety_guidelines: List[str] = []

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        Args:
            date_str (str): The date string to parse.

        Returns:
            datetime: The parsed datetime object.
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Incorrect date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task: 'Task'):
        """
        Adds a task to the project.

        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

    def add_health_and_safety_guideline(self, guideline: str):
        """
        Adds a health and safety guideline to the project.

        Args:
            guideline (str): The health and safety guideline to add.
        """
        self.health_and_safety_guidelines.append(guideline)

    def to_dict(self) -> Dict:
        """
        Converts the project instance to a dictionary.

        Returns:
            Dict: The dictionary representation of the project.
        """
        return {
            'name': self.name,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d"),
            'tasks': [task.to_dict() for task in self.tasks],
            'health_and_safety_guidelines': self.health_and_safety_guidelines
        }


class Task:
    """
    Represents a task within a project.
    """

    def __init__(self, description: str, assigned_to: str, due_date: str):
        """
        Initializes a new task.

        Args:
            description (str): The description of the task.
            assigned_to (str): The name of the person assigned to the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
        """
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = Project._parse_date(due_date)

    def to_dict(self) -> Dict:
        """
        Converts the task instance to a dictionary.

        Returns:
            Dict: The dictionary representation of the task.
        """
        return {
            'description': self.description,
            'assigned_to': self.assigned_to,
            'due_date': self.due_date.strftime("%Y-%m-%d")
        }


class ProjectManagementSystem:
    """
    A simple project management system for managing housing developments.
    """

    def __init__(self):
        """Initializes the project management system with an empty project list."""
        self.projects: List[Project] = []

    def create_project(self, name: str, start_date: str, end_date: str) -> Project:
        """
        Creates a new project.

        Args:
            name (str): The name of the project.
            start_date (str): The start date of the project.
            end_date (str): The end date of the project.

        Returns:
            Project: The newly created project.
        """
        new_project = Project(name, start_date, end_date)
        self.projects.append(new_project)
        return new_project

    def save_projects_to_file(self, filename: str):
        """
        Saves all projects to a JSON file.

        Args:
            filename (str): The name of the file to save the projects to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects_from_file(self, filename: str):
        """
        Loads projects from a JSON file.

        Args:
            filename (str): The name of the file to load projects from.
        """
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = self.create_project(
                        project_data['name'], 
                        project_data['start_date'], 
                        project_data['end_date']
                    )
                    for task_data in project_data['tasks']:
                        task = Task(
                            task_data['description'],
                            task_data['assigned_to'],
                            task_data['due_date']
                        )
                        project.add_task(task)
                    project.health_and_safety_guidelines = project_data['health_and_safety_guidelines']
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")


if __name__ == "__main__":
    # Example usage of the Project Management System
    pms = ProjectManagementSystem()
    
    # Create a new project
    project = pms.create_project("Westpoint Retirement Community", "2023-01-01", "2024-01-01")
    
    # Add tasks to the project
    project.add_task(Task("Prepare site for construction", "Alice", "2023-02-01"))
    project.add_task(Task("Lay foundation", "Bob", "2023-03-15"))
    
    # Add health and safety guidelines
    project.add_health_and_safety_guideline("Ensure all workers wear helmets on site.")
    project.add_health_and_safety_guideline("Conduct daily safety briefings.")
    
    # Save projects to a file
    pms.save_projects_to_file("projects.json")

    # Load projects from a file
    pms.load_projects_from_file("projects.json")
```
