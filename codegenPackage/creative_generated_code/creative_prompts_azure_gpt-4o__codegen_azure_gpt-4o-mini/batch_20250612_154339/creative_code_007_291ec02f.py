"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Develop a function to calculate legislative payroll deductions such as National Insurance contributions, maternity pay, and sick pay, adhering to UK statutory rules as managed by Perfect Payrolls.
Generated: DETERMINISTIC_291ec02f128ca43d
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PayrollDeductions:
    """
    A class to calculate legislative payroll deductions for employees in the UK.
    """

    def __init__(self, salary: float):
        """
        Initializes the PayrollDeductions class with the employee's salary.

        :param salary: Employee's gross salary before deductions
        """
        if salary < 0:
            raise ValueError("Salary must be a non-negative value.")

        self.salary = salary

    def calculate_national_insurance(self) -> float:
        """
        Calculates National Insurance contributions based on the salary.

        :return: The amount of National Insurance contribution
        """
        if self.salary <= 1040:
            return 0.0

        # Rates for National Insurance
        ni_threshold = 1040
        ni_rate = 0.12  # 12% on earnings above the threshold

        ni_contribution = (self.salary - ni_threshold) * ni_rate
        return ni_contribution

    def calculate_maternity_pay(self) -> float:
        """
        Calculates Statutory Maternity Pay (SMP).

        :return: The amount of Maternity Pay
        """
        if self.salary < 0:
            raise ValueError("Salary must be a non-negative value.")

        smp_rate = 0.9 * self.salary if self.salary < 1000 else 151.97
        return min(smp_rate, 600.0)  # capped at £600 for SMP calculation

    def calculate_sick_pay(self) -> float:
        """
        Calculates Statutory Sick Pay (SSP) based on the salary.

        :return: The amount of Sick Pay
        """
        if self.salary < 0:
            raise ValueError("Salary must be a non-negative value.")

        ssp_rate = 109.40  # Weekly SSP rate
        return ssp_rate  # Assuming the employee qualifies

    def calculate_total_deductions(self) -> float:
        """
        Calculates total legislative payroll deductions.

        :return: The total amount of deductions
        """
        ni = self.calculate_national_insurance()
        maternity = self.calculate_maternity_pay()
        sick_pay = self.calculate_sick_pay()

        total_deductions = ni + maternity + sick_pay
        return total_deductions

# Example usage
if __name__ == "__main__":
    try:
        salary = 2500.00  # Example salary input
        payroll = PayrollDeductions(salary)

        total_deductions = payroll.calculate_total_deductions()
        print(f"Total Payroll Deductions: £{total_deductions:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
