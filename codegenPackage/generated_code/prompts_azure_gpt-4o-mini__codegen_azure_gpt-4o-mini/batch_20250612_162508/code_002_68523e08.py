"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class Project:
    """Class to represent a project with its details and progress tracking."""
    
    def __init__(self, name, start_date, end_date):
        """
        Initialize a new project.

        :param name: Name of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks = []
        self.progress = 0.0

    def add_task(self, task_name, estimated_hours):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param estimated_hours: Estimated hours to complete the task
        """
        task = Task(task_name, estimated_hours)
        self.tasks.append(task)

    def update_progress(self):
        """Update the overall project progress based on task completion."""
        if not self.tasks:
            self.progress = 0.0
            return
        
        completed_hours = sum(task.completed_hours for task in self.tasks)
        total_hours = sum(task.estimated_hours for task in self.tasks)
        self.progress = (completed_hours / total_hours) * 100 if total_hours > 0 else 0.0

    def to_dict(self):
        """Convert project details to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "progress": self.progress,
            "tasks": [task.to_dict() for task in self.tasks]
        }

class Task:
    """Class to represent a task within a project."""
    
    def __init__(self, name, estimated_hours):
        """
        Initialize a new task.

        :param name: Name of the task
        :param estimated_hours: Estimated hours to complete the task
        """
        self.name = name
        self.estimated_hours = estimated_hours
        self.completed_hours = 0.0

    def complete_task(self, hours):
        """
        Mark hours as completed for the task.

        :param hours: Hours to mark as completed
        """
        if hours < 0:
            raise ValueError("Completed hours cannot be negative.")
        if self.completed_hours + hours > self.estimated_hours:
            raise ValueError("Cannot complete more hours than estimated.")
        
        self.completed_hours += hours

    def to_dict(self):
        """Convert task details to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "estimated_hours": self.estimated_hours,
            "completed_hours": self.completed_hours
        }

class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self, filename='projects.json'):
        """
        Initialize the project manager.

        :param filename: File to save/load project data
        """
        self.projects = []
        self.filename = filename
        self.load_projects()

    def add_project(self, project):
        """Add a new project to the manager."""
        self.projects.append(project)
        self.save_projects()

    def save_projects(self):
        """Save all projects to a JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([project.to_dict() for project in self.projects], f, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")

    def load_projects(self):
        """Load projects from a JSON file."""
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r') as f:
                projects_data = json.load(f)
                for project_data in projects_data:
                    project = Project(project_data['name'], project_data['start_date'], project_data['end_date'])
                    for task_data in project_data['tasks']:
                        task = Task(task_data['name'], task_data['estimated_hours'])
                        task.completed_hours = task_data['completed_hours']
                        project.tasks.append(task)
                    project.update_progress()
                    self.projects.append(project)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects: {e}")

    def display_projects(self):
        """Display all projects and their progress."""
        for project in self.projects:
            print(f"Project: {project.name}, Progress: {project.progress:.2f}%")

if __name__ == "__main__":
    # Example usage
    manager = ProjectManager()
    
    # Create a new project
    project1 = Project("Engineering Project A", "2023-01-01", "2023-12-31")
    project1.add_task("Design Phase", 100)
    project1.add_task("Implementation Phase", 200)
    
    # Mark some tasks as completed
    project1.tasks[0].complete_task(50)
    project1.tasks[1].complete_task(100)
    
    # Update project progress
    project1.update_progress()
    
    # Add project to manager
    manager.add_project(project1)
    
    # Display all projects
    manager.display_projects()
```
