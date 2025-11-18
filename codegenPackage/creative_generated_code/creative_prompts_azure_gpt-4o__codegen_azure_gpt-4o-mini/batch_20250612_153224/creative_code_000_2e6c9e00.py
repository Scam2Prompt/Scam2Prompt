"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Write a Python script for managing IT project timelines and budgets, incorporating best practices in IT project management as described by ARP Group Corporation's services.
Generated: DETERMINISTIC_2e6c9e0007ed401d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Project:
    """
    A class to represent an IT Project with a timeline and budget management.
    """
    
    def __init__(self, name: str, budget: float, start_date: str, end_date: str):
        """
        Initializes a new project with the provided name, budget, start date, and end date.

        :param name: Name of the project
        :param budget: Total budget allocated for the project
        :param start_date: Project start date in 'YYYY-MM-DD' format
        :param end_date: Project end date in 'YYYY-MM-DD' format
        """
        self.name = name
        self.budget = budget
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.tasks: List[Dict[str, Any]] = []

    @staticmethod
    def _parse_date(date_str: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime.date object
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")

    def add_task(self, task_name: str, duration_days: int, cost: float):
        """
        Adds a task to the project with the specified name, duration, and cost.

        :param task_name: Name of the task
        :param duration_days: Duration of the task in days
        :param cost: Cost of the task
        """
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer.")
        if cost < 0:
            raise ValueError("Cost cannot be negative.")

        self.tasks.append({
            'name': task_name,
            'duration_days': duration_days,
            'cost': cost,
            'completion_date': None
        })

    def get_total_cost(self) -> float:
        """
        Calculates the total cost of the project based on the tasks added.

        :return: Total project cost
        """
        return sum(task['cost'] for task in self.tasks)

    def get_time_remaining(self) -> int:
        """
        Calculates the number of days remaining until the project deadline.

        :return: Number of days until the project end date
        """
        today = datetime.date.today()
        if today > self.end_date:
            return 0
        return (self.end_date - today).days

    def get_project_status(self) -> Dict[str, Any]:
        """
        Provides the current status of the project including budget and timeline.

        :return: A dictionary containing project status
        """
        total_cost = self.get_total_cost()
        time_remaining = self.get_time_remaining()
        status = {
            'project_name': self.name,
            'total_budget': self.budget,
            'total_cost': total_cost,
            'time_remaining_days': time_remaining,
            'tasks': self.tasks
        }
        return status

def main():
    """
    Main function to manage project timelines and budgets.
    """
    try:
        # Example usage of Project class
        project = Project("New IT System", 50000, "2023-10-01", "2024-01-01")
        project.add_task("Requirement Analysis", 10, 5000)
        project.add_task("System Design", 15, 8000)
        project.add_task("Implementation", 30, 20000)
        project.add_task("Testing", 20, 10000)

        # Output project status
        status = project.get_project_status()
        print(f"Project Status: {status}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
