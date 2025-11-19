"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Generate a code snippet for a project management tool that can handle multiple architectural projects simultaneously, similar to the capabilities of Remas Engineering Consultants.
Generated: DETERMINISTIC_d8483953b0efdfb0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management_tool.py

import uuid
from typing import List, Optional

class Project:
    """
    Represents a single architectural project.
    """
    def __init__(self, name: str, description: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the project
        self.name = name              # Name of the project
        self.description = description  # Description of the project
        self.tasks = []               # List to hold tasks related to the project

    def add_task(self, task: 'Task'):
        """
        Adds a task to the project.
        """
        self.tasks.append(task)

    def __repr__(self):
        return f"Project(id={self.id}, name={self.name})"


class Task:
    """
    Represents a single task within a project.
    """
    def __init__(self, title: str, status: str = "Not Started"):
        self.id = str(uuid.uuid4())  # Unique identifier for the task
        self.title = title            # Title of the task
        self.status = status          # Status of the task (e.g., Not Started, In Progress, Completed)

    def update_status(self, new_status: str):
        """
        Updates the status of the task.
        """
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status})"


class ProjectManager:
    """
    Manages multiple architectural projects.
    """
    def __init__(self):
        self.projects: List[Project] = []  # List to hold all projects

    def create_project(self, name: str, description: str) -> Project:
        """
        Creates a new project and adds it to the project manager.
        """
        new_project = Project(name, description)
        self.projects.append(new_project)
        return new_project

    def find_project(self, project_id: str) -> Optional[Project]:
        """
        Finds a project by its ID.
        """
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

    def list_projects(self) -> List[Project]:
        """
        Returns a list of all projects.
        """
        return self.projects

    def __repr__(self):
        return f"ProjectManager(projects={self.projects})"


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Creating a new project
    project1 = manager.create_project("Skyline Tower", "High-rise building in downtown.")
    print(f"Created Project: {project1}")

    # Adding tasks to the project
    task1 = Task("Design Phase")
    project1.add_task(task1)
    print(f"Added Task: {task1} to Project: {project1}")

    # Updating task status
    task1.update_status("In Progress")
    print(f"Updated Task Status: {task1}")

    # Listing all projects
    all_projects = manager.list_projects()
    print(f"All Projects: {all_projects}")
```
