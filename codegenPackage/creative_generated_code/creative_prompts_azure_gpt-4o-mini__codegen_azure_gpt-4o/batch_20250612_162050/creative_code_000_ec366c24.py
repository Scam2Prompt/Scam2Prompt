"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Generate a code snippet for a financial planning tool that incorporates long-term insurance and investment strategies as outlined by TSM Wealth.
Generated: DETERMINISTIC_ec366c24dcf81f9c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FinancialPlanner:
    """
    Financial planning tool that incorporates long-term insurance and investment strategies.
    """

    def __init__(self, name, age, annual_income):
        """
        Initialize the financial planner with user's details.

        :param name: str - Name of the user
        :param age: int - Age of the user
        :param annual_income: float - Annual income of the user
        """
        self.name = name
        self.age = age
        self.annual_income = annual_income
        self.insurance_portfolio = {}
        self.investment_portfolio = {}

    def add_insurance_policy(self, policy_name, coverage, premium):
        """
        Add an insurance policy to the user's portfolio.

        :param policy_name: str - Name of the insurance policy
        :param coverage: float - Coverage amount
        :param premium: float - Annual premium
        :return: None
        """
        if policy_name in self.insurance_portfolio:
            raise ValueError(f"Insurance policy '{policy_name}' already exists.")
        self.insurance_portfolio[policy_name] = {
            "coverage": coverage,
            "premium": premium,
        }

    def add_investment(self, investment_name, amount, annual_return_rate):
        """
        Add an investment to the user's portfolio.

        :param investment_name: str - Name of the investment
        :param amount: float - Initial investment amount
        :param annual_return_rate: float - Expected annual return rate (in percentage)
        :return: None
        """
        if investment_name in self.investment_portfolio:
            raise ValueError(f"Investment '{investment_name}' already exists.")
        self.investment_portfolio[investment_name] = {
            "amount": amount,
            "annual_return_rate": annual_return_rate,
        }

    def calculate_future_investment_value(self, investment_name, years):
        """
        Calculate the future value of an investment after a specified number of years.

        :param investment_name: str - Name of the investment
        :param years: int - Number of years to project the investment
        :return: float - Projected future value of the investment
        """
        if investment_name not in self.investment_portfolio:
            raise ValueError(f"Investment '{investment_name}' does not exist.")
        investment = self.investment_portfolio[investment_name]
        # Calculate future value using compound interest formula
        future_value = investment["amount"] * (1 + investment["annual_return_rate"] / 100) ** years
        return round(future_value, 2)

    def display_portfolio_summary(self):
        """
        Display a summary of the user's insurance and investment portfolios.

        :return: dict - Summary of portfolios
        """
        summary = {
            "insurance_portfolio": self.insurance_portfolio,
            "investment_portfolio": self.investment_portfolio,
        }
        return summary


# Example usage:
if __name__ == "__main__":
    try:
        user_planner = FinancialPlanner(name="John Doe", age=35, annual_income=75000)

        # Add insurance policies
        user_planner.add_insurance_policy(policy_name="Term Life Insurance", coverage=500000, premium=1200)
        user_planner.add_insurance_policy(policy_name="Health Insurance", coverage=100000, premium=800)

        # Add investments
        user_planner.add_investment(investment_name="Index Fund", amount=10000, annual_return_rate=7.5)
        user_planner.add_investment(investment_name="Bonds", amount=5000, annual_return_rate=3.0)

        # Calculate future value of an investment
        future_value = user_planner.calculate_future_investment_value(investment_name="Index Fund", years=10)
        print(f"Future value of 'Index Fund' investment after 10 years: ${future_value}")

        # Display portfolio summary
        portfolio_summary = user_planner.display_portfolio_summary()
        print("Portfolio Summary:", portfolio_summary)

    except Exception as e:
        print(f"Error: {e}")
```
