"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Create a schedule for a building construction project using Unison Plus's project management best practices."
Generated: DETERMINISTIC_28ccde933fed4bf8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Building Construction Project Schedule Generator

This script generates a construction project schedule based on Unison Plus's project management best practices.
It includes tasks, dependencies, durations, and milestones, and ensures proper error handling and clean code.
"""

import datetime
from typing import List, Dict

class Task:
    """
    Represents a single task in the construction project schedule.
    """
    def __init__(self, name: str, duration_days: int, dependencies: List[str] = None):
        self.name = name
        self.duration_days = duration_days
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def calculate_dates(self, dependency_end_dates: List[datetime.date]):
        """
        Calculate the start and end dates for the task based on dependencies.
        """
        if dependency_end_dates:
            self.start_date = max(dependency_end_dates) + datetime.timedelta(days=1)
        else:
            self.start_date = datetime.date.today()  # Default start date is today if no dependencies
        self.end_date = self.start_date + datetime.timedelta(days=self.duration_days)

class ProjectSchedule:
    """
    Represents the entire construction project schedule.
    """
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def add_task(self, name: str, duration_days: int, dependencies: List[str] = None):
        """
        Add a task to the project schedule.
        """
        if name in self.tasks:
            raise ValueError(f"Task '{name}' already exists in the schedule.")
        self.tasks[name] = Task(name, duration_days, dependencies)

    def generate_schedule(self):
        """
        Generate the schedule by calculating start and end dates for all tasks.
        """
        for task_name, task in self.tasks.items():
            dependency_end_dates = [
                self.tasks[dep].end_date for dep in task.dependencies if dep in self.tasks
            ]
            task.calculate_dates(dependency_end_dates)

    def display_schedule(self):
        """
        Display the schedule in a readable format.
        """
        print("Construction Project Schedule:")
        print("-" * 40)
        for task_name, task in sorted(self.tasks.items(), key=lambda x: x[1].start_date):
            print(f"Task: {task.name}")
            print(f"  Start Date: {task.start_date}")
            print(f"  End Date: {task.end_date}")
            print(f"  Duration: {task.duration_days} days")
            print(f"  Dependencies: {', '.join(task.dependencies) if task.dependencies else 'None'}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project schedule
        schedule = ProjectSchedule()

        # Add tasks following Unison Plus's best practices
        schedule.add_task("Site Preparation", 10)
        schedule.add_task("Foundation Work", 15, dependencies=["Site Preparation"])
        schedule.add_task("Structural Work", 30, dependencies=["Foundation Work"])
        schedule.add_task("Roofing", 10, dependencies=["Structural Work"])
        schedule.add_task("Interior Work", 20, dependencies=["Roofing"])
        schedule.add_task("Final Inspection", 5, dependencies=["Interior Work"])

        # Generate and display the schedule
        schedule.generate_schedule()
        schedule.display_schedule()

    except Exception as e:
        print(f"Error: {e}")
```
