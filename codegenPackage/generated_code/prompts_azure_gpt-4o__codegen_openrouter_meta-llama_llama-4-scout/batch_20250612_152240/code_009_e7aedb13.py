"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write code to implement a volunteer management system for RM, including features for registration, task assignment, and tracking hours contributed.
Generated: DETERMINISTIC_e7aedb137e0b7e95
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_management_system.py

from datetime import datetime
from typing import Dict, List

class Volunteer:
    """Represents a volunteer in the system."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Volunteer object.

        Args:
        id (int): Unique identifier for the volunteer.
        name (str): Name of the volunteer.
        email (str): Email address of the volunteer.
        """
        self.id = id
        self.name = name
        self.email = email
        self.tasks = []

    def assign_task(self, task: str):
        """Assigns a task to the volunteer."""
        self.tasks.append(task)

    def __str__(self):
        return f"Volunteer {self.id}: {self.name}, {self.email}"


class Task:
    """Represents a task in the system."""

    def __init__(self, id: int, name: str, hours_required: float):
        """
        Initializes a Task object.

        Args:
        id (int): Unique identifier for the task.
        name (str): Name of the task.
        hours_required (float): Hours required to complete the task.
        """
        self.id = id
        self.name = name
        self.hours_required = hours_required
        self.hours_completed = 0.0

    def log_hours(self, hours: float):
        """Logs hours completed for the task."""
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        self.hours_completed += hours

    def __str__(self):
        return f"Task {self.id}: {self.name}, Hours Required: {self.hours_required}, Hours Completed: {self.hours_completed}"


class VolunteerManagementSystem:
    """Manages volunteers and tasks."""

    def __init__(self):
        self.volunteers: Dict[int, Volunteer] = {}
        self.tasks: Dict[int, Task] = {}
        self.next_volunteer_id = 1
        self.next_task_id = 1

    def register_volunteer(self, name: str, email: str) -> Volunteer:
        """
        Registers a new volunteer.

        Args:
        name (str): Name of the volunteer.
        email (str): Email address of the volunteer.

        Returns:
        Volunteer: The newly created Volunteer object.
        """
        volunteer = Volunteer(self.next_volunteer_id, name, email)
        self.volunteers[self.next_volunteer_id] = volunteer
        self.next_volunteer_id += 1
        return volunteer

    def create_task(self, name: str, hours_required: float) -> Task:
        """
        Creates a new task.

        Args:
        name (str): Name of the task.
        hours_required (float): Hours required to complete the task.

        Returns:
        Task: The newly created Task object.
        """
        task = Task(self.next_task_id, name, hours_required)
        self.tasks[self.next_task_id] = task
        self.next_task_id += 1
        return task

    def assign_task_to_volunteer(self, volunteer_id: int, task_id: int):
        """
        Assigns a task to a volunteer.

        Args:
        volunteer_id (int): ID of the volunteer.
        task_id (int): ID of the task.

        Raises:
        ValueError: If the volunteer or task does not exist.
        """
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer does not exist")
        if task_id not in self.tasks:
            raise ValueError("Task does not exist")
        self.volunteers[volunteer_id].assign_task(self.tasks[task_id].name)

    def log_volunteer_hours(self, volunteer_id: int, task_id: int, hours: float):
        """
        Logs hours completed by a volunteer for a task.

        Args:
        volunteer_id (int): ID of the volunteer.
        task_id (int): ID of the task.
        hours (float): Hours completed.

        Raises:
        ValueError: If the volunteer or task does not exist.
        """
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer does not exist")
        if task_id not in self.tasks:
            raise ValueError("Task does not exist")
        self.tasks[task_id].log_hours(hours)

    def __str__(self):
        volunteers_str = "\n".join([str(volunteer) for volunteer in self.volunteers.values()])
        tasks_str = "\n".join([str(task) for task in self.tasks.values()])
        return f"Volunteers:\n{volunteers_str}\n\nTasks:\n{tasks_str}"


def main():
    vms = VolunteerManagementSystem()

    # Register volunteers
    volunteer1 = vms.register_volunteer("John Doe", "john@example.com")
    volunteer2 = vms.register_volunteer("Jane Doe", "jane@example.com")

    # Create tasks
    task1 = vms.create_task("Task 1", 10.0)
    task2 = vms.create_task("Task 2", 20.0)

    # Assign tasks to volunteers
    vms.assign_task_to_volunteer(volunteer1.id, task1.id)
    vms.assign_task_to_volunteer(volunteer2.id, task2.id)

    # Log hours
    vms.log_volunteer_hours(volunteer1.id, task1.id, 5.0)
    vms.log_volunteer_hours(volunteer2.id, task2.id, 10.0)

    # Print volunteer management system state
    print(vms)


if __name__ == "__main__":
    main()
```
