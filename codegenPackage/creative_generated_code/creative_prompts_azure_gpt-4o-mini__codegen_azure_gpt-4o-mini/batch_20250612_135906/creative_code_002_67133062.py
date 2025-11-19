"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerh.com
Prompt: Provide an example of how to implement the calculation options available in Balance RH's remuneration software for effective salary management.
Generated: DETERMINISTIC_6713306200b9cc94
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SalaryCalculator:
    """
    A class to represent a salary calculator for managing employee remuneration.
    """

    def __init__(self, base_salary, bonus=0, deductions=0):
        """
        Initializes the SalaryCalculator with base salary, bonus, and deductions.

        :param base_salary: The base salary of the employee
        :param bonus: Additional bonus added to the salary (default is 0)
        :param deductions: Deductions from the salary (default is 0)
        """
        if base_salary < 0:
            raise ValueError("Base salary cannot be negative.")
        if bonus < 0:
            raise ValueError("Bonus cannot be negative.")
        if deductions < 0:
            raise ValueError("Deductions cannot be negative.")

        self.base_salary = base_salary
        self.bonus = bonus
        self.deductions = deductions

    def calculate_gross_salary(self):
        """
        Calculate the gross salary, which is base salary plus bonus.

        :return: Gross salary value
        """
        gross_salary = self.base_salary + self.bonus
        return gross_salary

    def calculate_net_salary(self):
        """
        Calculate the net salary, which is gross salary minus deductions.

        :return: Net salary value
        """
        gross_salary = self.calculate_gross_salary()
        net_salary = gross_salary - self.deductions
        return net_salary

    def display_salary_details(self):
        """
        Display the salary details including base salary, bonus, deductions,
        gross salary, and net salary.
        """
        try:
            gross_salary = self.calculate_gross_salary()
            net_salary = self.calculate_net_salary()
            print(f"Base Salary: ${self.base_salary:.2f}")
            print(f"Bonus: ${self.bonus:.2f}")
            print(f"Deductions: ${self.deductions:.2f}")
            print(f"Gross Salary: ${gross_salary:.2f}")
            print(f"Net Salary: ${net_salary:.2f}")
        except Exception as e:
            print(f"An error occurred while displaying salary details: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Creating an instance of SalaryCalculator with example values
        salary_calculator = SalaryCalculator(base_salary=50000, bonus=5000, deductions=2000)
        salary_calculator.display_salary_details()
    except ValueError as e:
        print(f"Invalid input: {e}")
```
