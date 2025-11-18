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
from datetime import datetime

class Task:
    """
    Represents a project task.
    """
    def __init__(self, task_id, name, description, assignee, due_date, status="Pending"):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the task.
        """
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {valid_statuses}")

    def serialize(self):
        """
        Serialize task data for storage or transfer.
        """
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "assignee": self.assignee,
            "due_date": self.due_date.strftime('%Y-%m-%d'),
            "status": self.status
        }


class Project:
    """
    Represents a project in the architecture-focused app.
    """
    def __init__(self, project_id, name, description, start_date=None):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date or datetime.now()
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task instance.")
        self.tasks.append(task)

    def remove_task(self, task_id):
        """
        Remove a task by its ID.
        """
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_tasks(self, status=None):
        """
        Get all tasks, optionally filtered by status.
        """
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

    def serialize(self):
        """
        Serialize project data for storage or transfer.
        """
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "tasks": [task.serialize() for task in self.tasks]
        }


class ArchitectureApp:
    """
    The main application for managing architecture-focused projects.
    """
    def __init__(self):
        self.projects = {}

    def create_project(self, project_id, name, description):
        """
        Create a new project.
        """
        if project_id in self.projects:
            raise ValueError(f"Project with ID '{project_id}' already exists.")
        self.projects[project_id] = Project(project_id, name, description)

    def delete_project(self, project_id):
        """
        Delete a project by its ID.
        """
        if project_id in self.projects:
            del self.projects[project_id]
        else:
            raise KeyError(f"Project with ID '{project_id}' does not exist.")

    def get_project(self, project_id):
        """
        Retrieve a project by its ID.
        """
        if project_id in self.projects:
            return self.projects[project_id]
        else:
            raise KeyError(f"Project with ID '{project_id}' does not exist.")

    def save_data(self, file_path):
        """
        Save all project data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                data = {project_id: project.serialize() for project_id, project in self.projects.items()}
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    def load_data(self, file_path):
        """
        Load project data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.projects = {}
                for project_id, project_data in data.items():
                    project = Project(
                        project_id=project_data['project_id'],
                        name=project_data['name'],
                        description=project_data['description'],
                        start_date=datetime.strptime(project_data['start_date'], '%Y-%m-%d')
                    )
                    for task_data in project_data['tasks']:
                        task = Task(
                            task_id=task_data['task_id'],
                            name=task_data['name'],
                            description=task_data['description'],
                            assignee=task_data['assignee'],
                            due_date=datetime.strptime(task_data['due_date'], '%Y-%m-%d'),
                            status=task_data['status']
                        )
                        project.add_task(task)
                    self.projects[project_id] = project
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading data from file: {e}")


# Example usage:
if __name__ == "__main__":
    app = ArchitectureApp()
    app.create_project("001", "Building Renovation", "Renovation of historical building.")
    project = app.get_project("001")
    new_task = Task(task_id="101", name="Draft Design", description="Create initial design drafts.", assignee="Alice", due_date=datetime(2023, 11, 15))
    project.add_task(new_task)
    app.save_data("projects.json")
    app.load_data("projects.json")
```
