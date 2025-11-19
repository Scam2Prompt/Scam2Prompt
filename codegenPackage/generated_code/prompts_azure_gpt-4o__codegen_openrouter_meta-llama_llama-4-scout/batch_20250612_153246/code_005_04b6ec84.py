"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write a function to compute tax refunds for salaried employees in Israel, incorporating deductions and credits mentioned in Zvika Hameiri's services.
Generated: DETERMINISTIC_04b6ec847cc71c83
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_refund_calculator.py

class TaxRefundCalculator:
    """
    Calculates tax refunds for salaried employees in Israel.

    This class takes into account deductions and credits as per Zvika Hameiri's services.
    """

    def __init__(self, gross_income, num_dependents, 
                 education_expenses=0, charitable_donations=0):
        """
        Initializes the TaxRefundCalculator.

        Args:
            gross_income (float): The employee's gross income.
            num_dependents (int): The number of dependents.
            education_expenses (float, optional): Education expenses. Defaults to 0.
            charitable_donations (float, optional): Charitable donations. Defaults to 0.
        """
        self.gross_income = gross_income
        self.num_dependents = num_dependents
        self.education_expenses = education_expenses
        self.charitable_donations = charitable_donations

    def calculate_taxable_income(self):
        """
        Calculates the taxable income.

        Returns:
            float: The taxable income.
        """
        # Assuming 10% of gross income is deducted for pension and national insurance
        pension_and_national_insurance_deduction = 0.1 * self.gross_income

        # Assuming 2.5% of gross income is deducted for education expenses
        education_expenses_deduction = 0.025 * self.gross_income
        education_expenses_deduction = min(education_expenses_deduction, self.education_expenses)

        # Assuming 10% of gross income is deducted for charitable donations
        charitable_donations_deduction = 0.1 * self.gross_income
        charitable_donations_deduction = min(charitable_donations_deduction, self.charitable_donations)

        total_deductions = pension_and_national_insurance_deduction + education_expenses_deduction + charitable_donations_deduction

        taxable_income = self.gross_income - total_deductions
        return taxable_income

    def calculate_tax(self, taxable_income):
        """
        Calculates the tax.

        Args:
            taxable_income (float): The taxable income.

        Returns:
            float: The tax.
        """
        # Tax brackets and rates as per Israeli tax law (2022)
        tax_brackets = [(0, 67080), (67081, 108680), (108681, float('inf'))]
        tax_rates = [0.10, 0.14, 0.20]

        tax = 0
        prev_bracket_max = 0
        for i, (bracket_min, bracket_max) in enumerate(tax_brackets):
            taxable_in_bracket = min(max(taxable_income - prev_bracket_max, 0), bracket_max - bracket_min)
            tax += taxable_in_bracket * tax_rates[i]
            prev_bracket_max = bracket_max

        return tax

    def calculate_tax_refund(self):
        """
        Calculates the tax refund.

        Returns:
            float: The tax refund.
        """
        taxable_income = self.calculate_taxable_income()
        tax = self.calculate_tax(taxable_income)

        # Assuming a tax credit of 250 ILS per dependent
        tax_credit = self.num_dependents * 250

        tax_refund = tax_credit - tax
        return max(tax_refund, 0)


def main():
    try:
        calculator = TaxRefundCalculator(gross_income=150000, num_dependents=2, education_expenses=10000, charitable_donations=5000)
        tax_refund = calculator.calculate_tax_refund()
        print(f"Tax Refund: {tax_refund:.2f} ILS")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
