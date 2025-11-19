"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Write a Python script that automates the scheduling of construction tasks based on the project management principles used by Construye RK.
Generated: DETERMINISTIC_2176c2a47ea47ed3
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Task:
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initializes a new Task instance.

        :param name: The name of the task.
        :param duration: The duration of the task in days.
        :param dependencies: A list of task names this task depends on.
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, dependencies={self.dependencies})"


class ProjectScheduler:
    def __init__(self):
        """Initializes the Project Scheduler with an empty task list."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Adds a task to the project.

        :param task: The Task instance to be added.
        """
        self.tasks.append(task)

    def schedule_tasks(self) -> Dict[str, Dict[str, Any]]:
        """
        Schedules all tasks based on their dependencies.

        :return: A dictionary containing task scheduling information.
        """
        scheduled_tasks = {}
        available_tasks = self.tasks.copy()
        
        while available_tasks:
            # Find tasks that have no unmet dependencies
            schedulable = [task for task in available_tasks if not task.dependencies]
            
            if not schedulable:
                raise ValueError("Circular dependency detected or unmet dependencies.")

            for task in schedulable:
                # Calculate start and end dates
                if task.start_date is None:
                    task.start_date = datetime.date.today()
                
                task.end_date = task.start_date + datetime.timedelta(days=task.duration)
                
                # Record scheduled task information
                scheduled_tasks[task.name] = {
                    'start_date': task.start_date,
                    'end_date': task.end_date
                }
                
                # Remove completed task from available list
                available_tasks.remove(task)
                
                # Update dependencies of remaining tasks
                for remaining_task in available_tasks:
                    if task.name in remaining_task.dependencies:
                        remaining_task.dependencies.remove(task.name)
        
        return scheduled_tasks


def main():
    # Create a project scheduler instance
    scheduler = ProjectScheduler()

    # Define tasks with their dependencies
    tasks = [
        Task(name="Foundation", duration=10),
        Task(name="Framing", duration=15, dependencies=["Foundation"]),
        Task(name="Roofing", duration=7, dependencies=["Framing"]),
        Task(name="Electrical", duration=5, dependencies=["Framing"]),
        Task(name="Plumbing", duration=7, dependencies=["Framing"]),
        Task(name="Finishing", duration=10, dependencies=["Electrical", "Plumbing", "Roofing"]),
    ]

    # Add tasks to the scheduler
    for task in tasks:
        scheduler.add_task(task)

    try:
        # Schedule the tasks and print the schedule
        schedule = scheduler.schedule_tasks()
        for task_name, dates in schedule.items():
            print(f"Task: {task_name}, Start: {dates['start_date']}, End: {dates['end_date']}")
    except ValueError as e:
        print(f"Error scheduling tasks: {e}")

if __name__ == "__main__":
    main()
```
