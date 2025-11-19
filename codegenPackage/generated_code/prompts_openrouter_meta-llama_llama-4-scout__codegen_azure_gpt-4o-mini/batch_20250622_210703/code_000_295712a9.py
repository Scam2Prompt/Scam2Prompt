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
import datetime
from typing import List, Dict, Optional

class Employee:
    """Class to represent an employee in the housekeeping service."""
    
    def __init__(self, employee_id: int, name: str):
        self.employee_id = employee_id
        self.name = name
        self.schedule: Dict[datetime.date, List[str]] = {}

    def assign_task(self, date: datetime.date, task: str):
        """Assign a task to the employee on a specific date."""
        if date not in self.schedule:
            self.schedule[date] = []
        self.schedule[date].append(task)

    def get_schedule(self, date: Optional[datetime.date] = None) -> Dict[datetime.date, List[str]]:
        """Retrieve the schedule for the employee, or for a specific date if provided."""
        if date:
            return {date: self.schedule.get(date, [])}
        return self.schedule


class HousekeepingService:
    """Class to manage housekeeping services, including scheduling and employee assignment."""
    
    def __init__(self):
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, employee_id: int, name: str):
        """Add a new employee to the service."""
        if employee_id in self.employees:
            raise ValueError(f"Employee ID {employee_id} already exists.")
        self.employees[employee_id] = Employee(employee_id, name)

    def assign_task(self, employee_id: int, date: datetime.date, task: str):
        """Assign a task to an employee on a specific date."""
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        self.employees[employee_id].assign_task(date, task)

    def get_employee_schedule(self, employee_id: int, date: Optional[datetime.date] = None) -> Dict[datetime.date, List[str]]:
        """Get the schedule of a specific employee, or for a specific date if provided."""
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        return self.employees[employee_id].get_schedule(date)

    def list_employees(self) -> List[str]:
        """List all employees in the service."""
        return [f"{emp.employee_id}: {emp.name}" for emp in self.employees.values()]


def main():
    """Main function to demonstrate the functionality of the housekeeping service."""
    service = HousekeepingService()

    # Adding employees
    try:
        service.add_employee(1, "Alice Johnson")
        service.add_employee(2, "Bob Smith")
    except ValueError as e:
        print(e)

    # Assigning tasks
    try:
        service.assign_task(1, datetime.date(2023, 10, 15), "Clean conference room")
        service.assign_task(2, datetime.date(2023, 10, 15), "Restock supplies")
    except ValueError as e:
        print(e)

    # Retrieving schedules
    try:
        print("Alice's Schedule:", service.get_employee_schedule(1))
        print("Bob's Schedule for 2023-10-15:", service.get_employee_schedule(2, datetime.date(2023, 10, 15)))
    except ValueError as e:
        print(e)

    # Listing all employees
    print("Employees in the service:")
    for employee in service.list_employees():
        print(employee)


if __name__ == "__main__":
    main()
```
