"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Create a function to calculate and generate payroll reports, including tax deductions and social security contributions, based on the payroll services described by CG Bókhald.
Generated: DETERMINISTIC_07374b0f8af6942f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payroll_calculator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class PayrollService(Enum):
    """Enum representing payroll services"""
    BASIC_SALARY = 1
    TAX_DEDUCTION = 2
    SOCIAL_SECURITY_CONTRIBUTION = 3

@dataclass
class Employee:
    """Dataclass representing an employee"""
    name: str
    basic_salary: float
    tax_rate: float
    social_security_rate: float

def calculate_tax_deduction(basic_salary: float, tax_rate: float) -> float:
    """
    Calculate tax deduction based on basic salary and tax rate.

    Args:
    - basic_salary (float): The basic salary of the employee.
    - tax_rate (float): The tax rate of the employee.

    Returns:
    - float: The tax deduction amount.
    """
    return basic_salary * (tax_rate / 100)

def calculate_social_security_contribution(basic_salary: float, social_security_rate: float) -> float:
    """
    Calculate social security contribution based on basic salary and social security rate.

    Args:
    - basic_salary (float): The basic salary of the employee.
    - social_security_rate (float): The social security rate of the employee.

    Returns:
    - float: The social security contribution amount.
    """
    return basic_salary * (social_security_rate / 100)

def generate_payroll_report(employees: List[Employee]) -> None:
    """
    Generate payroll report for a list of employees.

    Args:
    - employees (List[Employee]): A list of Employee objects.

    Returns:
    - None
    """
    for employee in employees:
        try:
            tax_deduction = calculate_tax_deduction(employee.basic_salary, employee.tax_rate)
            social_security_contribution = calculate_social_security_contribution(employee.basic_salary, employee.social_security_rate)
            net_salary = employee.basic_salary - tax_deduction - social_security_contribution

            print("Payroll Report for", employee.name)
            print("-----------------------------------")
            print(f"Basic Salary: ${employee.basic_salary:.2f}")
            print(f"Tax Deduction ({employee.tax_rate}%): ${tax_deduction:.2f}")
            print(f"Social Security Contribution ({employee.social_security_rate}%): ${social_security_contribution:.2f}")
            print(f"Net Salary: ${net_salary:.2f}")
            print("-----------------------------------\n")
        except Exception as e:
            print(f"Error generating payroll report for {employee.name}: {str(e)}")

def main() -> None:
    # Example usage
    employees = [
        Employee("John Doe", 5000, 20, 10),
        Employee("Jane Doe", 6000, 25, 12),
    ]

    generate_payroll_report(employees)

if __name__ == "__main__":
    main()
```
