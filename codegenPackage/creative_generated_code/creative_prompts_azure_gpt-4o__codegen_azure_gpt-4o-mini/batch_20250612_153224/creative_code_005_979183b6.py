"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Develop a payroll system for school staff, including pay slip generation and salary calculations, inspired by Him Saral's Payroll module.
Generated: DETERMINISTIC_979183b682e8791d
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
from typing import List, Dict

class Employee:
    """Represents an employee in the payroll system."""
    
    def __init__(self, employee_id: int, name: str, position: str, base_salary: float):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        """Calculates the total salary of the employee."""
        return self.base_salary

class PayrollSystem:
    """Handles payroll operations for employees."""
    
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Adds a new employee to the payroll system."""
        self.employees.append(employee)

    def generate_pay_slip(self, employee_id: int) -> Dict[str, str]:
        """Generates a pay slip for a specific employee."""
        employee = self.find_employee(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found.")

        salary = employee.calculate_salary()
        current_date = datetime.date.today()

        pay_slip = {
            "Employee ID": employee.employee_id,
            "Name": employee.name,
            "Position": employee.position,
            "Base Salary": f"${salary:.2f}",
            "Date": current_date.strftime("%Y-%m-%d")
        }
        return pay_slip

    def find_employee(self, employee_id: int) -> Employee:
        """Finds an employee by their ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def get_all_pay_slips(self) -> List[Dict[str, str]]:
        """Generates pay slips for all employees."""
        return [self.generate_pay_slip(emp.employee_id) for emp in self.employees]

# Example usage
if __name__ == "__main__":
    payroll_system = PayrollSystem()
    
    # Adding employees to the payroll system
    payroll_system.add_employee(Employee(1, "John Doe", "Teacher", 5000.00))
    payroll_system.add_employee(Employee(2, "Jane Smith", "Administrator", 6000.00))

    # Generating and printing pay slips
    try:
        for pay_slip in payroll_system.get_all_pay_slips():
            print(pay_slip)
    except ValueError as e:
        print(e)
```
