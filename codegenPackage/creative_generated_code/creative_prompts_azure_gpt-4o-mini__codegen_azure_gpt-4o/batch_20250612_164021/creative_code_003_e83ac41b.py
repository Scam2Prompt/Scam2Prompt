"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Develop a function that simulates investment management strategies tailored for small-to-medium sized businesses, inspired by the offerings of Genesis Investment Credit Union.
Generated: DETERMINISTIC_e83ac41b4b49f916
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentStrategy:
    """
    A class to simulate investment management strategies tailored for small-to-medium sized businesses.
    Inspired by Genesis Investment Credit Union.
    """
    
    def __init__(self, initial_investment, risk_tolerance, investment_horizon):
        """
        Initialize the investment strategy with the given parameters.

        :param initial_investment: float - The starting amount to be invested.
        :param risk_tolerance: str - Risk tolerance level ('low', 'medium', 'high').
        :param investment_horizon: int - Investment horizon in years.
        """
        if initial_investment <= 0 or investment_horizon <= 0:
            raise ValueError("Initial investment and investment horizon must be positive numbers.")
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")

        self.initial_investment = initial_investment
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.portfolio = {"stocks": 0, "bonds": 0, "cash": 0}  # Portfolio allocation

    def allocate_portfolio(self):
        """
        Allocate portfolio based on risk tolerance.
        """
        if self.risk_tolerance == 'low':
            self.portfolio = {"stocks": 30, "bonds": 50, "cash": 20}
        elif self.risk_tolerance == 'medium':
            self.portfolio = {"stocks": 50, "bonds": 40, "cash": 10}
        elif self.risk_tolerance == 'high':
            self.portfolio = {"stocks": 70, "bonds": 20, "cash": 10}

    def simulate_growth(self):
        """
        Simulate the growth of the investment over the investment horizon.

        :return: float - Final investment value after the simulation.
        """
        annual_growth_rates = {
            "stocks": {"low": 0.06, "medium": 0.08, "high": 0.12},
            "bonds": {"low": 0.03, "medium": 0.04, "high": 0.06},
            "cash": {"low": 0.01, "medium": 0.01, "high": 0.01},
        }

        growth_rate = lambda asset: annual_growth_rates[asset][self.risk_tolerance] + random.uniform(-0.02, 0.02)
        investment_value = self.initial_investment

        for year in range(self.investment_horizon):
            yearly_growth = sum(
                (self.portfolio[asset] / 100) * investment_value * growth_rate(asset)
                for asset in self.portfolio
            )
            investment_value += yearly_growth

        return round(investment_value, 2)

    def display_recommendations(self):
        """
        Display investment strategy recommendations.

        :return: dict - A summary of the recommendations.
        """
        self.allocate_portfolio()
        final_value = self.simulate_growth()

        return {
            "initial_investment": self.initial_investment,
            "investment_horizon": self.investment_horizon,
            "risk_tolerance": self.risk_tolerance,
            "portfolio_allocation": self.portfolio,
            "simulated_final_value": final_value,
        }


def manage_investment(initial_investment, risk_tolerance, investment_horizon):
    """
    Function to simulate investment management strategies for small-to-medium sized businesses.

    :param initial_investment: float - The starting investment amount.
    :param risk_tolerance: str - Risk tolerance level ('low', 'medium', 'high').
    :param investment_horizon: int - Investment horizon in years.
    :return: dict - Summary of simulated recommendations.
    """
    try:
        strategy = InvestmentStrategy(initial_investment, risk_tolerance, investment_horizon)
        recommendations = strategy.display_recommendations()
        return recommendations
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
# Uncomment the lines below to test the function.
# result = manage_investment(10000, 'medium', 5)
# print(result)
```
