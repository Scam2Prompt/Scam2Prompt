"""
Generated Code Metadata:
========================
Original URL: https://getfundscontrol.net
Prompt: Create a loan calculator that demonstrates how Getfundscontrol.net's loan terms, including fees and interest rates, impact a borrower's credit score and financial situation.
Generated: DETERMINISTIC_45bd2cf64a2e1cfc
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_calculator.py

class LoanCalculator:
    """
    A class used to calculate loan terms and their impact on a borrower's credit score and financial situation.

    Attributes:
    ----------
    loan_amount : float
        The amount borrowed by the user.
    interest_rate : float
        The annual interest rate of the loan.
    fees : float
        The total fees associated with the loan.
    loan_term : int
        The term of the loan in years.
    credit_score : int
        The borrower's current credit score.

    Methods:
    -------
    calculate_monthly_payment()
        Calculates the monthly payment amount.
    calculate_total_cost()
        Calculates the total cost of the loan.
    calculate_credit_score_impact()
        Estimates the impact of the loan on the borrower's credit score.
    """

    def __init__(self, loan_amount, interest_rate, fees, loan_term, credit_score):
        """
        Initializes the LoanCalculator object.

        Args:
        ----
        loan_amount (float): The amount borrowed by the user.
        interest_rate (float): The annual interest rate of the loan.
        fees (float): The total fees associated with the loan.
        loan_term (int): The term of the loan in years.
        credit_score (int): The borrower's current credit score.

        Raises:
        ------
        ValueError: If any of the input values are invalid.
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if fees < 0:
            raise ValueError("Fees cannot be negative.")
        if loan_term <= 0:
            raise ValueError("Loan term must be greater than zero.")
        if credit_score < 300 or credit_score > 850:
            raise ValueError("Credit score must be between 300 and 850.")

        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert to decimal
        self.fees = fees
        self.loan_term = loan_term
        self.credit_score = credit_score

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment amount.

        Returns:
        -------
        float: The monthly payment amount.
        """
        monthly_interest_rate = self.interest_rate / 12
        months = self.loan_term * 12
        monthly_payment = (self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / (
                (1 + monthly_interest_rate) ** months - 1)
        return round(monthly_payment, 2)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the loan.

        Returns:
        -------
        float: The total cost of the loan.
        """
        monthly_payment = self.calculate_monthly_payment()
        months = self.loan_term * 12
        total_cost = monthly_payment * months
        return round(total_cost, 2)

    def calculate_credit_score_impact(self):
        """
        Estimates the impact of the loan on the borrower's credit score.

        Returns:
        -------
        str: A description of the estimated impact on the credit score.
        """
        if self.credit_score >= 750:
            return "Good credit score. Loan may not significantly impact credit score."
        elif self.credit_score >= 700:
            return "Fair credit score. Loan may have a moderate impact on credit score."
        else:
            return "Poor credit score. Loan may have a significant negative impact on credit score."


def main():
    try:
        loan_amount = float(input("Enter the loan amount: $"))
        interest_rate = float(input("Enter the annual interest rate (%): "))
        fees = float(input("Enter the total fees: $"))
        loan_term = int(input("Enter the loan term (years): "))
        credit_score = int(input("Enter the borrower's current credit score: "))

        calculator = LoanCalculator(loan_amount, interest_rate, fees, loan_term, credit_score)

        print(f"Monthly payment: ${calculator.calculate_monthly_payment()}")
        print(f"Total cost: ${calculator.calculate_total_cost()}")
        print(f"Credit score impact: {calculator.calculate_credit_score_impact()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
