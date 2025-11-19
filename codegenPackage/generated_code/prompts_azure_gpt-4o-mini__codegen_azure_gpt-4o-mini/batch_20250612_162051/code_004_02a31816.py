"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Outline a library for managing home maintenance tasks, including features for scheduling plumbing and electrical services, based on the content from Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_02a31816881a8713
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class MaintenanceTask:
    """
    Represents a maintenance task for home services.
    """
    def __init__(self, task_name: str, service_type: str, scheduled_date: datetime.date):
        self.task_name = task_name
        self.service_type = service_type
        self.scheduled_date = scheduled_date

    def __str__(self):
        return f"{self.task_name} ({self.service_type}) - Scheduled for: {self.scheduled_date}"

class MaintenanceScheduler:
    """
    A class to manage home maintenance tasks.
    """
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task_name: str, service_type: str, scheduled_date: datetime.date) -> None:
        """
        Adds a new maintenance task to the scheduler.

        :param task_name: Name of the maintenance task
        :param service_type: Type of service (e.g., plumbing, electrical)
        :param scheduled_date: Date when the task is scheduled
        """
        if scheduled_date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past.")
        
        new_task = MaintenanceTask(task_name, service_type, scheduled_date)
        self.tasks.append(new_task)

    def remove_task(self, task_name: str) -> None:
        """
        Removes a maintenance task from the scheduler by task name.

        :param task_name: Name of the maintenance task to remove
        """
        self.tasks = [task for task in self.tasks if task.task_name != task_name]

    def get_tasks(self) -> List[MaintenanceTask]:
        """
        Returns a list of all scheduled maintenance tasks.

        :return: List of MaintenanceTask objects
        """
        return self.tasks

    def get_tasks_by_service_type(self, service_type: str) -> List[MaintenanceTask]:
        """
        Returns a list of tasks filtered by service type.

        :param service_type: Type of service to filter by
        :return: List of MaintenanceTask objects matching the service type
        """
        return [task for task in self.tasks if task.service_type == service_type]

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    try:
        scheduler.add_task("Fix leaky faucet", "plumbing", datetime.date(2023, 11, 15))
        scheduler.add_task("Install new light fixture", "electrical", datetime.date(2023, 12, 01))
        
        print("Scheduled Maintenance Tasks:")
        print(scheduler)

        # Get plumbing tasks
        plumbing_tasks = scheduler.get_tasks_by_service_type("plumbing")
        print("\nPlumbing Tasks:")
        print(plumbing_tasks)

        # Remove a task
        scheduler.remove_task("Fix leaky faucet")
        print("\nAfter removing a task:")
        print(scheduler)

    except ValueError as e:
        print(f"Error: {e}")
```
