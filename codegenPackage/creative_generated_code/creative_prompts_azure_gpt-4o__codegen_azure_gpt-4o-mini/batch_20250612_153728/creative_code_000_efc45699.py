"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Write Python code to integrate project management features into an architecture-focused app, inspired by the Études Architect App described on Celestia's website.
Generated: DETERMINISTIC_efc456991776ae34
Batch ID: 20250612_153728
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
from typing import List, Dict, Optional

class Project:
    """
    A class to represent a project within the architecture-focused app.
    """
    
    def __init__(self, title: str, description: str):
        """
        Initializes a new project with a title and description.
        
        :param title: Title of the project
        :param description: Description of the project
        """
        self.title = title
        self.description = description
        self.tasks = []
    
    def add_task(self, task: 'Task'):
        """
        Adds a task to the project.
        
        :param task: Task object to be added
        """
        self.tasks.append(task)
    
    def to_dict(self) -> Dict:
        """
        Converts the project to a dictionary format for easy serialization.
        
        :return: Dictionary representation of the project
        """
        return {
            'title': self.title,
            'description': self.description,
            'tasks': [task.to_dict() for task in self.tasks]
        }


class Task:
    """
    A class to represent a task within a project.
    """
    
    def __init__(self, name: str, completed: bool = False):
        """
        Initializes a new task with a name and completion status.
        
        :param name: Name of the task
        :param completed: Completion status of the task
        """
        self.name = name
        self.completed = completed
    
    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self.completed = True
    
    def to_dict(self) -> Dict:
        """
        Converts the task to a dictionary format for easy serialization.
        
        :return: Dictionary representation of the task
        """
        return {
            'name': self.name,
            'completed': self.completed
        }


class ProjectManager:
    """
    A class to manage projects and their tasks, including storage functionality.
    """
    
    def __init__(self, storage_file: str):
        """
        Initializes the ProjectManager with a path to the storage file.
        
        :param storage_file: Path to the JSON file for project storage
        """
        self.storage_file = storage_file
        self.projects: List[Project] = []
        self.load_projects()
    
    def load_projects(self):
        """
        Loads projects from the storage file if it exists.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    project_data = json.load(file)
                    for proj in project_data:
                        project = Project(proj['title'], proj['description'])
                        for task_data in proj['tasks']:
                            task = Task(task_data['name'], task_data['completed'])
                            project.add_task(task)
                        self.projects.append(project)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading projects: {e}")
    
    def save_projects(self):
        """
        Saves the current projects to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([proj.to_dict() for proj in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")
    
    def add_project(self, project: Project):
        """
        Adds a new project and saves it to storage.
        
        :param project: Project object to be added
        """
        self.projects.append(project)
        self.save_projects()
    
    def get_projects(self) -> List[Project]:
        """
        Returns the list of managed projects.
        
        :return: List of Project objects
        """
        return self.projects


# Example Usage
if __name__ == "__main__":
    project_manager = ProjectManager('projects.json')

    # Create a new project
    new_project = Project("Building Design", "Designing a new building.")
    new_project.add_task(Task("Create blueprint"))
    new_project.add_task(Task("Submit plans"))

    # Add project to manager
    project_manager.add_project(new_project)

    # List all projects
    for project in project_manager.get_projects():
        print(f"Project: {project.title}, Description: {project.description}")
        for task in project.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"  Task: {task.name}, Status: {status}")
```
