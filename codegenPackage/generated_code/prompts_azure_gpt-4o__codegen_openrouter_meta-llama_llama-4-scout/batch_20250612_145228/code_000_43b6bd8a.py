"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Write Python code to simulate a loan calculator for SGFC Finance's personal loan product, incorporating flexible repayment terms and competitive interest rates as described on their website.
Generated: DETERMINISTIC_43b6bd8a9171f54b
Batch ID: 20250612_145228
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
    A class used to simulate a loan calculator for SGFC Finance's personal loan product.

    Attributes:
    ----------
    loan_amount : float
        The amount borrowed by the user.
    interest_rate : float
        The annual interest rate of the loan.
    loan_term : int
        The loan term in years.

    Methods:
    -------
    calculate_monthly_repayment()
        Calculates the monthly repayment amount.
    calculate_total_interest()
        Calculates the total interest paid over the loan term.
    calculate_total_repayment()
        Calculates the total repayment amount.
    """

    def __init__(self, loan_amount, interest_rate, loan_term):
        """
        Initializes the LoanCalculator object.

        Parameters:
        ----------
        loan_amount : float
            The amount borrowed by the user.
        interest_rate : float
            The annual interest rate of the loan.
        loan_term : int
            The loan term in years.

        Raises:
        ------
        ValueError
            If loan_amount, interest_rate, or loan_term is not a positive number.
        """
        if loan_amount <= 0 or interest_rate <= 0 or loan_term <= 0:
            raise ValueError("Loan amount, interest rate, and loan term must be positive numbers.")

        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100 / 12  # Convert to monthly interest rate
        self.loan_term = loan_term * 12  # Convert to months

    def calculate_monthly_repayment(self):
        """
        Calculates the monthly repayment amount using the formula for monthly payments on a fixed-rate loan.

        Returns:
        -------
        float
            The monthly repayment amount.
        """
        monthly_repayment = self.loan_amount * self.interest_rate * (1 + self.interest_rate) ** self.loan_term / ((1 + self.interest_rate) ** self.loan_term - 1)
        return round(monthly_repayment, 2)

    def calculate_total_interest(self):
        """
        Calculates the total interest paid over the loan term.

        Returns:
        -------
        float
            The total interest paid.
        """
        monthly_repayment = self.calculate_monthly_repayment()
        total_interest = monthly_repayment * self.loan_term - self.loan_amount
        return round(total_interest, 2)

    def calculate_total_repayment(self):
        """
        Calculates the total repayment amount.

        Returns:
        -------
        float
            The total repayment amount.
        """
        monthly_repayment = self.calculate_monthly_repayment()
        total_repayment = monthly_repayment * self.loan_term
        return round(total_repayment, 2)


def main():
    try:
        loan_amount = float(input("Enter the loan amount: $"))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_term = int(input("Enter the loan term (in years): "))

        calculator = LoanCalculator(loan_amount, interest_rate, loan_term)

        print("\nLoan Calculator Results:")
        print(f"Monthly Repayment: ${calculator.calculate_monthly_repayment()}")
        print(f"Total Interest: ${calculator.calculate_total_interest()}")
        print(f"Total Repayment: ${calculator.calculate_total_repayment()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
