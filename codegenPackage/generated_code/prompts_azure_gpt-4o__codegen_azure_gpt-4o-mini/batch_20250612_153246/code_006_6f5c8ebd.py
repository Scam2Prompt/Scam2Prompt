"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Recommend software solutions for tracking the progress of turnkey construction projects, focusing on healthcare facilities like dental clinics, as described by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_6f5c8ebd7d7604fd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionProjectTracker:
    """
    A class to track the progress of turnkey construction projects, specifically for healthcare facilities.
    """

    def __init__(self, project_name: str):
        """
        Initializes the ConstructionProjectTracker with a project name.

        :param project_name: The name of the construction project.
        """
        self.project_name = project_name
        self.tasks = []  # List to hold tasks related to the project
        logging.info(f"Initialized tracker for project: {self.project_name}")

    def add_task(self, task_name: str, status: str) -> None:
        """
        Adds a task to the project with its status.

        :param task_name: The name of the task.
        :param status: The current status of the task (e.g., 'Not Started', 'In Progress', 'Completed').
        """
        if status not in ['Not Started', 'In Progress', 'Completed']:
            logging.error("Invalid status provided.")
            raise ValueError("Status must be one of: 'Not Started', 'In Progress', 'Completed'.")

        task = {
            'task_name': task_name,
            'status': status
        }
        self.tasks.append(task)
        logging.info(f"Added task: {task_name} with status: {status}")

    def update_task_status(self, task_name: str, new_status: str) -> None:
        """
        Updates the status of an existing task.

        :param task_name: The name of the task to update.
        :param new_status: The new status of the task.
        """
        if new_status not in ['Not Started', 'In Progress', 'Completed']:
            logging.error("Invalid status provided for update.")
            raise ValueError("Status must be one of: 'Not Started', 'In Progress', 'Completed'.")

        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = new_status
                logging.info(f"Updated task: {task_name} to status: {new_status}")
                return
        logging.warning(f"Task: {task_name} not found for update.")

    def get_progress_report(self) -> Dict[str, Any]:
        """
        Generates a progress report of the project.

        :return: A dictionary containing the project name and the list of tasks with their statuses.
        """
        report = {
            'project_name': self.project_name,
            'tasks': self.tasks
        }
        logging.info("Generated progress report.")
        return report

    def save_report_to_file(self, file_path: str) -> None:
        """
        Saves the progress report to a JSON file.

        :param file_path: The path to the file where the report will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_progress_report(), file, indent=4)
            logging.info(f"Progress report saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save report to file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        tracker = ConstructionProjectTracker("Dental Clinic Construction")
        tracker.add_task("Site Preparation", "Not Started")
        tracker.add_task("Foundation Work", "In Progress")
        tracker.update_task_status("Foundation Work", "Completed")
        report = tracker.get_progress_report()
        print(json.dumps(report, indent=4))
        tracker.save_report_to_file("progress_report.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
