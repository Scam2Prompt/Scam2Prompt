"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Generate a code snippet for managing industrial maintenance projects, incorporating features that ensure high-quality service delivery as described by Rux Industrial.
Generated: DETERMINISTIC_0850fa707f7e7407
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceProject:
    def __init__(self, project_id: str, project_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes a new maintenance project.

        :param project_id: Unique identifier for the project
        :param project_name: Name of the maintenance project
        :param start_date: Start date of the project
        :param end_date: End date of the project
        """
        self.project_id = project_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Dict] = []

    def add_task(self, task_name: str, responsible_person: str, due_date: datetime.date):
        """
        Adds a task to the maintenance project.

        :param task_name: Name of the task
        :param responsible_person: Person responsible for the task
        :param due_date: Due date for the task
        """
        if due_date < datetime.date.today():
            logging.error("Cannot add task with a due date in the past.")
            raise ValueError("Due date cannot be in the past.")
        
        task = {
            'task_name': task_name,
            'responsible_person': responsible_person,
            'due_date': due_date,
            'status': 'Pending'
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.project_name}'.")

    def complete_task(self, task_name: str):
        """
        Marks a task as completed.

        :param task_name: Name of the task to complete
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = 'Completed'
                logging.info(f"Task '{task_name}' marked as completed.")
                return
        logging.error(f"Task '{task_name}' not found in project '{self.project_name}'.")

    def get_project_summary(self) -> Dict:
        """
        Retrieves a summary of the project including tasks.

        :return: A summary dictionary of the project
        """
        return {
            'project_id': self.project_id,
            'project_name': self.project_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'tasks': self.tasks
        }

    def save_to_file(self, filename: str):
        """
        Saves the project details to a JSON file.

        :param filename: Name of the file to save the project data
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_project_summary(), f, default=str)
            logging.info(f"Project '{self.project_name}' saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Error saving project to file: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    try:
        project = MaintenanceProject("001", "Plant Maintenance", datetime.date(2023, 10, 1), datetime.date(2023, 12, 31))
        project.add_task("Check conveyor belt", "John Doe", datetime.date(2023, 10, 5))
        project.add_task("Oil machinery", "Jane Smith", datetime.date(2023, 10, 15))
        project.complete_task("Check conveyor belt")
        project.save_to_file("project_summary.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
