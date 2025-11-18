"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to simulate a loan repayment schedule, including monthly payments and interest, for different loan types mentioned in the guide (e.g., personal loan, consignado).
Generated: DETERMINISTIC_ec72f62f21afa106
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class Loan:
    """
    A class to represent a loan and calculate its repayment schedule.

    Attributes:
        principal (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate as a percentage.
        loan_term_months (int): The term of the loan in months.
        loan_type (str): The type of loan (e.g., 'personal', 'consignado').
    """

    def __init__(self, principal: float, annual_interest_rate: float, loan_term_months: int, loan_type: str):
        """
        Initializes the Loan class with the provided parameters.

        Args:
            principal (float): The principal amount of the loan.
            annual_interest_rate (float): The annual interest rate.
            loan_term_months (int): The loan term in months.
            loan_type (str): The type of loan.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if loan_term_months <= 0:
            raise ValueError("Loan term must be greater than zero.")
        
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.loan_term_months = loan_term_months
        self.loan_type = loan_type

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an annuity.

        Returns:
            float: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        if self.loan_term_months == 0:
            return self.principal  # No interest if the term is zero
        
        payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -self.loan_term_months)
        return payment

    def generate_repayment_schedule(self):
        """
        Generates a repayment schedule for the loan.

        Returns:
            list: A list of dictionaries containing the month, payment, principal, interest, and balance.
        """
        monthly_payment = self.calculate_monthly_payment()
        balance = self.principal
        schedule = []

        for month in range(1, self.loan_term_months + 1):
            interest_payment = balance * (self.annual_interest_rate / 12)
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            # Store the details of the current month in the schedule
            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal Payment': round(principal_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Remaining Balance': round(balance, 2)
            })

            # Stop if balance is paid off
            if balance < 0:
                break

        return schedule

    def print_schedule(self):
        """
        Prints the repayment schedule in a readable format.
        """
        print(f"Loan Type: {self.loan_type}")
        print(f"Loan Amount: ${self.principal:.2f}")
        print(f"Annual Interest Rate: {self.annual_interest_rate * 100:.2f}%")
        print(f"Loan Term: {self.loan_term_months} months")
        print("\nRepayment Schedule:")
        print(f"{'Month':<10}{'Payment':<15}{'Principal Payment':<20}{'Interest Payment':<20}{'Remaining Balance':<20}")
        schedule = self.generate_repayment_schedule()
        for entry in schedule:
            print(f"{entry['Month']:<10}{entry['Payment']:<15}{entry['Principal Payment']:<20}{entry['Interest Payment']:<20}{entry['Remaining Balance']:<20}")

# Example usage
if __name__ == "__main__":
    try:
        personal_loan = Loan(principal=10000, annual_interest_rate=5, loan_term_months=24, loan_type='Personal Loan')
        personal_loan.print_schedule()

        consignado_loan = Loan(principal=20000, annual_interest_rate=3, loan_term_months=36, loan_type='Consignado')
        consignado_loan.print_schedule()

    except ValueError as e:
        print(f"Error: {e}")
```
