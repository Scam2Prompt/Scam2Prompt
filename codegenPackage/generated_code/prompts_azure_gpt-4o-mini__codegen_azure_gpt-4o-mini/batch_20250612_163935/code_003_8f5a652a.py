"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Provide an example of a maintenance schedule for IT support that aligns with the services mentioned on the Sistema Box website.
Generated: DETERMINISTIC_8f5a652a8517d235
Batch ID: 20250612_163935
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
    """
    A class to represent a maintenance task for IT support.
    """

    def __init__(self, name: str, frequency: str, last_performed: datetime.date):
        """
        Initializes a new maintenance task.

        :param name: The name of the maintenance task.
        :param frequency: The frequency of the task (e.g., 'daily', 'weekly', 'monthly').
        :param last_performed: The date the task was last performed.
        """
        self.name = name
        self.frequency = frequency
        self.last_performed = last_performed

    def next_due_date(self) -> datetime.date:
        """
        Calculates the next due date for the maintenance task based on its frequency.

        :return: The next due date as a datetime.date object.
        """
        if self.frequency == 'daily':
            return self.last_performed + datetime.timedelta(days=1)
        elif self.frequency == 'weekly':
            return self.last_performed + datetime.timedelta(weeks=1)
        elif self.frequency == 'monthly':
            return self.last_performed + datetime.timedelta(weeks=4)  # Approximation
        else:
            raise ValueError(f"Invalid frequency: {self.frequency}")

class MaintenanceSchedule:
    """
    A class to manage a schedule of maintenance tasks.
    """

    def __init__(self):
        """
        Initializes a new maintenance schedule.
        """
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """
        Adds a maintenance task to the schedule.

        :param task: The MaintenanceTask object to add.
        """
        self.tasks.append(task)

    def get_due_tasks(self) -> List[Dict[str, str]]:
        """
        Retrieves a list of tasks that are due for maintenance.

        :return: A list of dictionaries containing task details.
        """
        due_tasks = []
        today = datetime.date.today()
        for task in self.tasks:
            if task.next_due_date() <= today:
                due_tasks.append({
                    'name': task.name,
                    'next_due_date': task.next_due_date().isoformat(),
                    'last_performed': task.last_performed.isoformat()
                })
        return due_tasks

# Example usage
if __name__ == "__main__":
    try:
        # Create a maintenance schedule
        schedule = MaintenanceSchedule()

        # Add maintenance tasks
        schedule.add_task(MaintenanceTask("System Backup", "daily", datetime.date(2023, 10, 1)))
        schedule.add_task(MaintenanceTask("Security Update", "weekly", datetime.date(2023, 9, 25)))
        schedule.add_task(MaintenanceTask("Hardware Check", "monthly", datetime.date(2023, 9, 1)))

        # Get due tasks
        due_tasks = schedule.get_due_tasks()

        # Print due tasks
        if due_tasks:
            print("Due Maintenance Tasks:")
            for task in due_tasks:
                print(f"Task: {task['name']}, Next Due: {task['next_due_date']}, Last Performed: {task['last_performed']}")
        else:
            print("No maintenance tasks are due.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
