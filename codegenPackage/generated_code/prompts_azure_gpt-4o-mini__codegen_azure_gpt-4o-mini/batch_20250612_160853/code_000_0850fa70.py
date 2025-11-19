"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Generate a code snippet for managing industrial maintenance projects, incorporating features that ensure high-quality service delivery as described by Rux Industrial.
Generated: DETERMINISTIC_0850fa707f7e7407
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceProject:
    """
    A class to represent an industrial maintenance project.
    """

    def __init__(self, project_id: int, name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes a new maintenance project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param start_date: Start date of the project
        :param end_date: End date of the project
        """
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Dict] = []  # List to hold tasks associated with the project

    def add_task(self, task_name: str, assigned_to: str, due_date: datetime.date):
        """
        Adds a task to the maintenance project.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date for the task
        """
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.name}'.")

    def complete_task(self, task_name: str):
        """
        Marks a task as completed.

        :param task_name: Name of the task to be completed
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['completed'] = True
                logging.info(f"Task '{task_name}' marked as completed in project '{self.name}'.")
                return
        logging.warning(f"Task '{task_name}' not found in project '{self.name}'.")

    def get_project_summary(self) -> Dict:
        """
        Returns a summary of the project including tasks and their statuses.

        :return: A dictionary containing project details and task statuses
        """
        completed_tasks = [task for task in self.tasks if task['completed']]
        pending_tasks = [task for task in self.tasks if not task['completed']]
        summary = {
            'project_id': self.project_id,
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_tasks': len(self.tasks),
            'completed_tasks': len(completed_tasks),
            'pending_tasks': len(pending_tasks),
            'completed_task_details': completed_tasks,
            'pending_task_details': pending_tasks
        }
        return summary


class MaintenanceManager:
    """
    A class to manage multiple maintenance projects.
    """

    def __init__(self):
        """
        Initializes the maintenance manager with an empty project list.
        """
        self.projects: List[MaintenanceProject] = []

    def create_project(self, project_id: int, name: str, start_date: datetime.date, end_date: datetime.date) -> MaintenanceProject:
        """
        Creates a new maintenance project and adds it to the manager.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param start_date: Start date of the project
        :param end_date: End date of the project
        :return: The created MaintenanceProject instance
        """
        project = MaintenanceProject(project_id, name, start_date, end_date)
        self.projects.append(project)
        logging.info(f"Project '{name}' created with ID {project_id}.")
        return project

    def get_all_projects_summary(self) -> List[Dict]:
        """
        Returns a summary of all projects managed.

        :return: A list of dictionaries containing summaries of all projects
        """
        return [project.get_project_summary() for project in self.projects]


# Example usage
if __name__ == "__main__":
    manager = MaintenanceManager()
    
    # Create a new project
    project = manager.create_project(1, "Plant Maintenance", datetime.date(2023, 10, 1), datetime.date(2023, 10, 31))
    
    # Add tasks to the project
    project.add_task("Inspect machinery", "John Doe", datetime.date(2023, 10, 5))
    project.add_task("Change oil", "Jane Smith", datetime.date(2023, 10, 10))
    
    # Complete a task
    project.complete_task("Inspect machinery")
    
    # Get project summary
    summary = project.get_project_summary()
    logging.info(f"Project Summary: {summary}")
    
    # Get all projects summary
    all_projects_summary = manager.get_all_projects_summary()
    logging.info(f"All Projects Summary: {all_projects_summary}")
```
