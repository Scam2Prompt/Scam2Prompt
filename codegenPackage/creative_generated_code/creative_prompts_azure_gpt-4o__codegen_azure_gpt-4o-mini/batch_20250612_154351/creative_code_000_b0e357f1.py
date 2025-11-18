"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finflix.me
Prompt: Write code to calculate monthly loan payments based on the loan amount, interest rate (4.9%), and repayment duration in months, as described on the flix-fin.me website.
Generated: DETERMINISTIC_b0e357f10753af8d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanCalculator:
    """
    A class to represent a loan calculator capable of calculating monthly payments.
    """

    def __init__(self, loan_amount: float, annual_interest_rate: float, months: int):
        """
        Initialize the LoanCalculator with loan amount, annual interest rate, and repayment duration.

        :param loan_amount: The total amount of the loan.
        :param annual_interest_rate: The annual interest rate as a percentage (e.g., 4.9 for 4.9%).
        :param months: The repayment duration in months.
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.months = months

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the loan.

        :return: The calculated monthly payment amount.
        :raises ValueError: If the inputs are invalid (negative values or zero months).
        """
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if self.months <= 0:
            raise ValueError("Months must be greater than zero.")
        
        monthly_interest_rate = self.annual_interest_rate / 12  # Monthly interest rate
        try:
            # Monthly payment formula
            monthly_payment = (self.loan_amount * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -self.months)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate cannot be zero.")

if __name__ == "__main__":
    # Example usage
    loan_amount = 10000  # Loan amount in dollars
    interest_rate = 4.9  # Annual interest rate in percent
    repayment_duration = 24  # Duration in months

    # Create a LoanCalculator instance
    calculator = LoanCalculator(loan_amount, interest_rate, repayment_duration)

    try:
        monthly_payment = calculator.calculate_monthly_payment()
        print(f"The monthly payment for the loan is: ${monthly_payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
