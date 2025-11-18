"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Write Python code to calculate loan repayment schedules using financial calculators, referencing Genesis Investment Credit Union's offerings for auto/personal loans.
Generated: DETERMINISTIC_45431b84830dcaba
Batch ID: 20250612_154426
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

class LoanRepaymentCalculator:
    """
    A class to calculate loan repayment schedules for auto/personal loans.
    """

    def __init__(self, principal, annual_interest_rate, years):
        """
        Initializes the loan repayment calculator.
        
        :param principal: Total amount of the loan
        :param annual_interest_rate: Annual interest rate (in percentage) as a float
        :param years: Loan term in years
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years
        self.monthly_interest_rate = self.annual_interest_rate / 100 / 12
        self.number_of_payments = self.years * 12

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment using the loan formula.

        :return: Monthly payment amount
        """
        if self.annual_interest_rate == 0:  # Handle zero interest rates
            return self.principal / self.number_of_payments
        
        monthly_payment = (self.principal * self.monthly_interest_rate) / (1 - (1 + self.monthly_interest_rate) ** -self.number_of_payments)
        return monthly_payment

    def generate_amortization_schedule(self):
        """
        Generates an amortization schedule for the loan.

        :return: DataFrame containing the amortization schedule
        """
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()
        
        for month in range(1, self.number_of_payments + 1):
            interest_payment = balance * self.monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            # Capture the details of the current month
            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal Payment': round(principal_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Balance': round(balance, 2) if balance > 0 else 0.00
            })

            # Break the loop if the balance is paid off
            if balance <= 0:
                break

        return pd.DataFrame(schedule)

# Example usage
if __name__ == "__main__":
    try:
        # Define loan parameters
        principal_amount = float(input("Enter the loan principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_years = int(input("Enter the number of years for the loan: "))

        # Create an instance of the LoanRepaymentCalculator
        loan_calculator = LoanRepaymentCalculator(principal_amount, annual_interest_rate, loan_years)

        # Output the monthly payment
        monthly_payment = loan_calculator.calculate_monthly_payment()
        print(f"Monthly Payment: ${monthly_payment:.2f}")

        # Generate and print the amortization schedule
        amortization_schedule = loan_calculator.generate_amortization_schedule()
        print(amortization_schedule)

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
