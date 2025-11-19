"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: Write a Python code snippet to implement a simple loan calculator for Panchsheel Bank's housing loan, taking into account the loan amount, interest rate, and loan tenure.
Generated: DETERMINISTIC_a0c5d71395242a9e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Panchsheel Bank Housing Loan Calculator

Calculates the monthly EMI for a housing loan based on the loan amount, interest rate, and loan tenure.
"""

class LoanCalculator:
    def __init__(self, loan_amount, interest_rate, loan_tenure):
        """
        Initializes the LoanCalculator with loan amount, interest rate, and loan tenure.

        Args:
            loan_amount (float): The total loan amount.
            interest_rate (float): The annual interest rate in percentage.
            loan_tenure (int): The loan tenure in years.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert to decimal
        self.loan_tenure = loan_tenure

    def calculate_emi(self):
        """
        Calculates the monthly EMI.

        Returns:
            float: The monthly EMI amount.
        """
        # Convert interest rate to monthly
        monthly_interest_rate = self.interest_rate / 12
        
        # Convert loan tenure to months
        loan_tenure_months = self.loan_tenure * 12

        # Calculate EMI using the formula: M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        #   M = monthly EMI
        #   P = loan amount
        #   r = monthly interest rate
        #   n = loan tenure in months
        emi = self.loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months) / (
                (1 + monthly_interest_rate) ** loan_tenure_months - 1)

        return round(emi, 2)

    def calculate_total_interest(self):
        """
        Calculates the total interest paid over the loan tenure.

        Returns:
            float: The total interest paid.
        """
        emi = self.calculate_emi()
        loan_tenure_months = self.loan_tenure * 12
        total_interest = (emi * loan_tenure_months) - self.loan_amount
        return round(total_interest, 2)

    def calculate_total_amount(self):
        """
        Calculates the total amount paid (loan amount + interest).

        Returns:
            float: The total amount paid.
        """
        return self.loan_amount + self.calculate_total_interest()


def main():
    try:
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_tenure = int(input("Enter the loan tenure (in years): "))

        calculator = LoanCalculator(loan_amount, interest_rate, loan_tenure)

        print(f"Monthly EMI: ₹{calculator.calculate_emi()}")
        print(f"Total Interest: ₹{calculator.calculate_total_interest()}")
        print(f"Total Amount: ₹{calculator.calculate_total_amount()}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
