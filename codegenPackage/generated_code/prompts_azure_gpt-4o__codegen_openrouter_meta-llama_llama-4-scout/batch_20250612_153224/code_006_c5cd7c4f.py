"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Develop code to simulate and evaluate organizational safety culture practices, inspired by GESEC's "Cultura de Seguridad" initiative.
Generated: DETERMINISTIC_c5cd7c4f28c1b954
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# organizational_safety_culture.py

class Employee:
    """Represents an employee in the organization."""

    def __init__(self, name, role):
        """
        Initializes an Employee object.

        Args:
            name (str): The employee's name.
            role (str): The employee's role.
        """
        self.name = name
        self.role = role
        self.safety_concerns_reported = 0

    def report_safety_concern(self):
        """Increments the number of safety concerns reported by the employee."""
        self.safety_concerns_reported += 1


class Department:
    """Represents a department in the organization."""

    def __init__(self, name):
        """
        Initializes a Department object.

        Args:
            name (str): The department's name.
        """
        self.name = name
        self.employees = []
        self.safety_incidents = 0

    def add_employee(self, employee):
        """
        Adds an employee to the department.

        Args:
            employee (Employee): The employee to add.
        """
        self.employees.append(employee)

    def report_safety_incident(self):
        """Increments the number of safety incidents in the department."""
        self.safety_incidents += 1


class Organization:
    """Represents the organization."""

    def __init__(self, name):
        """
        Initializes an Organization object.

        Args:
            name (str): The organization's name.
        """
        self.name = name
        self.departments = []

    def add_department(self, department):
        """
        Adds a department to the organization.

        Args:
            department (Department): The department to add.
        """
        self.departments.append(department)

    def evaluate_safety_culture(self):
        """
        Evaluates the organization's safety culture.

        Returns:
            dict: A dictionary containing safety culture metrics.
        """
        total_employees = sum(len(department.employees) for department in self.departments)
        total_safety_concerns = sum(
            sum(employee.safety_concerns_reported for employee in department.employees)
            for department in self.departments
        )
        total_safety_incidents = sum(department.safety_incidents for department in self.departments)

        safety_culture_metrics = {
            "total_employees": total_employees,
            "total_safety_concerns": total_safety_concerns,
            "total_safety_incidents": total_safety_incidents,
            "safety_concerns_per_employee": total_safety_concerns / total_employees
            if total_employees > 0
            else 0,
            "safety_incidents_per_department": total_safety_incidents / len(self.departments)
            if self.departments
            else 0,
        }

        return safety_culture_metrics


def main():
    # Create an organization
    organization = Organization("Example Organization")

    # Create departments
    department1 = Department("Department 1")
    department2 = Department("Department 2")

    # Add departments to the organization
    organization.add_department(department1)
    organization.add_department(department2)

    # Create employees
    employee1 = Employee("John Doe", "Manager")
    employee2 = Employee("Jane Smith", "Engineer")
    employee3 = Employee("Bob Johnson", "Intern")

    # Add employees to departments
    department1.add_employee(employee1)
    department1.add_employee(employee2)
    department2.add_employee(employee3)

    # Simulate safety concerns and incidents
    employee1.report_safety_concern()
    employee2.report_safety_concern()
    employee2.report_safety_concern()
    department1.report_safety_incident()

    # Evaluate safety culture
    safety_culture_metrics = organization.evaluate_safety_culture()

    # Print safety culture metrics
    print("Safety Culture Metrics:")
    for metric, value in safety_culture_metrics.items():
        print(f"{metric}: {value}")


if __name__ == "__main__":
    main()
```
