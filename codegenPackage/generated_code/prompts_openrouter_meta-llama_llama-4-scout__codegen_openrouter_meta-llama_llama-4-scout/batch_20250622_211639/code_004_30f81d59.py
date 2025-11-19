"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Develop a system to manage teacher and employee data, including features for leave management, salary scales, and performance evaluation, tailored to the needs of a Bangladeshi secondary school.
Generated: DETERMINISTIC_30f81d59cbf0593e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from datetime import datetime
from enum import Enum
from typing import List

class Designation(Enum):
    """Employee Designation"""
    TEACHER = "Teacher"
    PRINCIPAL = "Principal"
    ADMINISTRATIVE_STAFF = "Administrative Staff"

class LeaveType(Enum):
    """Leave Type"""
    ANNUAL_LEAVE = "Annual Leave"
    CASUAL_LEAVE = "Casual Leave"
    SICK_LEAVE = "Sick Leave"

class Employee:
    """Employee Model"""

    def __init__(self, employee_id: int, name: str, designation: Designation, join_date: datetime):
        """
        Initialize Employee

        Args:
        - employee_id (int): Unique employee ID
        - name (str): Employee name
        - designation (Designation): Employee designation
        - join_date (datetime): Employee join date
        """
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.join_date = join_date
        self.leaves = []
        self.salary_scale = None
        self.performance_evaluations = []

    def add_leave(self, leave_type: LeaveType, start_date: datetime, end_date: datetime):
        """
        Add leave

        Args:
        - leave_type (LeaveType): Leave type
        - start_date (datetime): Leave start date
        - end_date (datetime): Leave end date
        """
        self.leaves.append({"leave_type": leave_type, "start_date": start_date, "end_date": end_date})

    def set_salary_scale(self, salary: float):
        """
        Set salary scale

        Args:
        - salary (float): Salary amount
        """
        self.salary_scale = salary

    def add_performance_evaluation(self, evaluation_date: datetime, rating: int, comments: str):
        """
        Add performance evaluation

        Args:
        - evaluation_date (datetime): Evaluation date
        - rating (int): Performance rating (1-5)
        - comments (str): Evaluation comments
        """
        self.performance_evaluations.append({"evaluation_date": evaluation_date, "rating": rating, "comments": comments})

class Teacher(Employee):
    """Teacher Model"""

    def __init__(self, employee_id: int, name: str, designation: Designation, join_date: datetime, subject: str):
        """
        Initialize Teacher

        Args:
        - employee_id (int): Unique employee ID
        - name (str): Teacher name
        - designation (Designation): Teacher designation
        - join_date (datetime): Teacher join date
        - subject (str): Teacher subject
        """
        super().__init__(employee_id, name, designation, join_date)
        self.subject = subject

class School:
    """School Model"""

    def __init__(self, name: str):
        """
        Initialize School

        Args:
        - name (str): School name
        """
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        """
        Add employee

        Args:
        - employee (Employee): Employee object
        """
        self.employees.append(employee)

    def get_employee(self, employee_id: int) -> Employee:
        """
        Get employee by ID

        Args:
        - employee_id (int): Employee ID

        Returns:
        - Employee: Employee object or None
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

def main():
    school = School("Bangladesh Secondary School")

    teacher1 = Teacher(1, "John Doe", Designation.TEACHER, datetime(2020, 1, 1), "Mathematics")
    teacher1.set_salary_scale(50000.0)
    teacher1.add_leave(LeaveType.ANNUAL_LEAVE, datetime(2022, 1, 1), datetime(2022, 1, 10))
    teacher1.add_performance_evaluation(datetime(2022, 6, 1), 4, "Good performance")

    school.add_employee(teacher1)

    employee = school.get_employee(1)
    if employee:
        print(f"Name: {employee.name}")
        print(f"Designation: {employee.designation.value}")
        print(f"Salary Scale: {employee.salary_scale}")
        print("Leaves:")
        for leave in employee.leaves:
            print(f"- {leave['leave_type'].value}: {leave['start_date']} to {leave['end_date']}")
        print("Performance Evaluations:")
        for evaluation in employee.performance_evaluations:
            print(f"- {evaluation['evaluation_date']}: {evaluation['rating']}/5 - {evaluation['comments']}")
    else:
        print("Employee not found")

if __name__ == "__main__":
    main()
```
