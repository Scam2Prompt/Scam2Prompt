"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: "What are the key factors to consider when developing a loan calculator that takes into account the lender's APR, loan amount, and repayment period, as discussed on ziggyloan.com?"
Generated: DETERMINISTIC_7db0032a2f251d6d
Batch ID: 20250622_205144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Loan Calculator Implementation

This module provides a loan calculator that takes into account the lender's APR, 
loan amount, and repayment period to calculate the monthly repayment amount and 
total interest paid over the loan period.

Author: [Your Name]
Date: [Today's Date]
"""

class LoanCalculator:
    def __init__(self, apr: float, loan_amount: float, repayment_period: int):
        """
        Initializes the LoanCalculator with the given parameters.

        Args:
        - apr (float): The lender's APR (Annual Percentage Rate)
        - loan_amount (float): The loan amount
        - repayment_period (int): The repayment period in years

        Raises:
        - ValueError: If any of the input values are invalid
        """
        if apr < 0:
            raise ValueError("APR cannot be negative")
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero")
        if repayment_period <= 0:
            raise ValueError("Repayment period must be greater than zero")

        self.apr = apr / 100  # Convert APR to a decimal
        self.loan_amount = loan_amount
        self.repayment_period = repayment_period

    def calculate_monthly_repayment(self) -> float:
        """
        Calculates the monthly repayment amount.

        Returns:
        - float: The monthly repayment amount
        """
        # Convert repayment period from years to months
        repayment_period_months = self.repayment_period * 12

        # Calculate the monthly interest rate
        monthly_interest_rate = self.apr / 12

        # Calculate the monthly repayment amount using the formula:
        # M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        # M = monthly payment
        # P = principal loan amount
        # r = monthly interest rate
        # n = number of payments
        monthly_repayment = self.loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** repayment_period_months) / (
                (1 + monthly_interest_rate) ** repayment_period_months - 1)

        return round(monthly_repayment, 2)

    def calculate_total_interest(self) -> float:
        """
        Calculates the total interest paid over the loan period.

        Returns:
        - float: The total interest paid
        """
        monthly_repayment = self.calculate_monthly_repayment()
        repayment_period_months = self.repayment_period * 12
        total_interest = (monthly_repayment * repayment_period_months) - self.loan_amount

        return round(total_interest, 2)


def main():
    try:
        apr = float(input("Enter the lender's APR: "))
        loan_amount = float(input("Enter the loan amount: "))
        repayment_period = int(input("Enter the repayment period in years: "))

        calculator = LoanCalculator(apr, loan_amount, repayment_period)
        monthly_repayment = calculator.calculate_monthly_repayment()
        total_interest = calculator.calculate_total_interest()

        print(f"Monthly Repayment: ${monthly_repayment}")
        print(f"Total Interest Paid: ${total_interest}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
