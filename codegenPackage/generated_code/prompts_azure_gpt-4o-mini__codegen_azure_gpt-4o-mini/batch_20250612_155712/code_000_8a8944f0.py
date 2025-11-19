"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Generate a Python script to calculate the estimated fees for a settlement loan based on the terms provided by Rhino Finance.
Generated: DETERMINISTIC_8a8944f05801ab36
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SettlementLoanCalculator:
    """
    A class to calculate estimated fees for a settlement loan based on user-defined terms.
    """

    def __init__(self, loan_amount, interest_rate, loan_term_months):
        """
        Initializes the calculator with loan parameters.

        :param loan_amount: The total amount of the loan.
        :param interest_rate: The annual interest rate (as a percentage).
        :param loan_term_months: The term of the loan in months.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.loan_term_months = loan_term_months

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        if self.loan_term_months <= 0:
            raise ValueError("Loan term must be greater than zero.")
        
        monthly_rate = self.interest_rate / 12
        payment = (self.loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -self.loan_term_months)
        return payment

    def calculate_total_payment(self):
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_term_months
        return total_payment

    def calculate_total_interest(self):
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.loan_amount
        return total_interest

def main():
    """
    Main function to execute the loan calculator.
    """
    try:
        # User input for loan parameters
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_term_months = int(input("Enter the loan term (in months): "))

        # Create an instance of the calculator
        calculator = SettlementLoanCalculator(loan_amount, interest_rate, loan_term_months)

        # Calculate and display results
        monthly_payment = calculator.calculate_monthly_payment()
        total_payment = calculator.calculate_total_payment()
        total_interest = calculator.calculate_total_interest()

        print(f"\nMonthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
