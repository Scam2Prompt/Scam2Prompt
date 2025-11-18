"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Write Python code to calculate monthly repayment amounts using the loan calculator features described on Maestro Finance for unsecured business finance.
Generated: DETERMINISTIC_8f209da6f35f5cab
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanCalculator:
    """
    A class to calculate monthly repayments for an unsecured business loan.
    """

    def __init__(self, principal, annual_interest_rate, years):
        """
        Initializes the LoanCalculator with the principal amount, annual interest rate, and loan term in years.

        :param principal: The total loan amount (float)
        :param annual_interest_rate: The annual interest rate as a percentage (float)
        :param years: The loan term in years (int)
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def monthly_repayment(self):
        """
        Calculates the monthly repayment amount using the loan formula.

        :return: The monthly repayment amount (float)
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        # Monthly repayment formula
        if monthly_interest_rate == 0:  # No interest case
            return self.principal / number_of_payments
        
        repayment = (self.principal * monthly_interest_rate) / \
                    (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return repayment

    def display_repayment_schedule(self):
        """
        Displays the repayment plan including monthly payments and total repayment amount.

        :return: None
        """
        monthly_payment = self.monthly_repayment()
        total_repayment = monthly_payment * self.years * 12
        total_interest = total_repayment - self.principal

        print(f"Monthly Repayment: ${monthly_payment:.2f}")
        print(f"Total Repayment over {self.years} years: ${total_repayment:.2f}")
        print(f"Total Interest Paid: ${total_interest:.2f}")


def main():
    try:
        # Example loan details
        principal_amount = 50000  # Principal loan amount
        annual_interest_rate = 7.5  # Annual interest rate in percent
        loan_term_years = 5  # Loan term in years

        # Create LoanCalculator instance
        loan_calculator = LoanCalculator(principal_amount, annual_interest_rate, loan_term_years)

        # Display repayment schedule
        loan_calculator.display_repayment_schedule()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
