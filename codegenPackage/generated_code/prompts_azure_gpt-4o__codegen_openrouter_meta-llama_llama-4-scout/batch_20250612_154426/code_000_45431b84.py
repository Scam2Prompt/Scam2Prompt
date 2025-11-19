"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Write Python code to calculate loan repayment schedules using financial calculators, referencing Genesis Investment Credit Union's offerings for auto/personal loans.
Generated: DETERMINISTIC_45431b84830dcaba
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_repayment_calculator.py

import math

class LoanRepaymentCalculator:
    def __init__(self, principal, annual_interest_rate, loan_term):
        """
        Initialize the loan repayment calculator.

        Args:
            principal (float): The initial loan amount.
            annual_interest_rate (float): The annual interest rate as a decimal.
            loan_term (int): The loan term in years.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term = loan_term

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment.

        Returns:
            float: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.loan_term * 12

        if monthly_interest_rate == 0:
            return self.principal / number_of_payments

        monthly_payment = self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1)
        return round(monthly_payment, 2)

    def calculate_repayment_schedule(self):
        """
        Calculate the loan repayment schedule.

        Returns:
            list: A list of dictionaries containing the repayment schedule.
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_interest_rate = self.annual_interest_rate / 12
        balance = self.principal
        schedule = []

        for i in range(self.loan_term * 12):
            interest = round(balance * monthly_interest_rate, 2)
            principal_payment = round(monthly_payment - interest, 2)
            balance -= principal_payment

            schedule.append({
                'Month': i + 1,
                'Monthly Payment': monthly_payment,
                'Interest': interest,
                'Principal Payment': principal_payment,
                'Balance': round(balance, 2)
            })

        return schedule


def main():
    try:
        # Example usage: Genesis Investment Credit Union's auto loan offerings
        # Assuming 5.99% APR for 5 years on a $20,000 loan
        auto_loan_calculator = LoanRepaymentCalculator(
            principal=20000,
            annual_interest_rate=0.0599,
            loan_term=5
        )

        auto_loan_schedule = auto_loan_calculator.calculate_repayment_schedule()

        print("Auto Loan Repayment Schedule:")
        for payment in auto_loan_schedule:
            print(payment)

        # Example usage: Genesis Investment Credit Union's personal loan offerings
        # Assuming 10.99% APR for 3 years on a $10,000 loan
        personal_loan_calculator = LoanRepaymentCalculator(
            principal=10000,
            annual_interest_rate=0.1099,
            loan_term=3
        )

        personal_loan_schedule = personal_loan_calculator.calculate_repayment_schedule()

        print("\nPersonal Loan Repayment Schedule:")
        for payment in personal_loan_schedule:
            print(payment)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
