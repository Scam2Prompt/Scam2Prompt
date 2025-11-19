"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a project management workflow in Python for civil engineering tasks, including structural repairs, waterproofing, and painting, inspired by SOM Civil Engineers' project management approach.
Generated: DETERMINISTIC_17feb92a70f58f09
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class Task:
    """Class representing a task in the project management workflow."""
    
    def __init__(self, name: str, description: str, due_date: datetime.date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.date.today()

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __repr__(self) -> str:
        return f"Task(name={self.name}, due_date={self.due_date}, completed={self.completed})"


class Project:
    """Class representing a project containing multiple tasks."""
    
    def __init__(self, title: str):
        self.title = title
        self.tasks: List[Task] = []
        self.created_at = datetime.date.today()

    def add_task(self, task: Task):
        """Add a new task to the project."""
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """Return a list of pending tasks."""
        return [task for task in self.tasks if not task.completed]

    def __repr__(self) -> str:
        return f"Project(title={self.title}, tasks={self.tasks})"


class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(self, title: str) -> Project:
        """Create a new project."""
        if title in self.projects:
            raise ValueError(f"Project '{title}' already exists.")
        project = Project(title)
        self.projects[title] = project
        return project

    def get_project(self, title: str) -> Project:
        """Retrieve a project by title."""
        if title not in self.projects:
            raise KeyError(f"Project '{title}' not found.")
        return self.projects[title]

    def list_projects(self) -> List[str]:
        """List all project titles."""
        return list(self.projects.keys())

    def __repr__(self) -> str:
        return f"ProjectManager(projects={self.projects.keys()})"


# Example usage
if __name__ == "__main__":
    try:
        manager = ProjectManager()

        # Create a new project for civil engineering tasks
        civil_project = manager.create_project("Civil Engineering Tasks")

        # Add tasks to the project
        civil_project.add_task(Task("Structural Repairs", "Repair the structural integrity of the building.", datetime.date(2023, 12, 1)))
        civil_project.add_task(Task("Waterproofing", "Apply waterproofing to the basement.", datetime.date(2023, 11, 15)))
        civil_project.add_task(Task("Painting", "Paint the exterior of the building.", datetime.date(2023, 10, 30)))

        # List all projects
        print("Projects:", manager.list_projects())

        # List pending tasks for the civil project
        print("Pending Tasks:", civil_project.get_pending_tasks())

        # Mark a task as completed
        civil_project.tasks[0].mark_completed()
        print("Updated Pending Tasks:", civil_project.get_pending_tasks())

    except Exception as e:
        print(f"An error occurred: {e}")
```
