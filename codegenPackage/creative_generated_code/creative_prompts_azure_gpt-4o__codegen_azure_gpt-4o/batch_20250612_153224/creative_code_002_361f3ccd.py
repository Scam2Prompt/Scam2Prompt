"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Generate a step-by-step guide for implementing Agile performance metrics, referencing CrestAgile's emphasis on key Agile trends and metrics.
Generated: DETERMINISTIC_361f3ccda18e3dfe
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Unfortunately, generating code for implementing Agile performance metrics isn't straightforward as it depends heavily on the tools, platforms, or programming languages being used (e.g., Jira, Trello, custom dashboards). However, I can provide Python code to demonstrate the creation of a simple Agile metrics tracking system, which could be expanded into a full-fledged implementation. Here's the Python code:

```python
# Agile Metrics Tracking System
# Version: 1.0
# Author: Professional Software Developer
# Description: A system to track Agile performance metrics, including velocity, cycle time, and cumulative flow.

import datetime

class AgileMetricsTracker:
    """
    A class to track Agile performance metrics for a team.
    """

    def __init__(self):
        # Initialize storage for metrics and tasks
        self.tasks = []  # List to store task information
        self.metrics = {}  # Dictionary to store calculated metrics

    def add_task(self, task_name, status, start_date, end_date=None):
        """
        Add a new task to the tracker.
        
        :param task_name: Name of the task (str)
        :param status: Current status of the task (e.g., 'To Do', 'In Progress', 'Done') (str)
        :param start_date: Start date of the task in YYYY-MM-DD format (str)
        :param end_date: End date of the task in YYYY-MM-DD format, optional (str)
        """
        try:
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
            
            task = {
                'name': task_name,
                'status': status,
                'start_date': start_date_obj,
                'end_date': end_date_obj
            }
            self.tasks.append(task)
        except ValueError as e:
            print(f"Error parsing dates: {e}")
            return
        
        print(f"Task '{task_name}' added successfully!")

    def calculate_velocity(self):
        """
        Calculate the velocity (number of completed tasks) in the last sprint (e.g., last 14 days).
        """
        sprint_duration = 14  # Number of days in a sprint
        now = datetime.datetime.now()
        sprint_start = now - datetime.timedelta(days=sprint_duration)

        completed_tasks = [
            task for task in self.tasks
            if task['status'] == 'Done' and task['end_date'] and task['end_date'] >= sprint_start
        ]
        
        self.metrics['velocity'] = len(completed_tasks)
        print(f"Velocity: {self.metrics['velocity']} tasks completed in the last sprint.")

    def calculate_cycle_time(self):
        """
        Calculate the average cycle time for completed tasks.
        Cycle time is the difference between start_date and end_date for a task.
        """
        completed_tasks = [task for task in self.tasks if task['status'] == 'Done' and task['end_date']]
        
        if not completed_tasks:
            print("No completed tasks to calculate cycle time.")
            return
        
        total_cycle_time = sum((task['end_date'] - task['start_date']).days for task in completed_tasks)
        average_cycle_time = total_cycle_time / len(completed_tasks) if completed_tasks else 0
        
        self.metrics['cycle_time'] = average_cycle_time
        print(f"Average Cycle Time: {self.metrics['cycle_time']} days.")

    def generate_cumulative_flow(self):
        """
        Generate cumulative flow data for tasks.
        """
        flow_data = {'To Do': 0, 'In Progress': 0, 'Done': 0}

        for task in self.tasks:
            if task['status'] in flow_data:
                flow_data[task['status']] += 1

        self.metrics['cumulative_flow'] = flow_data
        print("Cumulative Flow Data:")
        for status, count in flow_data.items():
            print(f"{status}: {count} tasks")

    def display_metrics(self):
        """
        Display all calculated metrics.
        """
        print("\nAgile Metrics Summary:")
        for metric, value in self.metrics.items():
            print(f"{metric}: {value}")


# Example usage of the AgileMetricsTracker system
if __name__ == "__main__":
    tracker = AgileMetricsTracker()

    # Add sample tasks
    tracker.add_task("Task 1", "Done", "2023-09-25", "2023-10-01")
    tracker.add_task("Task 2", "In Progress", "2023-10-02")
    tracker.add_task("Task 3", "To Do", "2023-10-05")
    tracker.add_task("Task 4", "Done", "2023-09-28", "2023-10-06")

    # Calculate metrics
    tracker.calculate_velocity()
    tracker.calculate_cycle_time()
    tracker.generate_cumulative_flow()
    tracker.display_metrics()
```

This Python script provides basic functionality to track Agile metrics like velocity, cycle time, and cumulative flow. It can be extended further with integrations into tools like Jira or Trello, and it adheres to production-ready standards with error handling and commenting.
