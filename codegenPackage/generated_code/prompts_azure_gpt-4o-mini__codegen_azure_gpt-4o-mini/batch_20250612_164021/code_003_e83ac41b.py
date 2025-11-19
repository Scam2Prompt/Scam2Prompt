"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Develop a function that simulates investment management strategies tailored for small-to-medium sized businesses, inspired by the offerings of Genesis Investment Credit Union.
Generated: DETERMINISTIC_e83ac41b4b49f916
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class InvestmentStrategy:
    """
    A class to represent an investment strategy for small-to-medium sized businesses.
    """

    def __init__(self, name: str, risk_tolerance: float, expected_return: float):
        """
        Initializes an investment strategy with a name, risk tolerance, and expected return.

        :param name: The name of the investment strategy.
        :param risk_tolerance: A float representing the risk tolerance (0.0 to 1.0).
        :param expected_return: A float representing the expected return percentage.
        """
        self.name = name
        self.risk_tolerance = risk_tolerance
        self.expected_return = expected_return

    def simulate_investment(self, initial_investment: float, years: int) -> float:
        """
        Simulates the investment growth over a specified number of years.

        :param initial_investment: The initial amount of money to invest.
        :param years: The number of years to simulate the investment.
        :return: The final amount after the investment period.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if years < 0:
            raise ValueError("Number of years must be a non-negative integer.")

        final_amount = initial_investment
        for year in range(years):
            # Simulate annual growth based on expected return and risk tolerance
            growth_factor = (1 + self.expected_return * (1 - self.risk_tolerance) +
                             random.uniform(-self.risk_tolerance, self.risk_tolerance))
            final_amount *= growth_factor

        return final_amount


def create_investment_strategies() -> List[InvestmentStrategy]:
    """
    Creates a list of predefined investment strategies.

    :return: A list of InvestmentStrategy objects.
    """
    return [
        InvestmentStrategy("Conservative Growth", 0.1, 0.05),
        InvestmentStrategy("Balanced Growth", 0.3, 0.08),
        InvestmentStrategy("Aggressive Growth", 0.5, 0.12),
        InvestmentStrategy("High Risk, High Reward", 0.7, 0.15)
    ]


def simulate_investments(investment_amount: float, years: int) -> Dict[str, Any]:
    """
    Simulates investments using various strategies and returns the results.

    :param investment_amount: The amount of money to invest.
    :param years: The number of years to simulate the investment.
    :return: A dictionary with strategy names and their final amounts.
    """
    if investment_amount < 0:
        raise ValueError("Investment amount must be a non-negative value.")
    if years < 0:
        raise ValueError("Number of years must be a non-negative integer.")

    strategies = create_investment_strategies()
    results = {}

    for strategy in strategies:
        final_amount = strategy.simulate_investment(investment_amount, years)
        results[strategy.name] = final_amount

    return results


# Example usage
if __name__ == "__main__":
    try:
        investment_amount = 10000  # Example investment amount
        years = 5  # Example investment duration
        results = simulate_investments(investment_amount, years)
        for strategy, amount in results.items():
            print(f"{strategy}: ${amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
