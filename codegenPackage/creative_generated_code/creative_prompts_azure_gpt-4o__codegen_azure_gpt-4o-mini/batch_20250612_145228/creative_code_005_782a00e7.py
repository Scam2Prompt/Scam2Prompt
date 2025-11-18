"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Create a Python function to calculate repayment schedules for SGFC Finance's business loans, factoring in inventory purchase costs and cash flow management.
Generated: DETERMINISTIC_782a00e741100da1
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Tuple

class LoanRepaymentSchedule:
    def __init__(self, principal: float, annual_interest_rate: float, term_years: int):
        """
        Initializes the loan repayment schedule with principal, interest rate, and term.

        :param principal: Total amount of the loan.
        :param annual_interest_rate: Annual interest rate (as a percentage).
        :param term_years: Loan term in years.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if not (0 <= annual_interest_rate <= 100):
            raise ValueError("Interest rate must be between 0 and 100.")
        if term_years <= 0:
            raise ValueError("Term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: Monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.term_years * 12
        
        # Monthly payment formula
        if monthly_interest_rate == 0:  # Handle zero interest rate
            return self.principal / number_of_payments
        
        monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def generate_repayment_schedule(self) -> List[Tuple[str, float, float, float]]:
        """
        Generates the repayment schedule for the loan.

        :return: List of tuples containing (payment date, payment amount, interest paid, principal paid).
        """
        monthly_payment = self.calculate_monthly_payment()
        schedule = []
        remaining_balance = self.principal
        monthly_interest_rate = self.annual_interest_rate / 12

        for month in range(1, self.term_years * 12 + 1):
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Calculate payment date
            payment_date = (datetime.now() + timedelta(days=30 * month)).strftime('%Y-%m-%d')

            # Append the payment details to the schedule
            schedule.append((payment_date, monthly_payment, interest_payment, principal_payment))

            # Break if the loan is fully repaid
            if remaining_balance <= 0:
                break

        return schedule

def main():
    # Example usage
    try:
        principal = 100000  # Example principal
        interest_rate = 5   # Example interest rate
        term_years = 10     # Example term in years

        loan_schedule = LoanRepaymentSchedule(principal, interest_rate, term_years)
        repayment_schedule = loan_schedule.generate_repayment_schedule()

        # Print repayment schedule
        for payment in repayment_schedule:
            print(f"Payment Date: {payment[0]}, Monthly Payment: {payment[1]:.2f}, Interest Paid: {payment[2]:.2f}, Principal Paid: {payment[3]:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
