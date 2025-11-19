"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Develop a plan for implementing a project management system for a civil engineering company like SOM Civil Engineers, including features like task assignment, progress tracking, and team collaboration."
Generated: DETERMINISTIC_545925434b424a13
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

"""
Project Management System for a Civil Engineering Company
This system allows for task assignment, progress tracking, and team collaboration.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Task:
    """Class representing a task in the project management system."""
    
    def __init__(self, title: str, description: str, assigned_to: str, due_date: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the task
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date  # Expected format: 'YYYY-MM-DD'
        self.status = 'Pending'  # Initial status of the task
        self.created_at = datetime.now()

    def update_status(self, new_status: str):
        """Update the status of the task."""
        valid_statuses = ['Pending', 'In Progress', 'Completed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

class Project:
    """Class representing a project in the project management system."""
    
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the project
        self.name = name
        self.tasks: List[Task] = []  # List to hold tasks associated with the project

    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)

    def get_progress(self) -> Dict[str, int]:
        """Calculate the progress of the project based on task statuses."""
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return {'total': 0, 'completed': 0, 'progress_percentage': 0}

        completed_tasks = sum(1 for task in self.tasks if task.status == 'Completed')
        progress_percentage = (completed_tasks / total_tasks) * 100
        return {
            'total': total_tasks,
            'completed': completed_tasks,
            'progress_percentage': progress_percentage
        }

class ProjectManagementSystem:
    """Main class for managing projects and tasks."""
    
    def __init__(self):
        self.projects: List[Project] = []  # List to hold all projects

    def create_project(self, name: str) -> Project:
        """Create a new project."""
        project = Project(name)
        self.projects.append(project)
        return project

    def find_project(self, project_id: str) -> Optional[Project]:
        """Find a project by its ID."""
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

    def assign_task(self, project_id: str, title: str, description: str, assigned_to: str, due_date: str) -> Optional[Task]:
        """Assign a task to a project."""
        project = self.find_project(project_id)
        if project:
            task = Task(title, description, assigned_to, due_date)
            project.add_task(task)
            return task
        else:
            raise ValueError(f"Project with ID {project_id} not found.")

# Example usage
if __name__ == "__main__":
    try:
        pms = ProjectManagementSystem()
        project = pms.create_project("Bridge Construction")
        task1 = pms.assign_task(project.id, "Design Phase", "Complete the design of the bridge", "Alice", "2023-12-01")
        task2 = pms.assign_task(project.id, "Material Procurement", "Procure materials for construction", "Bob", "2023-11-15")

        # Update task status
        task1.update_status("Completed")

        # Get project progress
        progress = project.get_progress()
        print(f"Project Progress: {progress['completed']} out of {progress['total']} tasks completed ({progress['progress_percentage']:.2f}%)")
    except Exception as e:
        print(f"An error occurred: {e}")
```
