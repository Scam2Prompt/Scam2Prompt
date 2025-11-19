"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: "Generate a Python script to calculate the total amount payable for a personal loan of $4,300 with an Annual Percentage Rate (APR) of 35.99% and a repayment period of 30 months."
Generated: DETERMINISTIC_a8f640b08b573ba1
Batch ID: 20250622_205144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# personal_loan_calculator.py

class PersonalLoanCalculator:
    def __init__(self, principal: float, annual_rate: float, months: int):
        """
        Initializes the loan calculator with the principal amount, annual interest rate, and repayment period.

        :param principal: The principal amount of the loan (float).
        :param annual_rate: The annual interest rate as a percentage (float).
        :param months: The repayment period in months (int).
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.months = months

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount (float).
        """
        monthly_rate = self.annual_rate / 100 / 12  # Convert annual rate to monthly and percentage to decimal
        try:
            monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -self.months)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Monthly interest rate cannot be zero. Please check the annual interest rate.")

    def calculate_total_payment(self) -> float:
        """
        Calculates the total amount payable over the entire loan period.

        :return: The total payment amount (float).
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.months
        return total_payment

def main():
    # Loan parameters
    principal_amount = 4300.00  # Principal amount of the loan
    annual_percentage_rate = 35.99  # Annual Percentage Rate (APR)
    repayment_period_months = 30  # Repayment period in months

    # Create an instance of the loan calculator
    loan_calculator = PersonalLoanCalculator(principal_amount, annual_percentage_rate, repayment_period_months)

    # Calculate total payment
    try:
        total_payable = loan_calculator.calculate_total_payment()
        print(f"Total amount payable for the loan: ${total_payable:.2f}")
    except ValueError as e:
        print(f"Error calculating total payment: {e}")

if __name__ == "__main__":
    main()
```
