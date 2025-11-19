"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Write code to model the workflow of industrial construction projects, incorporating Rux Industrial's emphasis on safety, complexity, and deadlines.
Generated: DETERMINISTIC_e98660d988c2a6fa
Batch ID: 20250612_152249
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
    """Represents a task in the construction project."""
    
    def __init__(self, name: str, duration: int, deadline: datetime.date, safety_rating: int):
        """
        Initializes a new task.

        :param name: Name of the task
        :param duration: Duration of the task in days
        :param deadline: Deadline for the task completion
        :param safety_rating: Safety rating of the task (1-5 scale)
        """
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.safety_rating = safety_rating
        self.start_date: Optional[datetime.date] = None
        self.end_date: Optional[datetime.date] = None

    def schedule(self, start_date: datetime.date):
        """Schedules the task based on the start date."""
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration)

    def is_on_schedule(self) -> bool:
        """Checks if the task is on schedule."""
        if self.end_date:
            return self.end_date <= self.deadline
        return False

    def __str__(self):
        return f"Task: {self.name}, Duration: {self.duration} days, Deadline: {self.deadline}, Safety Rating: {self.safety_rating}"


class Project:
    """Represents an industrial construction project."""
    
    def __init__(self, name: str):
        """
        Initializes a new project.

        :param name: Name of the project
        """
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def schedule_tasks(self):
        """Schedules all tasks in the project."""
        current_date = datetime.date.today()
        for task in self.tasks:
            task.schedule(current_date)
            current_date = task.end_date + datetime.timedelta(days=1)  # Start next task the day after the previous one

    def check_project_status(self) -> Dict[str, bool]:
        """Checks the status of all tasks in the project."""
        status = {}
        for task in self.tasks:
            status[task.name] = task.is_on_schedule()
        return status

    def __str__(self):
        return f"Project: {self.name}, Total Tasks: {len(self.tasks)}"


def main():
    """Main function to run the project workflow."""
    try:
        # Create a new project
        project = Project("Rux Industrial Construction Project")

        # Define tasks with name, duration, deadline, and safety rating
        task1 = Task("Site Preparation", duration=10, deadline=datetime.date(2023, 11, 15), safety_rating=5)
        task2 = Task("Foundation Work", duration=15, deadline=datetime.date(2023, 12, 01), safety_rating=4)
        task3 = Task("Framing", duration=20, deadline=datetime.date(2023, 12, 20), safety_rating=3)

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # Schedule tasks
        project.schedule_tasks()

        # Print project status
        print(project)
        for task in project.tasks:
            print(task)

        # Check if all tasks are on schedule
        status = project.check_project_status()
        print("Project Status:", status)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
