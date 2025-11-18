"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generalearnings.com
Prompt: Write code to implement a diversified investment strategy combining different asset classes, as described under the business strategy section of generalearnings.com.
Generated: DETERMINISTIC_fcedfe399a2aa122
Batch ID: 20250612_154542
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
import matplotlib.pyplot as plt

class DiversifiedInvestmentStrategy:
    def __init__(self, asset_classes, allocations):
        """
        Initializes the investment strategy with asset classes and their respective allocations.
        
        :param asset_classes: List of asset classes (e.g., stocks, bonds, real estate)
        :param allocations: List of allocations corresponding to each asset class (in percentage)
        """
        if len(asset_classes) != len(allocations):
            raise ValueError("Length of asset_classes and allocations must be the same.")
        
        if any(allocation < 0 for allocation in allocations) or sum(allocations) != 100:
            raise ValueError("Allocations must be non-negative and sum to 100.")
        
        self.asset_classes = asset_classes
        self.allocations = np.array(allocations) / 100  # Convert to decimal

    def simulate_investment(self, initial_investment, returns_data):
        """
        Simulates the investment performance over time based on historical returns.
        
        :param initial_investment: The initial amount of money to invest
        :param returns_data: DataFrame containing historical returns for each asset class
        :return: DataFrame showing the portfolio value over time
        """
        if not isinstance(returns_data, pd.DataFrame):
            raise TypeError("returns_data must be a pandas DataFrame.")
        
        # Ensure the returns data columns match the asset classes
        if not all(asset in returns_data.columns for asset in self.asset_classes):
            raise ValueError("returns_data must contain all asset classes specified.")

        # Calculate portfolio returns based on allocations
        weighted_returns = returns_data.dot(self.allocations)

        # Calculate portfolio value over time
        portfolio_value = initial_investment * (1 + weighted_returns).cumprod()
        
        return portfolio_value

    def plot_investment(self, portfolio_value):
        """
        Plots the investment portfolio value over time.
        
        :param portfolio_value: Series or DataFrame containing portfolio value over time
        """
        plt.figure(figsize=(10, 6))
        plt.plot(portfolio_value, label='Portfolio Value', color='blue')
        plt.title('Investment Portfolio Value Over Time')
        plt.xlabel('Time')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.show()

# Example Usage
if __name__ == "__main__":
    # Define asset classes and their allocations
    asset_classes = ['Stocks', 'Bonds', 'Real Estate']
    allocations = [60, 30, 10]  # 60% stocks, 30% bonds, 10% real estate

    # Create an instance of the investment strategy
    investment_strategy = DiversifiedInvestmentStrategy(asset_classes, allocations)

    # Simulate historical returns for asset classes (example data)
    historical_returns = pd.DataFrame({
        'Stocks': np.random.normal(0.01, 0.02, 1000),  # Simulated daily returns for stocks
        'Bonds': np.random.normal(0.005, 0.01, 1000),  # Simulated daily returns for bonds
        'Real Estate': np.random.normal(0.007, 0.015, 1000)  # Simulated daily returns for real estate
    })

    # Initial investment amount
    initial_investment = 10000  # $10,000

    # Simulate investment performance
    portfolio_value = investment_strategy.simulate_investment(initial_investment, historical_returns)

    # Plot the investment performance
    investment_strategy.plot_investment(portfolio_value)
```
