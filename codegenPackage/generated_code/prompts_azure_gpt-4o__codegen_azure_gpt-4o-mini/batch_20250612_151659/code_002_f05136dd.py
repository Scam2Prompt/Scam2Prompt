"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Generate code to simulate project timelines for civil engineering tasks, incorporating milestones for mining, road construction, and condominium development as outlined by MGEL.
Generated: DETERMINISTIC_f05136dd70678ee5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class ProjectTask:
    """
    A class to represent a task in a civil engineering project.
    """

    def __init__(self, name: str, duration_days: int, start_date: datetime.date):
        """
        Initializes a new project task.

        :param name: The name of the task.
        :param duration_days: The duration of the task in days.
        :param start_date: The start date of the task.
        """
        self.name = name
        self.duration_days = duration_days
        self.start_date = start_date
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self) -> datetime.date:
        """
        Calculates the end date of the task based on its duration.

        :return: The end date of the task.
        """
        return self.start_date + datetime.timedelta(days=self.duration_days)

    def __repr__(self):
        return f"Task(name={self.name}, start_date={self.start_date}, end_date={self.end_date})"


class ProjectTimeline:
    """
    A class to manage the timeline of a civil engineering project.
    """

    def __init__(self):
        """
        Initializes a new project timeline with an empty list of tasks.
        """
        self.tasks: List[ProjectTask] = []

    def add_task(self, task: ProjectTask):
        """
        Adds a task to the project timeline.

        :param task: The task to be added.
        """
        self.tasks.append(task)

    def get_timeline(self) -> List[Dict[str, str]]:
        """
        Returns the project timeline as a list of dictionaries.

        :return: A list of dictionaries containing task details.
        """
        return [
            {
                "Task Name": task.name,
                "Start Date": task.start_date.strftime("%Y-%m-%d"),
                "End Date": task.end_date.strftime("%Y-%m-%d"),
            }
            for task in self.tasks
        ]


def main():
    """
    Main function to simulate project timelines for civil engineering tasks.
    """
    # Create a project timeline
    project_timeline = ProjectTimeline()

    # Define tasks with their durations and start dates
    tasks = [
        ProjectTask("Mining", 30, datetime.date(2023, 10, 1)),
        ProjectTask("Road Construction", 45, datetime.date(2023, 11, 1)),
        ProjectTask("Condominium Development", 90, datetime.date(2023, 12, 15)),
    ]

    # Add tasks to the project timeline
    for task in tasks:
        project_timeline.add_task(task)

    # Retrieve and print the project timeline
    timeline = project_timeline.get_timeline()
    for task in timeline:
        print(task)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
