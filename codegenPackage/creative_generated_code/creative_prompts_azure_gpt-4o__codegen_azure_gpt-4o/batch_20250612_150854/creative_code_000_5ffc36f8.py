"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecore.co
Prompt: Write Python code to simulate an investment portfolio using Immediate Core's interactive learning tools, incorporating risk management strategies like diversification and asset allocation.
Generated: DETERMINISTIC_5ffc36f8232b2af0
Batch ID: 20250612_150854
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
    A class to simulate and manage an investment portfolio using risk management strategies such as
    diversification and asset allocation.
    """

    def __init__(self, initial_capital, assets, allocations):
        """
        Initializes the investment portfolio.

        :param initial_capital: Float, the total initial capital to invest.
        :param assets: Dict, asset names and their historical returns as DataFrame.
        :param allocations: Dict, asset names and their allocation percentages.
        """
        self.initial_capital = initial_capital
        self.assets = assets
        self.allocations = allocations
        self.portfolio_value = initial_capital
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates inputs to ensure allocations sum to 100% and asset data is provided correctly.
        Raises ValueError for invalid inputs.
        """
        if not np.isclose(sum(self.allocations.values()), 100, atol=1e-2):
            raise ValueError("Allocations must sum to 100%. Check the allocation values.")
        for asset, data in self.assets.items():
            if not isinstance(data, pd.DataFrame) or 'returns' not in data.columns:
                raise ValueError(f"Asset '{asset}' must have a DataFrame with a 'returns' column.")

    def simulate(self, num_days):
        """
        Simulates portfolio performance over a specified number of days using historical returns.

        :param num_days: Integer, number of days to simulate.
        :return: DataFrame, simulated portfolio values over time.
        """
        # Initialize portfolio performance tracking
        simulation_results = pd.DataFrame(index=range(num_days), columns=['Portfolio Value'])
        simulation_results.iloc[0] = self.portfolio_value

        # Simulate daily portfolio performance
        for day in range(1, num_days):
            daily_return = 0
            for asset, allocation in self.allocations.items():
                asset_data = self.assets[asset]
                # Randomly sample daily return for this asset
                daily_asset_return = asset_data['returns'].sample().values[0]
                weighted_return = (allocation / 100) * daily_asset_return
                daily_return += weighted_return
            self.portfolio_value *= (1 + daily_return)
            simulation_results.iloc[day] = self.portfolio_value

        return simulation_results

    def risk_analysis(self):
        """
        Performs basic risk analysis on the portfolio.

        :return: Dict, containing risk metrics such as portfolio volatility and Sharpe ratio.
        """
        portfolio_returns = []
        for asset, allocation in self.allocations.items():
            asset_data = self.assets[asset]
            # Weighted returns for the asset
            weighted_returns = (allocation / 100) * asset_data['returns']
            portfolio_returns.append(weighted_returns)

        # Combine weighted returns for all assets
        portfolio_returns = pd.concat(portfolio_returns, axis=1).sum(axis=1)
        portfolio_volatility = portfolio_returns.std()
        portfolio_mean_return = portfolio_returns.mean()
        risk_free_rate = 0.02 / 252  # Daily risk-free rate (assuming 2% annualized)

        # Calculate Sharpe Ratio
        sharpe_ratio = (portfolio_mean_return - risk_free_rate) / portfolio_volatility

        return {
            'Volatility': portfolio_volatility,
            'Mean Return': portfolio_mean_return,
            'Sharpe Ratio': sharpe_ratio
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Example historical return data for assets
        asset_data_1 = pd.DataFrame({'returns': np.random.normal(0.0005, 0.02, 1000)})  # Asset 1
        asset_data_2 = pd.DataFrame({'returns': np.random.normal(0.0003, 0.01, 1000)})  # Asset 2

        # Define assets and allocations
        assets = {'Asset1': asset_data_1, 'Asset2': asset_data_2}
        allocations = {'Asset1': 60, 'Asset2': 40}

        # Initialize portfolio
        portfolio = InvestmentPortfolio(initial_capital=100000, assets=assets, allocations=allocations)

        # Simulate portfolio performance over 100 days
        simulation_results = portfolio.simulate(num_days=100)
        print("Simulation Results:")
        print(simulation_results)

        # Perform risk analysis
        risk_metrics = portfolio.risk_analysis()
        print("\nRisk Analysis:")
        print(risk_metrics)

    except Exception as e:
        print(f"An error occurred: {e}")
```
