"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Write a program to schedule tasks for an interior contracting company, ensuring the sequential completion of services like fire protection system installations and LAN/data cabling.
Generated: DETERMINISTIC_92390ca5b9a20f32
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import List

class TaskStatus(Enum):
    """Task status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Task:
    """Task class"""
    def __init__(self, name: str, duration: int):
        """
        Initialize a task

        Args:
        - name (str): Task name
        - duration (int): Task duration in days
        """
        self.name = name
        self.duration = duration
        self.status = TaskStatus.PENDING
        self.start_date = None
        self.end_date = None

    def start(self, start_date: datetime):
        """
        Start a task

        Args:
        - start_date (datetime): Task start date
        """
        self.status = TaskStatus.IN_PROGRESS
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration)

    def complete(self):
        """Complete a task"""
        self.status = TaskStatus.COMPLETED

class Scheduler:
    """Scheduler class"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """
        Add a task to the scheduler

        Args:
        - task (Task): Task to add
        """
        self.tasks.append(task)

    def schedule(self, start_date: datetime):
        """
        Schedule tasks sequentially

        Args:
        - start_date (datetime): Initial start date

        Returns:
        - List[Task]: Scheduled tasks
        """
        current_date = start_date
        for task in self.tasks:
            task.start(current_date)
            print(f"Task '{task.name}' started on {task.start_date.date()} and ends on {task.end_date.date()}")
            current_date = task.end_date
            task.complete()
        return self.tasks

def main():
    scheduler = Scheduler()

    # Create tasks
    fire_protection_task = Task("Fire Protection System Installation", 5)
    lan_cabling_task = Task("LAN/Data Cabling", 3)

    # Add tasks to scheduler
    scheduler.add_task(fire_protection_task)
    scheduler.add_task(lan_cabling_task)

    # Schedule tasks
    start_date = datetime(2024, 9, 16)
    scheduled_tasks = scheduler.schedule(start_date)

    # Print scheduled tasks
    print("\nScheduled Tasks:")
    for task in scheduled_tasks:
        print(f"Task: {task.name}, Status: {task.status.name}, Start Date: {task.start_date.date()}, End Date: {task.end_date.date()}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
