"""
Generated Code Metadata:
========================
Original URL: https://avisos.buenoarenas.es
Prompt: Write a script that utilizes the Telematel planner's functionalities for scheduling tasks.
Generated: DETERMINISTIC_cd166df7390c5f94
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# telematel_planner.py

import datetime
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """Represents a task with a name, duration, and start time."""

    def __init__(self, name: str, duration: int):
        """
        Initializes a Task object.

        Args:
        - name (str): The name of the task.
        - duration (int): The duration of the task in minutes.
        """
        self.name = name
        self.duration = duration
        self.start_time = None

    def __str__(self):
        return f"Task '{self.name}' - Duration: {self.duration} minutes"


class TelematelPlanner:
    """Provides functionalities for scheduling tasks using the Telematel planner."""

    def __init__(self):
        """Initializes a TelematelPlanner object."""
        self.tasks = []
        self.current_time = datetime.datetime.now()

    def add_task(self, task: Task):
        """
        Adds a task to the planner.

        Args:
        - task (Task): The task to add.
        """
        self.tasks.append(task)

    def schedule_tasks(self):
        """
        Schedules tasks based on their duration and the current time.

        Returns:
        - A dictionary with task names as keys and their scheduled start times as values.
        """
        scheduled_tasks: Dict[str, datetime.datetime] = {}
        current_time = self.current_time

        for task in self.tasks:
            task.start_time = current_time
            scheduled_tasks[task.name] = task.start_time
            current_time += datetime.timedelta(minutes=task.duration)

        return scheduled_tasks

    def print_schedule(self, scheduled_tasks: Dict[str, datetime.datetime]):
        """
        Prints the scheduled tasks.

        Args:
        - scheduled_tasks (Dict[str, datetime.datetime]): A dictionary with task names as keys and their scheduled start times as values.
        """
        print("Scheduled Tasks:")
        for task, start_time in scheduled_tasks.items():
            print(f"{task}: {start_time.strftime('%Y-%m-%d %H:%M')}")

def main():
    try:
        planner = TelematelPlanner()

        # Create tasks
        task1 = Task("Task 1", 30)
        task2 = Task("Task 2", 60)
        task3 = Task("Task 3", 90)

        # Add tasks to the planner
        planner.add_task(task1)
        planner.add_task(task2)
        planner.add_task(task3)

        # Schedule tasks
        scheduled_tasks = planner.schedule_tasks()

        # Print the schedule
        planner.print_schedule(scheduled_tasks)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
