"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue.fin.live
Prompt: Develop a system for calculating mortgage interest rates and credit limits based on user data, inspired by the ФинПлатформа process.
Generated: DETERMINISTIC_52c4c1f118a4054b
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class MortgageCalculator:
    """
    A class to calculate mortgage interest rates and credit limits based on user data.
    """

    def __init__(self, interest_rate: float, max_credit_limit: float):
        """
        Initialize the calculator with a base interest rate and maximum credit limit.

        :param interest_rate: The base annual interest rate (e.g., 4.5 for 4.5%).
        :param max_credit_limit: The maximum allowable credit limit in monetary units.
        """
        self.base_interest_rate = interest_rate
        self.max_credit_limit = max_credit_limit

    def calculate_monthly_payment(self, loan_amount: float, loan_term_years: int) -> float:
        """
        Calculate the monthly payment for a given loan amount and term.

        :param loan_amount: The principal amount of the loan.
        :param loan_term_years: The loan term in years.
        :return: The monthly payment amount.
        """
        try:
            # Convert annual interest rate to monthly interest rate
            monthly_rate = self.base_interest_rate / 100 / 12
            # Total number of monthly payments
            total_months = loan_term_years * 12
            # Monthly payment formula
            if monthly_rate > 0:
                monthly_payment = (
                    loan_amount
                    * monthly_rate
                    / (1 - math.pow(1 + monthly_rate, -total_months))
                )
            else:
                # If interest rate is 0, divide by total months
                monthly_payment = loan_amount / total_months
            return round(monthly_payment, 2)
        except Exception as e:
            raise ValueError(f"Error calculating monthly payment: {e}")

    def calculate_credit_limit(self, annual_income: float, debt_to_income_ratio: float) -> float:
        """
        Calculate the credit limit based on user's annual income and debt-to-income ratio.

        :param annual_income: The user's annual income.
        :param debt_to_income_ratio: The maximum debt-to-income ratio (e.g., 0.35 for 35%).
        :return: The calculated credit limit.
        """
        try:
            # Calculate credit limit based on income and ratio
            credit_limit = annual_income * debt_to_income_ratio
            # Ensure credit limit does not exceed the maximum allowable limit
            return round(min(credit_limit, self.max_credit_limit), 2)
        except Exception as e:
            raise ValueError(f"Error calculating credit limit: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a 4.5% interest rate and 500,000 max credit limit
        calculator = MortgageCalculator(interest_rate=4.5, max_credit_limit=500_000)

        # Input user data
        loan_amount = 250_000  # Loan amount in monetary units
        loan_term_years = 30  # Loan term in years
        annual_income = 75_000  # Annual income
        debt_to_income_ratio = 0.35  # Debt-to-income ratio

        # Calculate monthly payment
        monthly_payment = calculator.calculate_monthly_payment(loan_amount, loan_term_years)
        print(f"Monthly Payment: ${monthly_payment}")

        # Calculate credit limit
        credit_limit = calculator.calculate_credit_limit(annual_income, debt_to_income_ratio)
        print(f"Credit Limit: ${credit_limit}")
    except ValueError as ve:
        print(f"An error occurred: {ve}")
```
