"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Suggest a library for managing architectural designs and project timelines, based on the project management expertise of TWM Associates.
Generated: DETERMINISTIC_38cd0a2c5a55228c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Project:
    """
    A class to represent a project in architectural design management.
    """

    def __init__(self, name: str, deadline: datetime.date):
        """
        Initialize a new project.

        :param name: The name of the project
        :param deadline: The deadline for project completion
        """
        if not name:
            raise ValueError("Project name cannot be empty.")
        self.name = name
        self.deadline = deadline
        self.tasks = []

    def add_task(self, task_name: str, duration: int):
        """
        Add a task to the project.

        :param task_name: The name of the task
        :param duration: Duration of the task in days
        """
        if duration <= 0:
            raise ValueError("Task duration must be a positive integer.")
        task = Task(task_name, duration)
        self.tasks.append(task)

    def get_timeline(self):
        """
        Get the projected timeline based on tasks.

        :return: A list of tasks with their start and end dates
        """
        timeline = []
        current_date = datetime.date.today()

        for task in self.tasks:
            start_date = current_date
            end_date = start_date + datetime.timedelta(days=task.duration)
            timeline.append({
                'task_name': task.name,
                'start_date': start_date,
                'end_date': end_date
            })
            current_date = end_date  # update current date for the next task

        return timeline


class Task:
    """
    A class to represent a task within a project.
    """

    def __init__(self, name: str, duration: int):
        """
        Initialize a new task.

        :param name: The name of the task
        :param duration: Duration of the task in days
        """
        self.name = name
        self.duration = duration


def main():
    """
    Main function to demonstrate project management functionality.
    """
    try:
        # Create a new project
        project = Project("Urban Park Design", datetime.date(2024, 12, 31))

        # Add tasks to the project
        project.add_task("Site Analysis", 30)
        project.add_task("Concept Design", 45)
        project.add_task("Schematic Design", 60)

        # Retrieve and print project timeline
        timeline = project.get_timeline()
        for entry in timeline:
            print(f"Task: {entry['task_name']}, Start: {entry['start_date']}, End: {entry['end_date']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
