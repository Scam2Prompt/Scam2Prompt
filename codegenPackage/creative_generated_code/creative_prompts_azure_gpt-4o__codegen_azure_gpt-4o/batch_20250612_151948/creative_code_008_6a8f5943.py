"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamondhand.pages.dev
Prompt: Create a program that tracks and evaluates portfolio performance metrics, including identifying trends and optimizing airdrop strategies, based on the insights section of the HALO webpage.
Generated: DETERMINISTIC_6a8f594389a88f25
Batch ID: 20250612_151948
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


class PortfolioPerformanceTracker:
    def __init__(self, portfolio_data):
        """
        Initialize the portfolio tracker with portfolio data.

        :param portfolio_data: DataFrame containing portfolio data. It is expected to have columns:
            - 'asset': name of the asset
            - 'date': date of the performance metric
            - 'price': price of the asset
            - 'quantity': quantity of the asset held
            - 'value': total value of the asset (price * quantity)
        """
        if not isinstance(portfolio_data, pd.DataFrame):
            raise ValueError("portfolio_data must be a pandas DataFrame")
        self.portfolio_data = portfolio_data

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio over time.

        :return: DataFrame with total portfolio values grouped by date.
        """
        try:
            portfolio_values = self.portfolio_data.groupby('date')['value'].sum().reset_index()
            portfolio_values.rename(columns={'value': 'portfolio_value'}, inplace=True)
            return portfolio_values
        except Exception as e:
            raise RuntimeError(f"Error calculating portfolio value: {e}")

    def identify_price_trends(self):
        """
        Identify trends in asset prices.

        :return: Dictionary where keys are asset names and values are trend indicators ('uptrend', 'downtrend', 'neutral').
        """
        try:
            trends = {}
            for asset in self.portfolio_data['asset'].unique():
                asset_data = self.portfolio_data[self.portfolio_data['asset'] == asset]
                asset_prices = asset_data.sort_values('date')['price']  # Sort prices by date

                if len(asset_prices) < 2:
                    trends[asset] = 'neutral'  # Not enough data to identify a trend
                else:
                    price_change = asset_prices.iloc[-1] - asset_prices.iloc[0]
                    if price_change > 0:
                        trends[asset] = 'uptrend'
                    elif price_change < 0:
                        trends[asset] = 'downtrend'
                    else:
                        trends[asset] = 'neutral'

            return trends
        except Exception as e:
            raise RuntimeError(f"Error identifying price trends: {e}")

    def optimize_airdrop_strategy(self, airdrop_budget):
        """
        Optimize airdrop strategy based on asset performance.

        :param airdrop_budget: Total budget for the airdrop (in monetary value).
        :return: DataFrame indicating optimal allocation for airdrop across assets.
        """
        try:
            # Calculate asset values as a percentage of the total portfolio value
            total_value = self.portfolio_data['value'].sum()
            self.portfolio_data['allocation_percentage'] = (
                self.portfolio_data['value'] / total_value
            )

            # Allocate the airdrop budget proportionally to the allocation percentage
            self.portfolio_data['airdrop_allocation'] = (
                self.portfolio_data['allocation_percentage'] * airdrop_budget
            )

            # Return the allocation grouped by asset
            optimal_allocation = self.portfolio_data.groupby('asset')[['airdrop_allocation']].sum().reset_index()
            return optimal_allocation
        except Exception as e:
            raise RuntimeError(f"Error optimizing airdrop strategy: {e}")


# Example usage
if __name__ == "__main__":
    # Sample portfolio data
    portfolio_data = pd.DataFrame({
        'asset': ['BTC', 'ETH', 'BTC', 'ETH', 'SOL', 'SOL'],
        'date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01', '2023-01-01', '2023-02-01'],
        'price': [50000, 4000, 55000, 4100, 200, 220],
        'quantity': [1, 5, 1, 5, 20, 20],
        'value': [50000, 20000, 55000, 20500, 4000, 4400],
    })

    tracker = PortfolioPerformanceTracker(portfolio_data)

    # Calculate portfolio value over time
    portfolio_values = tracker.calculate_portfolio_value()
    print("Portfolio Values Over Time:")
    print(portfolio_values)

    # Identify price trends
    price_trends = tracker.identify_price_trends()
    print("\nPrice Trends:")
    print(price_trends)

    # Optimize airdrop strategy
    airdrop_budget = 10000  # Example budget
    optimal_airdrop_allocation = tracker.optimize_airdrop_strategy(airdrop_budget)
    print("\nOptimal Airdrop Allocation:")
    print(optimal_airdrop_allocation)
```
