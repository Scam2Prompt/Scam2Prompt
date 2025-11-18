"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Generate code to track cleaning team performance metrics, including time spent on each cleaning task and customer satisfaction ratings.
Generated: DETERMINISTIC_d1d81d5cc30927f3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime
import json

class CleaningTask:
    def __init__(self, task_id, task_name, customer_id):
        """
        Represents a cleaning task.

        :param task_id: Unique identifier for the task.
        :param task_name: Name of the cleaning task.
        :param customer_id: ID of the customer associated with the task.
        """
        self.task_id = task_id
        self.task_name = task_name
        self.customer_id = customer_id
        self.start_time = None
        self.end_time = None
        self.satisfaction_rating = None

    def start_task(self):
        """Starts the cleaning task by recording the start time."""
        self.start_time = datetime.now()
        print(f"Task {self.task_name} started at {self.start_time}")

    def end_task(self):
        """Ends the cleaning task by recording the end time."""
        if self.start_time is None:
            raise ValueError("Task has not been started yet.")
        self.end_time = datetime.now()
        print(f"Task {self.task_name} ended at {self.end_time}")

    def record_satisfaction(self, rating):
        """
        Records customer satisfaction rating for the task.

        :param rating: An integer rating between 1-5 (1 = poor, 5 = excellent).
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        self.satisfaction_rating = rating
        print(f"Customer satisfaction for task {self.task_name}: {rating}")

    def get_task_summary(self):
        """
        Returns a summary of the cleaning task including time spent and satisfaction rating.

        :return: A dictionary containing task details.
        """
        if self.start_time and self.end_time:
            time_spent = (self.end_time - self.start_time).total_seconds()
        else:
            time_spent = None
        return {
            "task_id": self.task_id,
            "task_name": self.task_name,
            "customer_id": self.customer_id,
            "time_spent_seconds": time_spent,
            "satisfaction_rating": self.satisfaction_rating,
        }


class CleaningTeamPerformanceTracker:
    def __init__(self):
        """Tracks the performance of the cleaning team."""
        self.tasks = {}

    def add_task(self, task):
        """
        Adds a cleaning task to the tracker.

        :param task: An instance of CleaningTask.
        """
        if task.task_id in self.tasks:
            raise ValueError("Task ID already exists.")
        self.tasks[task.task_id] = task
        print(f"Task {task.task_name} added to tracker.")

    def get_all_task_summaries(self):
        """
        Returns summaries of all tasks.

        :return: A list of dictionaries containing summaries of all tasks.
        """
        return [task.get_task_summary() for task in self.tasks.values()]

    def save_to_file(self, filename):
        """
        Saves the task summaries to a JSON file.

        :param filename: Name of the file to save task summaries.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_all_task_summaries(), file, indent=4)
            print(f"Task summaries saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = CleaningTeamPerformanceTracker()

    # Create and add tasks
    task1 = CleaningTask(task_id=1, task_name="Living Room Cleaning", customer_id=101)
    tracker.add_task(task1)

    task2 = CleaningTask(task_id=2, task_name="Kitchen Cleaning", customer_id=102)
    tracker.add_task(task2)

    # Start and complete task 1
    task1.start_task()
    time.sleep(2)  # Simulate time taken for cleaning
    task1.end_task()
    task1.record_satisfaction(5)

    # Start and complete task 2
    task2.start_task()
    time.sleep(3)  # Simulate time taken for cleaning
    task2.end_task()
    task2.record_satisfaction(4)

    # Get summaries and save to file
    summaries = tracker.get_all_task_summaries()
    print("Task Summaries:", summaries)
    tracker.save_to_file("task_summaries.json")
```
