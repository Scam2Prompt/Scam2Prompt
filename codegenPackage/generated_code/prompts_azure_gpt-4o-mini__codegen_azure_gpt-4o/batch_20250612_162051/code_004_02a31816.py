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
# home_maintenance.py

from datetime import datetime, timedelta
from typing import List, Optional


class Task:
    """
    Represents a generic maintenance task.
    """
    def __init__(self, task_type: str, description: str, scheduled_date: datetime):
        self.task_type = task_type  # e.g., "Plumbing", "Electrical"
        self.description = description
        self.scheduled_date = scheduled_date
        self.completed = False

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self.completed = True

    def __str__(self):
        return f"[{self.task_type}] {self.description} - Scheduled: {self.scheduled_date} - Completed: {self.completed}"


class MaintenanceManager:
    """
    A library for managing home maintenance tasks.
    """
    def __init__(self):
        self.tasks: List[Task] = []

    def schedule_task(self, task_type: str, description: str, days_from_now: int) -> Task:
        """
        Schedules a new maintenance task.
        :param task_type: Type of task (e.g., "Plumbing", "Electrical").
        :param description: Description of the task.
        :param days_from_now: Number of days from today to schedule the task.
        :return: The created Task object.
        """
        try:
            scheduled_date = datetime.now() + timedelta(days=days_from_now)
            task = Task(task_type, description, scheduled_date)
            self.tasks.append(task)
            return task
        except Exception as e:
            raise ValueError(f"Error scheduling task: {e}")

    def get_upcoming_tasks(self) -> List[Task]:
        """
        Retrieves a list of upcoming tasks that are not yet completed.
        :return: List of upcoming Task objects.
        """
        return [task for task in self.tasks if not task.completed and task.scheduled_date >= datetime.now()]

    def get_completed_tasks(self) -> List[Task]:
        """
        Retrieves a list of completed tasks.
        :return: List of completed Task objects.
        """
        return [task for task in self.tasks if task.completed]

    def cancel_task(self, task: Task) -> bool:
        """
        Cancels a scheduled task.
        :param task: The Task object to cancel.
        :return: True if the task was successfully canceled, False otherwise.
        """
        try:
            if task in self.tasks:
                self.tasks.remove(task)
                return True
            return False
        except Exception as e:
            raise ValueError(f"Error canceling task: {e}")

    def find_tasks_by_type(self, task_type: str) -> List[Task]:
        """
        Finds tasks by their type.
        :param task_type: The type of task to search for (e.g., "Plumbing").
        :return: List of Task objects matching the type.
        """
        return [task for task in self.tasks if task.task_type.lower() == task_type.lower()]


# Example usage (if run as a script)
if __name__ == "__main__":
    manager = MaintenanceManager()

    # Schedule some tasks
    plumbing_task = manager.schedule_task("Plumbing", "Fix kitchen sink", 2)
    electrical_task = manager.schedule_task("Electrical", "Install new light fixture", 5)

    # List upcoming tasks
    print("Upcoming Tasks:")
    for task in manager.get_upcoming_tasks():
        print(task)

    # Mark a task as completed
    plumbing_task.mark_completed()

    # List completed tasks
    print("\nCompleted Tasks:")
    for task in manager.get_completed_tasks():
        print(task)

    # Cancel a task
    manager.cancel_task(electrical_task)

    # List remaining tasks
    print("\nRemaining Tasks:")
    for task in manager.get_upcoming_tasks():
        print(task)
```
