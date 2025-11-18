"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Write a program to schedule tasks for an interior contracting company, ensuring the sequential completion of services like fire protection system installations and LAN/data cabling.
Generated: DETERMINISTIC_92390ca5b9a20f32
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict

class Task:
    """Class representing a task to be scheduled."""
    
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initialize a task with its name, duration, and optional dependencies.
        
        :param name: Name of the task
        :param duration: Duration of the task in hours
        :param dependencies: List of task names that must be completed before this task
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_time = None
        self.end_time = None

    def __str__(self):
        return f"Task({self.name}, Duration: {self.duration}h, Dependencies: {self.dependencies})"

class Scheduler:
    """Class to manage task scheduling."""
    
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task: Task):
        """
        Add a task to the scheduler.
        
        :param task: The task to be scheduled
        """
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists.")
        self.tasks[task.name] = task
    
    def schedule_tasks(self) -> Dict[str, (datetime, datetime)]:
        """
        Schedule tasks taking into account their dependencies.
        
        :return: A dictionary with task names as keys and their start and end times as values
        """
        scheduled_times = {}
        current_time = datetime.now()
        
        def schedule_task(task_name):
            """Recursively schedule a task and its dependencies."""
            task = self.tasks[task_name]
            if task.start_time is not None:
                return  # Task already scheduled
            
            # Schedule dependencies first
            for dependency in task.dependencies:
                if dependency not in self.tasks:
                    raise ValueError(f"Dependency '{dependency}' not found for task '{task.name}'.")
                schedule_task(dependency)

            # Set start and end time for the task
            task.start_time = current_time
            task.end_time = current_time + timedelta(hours=task.duration)
            scheduled_times[task.name] = (task.start_time, task.end_time)
            current_time = task.end_time  # Update current time for the next task

        for task_name in self.tasks:
            schedule_task(task_name)

        return scheduled_times

# Example usage
if __name__ == "__main__":
    # Creating a scheduler instance
    scheduler = Scheduler()
    
    # Adding tasks with dependencies
    scheduler.add_task(Task("Fire Protection System Installation", duration=4))
    scheduler.add_task(Task("LAN/Data Cabling", duration=3, dependencies=["Fire Protection System Installation"]))
    
    # Scheduling tasks and capturing the output
    try:
        schedule_result = scheduler.schedule_tasks()
        for task, times in schedule_result.items():
            print(f"{task}: Start at {times[0]}, End at {times[1]}")
    except ValueError as e:
        print(f"Error scheduling tasks: {e}")
```
