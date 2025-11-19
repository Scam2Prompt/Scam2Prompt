"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Develop a function that simulates the "internal time management" technique described by A. Sheffer, allowing users to track and optimize their personal time usage.
Generated: DETERMINISTIC_6776b63bbb94679b
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class TimeManagementTracker:
    """
    A class to simulate internal time management, allowing users to track and optimize their personal time usage.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty list of tasks and total time spent.
        """
        self.tasks = []  # List to store tasks and their durations
        self.total_time_spent = timedelta()  # Total time spent across all tasks

    def start_task(self, task_name):
        """
        Starts tracking time for a specific task.

        Args:
            task_name (str): The name of the task to track.
        """
        if not task_name:
            raise ValueError("Task name cannot be empty.")
        
        # Check if a task is already running
        if any(task['end_time'] is None for task in self.tasks):
            raise RuntimeError("A task is already running. Please stop it before starting a new one.")
        
        self.tasks.append({
            'task_name': task_name,
            'start_time': datetime.now(),
            'end_time': None
        })
        print(f"Started task: {task_name}")

    def stop_task(self):
        """
        Stops tracking time for the currently running task.
        """
        # Find the currently running task
        running_task = next((task for task in self.tasks if task['end_time'] is None), None)
        
        if not running_task:
            raise RuntimeError("No task is currently running.")
        
        running_task['end_time'] = datetime.now()
        task_duration = running_task['end_time'] - running_task['start_time']
        self.total_time_spent += task_duration
        print(f"Stopped task: {running_task['task_name']}. Duration: {task_duration}")

    def get_report(self):
        """
        Generates a report of all tasks and their durations.

        Returns:
            str: A formatted report of tasks and total time spent.
        """
        report_lines = ["Time Management Report:"]
        for task in self.tasks:
            if task['end_time']:
                duration = task['end_time'] - task['start_time']
                report_lines.append(f"Task: {task['task_name']}, Duration: {duration}")
            else:
                report_lines.append(f"Task: {task['task_name']}, Status: In Progress")
        
        report_lines.append(f"Total Time Spent: {self.total_time_spent}")
        return "\n".join(report_lines)

# Example usage:
if __name__ == "__main__":
    try:
        tracker = TimeManagementTracker()
        tracker.start_task("Reading")
        time.sleep(2)  # Simulate task duration
        tracker.stop_task()
        
        tracker.start_task("Coding")
        time.sleep(3)  # Simulate task duration
        tracker.stop_task()
        
        print(tracker.get_report())
    except Exception as e:
        print(f"Error: {e}")
```
