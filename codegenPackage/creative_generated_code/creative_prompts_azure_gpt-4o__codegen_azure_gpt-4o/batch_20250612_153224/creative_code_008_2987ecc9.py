"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Write code to implement a reporting system for tracking the efficiency of administrative processes in public institutions, inspired by Licitare's "Gestão de Processos e Procedimentos Administrativos."
Generated: DETERMINISTIC_2987ecc95ac613bf
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
Reporting System for Tracking the Efficiency of Administrative Processes in Public Institutions

This code implements a reporting system inspired by the concept of tracking administrative processes and procedures.
It includes functionality for creating, updating, and generating efficiency reports for processes and tasks.

Requirements: Python 3.x
"""

import json
import datetime


class AdministrativeProcess:
    """
    Represents an administrative process with associated tasks and efficiency tracking.
    """

    def __init__(self, process_id, name, description):
        """
        Initializes a new administrative process.

        :param process_id: Unique identifier for the process
        :param name: Name of the process
        :param description: Description of the process
        """
        self.process_id = process_id
        self.name = name
        self.description = description
        self.tasks = []
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def add_task(self, task):
        """
        Adds a task to the process.

        :param task: Task object to be added
        """
        self.tasks.append(task)
        self.updated_at = datetime.datetime.now()

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the process based on task completion times.

        :return: Efficiency percentage (0-100)
        """
        if not self.tasks:
            return 0  # No tasks, efficiency is zero

        total_time_estimated = sum(task.estimated_hours for task in self.tasks)
        total_time_actual = sum(task.actual_hours for task in self.tasks if task.completed)

        if total_time_estimated == 0:
            return 100  # Avoid division by zero

        efficiency = (total_time_actual / total_time_estimated) * 100
        return round(efficiency, 2)

    def generate_report(self):
        """
        Generates a report for the process.

        :return: Dictionary with process details
        """
        report = {
            "Process ID": self.process_id,
            "Name": self.name,
            "Description": self.description,
            "Created At": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "Updated At": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "Efficiency": f"{self.calculate_efficiency()}%",
            "Tasks": [task.to_dict() for task in self.tasks],
        }
        return report


class Task:
    """
    Represents a task within an administrative process.
    """

    def __init__(self, task_id, description, estimated_hours):
        """
        Initializes a new task.

        :param task_id: Unique identifier for the task
        :param description: Description of the task
        :param estimated_hours: Estimated hours to complete the task
        """
        self.task_id = task_id
        self.description = description
        self.estimated_hours = estimated_hours
        self.actual_hours = 0
        self.completed = False

    def mark_completed(self, actual_hours):
        """
        Marks the task as completed and records the actual hours spent.

        :param actual_hours: Actual hours spent on completing the task
        """
        if actual_hours < 0:
            raise ValueError("Actual hours cannot be negative.")
        self.completed = True
        self.actual_hours = actual_hours

    def to_dict(self):
        """
        Converts the task object to a dictionary.

        :return: Dictionary representation of the task
        """
        return {
            "Task ID": self.task_id,
            "Description": self.description,
            "Estimated Hours": self.estimated_hours,
            "Actual Hours": self.actual_hours,
            "Completed": self.completed,
        }


def main():
    """
    Main function demonstrating the reporting system.
    """
    try:
        # Create a new administrative process
        process = AdministrativeProcess(
            process_id="P001", name="Public Record Management", description="Managing public records efficiently."
        )

        # Add tasks to the process
        task1 = Task(task_id="T001", description="Digitize public records", estimated_hours=10)
        task2 = Task(task_id="T002", description="Archive old records", estimated_hours=5)

        process.add_task(task1)
        process.add_task(task2)

        # Simulate task completion
        task1.mark_completed(actual_hours=8)
        task2.mark_completed(actual_hours=6)

        # Generate efficiency report
        report = process.generate_report()

        # Print the report in JSON format for better readability
        print(json.dumps(report, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
