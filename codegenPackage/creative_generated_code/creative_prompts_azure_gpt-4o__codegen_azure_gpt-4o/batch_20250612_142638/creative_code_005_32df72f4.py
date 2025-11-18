"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Write code to implement risk management strategies for investment portfolios, including stress testing under different market scenarios, as detailed by AIvest Securities Limited.
Generated: DETERMINISTIC_32df72f4ff66dae4
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class PortfolioRiskManager:
    """
    PortfolioRiskManager class implements risk management strategies for investment portfolios.
    Includes stress testing under different market scenarios.
    """

    def __init__(self, portfolio):
        """
        Initialize the PortfolioRiskManager.

        :param portfolio: DataFrame containing portfolio holdings, with columns ['Asset', 'Weight', 'Price']
        """
        self.portfolio = portfolio
        self.validate_portfolio()

    def validate_portfolio(self):
        """
        Validate the input portfolio DataFrame for consistency.

        :raises ValueError: If portfolio data is inconsistent or missing columns.
        """
        required_columns = ['Asset', 'Weight', 'Price']
        if not all(col in self.portfolio.columns for col in required_columns):
            raise ValueError(f"Portfolio must contain the following columns: {required_columns}")
        if not np.isclose(self.portfolio['Weight'].sum(), 1.0, atol=0.001):
            raise ValueError("Portfolio weights must sum to 1.")

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.

        :return: Portfolio value.
        """
        return np.sum(self.portfolio['Weight'] * self.portfolio['Price'])

    def stress_test(self, scenario_changes):
        """
        Perform stress testing by simulating portfolio under given market scenarios.

        :param scenario_changes: Dictionary of asset price changes in percentages (e.g., {'Asset1': -20, 'Asset2': 5})
        :return: DataFrame with stressed portfolio values.
        """
        stressed_portfolio = self.portfolio.copy()
        
        # Apply stress changes to asset prices
        stressed_portfolio['Stressed Price'] = stressed_portfolio.apply(
            lambda row: row['Price'] * (1 + scenario_changes.get(row['Asset'], 0) / 100), axis=1
        )
        
        # Calculate new portfolio value
        stressed_portfolio['Stressed Value'] = stressed_portfolio['Weight'] * stressed_portfolio['Stressed Price']
        stressed_portfolio['Change (%)'] = ((stressed_portfolio['Stressed Price'] - stressed_portfolio['Price']) / stressed_portfolio['Price']) * 100
        
        return stressed_portfolio

    def simulate_market_scenarios(self, scenarios):
        """
        Simulate portfolio under multiple market scenarios.

        :param scenarios: List of dictionaries, each representing a market scenario (e.g., [{'Asset1': -20}, {'Asset2': 10}])
        :return: Dictionary of scenario names mapped to DataFrames with results.
        """
        results = {}
        for i, scenario in enumerate(scenarios):
            scenario_name = f"Scenario {i + 1}"
            results[scenario_name] = self.stress_test(scenario)
        return results


# Example Usage
if __name__ == "__main__":
    # Sample portfolio data
    portfolio_data = pd.DataFrame({
        'Asset': ['Stock A', 'Stock B', 'Stock C'],
        'Weight': [0.5, 0.3, 0.2],
        'Price': [100, 200, 300]
    })

    try:
        # Initialize risk manager
        risk_manager = PortfolioRiskManager(portfolio_data)

        # Define market scenarios
        market_scenarios = [
            {'Stock A': -10, 'Stock B': 5},  # Scenario 1: Stock A drops 10%, Stock B rises 5%
            {'Stock C': -15, 'Stock A': 20}  # Scenario 2: Stock C drops 15%, Stock A rises 20%
        ]

        # Simulate scenarios
        simulation_results = risk_manager.simulate_market_scenarios(market_scenarios)

        # Print results
        for scenario_name, result_df in simulation_results.items():
            print(f"\n{scenario_name}:\n{result_df}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
