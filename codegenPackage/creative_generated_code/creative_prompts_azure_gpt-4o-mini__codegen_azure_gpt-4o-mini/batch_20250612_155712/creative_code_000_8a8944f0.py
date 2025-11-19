"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Generate a Python script to calculate the estimated fees for a settlement loan based on the terms provided by Rhino Finance.
Generated: DETERMINISTIC_8a8944f05801ab36
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SettlementLoanCalculator:
    def __init__(self, loan_amount: float, interest_rate: float, term_months: int):
        """
        Initialize the SettlementLoanCalculator with loan amount, interest rate, and term in months.

        :param loan_amount: The total amount of the loan.
        :param interest_rate: The annual interest rate as a percentage (e.g., 5 for 5%).
        :param term_months: The duration of the loan in months.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.term_months = term_months

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        try:
            # Monthly interest rate
            monthly_rate = self.interest_rate / 12

            if monthly_rate == 0:  # Handle zero interest rate
                return self.loan_amount / self.term_months

            # Monthly payment formula
            monthly_payment = (self.loan_amount * monthly_rate) / \
                (1 - (1 + monthly_rate) ** -self.term_months)
            return monthly_payment
        except ZeroDivisionError:
            print("Error: Division by zero encountered in monthly payment calculation.")
            sys.exit(1)

    def total_payment(self) -> float:
        """
        Calculate the total payment over the life of the loan.

        :return: The total amount to be paid back.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.term_months
        return total_payment

    def total_interest(self) -> float:
        """
        Calculate the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        return self.total_payment() - self.loan_amount

def main():
    """
    Main function to execute the settlement loan calculation based on user input.
    """
    try:
        # Get user input
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        term_months = int(input("Enter the loan term in months: "))

        # Create an instance of the calculator
        calculator = SettlementLoanCalculator(loan_amount, interest_rate, term_months)

        # Display results
        print(f"Monthly Payment: ${calculator.calculate_monthly_payment():.2f}")
        print(f"Total Payment: ${calculator.total_payment():.2f}")
        print(f"Total Interest: ${calculator.total_interest():.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for loan amount, interest rate, and term.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
