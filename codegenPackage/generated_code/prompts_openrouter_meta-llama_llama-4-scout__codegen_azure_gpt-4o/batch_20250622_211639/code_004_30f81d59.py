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
# Import necessary modules
import datetime

# Define custom exceptions for error handling
class InvalidInputError(Exception):
    pass

class EmployeeNotFoundError(Exception):
    pass

# Base class for all employees
class Employee:
    def __init__(self, employee_id, name, role, salary_scale):
        """
        Initialize an Employee object.

        :param employee_id: Unique ID for the employee
        :param name: Name of the employee
        :param role: Role of the employee (e.g., Teacher, Admin)
        :param salary_scale: Salary scale of the employee
        """
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary_scale = salary_scale
        self.leave_balance = 30  # Default annual leave balance
        self.performance_score = None  # Performance score (to be updated later)

    def apply_leave(self, days):
        """
        Apply for leave.

        :param days: Number of leave days requested
        :raises InvalidInputError: If requested days exceed leave balance
        """
        if days <= 0:
            raise InvalidInputError("Leave days must be greater than zero.")
        if days > self.leave_balance:
            raise InvalidInputError("Insufficient leave balance.")
        self.leave_balance -= days
        return f"Leave approved for {days} days. Remaining balance: {self.leave_balance} days."

    def update_performance(self, score):
        """
        Update performance score.

        :param score: Performance score (0-100)
        :raises InvalidInputError: If score is not within the valid range
        """
        if not (0 <= score <= 100):
            raise InvalidInputError("Performance score must be between 0 and 100.")
        self.performance_score = score
        return f"Performance score updated to {score}."

    def __str__(self):
        """
        String representation of the Employee object.
        """
        return f"ID: {self.employee_id}, Name: {self.name}, Role: {self.role}, Salary Scale: {self.salary_scale}, Leave Balance: {self.leave_balance}, Performance Score: {self.performance_score}"

# Class to manage the school system
class SchoolSystem:
    def __init__(self):
        """
        Initialize the SchoolSystem object.
        """
        self.employees = {}  # Dictionary to store employees by their ID

    def add_employee(self, employee):
        """
        Add a new employee to the system.

        :param employee: Employee object
        :raises InvalidInputError: If employee ID already exists
        """
        if employee.employee_id in self.employees:
            raise InvalidInputError("Employee ID already exists.")
        self.employees[employee.employee_id] = employee
        return f"Employee {employee.name} added successfully."

    def remove_employee(self, employee_id):
        """
        Remove an employee from the system.

        :param employee_id: ID of the employee to be removed
        :raises EmployeeNotFoundError: If employee ID does not exist
        """
        if employee_id not in self.employees:
            raise EmployeeNotFoundError("Employee not found.")
        removed_employee = self.employees.pop(employee_id)
        return f"Employee {removed_employee.name} removed successfully."

    def get_employee(self, employee_id):
        """
        Retrieve employee details.

        :param employee_id: ID of the employee
        :raises EmployeeNotFoundError: If employee ID does not exist
        """
        if employee_id not in self.employees:
            raise EmployeeNotFoundError("Employee not found.")
        return self.employees[employee_id]

    def update_salary_scale(self, employee_id, new_scale):
        """
        Update the salary scale of an employee.

        :param employee_id: ID of the employee
        :param new_scale: New salary scale
        :raises EmployeeNotFoundError: If employee ID does not exist
        """
        if employee_id not in self.employees:
            raise EmployeeNotFoundError("Employee not found.")
        self.employees[employee_id].salary_scale = new_scale
        return f"Salary scale updated to {new_scale} for employee {self.employees[employee_id].name}."

    def __str__(self):
        """
        String representation of the SchoolSystem object.
        """
        return "\n".join(str(employee) for employee in self.employees.values())

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the school system
        school = SchoolSystem()

        # Add employees
        teacher = Employee(employee_id=1, name="Mr. Rahman", role="Teacher", salary_scale="Grade 5")
        admin = Employee(employee_id=2, name="Ms. Akter", role="Admin", salary_scale="Grade 3")
        school.add_employee(teacher)
        school.add_employee(admin)

        # Update performance score
        teacher.update_performance(85)

        # Apply leave
        admin.apply_leave(5)

        # Update salary scale
        school.update_salary_scale(employee_id=1, new_scale="Grade 6")

        # Print all employees
        print(school)

    except Exception as e:
        print(f"Error: {e}")
```
