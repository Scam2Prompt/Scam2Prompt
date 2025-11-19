"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Develop a risk management system that conducts stress tests on investment portfolios, simulating investment performance under different market scenarios, inspired by AIvest Securities Limited's risk management approach.
Generated: DETERMINISTIC_1f7c3fc28cc14d75
Batch ID: 20250622_211144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class RiskManagementSystem:
    """
    A Risk Management System for conducting stress tests on investment portfolios.
    Simulates investment performance under different market scenarios.
    """

    def __init__(self, portfolio):
        """
        Initialize the risk management system with a portfolio.

        :param portfolio: dict
            A dictionary representing the portfolio with asset names as keys and their values as values.
        """
        self.portfolio = portfolio
        self.market_scenarios = []

    def add_market_scenario(self, name, shock_factors):
        """
        Add a market scenario for stress testing.

        :param name: str
            Name of the market scenario.
        :param shock_factors: dict
            A dictionary with asset names as keys and shock factors (percentage changes) as values.
        """
        self.market_scenarios.append({"name": name, "shock_factors": shock_factors})

    def simulate_scenario(self, scenario):
        """
        Simulate the portfolio performance under a given market scenario.

        :param scenario: dict
            A market scenario with shock factors.
        :return: dict
            A dictionary representing the portfolio value after applying the scenario.
        """
        simulated_portfolio = {}
        for asset, value in self.portfolio.items():
            shock_factor = scenario["shock_factors"].get(asset, 0)  # Default to 0 if asset not in scenario
            simulated_value = value * (1 + shock_factor / 100)  # Apply shock factor
            simulated_portfolio[asset] = simulated_value
        return simulated_portfolio

    def run_stress_tests(self):
        """
        Run stress tests for all added market scenarios.

        :return: pd.DataFrame
            A DataFrame summarizing the portfolio performance under each scenario.
        """
        results = []
        for scenario in self.market_scenarios:
            simulated_portfolio = self.simulate_scenario(scenario)
            total_value = sum(simulated_portfolio.values())
            results.append({
                "Scenario": scenario["name"],
                "Simulated Portfolio": simulated_portfolio,
                "Total Value": total_value
            })
        return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    try:
        # Define the initial portfolio
        portfolio = {
            "Stock A": 100000,
            "Stock B": 150000,
            "Bond C": 200000,
            "Real Estate D": 300000
        }

        # Initialize the risk management system
        rms = RiskManagementSystem(portfolio)

        # Add market scenarios
        rms.add_market_scenario("Recession", {"Stock A": -20, "Stock B": -25, "Bond C": -10, "Real Estate D": -15})
        rms.add_market_scenario("Bull Market", {"Stock A": 30, "Stock B": 40, "Bond C": 5, "Real Estate D": 20})
        rms.add_market_scenario("Inflation Spike", {"Stock A": -10, "Stock B": -15, "Bond C": -5, "Real Estate D": -20})

        # Run stress tests
        results = rms.run_stress_tests()

        # Display results
        print("Stress Test Results:")
        print(results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
