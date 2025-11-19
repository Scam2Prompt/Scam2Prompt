"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: "What are the key factors to consider when developing a loan calculator that takes into account the lender's APR, loan amount, and repayment period, as discussed on ziggyloan.com?"
Generated: DETERMINISTIC_7db0032a2f251d6d
Batch ID: 20250622_205144
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
    A class to represent a loan calculator.

    Attributes
    ----------
    loan_amount : float
        The total amount of the loan.
    annual_percentage_rate : float
        The annual interest rate (APR) as a percentage.
    repayment_period_years : int
        The duration of the loan repayment in years.

    Methods
    -------
    calculate_monthly_payment():
        Calculates the monthly payment based on the loan amount, APR, and repayment period.
    calculate_total_payment():
        Calculates the total payment over the life of the loan.
    calculate_total_interest():
        Calculates the total interest paid over the life of the loan.
    """

    def __init__(self, loan_amount: float, annual_percentage_rate: float, repayment_period_years: int):
        """
        Initializes the LoanCalculator with loan amount, APR, and repayment period.

        Parameters
        ----------
        loan_amount : float
            The total amount of the loan.
        annual_percentage_rate : float
            The annual interest rate (APR) as a percentage.
        repayment_period_years : int
            The duration of the loan repayment in years.
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if annual_percentage_rate < 0:
            raise ValueError("Annual percentage rate cannot be negative.")
        if repayment_period_years <= 0:
            raise ValueError("Repayment period must be greater than zero.")

        self.loan_amount = loan_amount
        self.annual_percentage_rate = annual_percentage_rate
        self.repayment_period_years = repayment_period_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        Returns
        -------
        float
            The monthly payment amount.
        """
        monthly_rate = self.annual_percentage_rate / 100 / 12
        number_of_payments = self.repayment_period_years * 12

        if monthly_rate == 0:  # Handle case for zero interest rate
            return self.loan_amount / number_of_payments

        monthly_payment = (self.loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        Returns
        -------
        float
            The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.repayment_period_years * 12
        return total_payment

    def calculate_total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        Returns
        -------
        float
            The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.loan_amount
        return total_interest


# Example usage:
if __name__ == "__main__":
    try:
        loan_amount = 10000  # Example loan amount
        apr = 5.0            # Example APR
        repayment_period = 3  # Example repayment period in years

        loan_calculator = LoanCalculator(loan_amount, apr, repayment_period)
        monthly_payment = loan_calculator.calculate_monthly_payment()
        total_payment = loan_calculator.calculate_total_payment()
        total_interest = loan_calculator.calculate_total_interest()

        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
