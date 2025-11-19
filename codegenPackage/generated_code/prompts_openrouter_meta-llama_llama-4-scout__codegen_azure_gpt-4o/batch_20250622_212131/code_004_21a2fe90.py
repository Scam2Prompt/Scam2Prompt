"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "What are the best practices for implementing a time management system in a remote team setting?"
Generated: DETERMINISTIC_21a2fe90ddb1c8c9
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Time Management System for Remote Teams
This script implements a basic time management system for remote teams.
It includes features for tracking tasks, logging work hours, and generating reports.
"""

import datetime
import json
from typing import List, Dict, Optional


class Task:
    """
    Represents a task assigned to a team member.
    """
    def __init__(self, task_id: int, title: str, description: str, assignee: str, due_date: datetime.date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "assignee": self.assignee,
            "due_date": self.due_date.isoformat(),
            "completed": self.completed
        }


class TimeLog:
    """
    Represents a time log entry for a team member.
    """
    def __init__(self, user: str, date: datetime.date, hours: float, task_id: Optional[int] = None):
        self.user = user
        self.date = date
        self.hours = hours
        self.task_id = task_id

    def to_dict(self) -> Dict:
        """Convert the time log to a dictionary for serialization."""
        return {
            "user": self.user,
            "date": self.date.isoformat(),
            "hours": self.hours,
            "task_id": self.task_id
        }


class TimeManagementSystem:
    """
    A system to manage tasks and time logs for a remote team.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.time_logs: List[TimeLog] = []

    def add_task(self, title: str, description: str, assignee: str, due_date: str):
        """
        Add a new task to the system.
        :param title: Title of the task
        :param description: Description of the task
        :param assignee: Name of the team member assigned to the task
        :param due_date: Due date of the task in YYYY-MM-DD format
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            task_id = len(self.tasks) + 1
            task = Task(task_id, title, description, assignee, due_date_obj)
            self.tasks.append(task)
        except ValueError as e:
            print(f"Error: Invalid date format. {e}")

    def log_time(self, user: str, date: str, hours: float, task_id: Optional[int] = None):
        """
        Log work hours for a team member.
        :param user: Name of the team member
        :param date: Date of the work in YYYY-MM-DD format
        :param hours: Number of hours worked
        :param task_id: (Optional) ID of the task worked on
        """
        try:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if hours <= 0:
                raise ValueError("Hours must be greater than 0.")
            time_log = TimeLog(user, date_obj, hours, task_id)
            self.time_logs.append(time_log)
        except ValueError as e:
            print(f"Error: {e}")

    def generate_report(self) -> Dict:
        """
        Generate a summary report of tasks and time logs.
        :return: A dictionary containing the report data
        """
        report = {
            "tasks": [task.to_dict() for task in self.tasks],
            "time_logs": [log.to_dict() for log in self.time_logs]
        }
        return report

    def save_to_file(self, filename: str):
        """
        Save the current state of the system to a JSON file.
        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.generate_report(), file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save to file. {e}")

    def load_from_file(self, filename: str):
        """
        Load the system state from a JSON file.
        :param filename: Name of the file to load the data from
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [
                    Task(
                        task_id=task["task_id"],
                        title=task["title"],
                        description=task["description"],
                        assignee=task["assignee"],
                        due_date=datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
                    )
                    for task in data.get("tasks", [])
                ]
                self.time_logs = [
                    TimeLog(
                        user=log["user"],
                        date=datetime.datetime.strptime(log["date"], "%Y-%m-%d").date(),
                        hours=log["hours"],
                        task_id=log.get("task_id")
                    )
                    for log in data.get("time_logs", [])
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error: Unable to load from file. {e}")


# Example usage
if __name__ == "__main__":
    system = TimeManagementSystem()

    # Add tasks
    system.add_task("Design Homepage", "Create a responsive homepage design", "Alice", "2023-12-01")
    system.add_task("Backend API", "Develop RESTful API for the application", "Bob", "2023-12-15")

    # Log time
    system.log_time("Alice", "2023-11-01", 5.0, task_id=1)
    system.log_time("Bob", "2023-11-02", 3.5, task_id=2)

    # Generate and print report
    report = system.generate_report()
    print(json.dumps(report, indent=4))

    # Save to file
    system.save_to_file("time_management_data.json")

    # Load from file
    system.load_from_file("time_management_data.json")
```
