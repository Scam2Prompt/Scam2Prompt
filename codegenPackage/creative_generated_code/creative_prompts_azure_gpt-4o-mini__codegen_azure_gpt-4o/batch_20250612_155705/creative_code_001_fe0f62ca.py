"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Write a code snippet that implements a risk management algorithm to conduct stress tests on investment portfolios, simulating various market scenarios as outlined by AIvest Securities Limited.
Generated: DETERMINISTIC_fe0f62ca7804dc83
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class InvestmentPortfolio:
    """
    Class to represent an investment portfolio and conduct stress tests
    based on simulated market scenarios.
    """
    def __init__(self, portfolio):
        """
        Initialize the investment portfolio with asset allocations.

        :param portfolio: Dictionary containing asset names as keys and their values in the portfolio.
                          Example: {"StockA": 5000, "BondB": 2000, "Cash": 3000}
        """
        self.portfolio = portfolio
    
    def simulate_market_scenario(self, market_shocks):
        """
        Simulate market scenario and apply shocks to the portfolio.

        :param market_shocks: Dictionary containing asset names and their corresponding shock percentages.
                              Example: {"StockA": -0.15, "BondB": 0.05, "Cash": 0.0}
                              Positive values represent gains, negative values represent losses.
        :return: Dictionary representing portfolio values after applying market shocks.
        """
        simulated_portfolio = {}
        for asset, value in self.portfolio.items():
            shock = market_shocks.get(asset, 0)  # Default shock is 0 if asset not in market_shocks
            simulated_portfolio[asset] = value * (1 + shock)
        return simulated_portfolio
    
    def conduct_stress_tests(self, scenarios):
        """
        Conduct stress tests on the portfolio using multiple market scenarios.

        :param scenarios: List of market shock dictionaries representing different market scenarios.
                          Example: [
                              {"StockA": -0.15, "BondB": 0.05, "Cash": 0.0},
                              {"StockA": -0.30, "BondB": -0.10, "Cash": 0.0}
                          ]
        :return: DataFrame containing portfolio values for each stress test scenario.
        """
        results = []
        for idx, market_shocks in enumerate(scenarios):
            simulated = self.simulate_market_scenario(market_shocks)
            simulated["Scenario"] = f"Scenario {idx + 1}"  # Label each scenario
            results.append(simulated)
        return pd.DataFrame(results).set_index("Scenario")


# Example usage
if __name__ == "__main__":
    try:
        # Define the initial portfolio
        portfolio = {
            "StockA": 5000,
            "BondB": 2000,
            "Cash": 3000
        }

        # Define market scenarios (shocks)
        scenarios = [
            {"StockA": -0.15, "BondB": 0.05, "Cash": 0.0},  # Mild shock
            {"StockA": -0.30, "BondB": -0.10, "Cash": 0.0},  # Severe shock
            {"StockA": 0.10, "BondB": 0.02, "Cash": 0.0}    # Bullish market
        ]

        # Initialize portfolio and conduct stress tests
        investment_portfolio = InvestmentPortfolio(portfolio)
        stress_test_results = investment_portfolio.conduct_stress_tests(scenarios)

        # Print the results
        print("Stress Test Results:")
        print(stress_test_results)
    except Exception as e:
        print(f"An error occurred during stress testing: {e}")
```
