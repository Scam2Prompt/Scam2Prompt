"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Write Python code to calculate the repayment schedule for an SME loan scheme offered by the Development Bank of Mauritius, incorporating interest rates and loan terms mentioned on the website.
Generated: DETERMINISTIC_a4fab811ac775cfb
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sme_loan_repayment_schedule.py

from datetime import datetime, timedelta

class SME_Loan:
    def __init__(self, loan_amount, interest_rate, loan_term_in_years):
        """
        Initialize an SME loan object.

        Args:
            loan_amount (float): The loan amount.
            interest_rate (float): The annual interest rate as a decimal.
            loan_term_in_years (int): The loan term in years.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # convert to decimal
        self.loan_term_in_years = loan_term_in_years

    def calculate_monthly_repayment(self):
        """
        Calculate the monthly repayment.

        Returns:
            float: The monthly repayment amount.
        """
        monthly_interest_rate = self.interest_rate / 12
        loan_term_in_months = self.loan_term_in_years * 12

        monthly_repayment = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_in_months / (
                (1 + monthly_interest_rate) ** loan_term_in_months - 1)

        return round(monthly_repayment, 2)

    def generate_repayment_schedule(self):
        """
        Generate the repayment schedule.

        Returns:
            list: A list of dictionaries representing the repayment schedule.
        """
        monthly_repayment = self.calculate_monthly_repayment()
        loan_term_in_months = self.loan_term_in_years * 12
        balance = self.loan_amount
        schedule = []

        for i in range(loan_term_in_months):
            interest = round(balance * (self.interest_rate / 12), 2)
            principal = round(monthly_repayment - interest, 2)
            balance -= principal

            schedule.append({
                'Month': i + 1,
                'Monthly Repayment': monthly_repayment,
                'Interest': interest,
                'Principal': principal,
                'Balance': round(balance, 2)
            })

        return schedule


def main():
    try:
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_term_in_years = int(input("Enter the loan term (in years): "))

        sme_loan = SME_Loan(loan_amount, interest_rate, loan_term_in_years)
        repayment_schedule = sme_loan.generate_repayment_schedule()

        print("\nRepayment Schedule:")
        for month in repayment_schedule:
            print(f"Month: {month['Month']}")
            print(f"Monthly Repayment: MUR {month['Monthly Repayment']}")
            print(f"Interest: MUR {month['Interest']}")
            print(f"Principal: MUR {month['Principal']}")
            print(f"Balance: MUR {month['Balance']}\n")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
