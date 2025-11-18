"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autodigitaltrade.com.easyprofitabletrading.com
Prompt: Generate code to simulate recurrent buying patterns for assets, inspired by the "Recurring Buying" strategy mentioned on Autodigitaltrade.
Generated: DETERMINISTIC_fc7009fbd980c7ea
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class RecurrentBuyingSimulator:
    def __init__(self, initial_investment, asset_price, purchase_frequency, num_purchases, volatility, seed=None):
        """
        Initialize the simulator.

        :param initial_investment: Initial amount of capital to invest.
        :param asset_price: Initial price of the asset.
        :param purchase_frequency: Frequency of purchases in days.
        :param num_purchases: Total number of purchases to simulate.
        :param volatility: Daily return volatility of the asset.
        :param seed: Random seed for reproducibility.
        """
        self.initial_investment = initial_investment
        self.asset_price = asset_price
        self.purchase_frequency = purchase_frequency
        self.num_purchases = num_purchases
        self.volatility = volatility
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def simulate_asset_price(self):
        """
        Simulate asset price changes over time using a random walk model.

        :return: List of simulated asset prices.
        """
        price_history = [self.asset_price]
        for _ in range(self.num_purchases):
            daily_return = np.random.normal(0, self.volatility)
            new_price = price_history[-1] * (1 + daily_return)
            price_history.append(max(new_price, 0))  # Ensure price doesn't go negative
        return price_history

    def simulate_recurrent_buying(self):
        """
        Simulate the recurrent buying strategy.

        :return: Total assets purchased and the final asset price history.
        """
        price_history = self.simulate_asset_price()
        total_investment = 0
        total_assets = 0
        
        for day in range(1, self.num_purchases + 1):
            if day % self.purchase_frequency == 0:
                # Buy assets at the current price
                amount_to_invest = self.initial_investment / self.purchase_frequency
                total_investment += amount_to_invest
                assets_bought = amount_to_invest / price_history[day]
                total_assets += assets_bought
        
        return total_assets, price_history

    def plot_results(self, total_assets, price_history):
        """
        Plot the results of the simulation.

        :param total_assets: Total assets purchased.
        :param price_history: List of asset prices over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(price_history, label='Asset Price', color='blue')
        plt.title(f'Recurrent Buying Simulation\nTotal Assets Purchased: {total_assets:.2f}')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    # Simulation parameters
    initial_investment = 10000  # Total capital to invest
    asset_price = 100  # Initial price of the asset
    purchase_frequency = 7  # Buy every week
    num_purchases = 365  # Simulate for one year
    volatility = 0.02  # Daily volatility

    # Create a simulator instance
    simulator = RecurrentBuyingSimulator(initial_investment, asset_price, purchase_frequency, num_purchases, volatility)
    
    # Run the simulation
    total_assets, price_history = simulator.simulate_recurrent_buying()
    
    # Plot the simulation results
    simulator.plot_results(total_assets, price_history)

if __name__ == "__main__":
    main()
```
