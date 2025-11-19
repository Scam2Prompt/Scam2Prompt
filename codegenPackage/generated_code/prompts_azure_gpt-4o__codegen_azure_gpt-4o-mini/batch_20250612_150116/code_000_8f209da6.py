"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Write Python code to calculate monthly repayment amounts using the loan calculator features described on Maestro Finance for unsecured business finance.
Generated: DETERMINISTIC_8f209da6f35f5cab
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoanCalculator:
    """
    A class to calculate monthly repayment amounts for unsecured business finance loans.
    """

    def __init__(self, principal: float, annual_interest_rate: float, loan_term_years: int):
        """
        Initializes the LoanCalculator with the principal amount, annual interest rate, and loan term.

        :param principal: The total amount of the loan (float).
        :param annual_interest_rate: The annual interest rate as a percentage (float).
        :param loan_term_years: The term of the loan in years (int).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years

    def calculate_monthly_repayment(self) -> float:
        """
        Calculates the monthly repayment amount using the loan formula.

        :return: The monthly repayment amount (float).
        """
        monthly_interest_rate = self.annual_interest_rate / 12  # Monthly interest rate
        number_of_payments = self.loan_term_years * 12  # Total number of monthly payments

        # Calculate monthly repayment using the formula
        if monthly_interest_rate == 0:  # Handle case for zero interest rate
            return self.principal / number_of_payments

        monthly_repayment = (self.principal * monthly_interest_rate) / \
                            (1 - (1 + monthly_interest_rate) ** -number_of_payments)

        return monthly_repayment

def main():
    """
    Main function to execute the loan calculator.
    """
    try:
        # Example input values
        principal = 50000  # Principal amount in currency
        annual_interest_rate = 5.0  # Annual interest rate in percentage
        loan_term_years = 5  # Loan term in years

        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(principal, annual_interest_rate, loan_term_years)

        # Calculate and print the monthly repayment amount
        monthly_repayment = loan_calculator.calculate_monthly_repayment()
        print(f"Monthly Repayment Amount: ${monthly_repayment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
