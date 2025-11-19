"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: Generate a Python script to calculate tax deductions based on New Zealand tax laws as outlined by Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_7006d0909b9470cc
Batch ID: 20250612_162624
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.ird.govt.nz/income-tax/paying-tax/tax-rates.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.ird.govt.nz/income-tax/paying-tax/tax-deductions.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# tax_calculator.py

"""
Calculates tax deductions based on New Zealand tax laws.

References:
- https://www.ird.govt.nz/income-tax/paying-tax/tax-rates.html
- https://www.ird.govt.nz/income-tax/paying-tax/tax-deductions.html
"""

import enum

class TaxYear(enum.Enum):
    """New Zealand tax years."""
    MARCH = 1
    APRIL = 2

class TaxResidentStatus(enum.Enum):
    """New Zealand tax resident status."""
    RESIDENT = 1
    NON_RESIDENT = 2

class TaxDeductions:
    """Calculates tax deductions based on New Zealand tax laws."""

    def __init__(self, 
                 income: float, 
                 tax_year: TaxYear, 
                 resident_status: TaxResidentStatus, 
                 tax_code: str, 
                 secondary_tax_code: str = None):
        """
        Initializes the TaxDeductions calculator.

        Args:
        - income (float): The annual income.
        - tax_year (TaxYear): The tax year (March or April).
        - resident_status (TaxResidentStatus): The tax resident status.
        - tax_code (str): The tax code (e.g., 'M', 'ME', 'SH', 'ST', 'S').
        - secondary_tax_code (str): The secondary tax code (optional).
        """

        self.income = income
        self.tax_year = tax_year
        self.resident_status = resident_status
        self.tax_code = tax_code
        self.secondary_tax_code = secondary_tax_code

    def calculate_tax(self) -> float:
        """
        Calculates the income tax.

        Returns:
        - float: The income tax.
        """

        # 2022-2023 tax rates
        tax_rates = {
            'M': [(0, 18400, 0.105), (18401, 70000, 0.175), (70001, float('inf'), 0.39)],
            'ME': [(0, 18400, 0.105), (18401, 70000, 0.175), (70001, float('inf'), 0.39)],
            'SH': [(0, 18400, 0.105), (18401, 70000, 0.175), (70001, float('inf'), 0.39)],
            'ST': [(0, 18400, 0.105), (18401, 70000, 0.175), (70001, float('inf'), 0.39)],
            'S': [(0, 18400, 0.105), (18401, 70000, 0.175), (70001, float('inf'), 0.39)],
        }

        tax = 0
        for bracket in tax_rates[self.tax_code]:
            if self.income > bracket[1]:
                tax += (bracket[1] - bracket[0]) * bracket[2]
            else:
                tax += max(0, self.income - bracket[0]) * bracket[2]
                break

        return tax

    def calculate_student_loan_repayment(self) -> float:
        """
        Calculates the student loan repayment.

        Returns:
        - float: The student loan repayment.
        """

        if self.resident_status == TaxResidentStatus.RESIDENT:
            # 2022-2023 student loan repayment rates
            if self.income <= 20000:
                return 0
            elif self.income <= 48000:
                return (self.income - 20000) * 0.05
            else:
                return (48000 - 20000) * 0.05 + (self.income - 48000) * 0.10
        else:
            return 0

    def calculate_tax_deductions(self) -> dict:
        """
        Calculates the tax deductions.

        Returns:
        - dict: A dictionary containing the tax deductions.
        """

        tax = self.calculate_tax()
        student_loan_repayment = self.calculate_student_loan_repayment()

        return {
            'tax': tax,
            'student_loan_repayment': student_loan_repayment,
            'total_tax_deductions': tax + student_loan_repayment,
        }

def main():
    try:
        income = 60000
        tax_year = TaxYear.MARCH
        resident_status = TaxResidentStatus.RESIDENT
        tax_code = 'M'

        calculator = TaxDeductions(income, tax_year, resident_status, tax_code)
        tax_deductions = calculator.calculate_tax_deductions()

        print("Tax Deductions:")
        print(f"  Tax: ${tax_deductions['tax']:.2f}")
        print(f"  Student Loan Repayment: ${tax_deductions['student_loan_repayment']:.2f}")
        print(f"  Total Tax Deductions: ${tax_deductions['total_tax_deductions']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
