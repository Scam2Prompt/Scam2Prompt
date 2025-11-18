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
class MortgageCalculator:
    """
    A class to calculate mortgage interest rates and credit limits based on user data.
    """

    def __init__(self, credit_score: int, annual_income: float, loan_amount: float):
        """
        Initialize the MortgageCalculator with user's credit score, annual income, and loan amount.

        :param credit_score: User's credit score (0-850)
        :param annual_income: User's annual income in currency units
        :param loan_amount: Desired loan amount in currency units
        """
        self.credit_score = credit_score
        self.annual_income = annual_income
        self.loan_amount = loan_amount

    def calculate_interest_rate(self) -> float:
        """
        Calculate the mortgage interest rate based on credit score.

        :return: Interest rate as a percentage.
        """
        if self.credit_score < 300 or self.credit_score > 850:
            raise ValueError("Credit score must be between 300 and 850.")

        if self.credit_score >= 750:
            return 3.0
        elif self.credit_score >= 700:
            return 3.5
        elif self.credit_score >= 650:
            return 4.0
        elif self.credit_score >= 600:
            return 4.5
        else:
            return 5.0

    def calculate_credit_limit(self) -> float:
        """
        Calculate the credit limit based on annual income and loan amount.

        :return: Credit limit in currency units.
        """
        if self.annual_income <= 0:
            raise ValueError("Annual income must be greater than zero.")

        # A basic heuristic for determining credit limit
        credit_limit = self.annual_income * 5
        if self.loan_amount > credit_limit:
            raise ValueError("Loan amount exceeds calculated credit limit.")
        return credit_limit

    def get_mortgage_details(self) -> dict:
        """
        Get the mortgage details including interest rate and credit limit.

        :return: A dictionary containing interest rate and credit limit.
        """
        try:
            interest_rate = self.calculate_interest_rate()
            credit_limit = self.calculate_credit_limit()
            return {
                "interest_rate": interest_rate,
                "credit_limit": credit_limit,
            }
        except ValueError as e:
            return {"error": str(e)}


# Example of using the MortgageCalculator
if __name__ == "__main__":
    # User input simulation
    user_credit_score = 720  # Example credit score
    user_annual_income = 60000  # Example annual income
    user_loan_amount = 250000  # Example loan amount

    mortgage_calculator = MortgageCalculator(user_credit_score, user_annual_income, user_loan_amount)
    mortgage_details = mortgage_calculator.get_mortgage_details()

    print(mortgage_details)
```
