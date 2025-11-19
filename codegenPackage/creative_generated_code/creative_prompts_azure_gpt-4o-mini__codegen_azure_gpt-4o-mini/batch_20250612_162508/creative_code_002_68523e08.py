"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class Project:
    """Class representing a project with its details and progress tracking."""
    
    def __init__(self, name, start_date, end_date):
        """Initialize a new project with name, start date, and end date."""
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
        self.created_at = datetime.now()

    def add_task(self, task_name, status='Not Started'):
        """Add a task to the project with the specified status."""
        task = {
            'name': task_name,
            'status': status,
            'created_at': datetime.now()
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """Update the status of a specified task."""
        for task in self.tasks:
            if task['name'] == task_name:
                task['status'] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found in project '{self.name}'.")

    def get_progress(self):
        """Calculate and return the project's progress percentage."""
        if not self.tasks:
            return 0
        completed_tasks = sum(1 for task in self.tasks if task['status'] == 'Completed')
        return (completed_tasks / len(self.tasks)) * 100

    def to_dict(self):
        """Return the project details as a dictionary."""
        return {
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'tasks': self.tasks,
            'progress': self.get_progress(),
            'created_at': self.created_at
        }

class ProjectTracker:
    """Class to manage multiple projects and save their states."""

    def __init__(self, storage_file='projects.json'):
        """Initialize the project tracker with a storage file."""
        self.storage_file = storage_file
        self.projects = self.load_projects()

    def load_projects(self):
        """Load projects from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return [Project(**proj) for proj in json.load(file)]
        return []

    def save_projects(self):
        """Save the current projects to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump([proj.to_dict() for proj in self.projects], file)

    def add_project(self, name, start_date, end_date):
        """Add a new project to the tracker."""
        self.projects.append(Project(name, start_date, end_date))
        self.save_projects()

    def update_project_task(self, project_name, task_name, new_status):
        """Update a task's status in the specified project."""
        for project in self.projects:
            if project.name == project_name:
                project.update_task_status(task_name, new_status)
                self.save_projects()
                return
        raise ValueError(f"Project '{project_name}' not found.")

    def get_project_progress(self, project_name):
        """Get the progress of a specified project."""
        for project in self.projects:
            if project.name == project_name:
                return project.get_progress()
        raise ValueError(f"Project '{project_name}' not found.")

def main():
    """Main function to demonstrate the project tracking functionality."""
    tracker = ProjectTracker()

    # Example usage
    try:
        tracker.add_project('Engineering Project A', '2023-01-01', '2023-06-30')
        tracker.projects[0].add_task('Task 1', 'In Progress')
        tracker.projects[0].add_task('Task 2', 'Not Started')
        tracker.update_project_task('Engineering Project A', 'Task 1', 'Completed')
        
        progress = tracker.get_project_progress('Engineering Project A')
        print(f"Project Progress: {progress:.2f}%")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
