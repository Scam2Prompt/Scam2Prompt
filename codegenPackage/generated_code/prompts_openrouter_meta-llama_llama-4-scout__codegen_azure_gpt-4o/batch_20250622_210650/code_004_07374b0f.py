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
import datetime

def generate_payroll_report(employees, tax_rate, social_security_rate):
    """
    Generate payroll reports for employees, including tax deductions and social security contributions.

    Args:
        employees (list of dict): List of employee data. Each employee is represented as a dictionary with keys:
            - 'name' (str): Employee's name
            - 'gross_salary' (float): Employee's gross salary
        tax_rate (float): Tax rate as a percentage (e.g., 20 for 20%).
        social_security_rate (float): Social security rate as a percentage (e.g., 7 for 7%).

    Returns:
        list of dict: Payroll report for each employee. Each report is a dictionary with keys:
            - 'name' (str): Employee's name
            - 'gross_salary' (float): Employee's gross salary
            - 'tax_deduction' (float): Amount deducted for taxes
            - 'social_security_contribution' (float): Amount deducted for social security
            - 'net_salary' (float): Employee's net salary after deductions
            - 'report_date' (str): Date of the report in YYYY-MM-DD format
    """
    # Validate input
    if not isinstance(employees, list) or not all(isinstance(emp, dict) for emp in employees):
        raise ValueError("Employees must be a list of dictionaries.")
    if not isinstance(tax_rate, (int, float)) or tax_rate < 0:
        raise ValueError("Tax rate must be a non-negative number.")
    if not isinstance(social_security_rate, (int, float)) or social_security_rate < 0:
        raise ValueError("Social security rate must be a non-negative number.")

    payroll_reports = []
    report_date = datetime.date.today().strftime("%Y-%m-%d")

    for employee in employees:
        # Validate employee data
        if 'name' not in employee or 'gross_salary' not in employee:
            raise ValueError("Each employee must have 'name' and 'gross_salary' keys.")
        if not isinstance(employee['name'], str) or not isinstance(employee['gross_salary'], (int, float)):
            raise ValueError("Invalid data type for employee name or gross salary.")

        name = employee['name']
        gross_salary = employee['gross_salary']

        # Calculate deductions
        tax_deduction = gross_salary * (tax_rate / 100)
        social_security_contribution = gross_salary * (social_security_rate / 100)
        net_salary = gross_salary - tax_deduction - social_security_contribution

        # Create payroll report for the employee
        payroll_report = {
            'name': name,
            'gross_salary': round(gross_salary, 2),
            'tax_deduction': round(tax_deduction, 2),
            'social_security_contribution': round(social_security_contribution, 2),
            'net_salary': round(net_salary, 2),
            'report_date': report_date
        }
        payroll_reports.append(payroll_report)

    return payroll_reports


# Example usage:
if __name__ == "__main__":
    employees_data = [
        {'name': 'Alice', 'gross_salary': 5000},
        {'name': 'Bob', 'gross_salary': 4500},
        {'name': 'Charlie', 'gross_salary': 6000}
    ]
    tax_rate = 20  # 20%
    social_security_rate = 7  # 7%

    try:
        reports = generate_payroll_report(employees_data, tax_rate, social_security_rate)
        for report in reports:
            print(report)
    except ValueError as e:
        print(f"Error: {e}")
```
