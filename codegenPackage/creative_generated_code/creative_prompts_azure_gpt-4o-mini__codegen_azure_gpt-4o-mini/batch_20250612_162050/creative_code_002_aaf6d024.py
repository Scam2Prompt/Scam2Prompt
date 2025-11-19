"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Write a Python script to manage and monitor a network installation project, inspired by the services provided by Ray-Z Entreprise.
Generated: DETERMINISTIC_aaf6d024af0e0e8a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkInstallationProject:
    """
    A class to manage and monitor a network installation project.
    """

    def __init__(self, project_name):
        """
        Initialize a new network installation project.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.tasks = []
        self.start_date = datetime.now()
        self.status = "Initialized"
        logging.info(f"Project '{self.project_name}' initialized.")

    def add_task(self, task_name, deadline):
        """
        Add a task to the project.

        Args:
            task_name (str): The name of the task.
            deadline (str): The deadline for the task in 'YYYY-MM-DD' format.
        """
        task = {
            'name': task_name,
            'deadline': deadline,
            'completed': False,
            'created_at': datetime.now()
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.project_name}' with a deadline of {deadline}.")

    def complete_task(self, task_name):
        """
        Mark a task as completed.

        Args:
            task_name (str): The name of the task to be marked as completed.
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                logging.info(f"Task '{task_name}' marked as completed.")
                return
        logging.error(f"Task '{task_name}' not found.")

    def get_status(self):
        """
        Get the current status of the project, including the tasks.

        Returns:
            dict: A dictionary containing the project status and tasks.
        """
        completed_tasks = sum(task['completed'] for task in self.tasks)
        total_tasks = len(self.tasks)
        self.status = "Completed" if completed_tasks == total_tasks else "In Progress"

        project_status = {
            'project_name': self.project_name,
            'start_date': self.start_date,
            'status': self.status,
            'tasks': self.tasks
        }
        logging.info(f"Status retrieved for project '{self.project_name}'.")
        return project_status

    def save_to_file(self, filename):
        """
        Save the project data to a JSON file.

        Args:
            filename (str): The name of the file to save the project data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_status(), file, default=str)
            logging.info(f"Project data saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Failed to save project data to '{filename}': {e}")

    def load_from_file(self, filename):
        """
        Load project data from a JSON file.

        Args:
            filename (str): The name of the file to load the project data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.project_name = data['project_name']
                self.start_date = datetime.fromisoformat(data['start_date'])
                self.status = data['status']
                self.tasks = data['tasks']
            logging.info(f"Project data loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load project data from '{filename}': {e}")

# Example usage:
if __name__ == "__main__":
    project = NetworkInstallationProject("Office Network Setup")
    project.add_task("Install Routers", "2023-10-10")
    project.add_task("Configure Switches", "2023-10-12")
    project.complete_task("Install Routers")
    
    status = project.get_status()
    print(json.dumps(status, indent=4))

    project.save_to_file("project_data.json")
    new_project = NetworkInstallationProject("")
    new_project.load_from_file("project_data.json")
```
