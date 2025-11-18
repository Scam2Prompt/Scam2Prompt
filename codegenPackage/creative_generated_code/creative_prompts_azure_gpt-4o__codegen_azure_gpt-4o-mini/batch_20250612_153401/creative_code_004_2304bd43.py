"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Write a function to calculate loan repayment schedules for educational credits in a CMS system designed for cooperatives.
Generated: DETERMINISTIC_2304bd43bbf918b5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Tuple
import numpy as np

class LoanRepaymentSchedule:
    """
    A class to represent a loan repayment schedule for educational credits.
    """

    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the LoanRepaymentSchedule with principal, annual interest rate, and term in years.

        :param principal: The total loan amount (principal).
        :param annual_rate: The annual interest rate (in percentage).
        :param years: The number of years to repay the loan.
        """
        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment using the formula for an amortizing loan.

        :return: The fixed monthly payment amount.
        :raises ValueError: If the principal or annual_rate is less than or equal to zero.
        """
        if self.principal <= 0 or self.annual_rate < 0:
            raise ValueError("Principal must be greater than 0 and annual rate must be non-negative.")

        monthly_rate = self.annual_rate / 12
        number_of_payments = self.years * 12
        
        # Handle the case where the interest rate is zero
        if self.annual_rate == 0:
            return self.principal / number_of_payments
        
        monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        return monthly_payment

    def generate_schedule(self) -> List[Tuple[int, float, float, float]]:
        """
        Generate the loan repayment schedule.

        :return: A list of tuples containing month number, principal payment, interest payment, balance.
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_rate = self.annual_rate / 12
        balance = self.principal
        schedule = []

        for month in range(1, self.years * 12 + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            
            # Append the month, principal payment, interest payment, and remaining balance to the schedule
            schedule.append((month, round(principal_payment, 2), round(interest_payment, 2), round(balance, 2)))

        return schedule

# Example usage:
if __name__ == "__main__":
    try:
        loan = LoanRepaymentSchedule(principal=10000, annual_rate=5, years=5)
        schedule = loan.generate_schedule()

        print("Month | Principal Payment | Interest Payment | Remaining Balance")
        print("-" * 60)
        for month, principal, interest, balance in schedule:
            print(f"{month:5} | {principal:17} | {interest:15} | {balance:18}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
