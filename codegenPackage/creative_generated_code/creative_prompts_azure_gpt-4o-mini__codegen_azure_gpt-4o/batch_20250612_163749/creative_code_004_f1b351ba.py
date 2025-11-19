"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: What are the key features of the Perfect Payrolls service that ensure compliance with UK payroll legislation, and how can I implement them in my payroll system?
Generated: DETERMINISTIC_f1b351ba09e8a11c
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for implementing key features in a payroll system to ensure compliance with UK payroll legislation:

```python
import datetime

class PayrollSystem:
    """
    A payroll system to ensure compliance with UK payroll legislation.
    """

    def __init__(self):
        """
        Initializes the payroll system with empty employee records.
        """
        self.employees = []

    def add_employee(self, name, ni_number, tax_code, salary):
        """
        Adds an employee to the payroll system.

        Args:
            name (str): Employee's full name.
            ni_number (str): National Insurance number (must be valid format).
            tax_code (str): Tax code (e.g., 1257L for standard UK tax codes).
            salary (float): Annual salary in GBP.
        """
        if not self._validate_ni_number(ni_number):
            raise ValueError("Invalid National Insurance number format.")
        if not self._validate_tax_code(tax_code):
            raise ValueError("Invalid tax code format.")
        if salary < 0:
            raise ValueError("Salary must be a positive number.")

        employee = {
            'name': name,
            'ni_number': ni_number,
            'tax_code': tax_code,
            'salary': salary,
            'pay_date': None,  # Latest pay date will be stored here
        }
        self.employees.append(employee)

    def calculate_payroll(self):
        """
        Calculates payroll for all employees based on their annual salary.

        Returns:
            list: A list of dictionaries containing employee pay information.
        """
        payroll = []
        for employee in self.employees:
            monthly_salary = round(employee['salary'] / 12, 2)  # Divide annual salary by months
            tax_deductions = self._calculate_tax(monthly_salary, employee['tax_code'])
            ni_contributions = self._calculate_ni_contribution(monthly_salary)
            net_salary = monthly_salary - tax_deductions - ni_contributions

            payroll.append({
                'name': employee['name'],
                'monthly_salary': monthly_salary,
                'tax_deductions': tax_deductions,
                'ni_contributions': ni_contributions,
                'net_salary': round(net_salary, 2),
            })
        return payroll

    def pay_employees(self):
        """
        Pays all employees and updates their pay date.

        Returns:
            str: Confirmation message of payroll processing.
        """
        today = datetime.date.today()
        payroll_data = self.calculate_payroll()
        for idx, employee in enumerate(self.employees):
            # Update employee's latest pay date
            employee['pay_date'] = today
            print(f"Paid {employee['name']} - Net Salary: £{payroll_data[idx]['net_salary']}")
        return "Payroll processing completed."

    def _validate_ni_number(self, ni_number):
        """
        Validates the format of the National Insurance (NI) number.

        Args:
            ni_number (str): NI number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # NI number format: Prefix (2 letters) + digits (6 numbers) + suffix (1 letter)
        import re
        pattern = r"^[A-Z]{2}[0-9]{6}[A-Z]$"
        return bool(re.match(pattern, ni_number))

    def _validate_tax_code(self, tax_code):
        """
        Validates the format of the tax code.

        Args:
            tax_code (str): Tax code to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Standard tax code format (e.g., 1257L or similar)
        import re
        pattern = r"^[0-9]{4}[L]$"
        return bool(re.match(pattern, tax_code))

    def _calculate_tax(self, monthly_salary, tax_code):
        """
        Calculates income tax based on the employee's tax code.

        Args:
            monthly_salary (float): Monthly salary.
            tax_code (str): Tax code.

        Returns:
            float: Estimated tax deductions.
        """
        # Example: Tax-free allowance from tax code (1257 => £12570 annual allowance)
        tax_free_allowance = int(tax_code[:-1]) * 10
        taxable_income = max(monthly_salary * 12 - tax_free_allowance, 0) / 12  # Monthly taxable income
        
        # Example tax bands (simplified for demonstration):
        basic_rate_tax = 0.2  # 20% for earnings up to £50k annually
        higher_rate_tax = 0.4  # 40% for earnings above £50k annually

        if taxable_income <= 4166.67:  # £50k annually / 12 months
            return round(taxable_income * basic_rate_tax, 2)
        else:
            basic_tax = 4166.67 * basic_rate_tax
            higher_tax = (taxable_income - 4166.67) * higher_rate_tax
            return round(basic_tax + higher_tax, 2)

    def _calculate_ni_contribution(self, monthly_salary):
        """
        Calculates National Insurance contributions based on monthly salary.

        Args:
            monthly_salary (float): Monthly salary.

        Returns:
            float: Estimated NI contributions.
        """
        # Example NI thresholds (simplified for demonstration):
        primary_threshold = 1048  # Monthly earnings threshold
        upper_threshold = 4189  # Monthly upper earnings threshold

        ni_rate_lower = 0.12  # 12% for earnings above primary threshold
        ni_rate_upper = 0.02  # 2% for earnings above upper threshold

        if monthly_salary <= primary_threshold:
            return 0.0
        elif monthly_salary <= upper_threshold:
            return round((monthly_salary - primary_threshold) * ni_rate_lower, 2)
        else:
            lower_ni = (upper_threshold - primary_threshold) * ni_rate_lower
            upper_ni = (monthly_salary - upper_threshold) * ni_rate_upper
            return round(lower_ni + upper_ni, 2)

# Example Usage:
if __name__ == "__main__":
    payroll_system = PayrollSystem()

    try:
        payroll_system.add_employee("John Doe", "AB123456C", "1257L", 30000)
        payroll_system.add_employee("Jane Smith", "CD987654A", "1257L", 60000)

        print(payroll_system.pay_employees())
    except ValueError as e:
        print(f"Error: {e}")
```

This code implements a scalable payroll system with key features like tax calculation, NI contributions, and validation of UK-specific formats for National Insurance numbers and tax codes.
