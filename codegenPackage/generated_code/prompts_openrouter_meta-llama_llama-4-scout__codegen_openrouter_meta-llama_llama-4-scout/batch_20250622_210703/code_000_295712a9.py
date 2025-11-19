"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write a Python script to manage housekeeping services, including scheduling and employee assignment, for a facility management company like Ashvi Facility Management Services.
Generated: DETERMINISTIC_295712a98c063808
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# housekeeping_services.py

from datetime import datetime, timedelta
from typing import Dict, List

class Employee:
    """Represents a housekeeping employee."""

    def __init__(self, employee_id: int, name: str):
        """
        Initializes an Employee object.

        Args:
        - employee_id (int): Unique employee ID.
        - name (str): Employee name.
        """
        self.employee_id = employee_id
        self.name = name
        self.tasks = []

    def assign_task(self, task: str):
        """Assigns a task to the employee."""
        self.tasks.append(task)


class Task:
    """Represents a housekeeping task."""

    def __init__(self, task_id: int, description: str, scheduled_time: datetime):
        """
        Initializes a Task object.

        Args:
        - task_id (int): Unique task ID.
        - description (str): Task description.
        - scheduled_time (datetime): Scheduled time for the task.
        """
        self.task_id = task_id
        self.description = description
        self.scheduled_time = scheduled_time
        self.assigned_employee = None

    def assign_employee(self, employee: Employee):
        """Assigns an employee to the task."""
        self.assigned_employee = employee
        employee.assign_task(f"Task {self.task_id}: {self.description}")


class HousekeepingService:
    """Manages housekeeping services, including scheduling and employee assignment."""

    def __init__(self):
        self.employees: Dict[int, Employee] = {}
        self.tasks: Dict[int, Task] = {}
        self.task_id_counter = 1
        self.employee_id_counter = 1

    def add_employee(self, name: str) -> Employee:
        """
        Adds a new employee.

        Args:
        - name (str): Employee name.

        Returns:
        - Employee: The newly added employee.
        """
        employee = Employee(self.employee_id_counter, name)
        self.employees[self.employee_id_counter] = employee
        self.employee_id_counter += 1
        return employee

    def schedule_task(self, description: str, scheduled_time: datetime) -> Task:
        """
        Schedules a new task.

        Args:
        - description (str): Task description.
        - scheduled_time (datetime): Scheduled time for the task.

        Returns:
        - Task: The newly scheduled task.
        """
        task = Task(self.task_id_counter, description, scheduled_time)
        self.tasks[self.task_id_counter] = task
        self.task_id_counter += 1
        return task

    def assign_task_to_employee(self, task_id: int, employee_id: int):
        """
        Assigns a task to an employee.

        Args:
        - task_id (int): ID of the task to assign.
        - employee_id (int): ID of the employee to assign to.

        Raises:
        - ValueError: If the task or employee does not exist.
        """
        task = self.tasks.get(task_id)
        employee = self.employees.get(employee_id)
        if task is None:
            raise ValueError(f"Task {task_id} does not exist")
        if employee is None:
            raise ValueError(f"Employee {employee_id} does not exist")
        task.assign_employee(employee)

    def print_schedule(self):
        """Prints the schedule of tasks and assigned employees."""
        for task in self.tasks.values():
            if task.assigned_employee:
                print(f"Task {task.task_id}: {task.description} at {task.scheduled_time} assigned to {task.assigned_employee.name}")
            else:
                print(f"Task {task.task_id}: {task.description} at {task.scheduled_time} - Not assigned")


def main():
    housekeeping_service = HousekeepingService()

    # Add employees
    employee1 = housekeeping_service.add_employee("John Doe")
    employee2 = housekeeping_service.add_employee("Jane Smith")

    # Schedule tasks
    task1 = housekeeping_service.schedule_task("Clean room 101", datetime.now() + timedelta(days=1))
    task2 = housekeeping_service.schedule_task("Clean room 202", datetime.now() + timedelta(days=2))

    # Assign tasks to employees
    housekeeping_service.assign_task_to_employee(task1.task_id, employee1.employee_id)
    housekeeping_service.assign_task_to_employee(task2.task_id, employee2.employee_id)

    # Print schedule
    housekeeping_service.print_schedule()


if __name__ == "__main__":
    main()
```
