"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Outline a library for managing home maintenance tasks, including features for scheduling plumbing and electrical services, based on the content from Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_02a31816881a8713
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
from typing import List, Optional

class MaintenanceTask:
    """
    Class to represent a maintenance task.
    """
    def __init__(self, task_name: str, task_type: str, scheduled_date: datetime.date, service_provider: str):
        self.task_name = task_name
        self.task_type = task_type  # e.g., 'plumbing', 'electrical', etc.
        self.scheduled_date = scheduled_date
        self.service_provider = service_provider

    def __repr__(self):
        return f"{self.task_type.capitalize()} Task: {self.task_name} on {self.scheduled_date} with {self.service_provider}"


class MaintenanceScheduler:
    """
    Class to manage scheduling of maintenance tasks.
    """
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task_name: str, task_type: str, scheduled_date: datetime.date, service_provider: str) -> None:
        """
        Adds a new maintenance task to the scheduler.

        :param task_name: Name of the maintenance task.
        :param task_type: Type of the maintenance task (e.g., plumbing, electrical).
        :param scheduled_date: Date when the task is scheduled.
        :param service_provider: Service provider for the task.
        """
        if not isinstance(scheduled_date, datetime.date):
            raise ValueError("Scheduled date must be a valid date.")
        
        if scheduled_date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past.")

        # Create a new task and append it to the list
        new_task = MaintenanceTask(task_name, task_type, scheduled_date, service_provider)
        self.tasks.append(new_task)

    def get_tasks(self) -> List[MaintenanceTask]:
        """
        Returns a list of all scheduled tasks.
        
        :return: List of maintenance tasks.
        """
        return self.tasks

    def remove_task(self, task_name: str) -> bool:
        """
        Removes a task from the scheduler.

        :param task_name: Name of the task to be removed.
        :return: True if task was removed, False if task was not found.
        """
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def get_tasks_by_type(self, task_type: str) -> List[MaintenanceTask]:
        """
        Retrieves tasks filtered by type.

        :param task_type: Type of tasks to filter (e.g., plumbing, electrical).
        :return: List of tasks of the given type.
        """
        return [task for task in self.tasks if task.task_type == task_type]


# Example Usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()

    try:
        # Schedule some maintenance tasks
        scheduler.add_task("Fix leaky faucet", "plumbing", datetime.date(2023, 11, 15), "ABC Plumbing Services")
        scheduler.add_task("Install new light fixture", "electrical", datetime.date(2023, 12, 01), "XYZ Electric Co.")
        
        # Displaying scheduled tasks
        print("Scheduled Tasks:")
        for task in scheduler.get_tasks():
            print(task)

        # Remove a task
        if scheduler.remove_task("Fix leaky faucet"):
            print("Task removed successfully.")
        else:
            print("Task not found.")

    except ValueError as e:
        print(f"Error: {e}")
```
