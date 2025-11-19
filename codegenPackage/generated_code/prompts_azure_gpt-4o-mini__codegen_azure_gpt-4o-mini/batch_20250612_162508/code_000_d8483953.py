"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate a code snippet for a project management tool that can handle multiple architectural projects simultaneously, similar to the capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_d8483953b0efdfb0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class Project:
    """Class representing a project in the project management tool."""
    
    def __init__(self, name: str, description: str, deadline: datetime):
        """Initialize a new project with a unique ID, name, description, and deadline."""
        self.id = uuid.uuid4()  # Unique identifier for the project
        self.name = name
        self.description = description
        self.deadline = deadline
        self.tasks: List['Task'] = []  # List to hold tasks associated with the project

    def add_task(self, task: 'Task'):
        """Add a task to the project."""
        self.tasks.append(task)

    def __str__(self):
        """String representation of the project."""
        return f"Project({self.name}, Deadline: {self.deadline})"


class Task:
    """Class representing a task within a project."""
    
    def __init__(self, name: str, assigned_to: str, status: str = "Pending"):
        """Initialize a new task with a name, assignee, and status."""
        self.id = uuid.uuid4()  # Unique identifier for the task
        self.name = name
        self.assigned_to = assigned_to
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the task."""
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """String representation of the task."""
        return f"Task({self.name}, Assigned to: {self.assigned_to}, Status: {self.status})"


class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        """Initialize the project manager with an empty project list."""
        self.projects: List[Project] = []

    def create_project(self, name: str, description: str, deadline: datetime) -> Project:
        """Create a new project and add it to the project manager."""
        project = Project(name, description, deadline)
        self.projects.append(project)
        return project

    def get_project(self, project_id: uuid.UUID) -> Optional[Project]:
        """Retrieve a project by its unique ID."""
        for project in self.projects:
            if project.id == project_id:
                return project
        return None  # Return None if project not found

    def list_projects(self) -> List[Project]:
        """List all projects managed by the project manager."""
        return self.projects

    def __str__(self):
        """String representation of the project manager."""
        return f"ProjectManager(Projects: {len(self.projects)})"


# Example usage
if __name__ == "__main__":
    try:
        manager = ProjectManager()
        project1 = manager.create_project("Building A", "Construction of Building A", datetime(2024, 12, 31))
        task1 = Task("Foundation", "Alice")
        project1.add_task(task1)
        
        print(project1)
        print(task1)
        
        task1.update_status("In Progress")
        print(task1)
        
        # List all projects
        for project in manager.list_projects():
            print(project)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
