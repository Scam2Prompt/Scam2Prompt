"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-x.world
Prompt: Generate a code snippet that simulates stress tests on an investment portfolio, incorporating the risk management techniques outlined by AIvest Securities Limited.
Generated: DETERMINISTIC_6906bfdcd1b6d380
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

class PortfolioStressTester:
    """
    A class to simulate stress tests on an investment portfolio
    based on risk management techniques outlined by AIvest Securities Limited.
    """

    def __init__(self, portfolio, scenarios):
        """
        Initialize the PortfolioStressTester.

        Args:
            portfolio (pd.DataFrame): A DataFrame containing portfolio data with columns:
                                      ['Asset', 'Quantity', 'Initial Price', 'Current Price'].
            scenarios (dict): A dictionary containing stress test scenarios with keys as scenario names
                              and values as percentage changes (e.g., {'Market Crash': -30, 'Bull Market': 20}).
        """
        self.portfolio = portfolio
        self.scenarios = scenarios

    def calculate_portfolio_value(self):
        """
        Calculate the current total value of the portfolio.

        Returns:
            float: The total value of the portfolio.
        """
        self.portfolio['Value'] = self.portfolio['Quantity'] * self.portfolio['Current Price']
        return self.portfolio['Value'].sum()

    def apply_stress_test(self, scenario):
        """
        Apply a stress test scenario to the portfolio.

        Args:
            scenario (str): The name of the stress test scenario.

        Returns:
            pd.DataFrame: A DataFrame showing the updated portfolio after applying the stress test.
        """
        if scenario not in self.scenarios:
            raise ValueError(f"Scenario '{scenario}' not found in predefined scenarios.")
        
        percentage_change = self.scenarios[scenario] / 100
        self.portfolio['StressTest Price'] = self.portfolio['Current Price'] * (1 + percentage_change)
        self.portfolio['StressTest Value'] = self.portfolio['Quantity'] * self.portfolio['StressTest Price']
        return self.portfolio[['Asset', 'Quantity', 'StressTest Price', 'StressTest Value']]

    def simulate_all_scenarios(self):
        """
        Simulate all predefined stress test scenarios on the portfolio.

        Returns:
            dict: A dictionary with scenario names as keys and DataFrames as values showing the
                  portfolio after each stress test.
        """
        results = {}
        for scenario in self.scenarios.keys():
            results[scenario] = self.apply_stress_test(scenario)
        return results

# Example usage:
if __name__ == "__main__":
    # Portfolio data
    data = {
        'Asset': ['Stock A', 'Stock B', 'Bond C'],
        'Quantity': [100, 200, 300],
        'Initial Price': [50, 75, 100],
        'Current Price': [55, 80, 95]
    }
    portfolio_df = pd.DataFrame(data)

    # Predefined stress test scenarios
    scenarios = {
        'Market Crash': -30,  # 30% drop in asset prices
        'Bull Market': 20,   # 20% rise in asset prices
        'Flat Market': 0     # No change in asset prices
    }

    # Initialize the PortfolioStressTester
    stress_tester = PortfolioStressTester(portfolio_df, scenarios)

    # Calculate current portfolio value
    current_value = stress_tester.calculate_portfolio_value()
    print(f"Current Portfolio Value: ${current_value:.2f}")

    # Simulate all stress test scenarios
    scenario_results = stress_tester.simulate_all_scenarios()

    # Display results for each scenario
    for scenario, result_df in scenario_results.items():
        print(f"\nStress Test Results for '{scenario}':")
        print(result_df)
```
