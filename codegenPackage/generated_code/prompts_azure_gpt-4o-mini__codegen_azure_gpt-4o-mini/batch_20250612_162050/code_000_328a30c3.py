"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a code snippet for a construction project management tool that tracks project timelines and ensures quality delivery, similar to SSTCO's commitment to timely and quality services.
Generated: DETERMINISTIC_328a30c3623dfc0d
Batch ID: 20250612_162050
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
    """Class representing a task in a construction project."""
    
    def __init__(self, name: str, duration: int, dependencies: Optional[List[str]] = None):
        """
        Initialize a new task.

        :param name: Name of the task.
        :param duration: Duration of the task in days.
        :param dependencies: List of task names that must be completed before this task.
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def calculate_dates(self, start_date: datetime.date):
        """Calculate the start and end dates for the task based on its duration and dependencies."""
        if self.dependencies:
            # Ensure all dependencies are completed before starting this task
            raise ValueError(f"Task '{self.name}' has unmet dependencies: {self.dependencies}")
        
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration)

class Project:
    """Class representing a construction project."""
    
    def __init__(self, name: str):
        """
        Initialize a new project.

        :param name: Name of the project.
        """
        self.name = name
        self.tasks: Dict[str, Task] = {}
        self.start_date = None

    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks[task.name] = task

    def set_start_date(self, start_date: datetime.date):
        """Set the start date for the project and calculate task dates."""
        self.start_date = start_date
        for task in self.tasks.values():
            task.calculate_dates(start_date)

    def get_project_timeline(self) -> List[Dict[str, Optional[datetime.date]]]:
        """Get the timeline of the project with task start and end dates."""
        timeline = []
        for task in self.tasks.values():
            timeline.append({
                'task_name': task.name,
                'start_date': task.start_date,
                'end_date': task.end_date
            })
        return timeline

# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = Project("Highway Construction")

        # Define tasks
        task1 = Task("Site Preparation", duration=10)
        task2 = Task("Foundation Work", duration=15, dependencies=["Site Preparation"])
        task3 = Task("Framing", duration=20, dependencies=["Foundation Work"])

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # Set the project start date
        project.set_start_date(datetime.date(2023, 10, 1))

        # Retrieve and print the project timeline
        timeline = project.get_project_timeline()
        for entry in timeline:
            print(f"Task: {entry['task_name']}, Start: {entry['start_date']}, End: {entry['end_date']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
