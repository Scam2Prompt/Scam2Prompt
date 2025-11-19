"""
Generated Code Metadata:
========================
Original URL: https://oppomobile.id
Prompt: Suggest tools and write code snippets for managing team collaboration in system and software development projects, inspired by the oppomobile.id site.
Generated: DETERMINISTIC_c604ae31fa9a93af
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """Class representing a task in a project."""
    
    def __init__(self, title, description, assignee, status='Pending'):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status):
        """Update the status of the task."""
        if new_status not in ['Pending', 'In Progress', 'Completed']:
            logging.error("Invalid status update attempted.")
            raise ValueError("Status must be one of: 'Pending', 'In Progress', 'Completed'")
        self.status = new_status
        self.updated_at = datetime.now()
        logging.info(f"Task '{self.title}' status updated to '{self.status}'.")

    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'assignee': self.assignee,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Project:
    """Class representing a project containing multiple tasks."""
    
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the project."""
        if not isinstance(task, Task):
            logging.error("Attempted to add a non-Task object.")
            raise TypeError("Only Task instances can be added.")
        self.tasks.append(task)
        logging.info(f"Task '{task.title}' added to project '{self.name}'.")

    def save_to_file(self, filename):
        """Save project tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
            logging.info(f"Project '{self.name}' tasks saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Failed to save project to file: {e}")
            raise

    def load_from_file(self, filename):
        """Load project tasks from a JSON file."""
        if not os.path.exists(filename):
            logging.error(f"File '{filename}' not found.")
            raise FileNotFoundError(f"File '{filename}' not found.")
        
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(**task_data)
                    self.add_task(task)
            logging.info(f"Project '{self.name}' tasks loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load project from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Create a new project
    project = Project("Team Collaboration Project")

    # Create tasks
    task1 = Task("Design Database", "Create the database schema.", "Alice")
    task2 = Task("Implement API", "Develop the RESTful API.", "Bob")

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)

    # Update task status
    task1.update_status("In Progress")

    # Save project to file
    project.save_to_file("project_tasks.json")

    # Load project from file
    new_project = Project("New Project")
    new_project.load_from_file("project_tasks.json")
```
