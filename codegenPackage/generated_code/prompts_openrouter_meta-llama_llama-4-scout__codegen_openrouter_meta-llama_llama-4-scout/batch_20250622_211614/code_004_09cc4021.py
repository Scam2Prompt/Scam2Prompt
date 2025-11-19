"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: "Write a code snippet to calculate statutory payments and deductions for employees in the UK using Perfect Payrolls' payroll processing rules."
Generated: DETERMINISTIC_09cc4021057fdd2c
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# statutory_payroll_calculations.py

from datetime import datetime
from enum import Enum
from typing import Dict

class EmployeeStatus(Enum):
    FULL_TIME = 1
    PART_TIME = 2

class PayrollCalculator:
    def __init__(self, 
                 gross_pay: float, 
                 employee_status: EmployeeStatus, 
                 is_apprentice: bool = False, 
                 has_student_loan: bool = False):
        """
        Initialize the PayrollCalculator.

        Args:
        - gross_pay (float): The employee's gross pay.
        - employee_status (EmployeeStatus): The employee's status (full-time or part-time).
        - is_apprentice (bool): Whether the employee is an apprentice. Defaults to False.
        - has_student_loan (bool): Whether the employee has a student loan. Defaults to False.
        """
        self.gross_pay = gross_pay
        self.employee_status = employee_status
        self.is_apprentice = is_apprentice
        self.has_student_loan = has_student_loan

    def calculate_national_insurance(self) -> float:
        """
        Calculate National Insurance Contributions (NICs).

        Returns:
        - float: The NICs amount.
        """
        # 2022-2023 NICs rates
        primary_class_1_rate = 0.12  # 12% on earnings between £166 and £962 per week
        primary_class_1_rate_above = 0.02  # 2% on earnings above £962 per week
        secondary_class_1_rate = 0.15  # 15.05% on earnings above £166 per week for employers

        if self.employee_status == EmployeeStatus.FULL_TIME:
            # Assume a full-time employee earns above £962 per week
            nic = (self.gross_pay * primary_class_1_rate) + ((self.gross_pay - 962) * primary_class_1_rate_above)
        else:
            # Assume a part-time employee earns below £962 per week
            nic = self.gross_pay * primary_class_1_rate

        return nic

    def calculate_pension_contribution(self) -> float:
        """
        Calculate pension contribution.

        Returns:
        - float: The pension contribution amount.
        """
        # Assuming 5% of gross pay for pension contribution
        pension_contribution_rate = 0.05
        return self.gross_pay * pension_contribution_rate

    def calculate_student_loan_repayment(self) -> float:
        """
        Calculate student loan repayment.

        Returns:
        - float: The student loan repayment amount.
        """
        # 2022-2023 student loan repayment rate
        student_loan_repayment_rate = 0.09  # 9% on earnings above £27,295 per year

        # Assume a monthly pay period
        monthly_gross_pay = self.gross_pay / 4  # Assuming 4 weeks in a month
        annual_gross_pay = monthly_gross_pay * 12

        if annual_gross_pay > 27295:
            student_loan_repayment = (annual_gross_pay - 27295) * student_loan_repayment_rate / 12
        else:
            student_loan_repayment = 0

        return student_loan_repayment

    def calculate_tax(self) -> float:
        """
        Calculate income tax.

        Returns:
        - float: The income tax amount.
        """
        # 2022-2023 income tax rates
        basic_rate = 0.20  # 20% on earnings between £12,571 and £50,270 per year
        higher_rate = 0.40  # 40% on earnings between £50,271 and £150,000 per year
        additional_rate = 0.45  # 45% on earnings above £150,000 per year

        # Assume a monthly pay period
        monthly_gross_pay = self.gross_pay / 4  # Assuming 4 weeks in a month
        annual_gross_pay = monthly_gross_pay * 12

        if annual_gross_pay <= 12571:
            tax = 0
        elif annual_gross_pay <= 50270:
            tax = (annual_gross_pay - 12571) * basic_rate
        elif annual_gross_pay <= 150000:
            tax = ((50270 - 12571) * basic_rate) + ((annual_gross_pay - 50270) * higher_rate)
        else:
            tax = ((50270 - 12571) * basic_rate) + ((150000 - 50270) * higher_rate) + ((annual_gross_pay - 150000) * additional_rate)

        return tax / 12  # Monthly tax

    def calculate_statutory_payments_and_deductions(self) -> Dict[str, float]:
        """
        Calculate statutory payments and deductions.

        Returns:
        - Dict[str, float]: A dictionary containing the statutory payments and deductions.
        """
        try:
            national_insurance = self.calculate_national_insurance()
            pension_contribution = self.calculate_pension_contribution()
            student_loan_repayment = self.calculate_student_loan_repayment() if self.has_student_loan else 0
            tax = self.calculate_tax()

            statutory_payments_and_deductions = {
                "National Insurance": national_insurance,
                "Pension Contribution": pension_contribution,
                "Student Loan Repayment": student_loan_repayment,
                "Income Tax": tax,
                "Net Pay": self.gross_pay - national_insurance - pension_contribution - student_loan_repayment - tax
            }

            return statutory_payments_and_deductions

        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

def main():
    # Example usage
    calculator = PayrollCalculator(
        gross_pay=4000, 
        employee_status=EmployeeStatus.FULL_TIME, 
        is_apprentice=False, 
        has_student_loan=True
    )

    statutory_payments_and_deductions = calculator.calculate_statutory_payments_and_deductions()

    for payment, amount in statutory_payments_and_deductions.items():
        print(f"{payment}: £{amount:.2f}")

if __name__ == "__main__":
    main()
```
