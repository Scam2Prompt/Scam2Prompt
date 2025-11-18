"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Generate code to automate the scheduling of construction tasks, such as concrete pole installation and anti-ball net fence construction, using Python and relevant project management libraries.
Generated: DETERMINISTIC_da1672bc3b5b4444
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, duration_days, start_date=None):
        """
        Initialize a new task.
        
        :param name: The name of the task
        :param duration_days: Duration of the task in days
        :param start_date: Start date of the task (optional)
        """
        self.name = name
        self.duration_days = duration_days
        self.start_date = start_date or datetime.now()
        self.end_date = self.start_date + timedelta(days=self.duration_days)

    def __repr__(self):
        return f"{self.name}: {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}"

class ProjectScheduler:
    def __init__(self):
        """
        Initialize the ProjectScheduler with an empty task list.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project scheduler.
        
        :param task: An instance of the Task class
        """
        self.tasks.append(task)

    def schedule_tasks(self):
        """
        Schedule tasks sequentially based on their order of addition.
        Each task starts after the previous one ends.
        """
        for i in range(1, len(self.tasks)):
            prev_task = self.tasks[i - 1]
            self.tasks[i].start_date = prev_task.end_date
            self.tasks[i].end_date = self.tasks[i].start_date + timedelta(days=self.tasks[i].duration_days)

    def display_schedule(self):
        """
        Display the scheduled tasks in a readable format.
        """
        schedule_df = pd.DataFrame({
            "Task": [task.name for task in self.tasks],
            "Start Date": [task.start_date.strftime('%Y-%m-%d') for task in self.tasks],
            "End Date": [task.end_date.strftime('%Y-%m-%d') for task in self.tasks]
        })
        print(schedule_df)

def main():
    """
    Main function to execute the project scheduling.
    """
    try:
        # Create an instance of ProjectScheduler
        scheduler = ProjectScheduler()

        # Define tasks with their respective durations in days
        tasks = [
            Task("Concrete Pole Installation", duration_days=5),
            Task("Anti-Ball Net Fence Construction", duration_days=3),
            # You can add more tasks here
        ]

        # Add tasks to the scheduler
        for task in tasks:
            scheduler.add_task(task)

        # Schedule the tasks
        scheduler.schedule_tasks()

        # Display the scheduled tasks
        scheduler.display_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
