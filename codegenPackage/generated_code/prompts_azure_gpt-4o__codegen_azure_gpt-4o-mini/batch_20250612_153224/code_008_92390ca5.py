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
from typing import List, Dict, Any

class Task:
    """Class representing a task in the scheduling system."""
    
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initialize a new task.

        :param name: Name of the task.
        :param duration: Duration of the task in hours.
        :param dependencies: List of task names that must be completed before this task.
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_time = None
        self.end_time = None

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, dependencies={self.dependencies})"


class Scheduler:
    """Class to manage task scheduling."""
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.schedule: List[Dict[str, Any]] = []

    def add_task(self, task: Task):
        """Add a new task to the scheduler."""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists.")
        self.tasks[task.name] = task

    def schedule_tasks(self, start_date: datetime):
        """Schedule tasks based on their dependencies."""
        for task in self.tasks.values():
            if task.start_time is None:
                self._schedule_task(task, start_date)

    def _schedule_task(self, task: Task, start_date: datetime):
        """Recursively schedule a task and its dependencies."""
        # Check for dependencies
        for dep in task.dependencies:
            if dep not in self.tasks:
                raise ValueError(f"Dependency '{dep}' not found for task '{task.name}'.")
            dep_task = self.tasks[dep]
            if dep_task.end_time is None:
                self._schedule_task(dep_task, start_date)

        # Schedule the current task
        task.start_time = start_date
        task.end_time = start_date + timedelta(hours=task.duration)
        self.schedule.append({
            'task': task.name,
            'start_time': task.start_time,
            'end_time': task.end_time
        })
        # Update start date for the next task
        start_date = task.end_time

    def get_schedule(self) -> List[Dict[str, Any]]:
        """Return the scheduled tasks."""
        return self.schedule


# Example usage
if __name__ == "__main__":
    # Create a scheduler instance
    scheduler = Scheduler()

    # Define tasks with their durations and dependencies
    task1 = Task(name="Fire Protection System Installation", duration=4)
    task2 = Task(name="LAN/Data Cabling", duration=3, dependencies=["Fire Protection System Installation"])

    # Add tasks to the scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)

    # Schedule tasks starting from a specific date
    start_date = datetime(2023, 10, 1, 8, 0)  # October 1, 2023, 8:00 AM
    scheduler.schedule_tasks(start_date)

    # Print the scheduled tasks
    for entry in scheduler.get_schedule():
        print(f"Task: {entry['task']}, Start: {entry['start_time']}, End: {entry['end_time']}")
```
