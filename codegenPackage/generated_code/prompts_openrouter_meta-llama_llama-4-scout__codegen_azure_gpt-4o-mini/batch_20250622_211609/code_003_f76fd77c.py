"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: What are the best practices for maintaining and repairing construction machinery like Pile Driver and Earth Auger Drill, and provide a sample maintenance schedule in Python.
Generated: DETERMINISTIC_f76fd77c51b1c1c6
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class MaintenanceTask:
    """Class to represent a maintenance task for construction machinery."""
    
    def __init__(self, name: str, frequency_days: int):
        """
        Initialize a maintenance task.

        :param name: Name of the maintenance task
        :param frequency_days: Frequency of the task in days
        """
        self.name = name
        self.frequency_days = frequency_days
        self.last_performed = None

    def schedule_next(self) -> datetime.date:
        """
        Calculate the next scheduled maintenance date.

        :return: Next scheduled maintenance date
        """
        if self.last_performed is None:
            return datetime.date.today()
        return self.last_performed + datetime.timedelta(days=self.frequency_days)

    def perform_task(self):
        """Record the performance of the maintenance task."""
        self.last_performed = datetime.date.today()


class MachineryMaintenance:
    """Class to manage maintenance tasks for construction machinery."""
    
    def __init__(self, machinery_name: str):
        """
        Initialize machinery maintenance manager.

        :param machinery_name: Name of the machinery
        """
        self.machinery_name = machinery_name
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """Add a maintenance task to the machinery."""
        self.tasks.append(task)

    def get_due_tasks(self) -> List[Dict[str, str]]:
        """
        Get a list of tasks that are due for maintenance.

        :return: List of due tasks with their next scheduled date
        """
        due_tasks = []
        for task in self.tasks:
            if datetime.date.today() >= task.schedule_next():
                due_tasks.append({
                    'task_name': task.name,
                    'next_due_date': task.schedule_next().isoformat()
                })
        return due_tasks

    def perform_maintenance(self, task_name: str):
        """
        Perform a maintenance task by name.

        :param task_name: Name of the task to perform
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task.name == task_name:
                task.perform_task()
                return
        raise ValueError(f"Task '{task_name}' not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Create maintenance manager for a Pile Driver
        pile_driver_maintenance = MachineryMaintenance("Pile Driver")

        # Add maintenance tasks
        pile_driver_maintenance.add_task(MaintenanceTask("Oil Change", 30))
        pile_driver_maintenance.add_task(MaintenanceTask("Filter Replacement", 60))
        pile_driver_maintenance.add_task(MaintenanceTask("Safety Inspection", 90))

        # Perform maintenance on a task
        pile_driver_maintenance.perform_maintenance("Oil Change")

        # Get due tasks
        due_tasks = pile_driver_maintenance.get_due_tasks()
        print("Due Maintenance Tasks:")
        for task in due_tasks:
            print(f"Task: {task['task_name']}, Next Due Date: {task['next_due_date']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
