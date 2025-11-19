"""
Generated Code Metadata:
========================
Original URL: https://braavos.rs
Prompt: Write a Python script to create a simple project management tool for architectural firms like Études, including features for task assignment and resource allocation.
Generated: DETERMINISTIC_7ced2f7da4eabe7e
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Task:
    """Class representing a task in the project management tool."""
    
    def __init__(self, title: str, description: str, assigned_to: Optional[str] = None):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to

    def assign(self, user: str):
        """Assign a user to the task."""
        self.assigned_to = user

    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'assigned_to': self.assigned_to
        }

class Project:
    """Class representing a project with tasks."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Dict]:
        """Get a list of tasks in the project."""
        return [task.to_dict() for task in self.tasks]

    def to_dict(self) -> Dict:
        """Convert the project to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'tasks': self.get_tasks()
        }

class ProjectManager:
    """Class to manage multiple projects."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(self, name: str):
        """Create a new project."""
        if name in self.projects:
            raise ValueError(f"Project '{name}' already exists.")
        self.projects[name] = Project(name)

    def add_task_to_project(self, project_name: str, task: Task):
        """Add a task to a specified project."""
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' does not exist.")
        self.projects[project_name].add_task(task)

    def save_projects(self, filename: str):
        """Save all projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({name: project.to_dict() for name, project in self.projects.items()}, file, indent=4)
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects(self, filename: str):
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, project_data in data.items():
                    project = Project(name)
                    for task_data in project_data['tasks']:
                        task = Task(task_data['title'], task_data['description'], task_data['assigned_to'])
                        project.add_task(task)
                    self.projects[name] = project
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    manager.create_project("Architectural Design")
    
    # Add tasks to the project
    task1 = Task("Initial Sketch", "Create initial sketches for the project.")
    task2 = Task("Client Meeting", "Schedule a meeting with the client.")
    
    manager.add_task_to_project("Architectural Design", task1)
    manager.add_task_to_project("Architectural Design", task2)
    
    # Assign a user to a task
    task1.assign("Alice")
    
    # Save projects to a file
    manager.save_projects("projects.json")
    
    # Load projects from a file
    manager.load_projects("projects.json")
    
    # Print loaded projects
    for project_name, project in manager.projects.items():
        print(f"Project: {project_name}")
        for task in project.get_tasks():
            print(f"  Task: {task['title']}, Assigned to: {task['assigned_to']}")
```
