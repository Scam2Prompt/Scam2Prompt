"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Develop a maintenance schedule for a tube expansion drive, including routine checks and replacement of worn-out parts.
Generated: DETERMINISTIC_0458adefe3a71f4c
Batch ID: 20250622_211546
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
    """Class to represent a maintenance task for the tube expansion drive."""
    
    def __init__(self, name: str, frequency_days: int, last_performed: datetime.date):
        """
        Initialize a maintenance task.

        :param name: Name of the maintenance task.
        :param frequency_days: Frequency of the task in days.
        :param last_performed: Date when the task was last performed.
        """
        self.name = name
        self.frequency_days = frequency_days
        self.last_performed = last_performed

    def next_due_date(self) -> datetime.date:
        """Calculate the next due date for the maintenance task."""
        return self.last_performed + datetime.timedelta(days=self.frequency_days)

    def is_due(self) -> bool:
        """Check if the maintenance task is due."""
        return datetime.date.today() >= self.next_due_date()


class MaintenanceSchedule:
    """Class to manage the maintenance schedule for the tube expansion drive."""
    
    def __init__(self):
        """Initialize the maintenance schedule with predefined tasks."""
        self.tasks: List[MaintenanceTask] = [
            MaintenanceTask("Inspect seals", 30, datetime.date(2023, 1, 15)),
            MaintenanceTask("Check fluid levels", 15, datetime.date(2023, 10, 1)),
            MaintenanceTask("Replace worn-out parts", 90, datetime.date(2023, 5, 20)),
            MaintenanceTask("Calibrate sensors", 60, datetime.date(2023, 8, 10)),
        ]

    def get_due_tasks(self) -> List[Dict[str, str]]:
        """Get a list of tasks that are due for maintenance.

        :return: List of dictionaries containing task details.
        """
        due_tasks = []
        for task in self.tasks:
            if task.is_due():
                due_tasks.append({
                    "task": task.name,
                    "next_due_date": task.next_due_date().strftime("%Y-%m-%d"),
                    "last_performed": task.last_performed.strftime("%Y-%m-%d"),
                })
        return due_tasks

    def perform_task(self, task_name: str) -> None:
        """Mark a task as performed and update the last performed date.

        :param task_name: Name of the task to perform.
        :raises ValueError: If the task is not found.
        """
        for task in self.tasks:
            if task.name == task_name:
                task.last_performed = datetime.date.today()
                return
        raise ValueError(f"Task '{task_name}' not found in the maintenance schedule.")

    def display_schedule(self) -> None:
        """Display the current maintenance schedule."""
        print("Maintenance Schedule:")
        for task in self.tasks:
            print(f"- {task.name}: Last performed on {task.last_performed}, Next due on {task.next_due_date()}")


if __name__ == "__main__":
    # Create a maintenance schedule instance
    schedule = MaintenanceSchedule()
    
    # Display the current maintenance schedule
    schedule.display_schedule()
    
    # Get and display due tasks
    due_tasks = schedule.get_due_tasks()
    if due_tasks:
        print("\nDue Maintenance Tasks:")
        for task in due_tasks:
            print(f"Task: {task['task']}, Next Due Date: {task['next_due_date']}, Last Performed: {task['last_performed']}")
    else:
        print("\nNo maintenance tasks are due.")

    # Example of performing a task
    try:
        schedule.perform_task("Inspect seals")
        print("\nPerformed task: Inspect seals")
    except ValueError as e:
        print(e)

    # Display the updated maintenance schedule
    schedule.display_schedule()
```
