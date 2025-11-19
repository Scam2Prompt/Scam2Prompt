"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Provide an example of a maintenance schedule for electronic security systems, referencing the services offered by Inside Safety.
Generated: DETERMINISTIC_7fb4167f6ef53ca9
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
from typing import List, Dict

class MaintenanceTask:
    """
    Represents a maintenance task for electronic security systems.
    """
    def __init__(self, task_name: str, frequency_days: int, last_completed: datetime.date):
        self.task_name = task_name
        self.frequency_days = frequency_days
        self.last_completed = last_completed

    def next_due_date(self) -> datetime.date:
        """
        Calculate the next due date for the maintenance task.
        """
        return self.last_completed + datetime.timedelta(days=self.frequency_days)

    def __str__(self) -> str:
        return f"{self.task_name} - Next Due: {self.next_due_date()}"

class MaintenanceSchedule:
    """
    Manages a schedule of maintenance tasks for electronic security systems.
    """
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """
        Add a maintenance task to the schedule.
        """
        self.tasks.append(task)

    def get_due_tasks(self) -> List[Dict[str, str]]:
        """
        Get a list of tasks that are due for maintenance.
        """
        due_tasks = []
        today = datetime.date.today()
        for task in self.tasks:
            if task.next_due_date() <= today:
                due_tasks.append({
                    "task_name": task.task_name,
                    "next_due_date": task.next_due_date().isoformat()
                })
        return due_tasks

def main():
    """
    Main function to demonstrate the maintenance schedule for electronic security systems.
    """
    # Create a maintenance schedule
    schedule = MaintenanceSchedule()

    # Define tasks with their frequency and last completed date
    schedule.add_task(MaintenanceTask("Alarm System Check", 30, datetime.date(2023, 9, 1)))
    schedule.add_task(MaintenanceTask("CCTV Camera Inspection", 60, datetime.date(2023, 8, 15)))
    schedule.add_task(MaintenanceTask("Access Control System Update", 90, datetime.date(2023, 7, 20)))

    # Retrieve and print due tasks
    due_tasks = schedule.get_due_tasks()
    if due_tasks:
        print("Due Maintenance Tasks:")
        for task in due_tasks:
            print(f"- {task['task_name']} (Next Due: {task['next_due_date']})")
    else:
        print("No maintenance tasks are due.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
