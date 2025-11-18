"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Write Python code to calculate quarterly tax payments for an independent business owner, considering Israeli tax regulations as described by Zvika Hameiri's accounting services.
Generated: DETERMINISTIC_fda5eb7741dbaa52
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TaxCalculator:
    """
    A class to calculate quarterly tax payments for independent business owners in Israel.
    
    Attributes:
        income (float): The total income for the quarter.
        expenses (float): The total expenses for the quarter.
        tax_rate (float): The applicable tax rate as a decimal (e.g., 0.25 for 25%).
    """

    def __init__(self, income: float, expenses: float, tax_rate: float):
        """
        Initializes the TaxCalculator with income, expenses, and tax rate.

        Args:
            income (float): Total income for the quarter.
            expenses (float): Total expenses for the quarter.
            tax_rate (float): Applicable tax rate as a decimal.
        """
        if income < 0 or expenses < 0 or not (0 <= tax_rate <= 1):
            raise ValueError("Income and expenses must be non-negative and tax rate must be between 0 and 1.")
        
        self.income = income
        self.expenses = expenses
        self.tax_rate = tax_rate

    def calculate_taxable_income(self) -> float:
        """
        Calculates taxable income by subtracting expenses from income.

        Returns:
            float: Taxable income for the quarter.
        """
        return self.income - self.expenses

    def calculate_tax_payment(self) -> float:
        """
        Calculates the tax payment based on taxable income and tax rate.

        Returns:
            float: Tax payment for the quarter.
        """
        taxable_income = self.calculate_taxable_income()
        if taxable_income <= 0:
            return 0.0  # No tax due if the taxable income is zero or negative
        
        tax_payment = taxable_income * self.tax_rate
        return tax_payment

def main():
    """
    Main function to run the tax calculation process.
    """
    try:
        # Example values for income, expenses, and tax rate
        income = float(input("Enter total income for the quarter: "))
        expenses = float(input("Enter total expenses for the quarter: "))
        tax_rate = float(input("Enter tax rate (as a decimal, e.g., 0.25 for 25%): "))

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(income, expenses, tax_rate)

        # Calculate the tax payment
        tax_payment = tax_calculator.calculate_tax_payment()

        # Output the result
        print(f"Quarterly tax payment: {tax_payment:.2f} NIS")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
