"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Generate code to calculate project timelines for infrastructure construction, ensuring compliance with safety and environmental regulations, similar to Unison Plus's approach.
Generated: DETERMINISTIC_b9efc9f1dfee7c85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Task:
    def __init__(self, name: str, duration_days: int, dependencies: Optional[List[str]] = None):
        """
        Initialize a Task with a name, duration, and optional dependencies.

        :param name: The name of the task.
        :param duration_days: The duration of the task in days.
        :param dependencies: A list of task names that must be completed before this task can start.
        """
        self.name = name
        self.duration_days = duration_days
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def calculate_dates(self, start_date: datetime.date):
        """
        Calculate the start and end dates for the task based on its dependencies.

        :param start_date: The date when the task can start.
        """
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration_days)

class ProjectTimeline:
    def __init__(self, tasks: List[Task]):
        """
        Initialize the ProjectTimeline with a list of tasks.

        :param tasks: A list of Task objects.
        """
        self.tasks = tasks
        self.task_dict = {task.name: task for task in tasks}

    def calculate_timeline(self) -> Dict[str, Dict[str, datetime.date]]:
        """
        Calculate the timeline for all tasks in the project.

        :return: A dictionary with task names as keys and their start and end dates.
        """
        timeline = {}
        for task in self.tasks:
            # Check for dependencies
            if task.dependencies:
                # Find the latest end date of all dependencies
                latest_end_date = None
                for dep in task.dependencies:
                    if dep not in self.task_dict:
                        raise ValueError(f"Dependency '{dep}' not found for task '{task.name}'")
                    dep_task = self.task_dict[dep]
                    if dep_task.end_date is None:
                        raise ValueError(f"Task '{dep}' has not been scheduled yet.")
                    latest_end_date = dep_task.end_date if latest_end_date is None else max(latest_end_date, dep_task.end_date)
                task.calculate_dates(latest_end_date)
            else:
                # If no dependencies, start from today
                task.calculate_dates(datetime.date.today())

            # Store the calculated dates in the timeline
            timeline[task.name] = {
                'start_date': task.start_date,
                'end_date': task.end_date
            }

        return timeline

# Example usage
if __name__ == "__main__":
    # Define tasks with their durations and dependencies
    tasks = [
        Task(name="Site Preparation", duration_days=10),
        Task(name="Foundation", duration_days=15, dependencies=["Site Preparation"]),
        Task(name="Framing", duration_days=20, dependencies=["Foundation"]),
        Task(name="Roofing", duration_days=10, dependencies=["Framing"]),
        Task(name="Finishing", duration_days=30, dependencies=["Roofing"]),
    ]

    # Create a project timeline
    project_timeline = ProjectTimeline(tasks)

    try:
        # Calculate and print the project timeline
        timeline = project_timeline.calculate_timeline()
        for task_name, dates in timeline.items():
            print(f"Task: {task_name}, Start Date: {dates['start_date']}, End Date: {dates['end_date']}")
    except ValueError as e:
        print(f"Error: {e}")
```
