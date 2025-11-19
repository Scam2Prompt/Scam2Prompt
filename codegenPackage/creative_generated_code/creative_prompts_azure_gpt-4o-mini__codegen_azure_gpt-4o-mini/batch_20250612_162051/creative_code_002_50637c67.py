"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guillenrealtygrouphtx.com
Prompt: How does the mortgage calculator on Guillen Realty Group's site assist potential home buyers in their purchasing decisions?
Generated: DETERMINISTIC_50637c6779f7c595
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MortgageCalculator:
    """
    A simple mortgage calculator to help potential home buyers
    estimate their monthly mortgage payments based on loan amount,
    interest rate, and loan term.
    """

    def __init__(self, loan_amount, annual_interest_rate, loan_term_years):
        """
        Initialize the mortgage calculator with loan details.

        :param loan_amount: Total amount of the mortgage loan.
        :param annual_interest_rate: Annual interest rate as a percentage.
        :param loan_term_years: Duration of the loan in years.
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly mortgage payment.

        :return: Monthly payment amount.
        :raises ValueError: If any of the input parameters are invalid.
        """
        # Validate inputs
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if self.annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if self.loan_term_years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        # Convert annual interest rate to a monthly interest rate
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.loan_term_years * 12

        # Calculate monthly payment using the formula for fixed-rate mortgages
        monthly_payment = (
            self.loan_amount * monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        )

        return monthly_payment

def main():
    """
    Main function to execute the mortgage calculator.
    """
    try:
        # Example input values
        loan_amount = 300000  # Example loan amount
        annual_interest_rate = 3.5  # Example interest rate
        loan_term_years = 30  # Example loan term

        # Instantiate the mortgage calculator
        calculator = MortgageCalculator(loan_amount, annual_interest_rate, loan_term_years)

        # Calculate monthly payment
        monthly_payment = calculator.calculate_monthly_payment()

        # Output the result
        print(f"Monthly payment for a loan of ${loan_amount} at an interest rate of "
              f"{annual_interest_rate}% over {loan_term_years} years is: ${monthly_payment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
