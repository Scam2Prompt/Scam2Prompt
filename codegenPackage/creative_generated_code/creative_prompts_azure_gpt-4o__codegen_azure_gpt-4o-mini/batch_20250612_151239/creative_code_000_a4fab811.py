"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Write Python code to calculate the repayment schedule for an SME loan scheme offered by the Development Bank of Mauritius, incorporating interest rates and loan terms mentioned on the website.
Generated: DETERMINISTIC_a4fab811ac775cfb
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class LoanRepaymentSchedule:
    """
    A class to calculate the repayment schedule for an SME loan scheme.
    """

    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initialize the LoanRepaymentSchedule with principal, interest rate, and loan term.

        :param principal: The loan amount (principal)
        :param annual_interest_rate: The annual interest rate (in percentage)
        :param years: The term of the loan in years
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years
        self.months = years * 12
        self.monthly_interest_rate = self.annual_interest_rate / 12

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment using the amortization formula.

        :return: Monthly payment amount
        """
        if self.monthly_interest_rate == 0:
            return self.principal / self.months

        monthly_payment = (self.principal * self.monthly_interest_rate) / \
                          (1 - (1 + self.monthly_interest_rate) ** (-self.months))
        return monthly_payment

    def generate_repayment_schedule(self) -> pd.DataFrame:
        """
        Generate a repayment schedule with the details of each payment.

        :return: A pandas DataFrame containing the repayment schedule
        """
        monthly_payment = self.calculate_monthly_payment()
        schedule = []

        remaining_balance = self.principal

        for month in range(1, self.months + 1):
            interest_payment = remaining_balance * self.monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Ensure remaining balance does not go negative
            remaining_balance = max(remaining_balance, 0)

            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal Payment': round(principal_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Remaining Balance': round(remaining_balance, 2)
            })

        return pd.DataFrame(schedule)

if __name__ == "__main__":
    # Example usage: principal of 100,000, interest rate of 5%, loan term of 10 years
    try:
        loan_schedule = LoanRepaymentSchedule(principal=100000, annual_interest_rate=5, years=10)
        repayment_schedule_df = loan_schedule.generate_repayment_schedule()
        print(repayment_schedule_df)
    except ValueError as e:
        print(f"Error: {e}")
```
