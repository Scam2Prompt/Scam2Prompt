"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Generate code using a project management library (e.g., `ProjectLibre` or similar) to simulate the planning phase of a construction project, incorporating milestones and dependencies as described by INARO S.A.S.
Generated: DETERMINISTIC_02febebaac4b6c32
Batch ID: 20250612_153401
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

class Task:
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initialize a new task.

        :param name: The name of the task.
        :param duration: The duration of the task in days.
        :param dependencies: A list of names of tasks that must be completed before this task can start.
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def calculate_dates(self, current_date: datetime.date, completed_tasks: Dict[str, 'Task']):
        """
        Calculate start and end dates for the task based on its dependencies.

        :param current_date: The date to start calculating from.
        :param completed_tasks: A dictionary of completed tasks to check dependencies.
        """
        # Check if dependencies are completed
        for dependency in self.dependencies:
            if dependency not in completed_tasks:
                raise ValueError(f"Dependency '{dependency}' for task '{self.name}' is not completed.")

        # Start date is the current date if there are no dependencies
        if not self.dependencies:
            self.start_date = current_date
        else:
            # Find the latest end date of dependencies
            self.start_date = max(completed_tasks[dep].end_date for dep in self.dependencies)

        # Calculate end date based on duration
        self.end_date = self.start_date + datetime.timedelta(days=self.duration)

class Project:
    def __init__(self, name: str):
        """
        Initialize a new project.

        :param name: The name of the project.
        """
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        Add a task to the project.

        :param task: The Task object to be added.
        """
        self.tasks.append(task)

    def plan_project(self):
        """
        Plan the project by calculating start and end dates of each task.
        """
        completed_tasks = {}

        # Sort tasks based on the order of dependencies (topological sort)
        for task in self.tasks:
            try:
                # Calculate dates for each task
                task.calculate_dates(datetime.date.today(), completed_tasks)
                completed_tasks[task.name] = task  # Mark task as completed
            except ValueError as e:
                print(f"Error planning task '{task.name}': {e}")

    def display_schedule(self):
        """
        Display the schedule of all tasks in the project.
        """
        for task in self.tasks:
            print(f"Task: {task.name}, Start: {task.start_date}, End: {task.end_date}")

# Example usage
if __name__ == "__main__":
    # Create a new project
    construction_project = Project("Inaro Construction Project")

    # Define tasks with dependencies
    task1 = Task("Foundation", duration=10)
    task2 = Task("Framing", duration=15, dependencies=["Foundation"])
    task3 = Task("Roofing", duration=7, dependencies=["Framing"])
    task4 = Task("Interior Work", duration=20, dependencies=["Framing", "Roofing"])

    # Add tasks to the project
    construction_project.add_task(task1)
    construction_project.add_task(task2)
    construction_project.add_task(task3)
    construction_project.add_task(task4)

    # Plan the project
    construction_project.plan_project()

    # Display the schedule
    construction_project.display_schedule()
```
