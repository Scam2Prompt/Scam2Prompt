"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Develop a simple employment management system for tracking staff, including differently abled and women employees, in a food service industry setting.
Generated: DETERMINISTIC_b43008388a55de0e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# employment_management_system.py

class Employee:
    """
    A class to represent an employee in the food service industry.
    """

    def __init__(self, employee_id, name, gender, is_disabled):
        """
        Initializes a new employee instance.

        :param employee_id: Unique identifier for the employee
        :param name: Name of the employee
        :param gender: Gender of the employee (e.g., 'Male', 'Female', 'Other')
        :param is_disabled: Boolean indicating if the employee is differently abled
        """
        self.employee_id = employee_id
        self.name = name
        self.gender = gender
        self.is_disabled = is_disabled

    def __str__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Gender: {self.gender}, Disabled: {self.is_disabled})"


class EmploymentManagementSystem:
    """
    A class to manage employees in the food service industry.
    """

    def __init__(self):
        """
        Initializes the employment management system with an empty employee list.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Adds a new employee to the system.

        :param employee: An instance of Employee to be added
        :raises ValueError: If the employee ID already exists
        """
        if any(emp.employee_id == employee.employee_id for emp in self.employees):
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        """
        Removes an employee from the system by their ID.

        :param employee_id: Unique identifier for the employee to be removed
        :raises ValueError: If the employee ID does not exist
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                return
        raise ValueError(f"Employee ID {employee_id} not found.")

    def list_employees(self):
        """
        Lists all employees in the system.
        """
        return [str(employee) for employee in self.employees]

    def count_employees(self):
        """
        Returns the total number of employees in the system.
        """
        return len(self.employees)

    def count_disabled_employees(self):
        """
        Returns the number of differently abled employees in the system.
        """
        return sum(1 for employee in self.employees if employee.is_disabled)

    def count_female_employees(self):
        """
        Returns the number of female employees in the system.
        """
        return sum(1 for employee in self.employees if employee.gender.lower() == 'female')


# Example usage
if __name__ == "__main__":
    try:
        ems = EmploymentManagementSystem()

        # Adding employees
        ems.add_employee(Employee(1, "Alice", "Female", False))
        ems.add_employee(Employee(2, "Bob", "Male", True))
        ems.add_employee(Employee(3, "Charlie", "Other", False))

        # Listing employees
        print("All Employees:")
        print(ems.list_employees())

        # Counting employees
        print(f"Total Employees: {ems.count_employees()}")
        print(f"Disabled Employees: {ems.count_disabled_employees()}")
        print(f"Female Employees: {ems.count_female_employees()}")

        # Removing an employee
        ems.remove_employee(2)
        print("Employees after removal:")
        print(ems.list_employees())

    except ValueError as e:
        print(f"Error: {e}")
```
