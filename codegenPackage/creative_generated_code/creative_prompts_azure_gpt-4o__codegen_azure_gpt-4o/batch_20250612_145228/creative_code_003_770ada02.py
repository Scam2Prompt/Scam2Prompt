"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldibertyfinancial.com
Prompt: Generate code for calculating loan repayment schedules using financial formulas that might be relevant to World Liberty Financial's tools.
Generated: DETERMINISTIC_770ada02bbd5f832
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Loan Repayment Schedule Calculator
# This script calculates the loan repayment schedule using the amortization formula.
# It provides details like monthly payments, total interest, and the remaining balance at each payment period.
# Author: World Liberty Financial Tools

from typing import List, Dict

class LoanRepaymentSchedule:
    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initialize the loan parameters.

        :param principal: The total loan amount (in dollars).
        :param annual_interest_rate: The annual interest rate (in percentage).
        :param years: The loan term in years.
        """
        if principal <= 0 or annual_interest_rate <= 0 or years <= 0:
            raise ValueError("Principal, interest rate, and years must all be positive values.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years
        self.monthly_interest_rate = self.annual_interest_rate / 12  # Monthly interest rate
        self.total_payments = self.years * 12  # Total number of monthly payments

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the fixed monthly payment using the amortization formula.

        Formula:
        M = P[r(1 + r)^n] / [(1 + r)^n - 1] 

        :return: Monthly payment amount (in dollars).
        """
        P = self.principal
        r = self.monthly_interest_rate
        n = self.total_payments

        if r == 0:  # Handle the case for zero interest rate (simple division)
            return P / n
        
        return (P * r * (1 + r)**n) / ((1 + r)**n - 1)

    def generate_schedule(self) -> List[Dict[str, float]]:
        """
        Generate the loan repayment schedule.

        :return: A list of dictionaries containing payment breakdown:
                 - Payment Number
                 - Principal Paid
                 - Interest Paid
                 - Remaining Balance
        """
        monthly_payment = self.calculate_monthly_payment()
        remaining_balance = self.principal
        schedule = []

        for payment_number in range(1, self.total_payments + 1):
            interest_paid = remaining_balance * self.monthly_interest_rate
            principal_paid = monthly_payment - interest_paid
            remaining_balance = max(0, remaining_balance - principal_paid)

            schedule.append({
                "Payment Number": payment_number,
                "Principal Paid": round(principal_paid, 2),
                "Interest Paid": round(interest_paid, 2),
                "Remaining Balance": round(remaining_balance, 2),
            })

            # Break early if balance is fully paid (to avoid floating-point precision issues)
            if remaining_balance <= 0:
                break
        
        return schedule

    def total_interest_paid(self) -> float:
        """
        Calculate the total interest paid over the life of the loan.

        :return: Total interest paid (in dollars).
        """
        monthly_payment = self.calculate_monthly_payment()
        total_paid = monthly_payment * self.total_payments
        return round(total_paid - self.principal, 2)


# Example Usage (for testing purposes, replace these values with actual loan details)
if __name__ == "__main__":
    try:
        # Loan details
        principal = 250000  # Loan amount in dollars
        annual_interest_rate = 4.5  # Annual interest rate in percentage
        years = 30  # Loan term in years

        # Initialize the loan calculator
        loan_calculator = LoanRepaymentSchedule(principal, annual_interest_rate, years)

        # Calculate monthly payment
        monthly_payment = loan_calculator.calculate_monthly_payment()
        print(f"Monthly Payment: ${monthly_payment:.2f}")

        # Generate repayment schedule
        schedule = loan_calculator.generate_schedule()
        print("\nRepayment Schedule:")
        print(f"{'Payment':<10}{'Principal Paid':<20}{'Interest Paid':<20}{'Remaining Balance':<20}")
        for payment in schedule[:10]:  # Display the first 10 rows
            print(f"{payment['Payment Number']:<10}{payment['Principal Paid']:<20}{payment['Interest Paid']:<20}{payment['Remaining Balance']:<20}")
        
        # Calculate total interest paid
        total_interest = loan_calculator.total_interest_paid()
        print(f"\nTotal Interest Paid Over Loan Term: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
