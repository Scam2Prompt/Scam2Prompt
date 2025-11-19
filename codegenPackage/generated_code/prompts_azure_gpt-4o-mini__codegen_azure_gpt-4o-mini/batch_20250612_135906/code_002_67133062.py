"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Provide an example of how to implement the calculation options available in Balance RH's remuneration software for effective salary management.
Generated: DETERMINISTIC_6713306200b9cc94
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SalaryManager:
    """
    A class to manage salary calculations for employees.
    """

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, base_salary):
        """
        Adds a new employee to the salary management system.

        :param employee_id: Unique identifier for the employee
        :param base_salary: Base salary of the employee
        """
        if employee_id in self.employees:
            raise ValueError(f"Employee ID {employee_id} already exists.")
        if base_salary < 0:
            raise ValueError("Base salary must be a non-negative value.")
        
        self.employees[employee_id] = {
            'base_salary': base_salary,
            'bonuses': 0,
            'deductions': 0
        }

    def add_bonus(self, employee_id, bonus_amount):
        """
        Adds a bonus to an employee's salary.

        :param employee_id: Unique identifier for the employee
        :param bonus_amount: Amount of the bonus to be added
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        if bonus_amount < 0:
            raise ValueError("Bonus amount must be a non-negative value.")
        
        self.employees[employee_id]['bonuses'] += bonus_amount

    def add_deduction(self, employee_id, deduction_amount):
        """
        Adds a deduction to an employee's salary.

        :param employee_id: Unique identifier for the employee
        :param deduction_amount: Amount of the deduction to be applied
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        if deduction_amount < 0:
            raise ValueError("Deduction amount must be a non-negative value.")
        
        self.employees[employee_id]['deductions'] += deduction_amount

    def calculate_total_salary(self, employee_id):
        """
        Calculates the total salary for an employee, including bonuses and deductions.

        :param employee_id: Unique identifier for the employee
        :return: Total salary after applying bonuses and deductions
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        
        employee = self.employees[employee_id]
        total_salary = employee['base_salary'] + employee['bonuses'] - employee['deductions']
        return total_salary

    def get_employee_report(self, employee_id):
        """
        Generates a report for an employee's salary details.

        :param employee_id: Unique identifier for the employee
        :return: Dictionary containing employee salary details
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} does not exist.")
        
        employee = self.employees[employee_id]
        report = {
            'base_salary': employee['base_salary'],
            'bonuses': employee['bonuses'],
            'deductions': employee['deductions'],
            'total_salary': self.calculate_total_salary(employee_id)
        }
        return report


# Example usage
if __name__ == "__main__":
    salary_manager = SalaryManager()
    
    # Adding employees
    salary_manager.add_employee("E001", 50000)
    salary_manager.add_employee("E002", 60000)

    # Adding bonuses and deductions
    salary_manager.add_bonus("E001", 5000)
    salary_manager.add_deduction("E001", 2000)

    # Calculating total salary
    total_salary_e001 = salary_manager.calculate_total_salary("E001")
    print(f"Total Salary for E001: {total_salary_e001}")

    # Generating employee report
    report_e001 = salary_manager.get_employee_report("E001")
    print(f"Employee Report for E001: {report_e001}")
```
