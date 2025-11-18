"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Write a script to simulate recurrent buying patterns for assets, as described in SyncExpertTrade's trading strategy, using historical price data.
Generated: DETERMINISTIC_cfd6643fae4f44d1
Batch ID: 20250612_154622
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
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RecurrentBuyingSimulation:
    """
    Class to simulate recurrent buying patterns for assets using historical price data.
    """

    def __init__(self, data: pd.DataFrame, initial_balance: float, buy_interval_days: int, buy_percentage: float):
        """
        Initialize the simulation parameters.

        :param data: DataFrame containing historical price data with at least a 'date' and 'price' column.
        :param initial_balance: The starting balance for the simulation.
        :param buy_interval_days: Number of days between each asset purchase.
        :param buy_percentage: Percentage of current balance to allocate for buying assets.
        """
        self.data = data
        self.initial_balance = initial_balance
        self.buy_interval_days = buy_interval_days
        self.buy_percentage = buy_percentage
        self.current_balance = initial_balance
        self.asset_holdings = 0.0
        self.last_buy_date = None

    def simulate(self):
        """
        Run the buying simulation based on the defined strategy.
        :return: A DataFrame with simulation results.
        """
        results = []
        
        # Sort data by date to ensure proper chronological order
        self.data.sort_values(by='date', inplace=True)

        # Loop through historical data
        for index, row in self.data.iterrows():
            date = pd.to_datetime(row['date'])
            price = row['price']

            # Check if it's time to buy (based on interval or first purchase)
            if self.last_buy_date is None or (date - self.last_buy_date).days >= self.buy_interval_days:
                buy_amount = self.current_balance * self.buy_percentage
                if buy_amount > self.current_balance:
                    logging.warning("Buy amount exceeds current balance. Skipping purchase.")
                    continue

                # Calculate asset quantity to purchase
                asset_quantity = buy_amount / price

                # Update portfolio and balance
                self.asset_holdings += asset_quantity
                self.current_balance -= buy_amount
                self.last_buy_date = date

                logging.info(f"Bought {asset_quantity:.4f} units at {price:.2f} on {date.date()}.")

            # Record the daily portfolio status
            portfolio_value = self.current_balance + (self.asset_holdings * price)
            results.append({
                'date': date,
                'price': price,
                'current_balance': self.current_balance,
                'asset_holdings': self.asset_holdings,
                'portfolio_value': portfolio_value
            })

        return pd.DataFrame(results)

if __name__ == "__main__":
    # Example historical price data (replace with actual data)
    historical_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'price': [100, 102, 105, 108, 110]
    })

    # Simulation parameters
    initial_balance = 1000.0  # Starting balance in currency
    buy_interval_days = 2     # Buy every 2 days
    buy_percentage = 0.1      # Use 10% of current balance for each purchase

    # Initialize and run simulation
    simulator = RecurrentBuyingSimulation(historical_data, initial_balance, buy_interval_days, buy_percentage)
    simulation_results = simulator.simulate()

    # Display results
    print(simulation_results)
```
