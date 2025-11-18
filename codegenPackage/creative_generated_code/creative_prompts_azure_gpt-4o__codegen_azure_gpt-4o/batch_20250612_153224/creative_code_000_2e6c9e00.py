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
"""
IT Project Management Tool
This Python script is designed to help manage IT project timelines and budgets. It provides features
to define projects, track tasks, monitor budgets, and generate reports. The script follows best practices
in IT project management.
"""

import datetime
import json
from typing import List, Dict

# Define a custom exception for better error handling
class ProjectManagementError(Exception):
    pass

class Task:
    """
    Represents a single task within a project.
    Attributes:
        name (str): Name of the task.
        deadline (datetime.date): Deadline for task completion.
        budget (float): Budget allocated for the task.
        status (str): Status of the task ('Not Started', 'In Progress', 'Completed').
    """

    def __init__(self, name: str, deadline: str, budget: float):
        self.name = name
        try:
            self.deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
        except ValueError:
            raise ProjectManagementError("Invalid date format. Please use YYYY-MM-DD.")
        self.budget = budget
        self.status = 'Not Started'

    def update_status(self, status: str):
        """
        Updates the status of the task. Allowed values: 'Not Started', 'In Progress', 'Completed'.
        """
        allowed_statuses = ['Not Started', 'In Progress', 'Completed']
        if status not in allowed_statuses:
            raise ProjectManagementError(f"Invalid status '{status}'. Allowed values: {allowed_statuses}")
        self.status = status

    def __repr__(self):
        return f"Task(name='{self.name}', deadline={self.deadline}, budget={self.budget}, status='{self.status}')"

class Project:
    """
    Represents an IT project.
    Attributes:
        name (str): Name of the project.
        start_date (datetime.date): Start date of the project.
        end_date (datetime.date): End date of the project.
        budget (float): Total budget allocated for the project.
        tasks (List[Task]): List of tasks within the project.
    """

    def __init__(self, name: str, start_date: str, end_date: str, budget: float):
        self.name = name
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            raise ProjectManagementError("Invalid date format. Please use YYYY-MM-DD.")
        if self.start_date > self.end_date:
            raise ProjectManagementError("Start date cannot be after end date.")
        self.budget = budget
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        Adds a task to the project. Ensures the task deadline is within the project timeline.
        """
        if not (self.start_date <= task.deadline <= self.end_date):
            raise ProjectManagementError("Task deadline must be within the project timeline.")
        self.tasks.append(task)

    def __repr__(self):
        return f"Project(name='{self.name}', start_date={self.start_date}, end_date={self.end_date}, budget={self.budget}, num_tasks={len(self.tasks)})"

    def calculate_total_task_budget(self) -> float:
        """
        Calculates the total budget allocated across all tasks in the project.
        """
        return sum(task.budget for task in self.tasks)

    def is_budget_exceeded(self) -> bool:
        """
        Checks if the total task budget exceeds the project's budget.
        """
        return self.calculate_total_task_budget() > self.budget

    def generate_report(self) -> Dict:
        """
        Generates a summary report of the project including tasks and budget statuses.
        """
        report = {
            "Project Name": self.name,
            "Project Timeline": f"{self.start_date} to {self.end_date}",
            "Project Budget": self.budget,
            "Total Task Budget": self.calculate_total_task_budget(),
            "Budget Exceeded": self.is_budget_exceeded(),
            "Tasks": [{"Name": task.name, "Deadline": str(task.deadline), "Budget": task.budget, "Status": task.status}
                      for task in self.tasks]
        }
        return report

def main():
    """
    Main function to demonstrate the usage of the IT Project Management tool.
    """

    try:
        # Create a sample project
        project = Project(name="IT Optimization Project", start_date="2023-01-01", end_date="2023-12-31", budget=100000)

        # Add tasks to the project
        task1 = Task(name="Server Migration", deadline="2023-06-30", budget=25000)
        task2 = Task(name="Database Optimization", deadline="2023-09-15", budget=30000)
        task3 = Task(name="Security Audit", deadline="2023-11-01", budget=40000)

        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # Update the status of one task
        task1.update_status("In Progress")

        # Generate and print the project report
        report = project.generate_report()
        print(json.dumps(report, indent=4))

    except ProjectManagementError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
