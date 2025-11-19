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
class LoanCalculator:
    """
    A simple loan calculator for Panchsheel Bank's housing loan.
    """

    def __init__(self, loan_amount: float, annual_interest_rate: float, loan_tenure_years: int):
        """
        Initializes the LoanCalculator with loan amount, interest rate, and tenure.

        :param loan_amount: The total amount of the loan.
        :param annual_interest_rate: The annual interest rate (in percentage).
        :param loan_tenure_years: The tenure of the loan in years.
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if loan_tenure_years <= 0:
            raise ValueError("Loan tenure must be greater than zero.")

        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.loan_tenure_years = loan_tenure_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan.

        :return: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.loan_tenure_years * 12

        # Calculate monthly payment using the formula
        if monthly_interest_rate == 0:  # Handle case for zero interest rate
            return self.loan_amount / number_of_payments

        monthly_payment = (self.loan_amount * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_tenure_years * 12
        return total_payment

    def calculate_total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.loan_amount
        return total_interest


if __name__ == "__main__":
    try:
        # Example usage
        loan_amount = 500000  # Loan amount in currency units
        annual_interest_rate = 7.5  # Annual interest rate in percentage
        loan_tenure_years = 20  # Loan tenure in years

        loan_calculator = LoanCalculator(loan_amount, annual_interest_rate, loan_tenure_years)

        print(f"Monthly Payment: {loan_calculator.calculate_monthly_payment():.2f}")
        print(f"Total Payment: {loan_calculator.calculate_total_payment():.2f}")
        print(f"Total Interest: {loan_calculator.calculate_total_interest():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
