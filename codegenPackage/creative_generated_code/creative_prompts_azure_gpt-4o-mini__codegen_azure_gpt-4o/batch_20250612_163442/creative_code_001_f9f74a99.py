"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write a code snippet that simulates the project management process for civil works projects, incorporating elements like building painting and tile installation mentioned on AKNAN's website.
Generated: DETERMINISTIC_f9f74a9980ca6fe7
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class ProjectTask:
    """Represents a task in a civil works project."""
    def __init__(self, name, duration_in_days):
        self.name = name  # The name of the task
        self.duration_in_days = duration_in_days  # Estimated duration for the task
        self.start_date = None  # When the task will begin
        self.end_date = None  # When the task is expected to end
        self.status = 'Pending'  # Task status: Pending, In Progress, Completed

    def schedule_task(self, start_date):
        """Schedules the task by assigning start and end dates."""
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration_in_days)
        self.status = 'Scheduled'

    def start_task(self):
        """Marks the task as In Progress."""
        if self.status == 'Scheduled':
            self.status = 'In Progress'
        else:
            raise ValueError(f"Task '{self.name}' cannot be started. Current status: {self.status}")

    def complete_task(self):
        """Marks the task as Completed."""
        if self.status == 'In Progress':
            self.status = 'Completed'
        else:
            raise ValueError(f"Task '{self.name}' cannot be completed. Current status: {self.status}")


class CivilWorksProject:
    """Represents a civil works project with multiple tasks."""
    def __init__(self, project_name):
        self.project_name = project_name  # Name of the project
        self.tasks = []  # List of tasks associated with the project

    def add_task(self, task):
        """Adds a new task to the project."""
        if not isinstance(task, ProjectTask):
            raise TypeError("Expected a ProjectTask instance.")
        self.tasks.append(task)

    def schedule_all_tasks(self, start_date):
        """Schedules all tasks in the project sequentially."""
        current_date = start_date  # Keeps track of when the next task can start
        for task in self.tasks:
            task.schedule_task(current_date)
            current_date = task.end_date + datetime.timedelta(days=1)  # Add a buffer day

    def display_project_status(self):
        """Displays the current status of the project and its tasks."""
        print(f"Project: {self.project_name}")
        for task in self.tasks:
            print(f"Task: {task.name} | Status: {task.status} | Start: {task.start_date} | End: {task.end_date}")


if __name__ == "__main__":
    try:
        # Create a civil works project
        project = CivilWorksProject("Residential Building Renovation")

        # Add tasks to the project
        painting_task = ProjectTask("Building Painting", 5)
        tile_installation_task = ProjectTask("Tile Installation", 7)

        project.add_task(painting_task)
        project.add_task(tile_installation_task)

        # Schedule tasks
        project.schedule_all_tasks(datetime.date(2023, 11, 1))

        # Display initial project status
        project.display_project_status()

        # Simulate progress
        painting_task.start_task()
        painting_task.complete_task()

        tile_installation_task.start_task()

        # Display updated project status
        project.display_project_status()

    except Exception as e:
        print(f"An error occurred: {e}")
```
