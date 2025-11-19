"""
Generated Code Metadata:
========================
Original URL: https://cryptosolutionz.com
Prompt: Create a Python script to generate personalized trading plans based on user-defined risk appetite and investment goals, similar to the custom strategies discussed on Crypto Solutionz.
Generated: DETERMINISTIC_5ba043c4178172f4
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TradingPlan:
    def __init__(self, risk_appetite, investment_goals):
        """
        Initialize the TradingPlan with user-defined risk appetite and investment goals.

        :param risk_appetite: str, user's risk appetite (e.g., 'low', 'medium', 'high')
        :param investment_goals: list, user's investment goals (e.g., ['short-term', 'long-term'])
        """
        self.risk_appetite = risk_appetite.lower()
        self.investment_goals = investment_goals
        self.strategy = self.generate_strategy()

    def generate_strategy(self):
        """
        Generate a trading strategy based on risk appetite and investment goals.

        :return: dict, a trading strategy
        """
        strategy = {
            'risk_appetite': self.risk_appetite,
            'investment_goals': self.investment_goals,
            'recommended_assets': self.recommend_assets(),
            'allocation': self.allocate_investment()
        }
        return strategy

    def recommend_assets(self):
        """
        Recommend assets based on risk appetite.

        :return: list, recommended assets
        """
        if self.risk_appetite == 'low':
            return ['Bonds', 'Stablecoins']
        elif self.risk_appetite == 'medium':
            return ['Index Funds', 'Blue-chip Stocks']
        elif self.risk_appetite == 'high':
            return ['Cryptocurrencies', 'Tech Stocks']
        else:
            raise ValueError("Invalid risk appetite. Choose 'low', 'medium', or 'high'.")

    def allocate_investment(self):
        """
        Allocate investment based on risk appetite.

        :return: dict, asset allocation
        """
        allocation = {}
        if self.risk_appetite == 'low':
            allocation = {'Bonds': 70, 'Stablecoins': 30}
        elif self.risk_appetite == 'medium':
            allocation = {'Index Funds': 50, 'Blue-chip Stocks': 30, 'Bonds': 20}
        elif self.risk_appetite == 'high':
            allocation = {'Cryptocurrencies': 60, 'Tech Stocks': 40}
        return allocation

    def to_json(self):
        """
        Convert the trading plan to a JSON string.

        :return: str, JSON representation of the trading plan
        """
        return json.dumps(self.strategy, indent=4)

def main():
    """
    Main function to execute the trading plan generation.
    """
    try:
        # User input for risk appetite and investment goals
        risk_appetite = input("Enter your risk appetite (low, medium, high): ")
        investment_goals = input("Enter your investment goals (comma-separated): ").split(',')

        # Create a TradingPlan instance
        trading_plan = TradingPlan(risk_appetite, [goal.strip() for goal in investment_goals])

        # Output the generated trading plan
        print("Your personalized trading plan:")
        print(trading_plan.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
