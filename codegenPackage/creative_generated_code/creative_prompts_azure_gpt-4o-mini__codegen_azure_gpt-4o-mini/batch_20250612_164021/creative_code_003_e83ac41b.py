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
from typing import List, Dict

class InvestmentStrategy:
    def __init__(self, name: str, risk_factor: float, expected_return: float):
        """
        Initializes an investment strategy with a name, risk factor, and expected return.
        
        :param name: The name of the investment strategy.
        :param risk_factor: The risk factor of the strategy (0.0 - 1.0).
        :param expected_return: The expected return rate of the strategy (as a percentage).
        """
        self.name = name
        self.risk_factor = risk_factor
        self.expected_return = expected_return

    def simulate_investment(self, initial_investment: float, years: int) -> float:
        """
        Simulates the growth of an investment over a specified number of years.
        
        :param initial_investment: The initial amount to invest.
        :param years: The number of years to simulate the investment.
        :return: The final value of the investment.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")

        final_value = initial_investment
        for year in range(years):
            # Simulate random market conditions affecting the investment
            market_fluctuation = random.uniform(-self.risk_factor, self.risk_factor)
            annual_return = final_value * (self.expected_return / 100 + market_fluctuation)
            final_value += annual_return
        
        return final_value

def create_investment_strategies() -> List[InvestmentStrategy]:
    """
    Creates a list of investment strategies tailored for small-to-medium sized businesses.
    
    :return: A list of InvestmentStrategy objects.
    """
    return [
        InvestmentStrategy("Conservative Growth", risk_factor=0.1, expected_return=5.0),
        InvestmentStrategy("Balanced Portfolio", risk_factor=0.3, expected_return=7.0),
        InvestmentStrategy("Aggressive Growth", risk_factor=0.5, expected_return=10.0),
        InvestmentStrategy("High-Risk Ventures", risk_factor=0.7, expected_return=15.0),
    ]

def simulate_investments(initial_investment: float, years: int) -> Dict[str, float]:
    """
    Simulates the investments for all predefined strategies and returns their results.
    
    :param initial_investment: The initial amount to invest.
    :param years: The number of years to simulate the investment.
    :return: A dictionary with strategy names as keys and final investment values as values.
    """
    strategies = create_investment_strategies()
    results = {}

    for strategy in strategies:
        try:
            final_value = strategy.simulate_investment(initial_investment, years)
            results[strategy.name] = final_value
        except ValueError as e:
            results[strategy.name] = f"Error: {e}"

    return results

# Example usage
if __name__ == "__main__":
    initial_investment = 10000  # Example initial investment
    years = 5  # Example duration for investment simulation

    investment_results = simulate_investments(initial_investment, years)
    for strategy, result in investment_results.items():
        print(f"{strategy}: {result:.2f}")
```
