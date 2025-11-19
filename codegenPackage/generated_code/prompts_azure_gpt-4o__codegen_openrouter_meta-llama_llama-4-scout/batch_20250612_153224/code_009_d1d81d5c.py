"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate code to track cleaning team performance metrics, including time spent on each cleaning task and customer satisfaction ratings.
Generated: DETERMINISTIC_d1d81d5cc30927f3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_team_performance_tracker.py

from datetime import datetime
from typing import Dict, List

class CleaningTask:
    """Represents a cleaning task with its details."""

    def __init__(self, task_id: int, task_name: str, time_spent: float, satisfaction_rating: float):
        """
        Initializes a CleaningTask object.

        Args:
        - task_id (int): Unique identifier for the task.
        - task_name (str): Name of the cleaning task.
        - time_spent (float): Time spent on the task in hours.
        - satisfaction_rating (float): Customer satisfaction rating (out of 5).
        """
        self.task_id = task_id
        self.task_name = task_name
        self.time_spent = time_spent
        self.satisfaction_rating = satisfaction_rating

class CleaningTeamPerformanceTracker:
    """Tracks cleaning team performance metrics."""

    def __init__(self):
        """Initializes a CleaningTeamPerformanceTracker object."""
        self.tasks: Dict[int, CleaningTask] = {}
        self.total_time_spent: float = 0.0
        self.total_satisfaction_rating: float = 0.0
        self.task_count: int = 0

    def add_task(self, task: CleaningTask):
        """
        Adds a cleaning task to the tracker.

        Args:
        - task (CleaningTask): The task to add.
        """
        self.tasks[task.task_id] = task
        self.total_time_spent += task.time_spent
        self.total_satisfaction_rating += task.satisfaction_rating
        self.task_count += 1

    def get_task(self, task_id: int) -> CleaningTask:
        """
        Retrieves a cleaning task by its ID.

        Args:
        - task_id (int): The ID of the task to retrieve.

        Returns:
        - CleaningTask: The task with the given ID, or None if not found.
        """
        return self.tasks.get(task_id)

    def get_average_time_spent(self) -> float:
        """
        Calculates the average time spent on tasks.

        Returns:
        - float: The average time spent in hours.
        """
        if self.task_count == 0:
            return 0.0
        return self.total_time_spent / self.task_count

    def get_average_satisfaction_rating(self) -> float:
        """
        Calculates the average customer satisfaction rating.

        Returns:
        - float: The average satisfaction rating (out of 5).
        """
        if self.task_count == 0:
            return 0.0
        return self.total_satisfaction_rating / self.task_count

    def generate_performance_report(self) -> str:
        """
        Generates a performance report.

        Returns:
        - str: A formatted report with performance metrics.
        """
        report = "Cleaning Team Performance Report\n"
        report += "--------------------------------\n"
        report += f"Task Count: {self.task_count}\n"
        report += f"Total Time Spent: {self.total_time_spent:.2f} hours\n"
        report += f"Average Time Spent: {self.get_average_time_spent():.2f} hours\n"
        report += f"Total Satisfaction Rating: {self.total_satisfaction_rating:.2f}/5\n"
        report += f"Average Satisfaction Rating: {self.get_average_satisfaction_rating():.2f}/5\n"
        report += "--------------------------------\n"
        report += "Task Details:\n"
        for task in self.tasks.values():
            report += f"Task ID: {task.task_id}, Task Name: {task.task_name}, Time Spent: {task.time_spent:.2f} hours, Satisfaction Rating: {task.satisfaction_rating}/5\n"
        return report

def main():
    try:
        tracker = CleaningTeamPerformanceTracker()

        # Example tasks
        task1 = CleaningTask(1, "Room Cleaning", 2.5, 4.5)
        task2 = CleaningTask(2, "Bathroom Cleaning", 1.8, 4.8)
        task3 = CleaningTask(3, "Kitchen Cleaning", 3.2, 4.2)

        # Add tasks to the tracker
        tracker.add_task(task1)
        tracker.add_task(task2)
        tracker.add_task(task3)

        # Generate and print performance report
        report = tracker.generate_performance_report()
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
