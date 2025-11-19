"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Write a Python function that calculates the total repayment amount for a group loan based on the unique terms provided by SGFC Finance, including interest rates and loan duration.
Generated: DETERMINISTIC_94e572ef077466c5
Batch ID: 20250612_163406
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
    A class to calculate total repayment amount for a group loan.
    """

    def __init__(self, principal, annual_interest_rate, years):
        """
        Initializes the LoanCalculator with loan details.

        Args:
            principal (float): The amount of the loan.
            annual_interest_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
            years (int): The duration of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan duration must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def calculate_total_repayment(self):
        """
        Calculates the total repayment amount for the loan.

        Returns:
            float: The total repayment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        # Calculate monthly payment using the formula for an annuity
        if monthly_interest_rate > 0:
            monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        else:
            monthly_payment = self.principal / number_of_payments

        total_repayment = monthly_payment * number_of_payments
        return total_repayment

# Example usage
if __name__ == "__main__":
    try:
        loan = LoanCalculator(principal=10000, annual_interest_rate=5, years=3)
        total_repayment = loan.calculate_total_repayment()
        print(f"Total repayment amount: ${total_repayment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
