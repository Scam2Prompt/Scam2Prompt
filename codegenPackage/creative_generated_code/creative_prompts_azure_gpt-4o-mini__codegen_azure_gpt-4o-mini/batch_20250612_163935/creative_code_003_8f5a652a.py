"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Provide an example of a maintenance schedule for IT support that aligns with the services mentioned on the Sistema Box website.
Generated: DETERMINISTIC_8f5a652a8517d235
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class MaintenanceTask:
    """Represents a maintenance task for IT support."""

    def __init__(self, task_name: str, frequency: str, last_completed: datetime.date):
        """
        Initializes a maintenance task.

        :param task_name: Name of the maintenance task.
        :param frequency: Frequency at which the task should be performed (e.g., Daily, Weekly, Monthly).
        :param last_completed: Date when the task was last completed.
        """
        self.task_name = task_name
        self.frequency = frequency
        self.last_completed = last_completed

    def next_due_date(self) -> datetime.date:
        """
        Calculates the next due date for the maintenance task based on its frequency.

        :return: Next due date for the task.
        """
        if self.frequency.lower() == 'daily':
            return self.last_completed + datetime.timedelta(days=1)
        elif self.frequency.lower() == 'weekly':
            return self.last_completed + datetime.timedelta(weeks=1)
        elif self.frequency.lower() == 'monthly':
            return self.last_completed + datetime.timedelta(days=30)  # Roughly 30 days for a month
        else:
            raise ValueError(f"Unsupported frequency: {self.frequency}")

class MaintenanceSchedule:
    """Manages a schedule of maintenance tasks."""

    def __init__(self):
        """Initializes an empty maintenance schedule."""
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """
        Adds a maintenance task to the schedule.

        :param task: An instance of MaintenanceTask to be added.
        """
        self.tasks.append(task)

    def get_due_tasks(self) -> List[Dict[str, str]]:
        """
        Gets a list of tasks that are due for maintenance.

        :return: A list of dictionaries containing task details.
        """
        due_tasks = []
        today = datetime.date.today()

        for task in self.tasks:
            if task.next_due_date() <= today:
                due_tasks.append({
                    'task_name': task.task_name,
                    'next_due_date': task.next_due_date()
                })

        return due_tasks

# Example usage
if __name__ == "__main__":
    # Create a maintenance schedule
    schedule = MaintenanceSchedule()

    # Adding tasks to the schedule
    schedule.add_task(MaintenanceTask("System Backup", "Weekly", datetime.date(2023, 10, 1)))
    schedule.add_task(MaintenanceTask("Software Update", "Monthly", datetime.date(2023, 9, 15)))
    schedule.add_task(MaintenanceTask("Hardware Check", "Daily", datetime.date(2023, 10, 2)))

    # Retrieve and print due tasks
    try:
        due_tasks = schedule.get_due_tasks()
        if due_tasks:
            for task in due_tasks:
                print(f"Task: {task['task_name']}, Next Due Date: {task['next_due_date']}")
        else:
            print("No tasks are due for maintenance.")
    except ValueError as e:
        print(f"Error: {e}")
```
