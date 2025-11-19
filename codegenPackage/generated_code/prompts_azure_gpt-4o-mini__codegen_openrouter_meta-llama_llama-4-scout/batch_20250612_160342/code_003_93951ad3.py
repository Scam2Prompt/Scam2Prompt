"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Draft a comprehensive work summary report that aligns with the practical examples available on 账云范文网.
Generated: DETERMINISTIC_93951ad3888e133b
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WorkSummaryReport:
    def __init__(self, title, date, tasks):
        """
        Initialize a WorkSummaryReport object.

        Args:
            title (str): The title of the report.
            date (str): The date of the report in YYYY-MM-DD format.
            tasks (list): A list of tasks completed, where each task is a dictionary containing 'task_name', 'start_time', 'end_time', and 'description'.
        """
        self.title = title
        self.date = date
        self.tasks = tasks

    def calculate_total_time(self):
        """
        Calculate the total time spent on all tasks.

        Returns:
            int: The total time spent in minutes.
        """
        total_minutes = 0
        for task in self.tasks:
            start_time = datetime.datetime.strptime(task['start_time'], '%H:%M')
            end_time = datetime.datetime.strptime(task['end_time'], '%H:%M')
            task_duration = (end_time - start_time).total_seconds() / 60
            total_minutes += task_duration
        return total_minutes

    def generate_report(self):
        """
        Generate a comprehensive work summary report.

        Returns:
            str: The report as a string.
        """
        report = f"# {self.title} - {self.date}\n\n"
        report += "## Tasks Completed\n\n"
        for i, task in enumerate(self.tasks, start=1):
            report += f"### Task {i}: {task['task_name']}\n"
            report += f"**Start Time:** {task['start_time']}\n"
            report += f"**End Time:** {task['end_time']}\n"
            report += f"**Description:** {task['description']}\n\n"
        report += f"## Total Time Spent: {self.calculate_total_time()} minutes\n\n"
        return report

def main():
    try:
        title = "Daily Work Summary"
        date = datetime.date.today().strftime('%Y-%m-%d')
        tasks = [
            {
                'task_name': 'Task 1',
                'start_time': '09:00',
                'end_time': '10:30',
                'description': 'Completed task 1'
            },
            {
                'task_name': 'Task 2',
                'start_time': '10:45',
                'end_time': '12:00',
                'description': 'Completed task 2'
            }
        ]
        report = WorkSummaryReport(title, date, tasks)
        logging.info(report.generate_report())
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
