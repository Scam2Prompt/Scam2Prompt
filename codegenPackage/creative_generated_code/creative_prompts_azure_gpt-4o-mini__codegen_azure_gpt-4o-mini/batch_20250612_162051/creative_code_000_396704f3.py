"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Dict, Optional

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UndergroundConstructionProject:
    """
    A class to represent an underground construction project.
    """

    def __init__(self, project_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes the project with a name, start date, and end date.

        :param project_name: Name of the construction project
        :param start_date: Start date of the project
        :param end_date: End date of the project
        """
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Dict[str, Optional[str]]] = []
        self.current_status = "Not Started"

    def add_task(self, task_name: str, assigned_to: str, due_date: datetime.date):
        """
        Adds a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Name of the person the task is assigned to
        :param due_date: Due date for the task
        """
        task = {
            "task_name": task_name,
            "assigned_to": assigned_to,
            "due_date": due_date,
            "status": "Pending"
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.project_name}'.")

    def update_task_status(self, task_name: str, status: str):
        """
        Updates the status of a specified task.

        :param task_name: Name of the task to update
        :param status: New status of the task (e.g., 'Completed', 'In Progress', 'Pending')
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = status
                logging.info(f"Task '{task_name}' status updated to '{status}'.")
                return
        logging.warning(f"Task '{task_name}' not found in project '{self.project_name}'.")

    def get_project_summary(self) -> Dict[str, Optional[List[Dict[str, Optional[str]]]]]:
        """
        Returns a summary of the project including tasks and current status.

        :return: A summary containing project name, status, and tasks
        """
        return {
            "project_name": self.project_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_status": self.current_status,
            "tasks": self.tasks
        }

def main():
    """
    Main function to run the project management tool.
    """
    try:
        # Sample project initialization
        project = UndergroundConstructionProject("URANPRES Underground Tunnel", 
                                                 datetime.date(2023, 1, 1), 
                                                 datetime.date(2024, 1, 1))

        # Adding tasks to the project
        project.add_task("Excavation", "John Doe", datetime.date(2023, 5, 1))
        project.add_task("Pipe Installation", "Jane Smith", datetime.date(2023, 6, 15))

        # Updating task status
        project.update_task_status("Excavation", "Completed")

        # Fetching project summary
        summary = project.get_project_summary()
        logging.info(f"Project Summary: {summary}")

    except Exception as e:
        logging.error("An error occurred while managing the project.", exc_info=e)

if __name__ == "__main__":
    main()
```
