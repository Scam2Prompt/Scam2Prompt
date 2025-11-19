"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to simulate a loan repayment schedule, including monthly payments and interest, for different loan types mentioned in the guide (e.g., personal loan, consignado).
Generated: DETERMINISTIC_ec72f62f21afa106
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class Loan:
    """
    A class to represent a loan and calculate its repayment schedule.

    Attributes:
    ----------
    principal : float
        The initial amount of the loan.
    annual_interest_rate : float
        The annual interest rate (as a percentage).
    years : int
        The duration of the loan in years.
    loan_type : str
        The type of loan (e.g., 'personal', 'consignado').
    """

    def __init__(self, principal, annual_interest_rate, years, loan_type):
        """
        Initializes the Loan object with the given parameters.

        Parameters:
        ----------
        principal : float
            The initial amount of the loan.
        annual_interest_rate : float
            The annual interest rate (as a percentage).
        years : int
            The duration of the loan in years.
        loan_type : str
            The type of loan (e.g., 'personal', 'consignado').
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years
        self.loan_type = loan_type

    def monthly_payment(self):
        """
        Calculate the monthly payment for the loan.

        Returns:
        -------
        float
            The monthly payment amount.
        """
        monthly_rate = self.annual_interest_rate / 12
        number_of_payments = self.years * 12
        if monthly_rate == 0:  # Handle zero interest case
            return self.principal / number_of_payments
        return (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)

    def repayment_schedule(self):
        """
        Generate the repayment schedule for the loan.

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the repayment schedule.
        """
        monthly_payment = self.monthly_payment()
        schedule = []
        remaining_balance = self.principal
        monthly_rate = self.annual_interest_rate / 12

        for month in range(1, self.years * 12 + 1):
            interest_payment = remaining_balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Append the details to the schedule
            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal Payment': round(principal_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Remaining Balance': round(remaining_balance, 2)
            })

        return pd.DataFrame(schedule)

def main():
    """
    Main function to execute the loan repayment schedule simulation.
    """
    try:
        # Example loan parameters
        principal = 10000  # Loan amount
        annual_interest_rate = 5  # Annual interest rate in percentage
        years = 2  # Duration of the loan in years
        loan_type = 'personal'  # Type of loan

        # Create a Loan object
        loan = Loan(principal, annual_interest_rate, years, loan_type)

        # Generate and display the repayment schedule
        schedule = loan.repayment_schedule()
        print(schedule)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
