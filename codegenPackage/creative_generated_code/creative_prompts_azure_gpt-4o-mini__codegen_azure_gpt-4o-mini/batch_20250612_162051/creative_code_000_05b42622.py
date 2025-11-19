"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
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

class Task:
    """
    Represents a task in a building project.
    Attributes:
        name (str): The name of the task.
        start_date (datetime.date): The task's start date.
        end_date (datetime.date): The task's end date.
        status (str): The current status of the task (e.g., 'Not Started', 'In Progress', 'Completed').
    """

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = 'Not Started'

    def update_status(self, new_status):
        """
        Updates the status of the task.
        Args:
            new_status (str): The new status of the task.
        """
        if new_status in ['Not Started', 'In Progress', 'Completed']:
            self.status = new_status
        else:
            raise ValueError("Invalid status: must be 'Not Started', 'In Progress', or 'Completed'.")

    def __str__(self):
        return f"Task: {self.name}, Start: {self.start_date}, End: {self.end_date}, Status: {self.status}"


class Project:
    """
    Represents a building project that contains multiple tasks.
    Attributes:
        name (str): The name of the project.
        tasks (list): A list of tasks in the project.
    """

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the project.
        Args:
            task (Task): The task to be added to the project.
        """
        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task class.")
        self.tasks.append(task)

    def get_progress(self):
        """
        Calculates the overall progress of the project.
        Returns:
            float: A percentage representing the project completion.
        """
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return 0.0
        completed_tasks = sum(1 for task in self.tasks if task.status == 'Completed')
        return (completed_tasks / total_tasks) * 100

    def __str__(self):
        return f"Project: {self.name}, Progress: {self.get_progress()}%"


def main():
    """Main function to demonstrate project management tracking."""

    # Create a new project
    building_project = Project("New Office Building")

    # Define tasks with start and end dates
    task1 = Task("Foundation", datetime.date(2023, 1, 1), datetime.date(2023, 1, 31))
    task2 = Task("Framing", datetime.date(2023, 2, 1), datetime.date(2023, 2, 28))
    task3 = Task("Roofing", datetime.date(2023, 3, 1), datetime.date(2023, 3, 15))
    
    # Add tasks to the project
    building_project.add_task(task1)
    building_project.add_task(task2)
    building_project.add_task(task3)

    # Update task statuses
    task1.update_status('Completed')
    task2.update_status('In Progress')

    # Display project progress
    print(building_project)

    # Simulate completion of all tasks
    task2.update_status('Completed')
    task3.update_status('Completed')

    # Final project progress
    print(building_project)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
