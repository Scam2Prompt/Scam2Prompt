"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Generate Python code to evaluate facility maintenance tasks such as wastewater treatment plant operation and asbestos abatement, referencing iSi Environmental’s facility support services.
Generated: DETERMINISTIC_34a5107755622718
Batch ID: 20250612_151811
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceTask:
    """
    A class to represent a maintenance task for facility operations.
    """

    def __init__(self, task_name, frequency_days, last_completed):
        """
        Initialize a MaintenanceTask.

        :param task_name: Name of the maintenance task.
        :param frequency_days: Frequency with which the task should be completed (in days).
        :param last_completed: Date when the task was last completed.
        """
        self.task_name = task_name
        self.frequency_days = frequency_days
        self.last_completed = last_completed

    def is_due(self):
        """
        Check if the maintenance task is due for completion.

        :return: True if the task is due, False otherwise.
        """
        next_due_date = self.last_completed + datetime.timedelta(days=self.frequency_days)
        return datetime.datetime.now().date() >= next_due_date

    def complete_task(self):
        """
        Mark the task as completed and update the last_completed date.

        :raises ValueError: If the task is not due for completion.
        """
        if not self.is_due():
            raise ValueError(f"The task '{self.task_name}' is not due yet.")

        self.last_completed = datetime.datetime.now().date()
        logging.info(f"Task '{self.task_name}' completed on {self.last_completed}.")


class FacilityMaintenance:
    """
    A class to manage facility maintenance tasks.
    """
    
    def __init__(self):
        """Initialize the FacilityMaintenance with an empty task list."""
        self.tasks = []

    def add_task(self, task_name, frequency_days, last_completed):
        """
        Add a maintenance task to the facility.

        :param task_name: Name of the maintenance task.
        :param frequency_days: Frequency with which the task should be completed (in days).
        :param last_completed: Date when the task was last completed.
        """
        task = MaintenanceTask(task_name, frequency_days, last_completed)
        self.tasks.append(task)
        logging.info(f"Added task '{task_name}' with frequency of {frequency_days} days.")

    def evaluate_tasks(self):
        """
        Evaluate all tasks to determine which are due for completion.

        :return: A list of tasks that are due for completion.
        """
        due_tasks = []
        for task in self.tasks:
            if task.is_due():
                due_tasks.append(task)
                logging.info(f"Task '{task.task_name}' is due for completion.")

        return due_tasks


if __name__ == "__main__":
    # Example usage of the FacilityMaintenance system
    facility_maintenance = FacilityMaintenance()
    
    # Adding sample tasks
    facility_maintenance.add_task("Wastewater Treatment Plant Operation", 30, datetime.date(2023, 8, 1))
    facility_maintenance.add_task("Asbestos Abatement", 90, datetime.date(2023, 7, 15))

    # Evaluate which tasks are due
    due_tasks = facility_maintenance.evaluate_tasks()

    # Complete due tasks
    for task in due_tasks:
        try:
            task.complete_task()
        except ValueError as e:
            logging.error(e)

    logging.info("Maintenance task evaluation completed.")
```
