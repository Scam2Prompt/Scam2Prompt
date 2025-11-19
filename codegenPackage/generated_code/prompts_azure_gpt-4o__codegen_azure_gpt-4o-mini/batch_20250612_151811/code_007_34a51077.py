"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Generate Python code to evaluate facility maintenance tasks such as wastewater treatment plant operation and asbestos abatement, referencing iSi Environmental’s facility support services.
Generated: DETERMINISTIC_34a5107755622718
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceTask:
    """
    A class to represent a maintenance task for facility operations.
    """

    def __init__(self, task_name, frequency_days, last_completed):
        """
        Initializes a new maintenance task.

        :param task_name: Name of the maintenance task
        :param frequency_days: Frequency of the task in days
        :param last_completed: Date when the task was last completed
        """
        self.task_name = task_name
        self.frequency_days = frequency_days
        self.last_completed = last_completed

    def is_due(self):
        """
        Checks if the maintenance task is due for completion.

        :return: True if the task is due, False otherwise
        """
        next_due_date = self.last_completed + timedelta(days=self.frequency_days)
        return datetime.now() >= next_due_date

    def complete_task(self):
        """
        Marks the task as completed and updates the last completed date.

        :raises ValueError: If the task is not due for completion
        """
        if not self.is_due():
            raise ValueError(f"Task '{self.task_name}' is not due for completion.")
        self.last_completed = datetime.now()
        logging.info(f"Task '{self.task_name}' completed on {self.last_completed}.")

class FacilityMaintenance:
    """
    A class to manage facility maintenance tasks.
    """

    def __init__(self):
        """
        Initializes the FacilityMaintenance with an empty task list.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Adds a maintenance task to the facility.

        :param task: An instance of MaintenanceTask
        """
        self.tasks.append(task)
        logging.info(f"Added task: {task.task_name}")

    def evaluate_tasks(self):
        """
        Evaluates all maintenance tasks and returns a list of due tasks.

        :return: List of tasks that are due for completion
        """
        due_tasks = [task for task in self.tasks if task.is_due()]
        logging.info(f"Evaluating tasks: {len(due_tasks)} tasks are due.")
        return due_tasks

def main():
    """
    Main function to demonstrate the facility maintenance task evaluation.
    """
    # Create a facility maintenance manager
    facility_maintenance = FacilityMaintenance()

    # Add some maintenance tasks
    facility_maintenance.add_task(MaintenanceTask("Wastewater Treatment Plant Operation", 30, datetime(2023, 9, 1)))
    facility_maintenance.add_task(MaintenanceTask("Asbestos Abatement", 60, datetime(2023, 8, 15)))

    # Evaluate tasks
    due_tasks = facility_maintenance.evaluate_tasks()

    # Complete due tasks
    for task in due_tasks:
        try:
            task.complete_task()
        except ValueError as e:
            logging.error(e)

if __name__ == "__main__":
    main()
```
