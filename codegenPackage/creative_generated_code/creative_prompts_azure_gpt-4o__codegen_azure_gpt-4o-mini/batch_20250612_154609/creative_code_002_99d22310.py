"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topdigitaltrade.com.simplebittstockoption.com
Prompt: Develop a program to simulate recurrent buying patterns for assets, as described in Topdigitaltrade's "Recurring Buying" strategy.
Generated: DETERMINISTIC_99d223105de5d9c5
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Asset:
    """Class to represent an asset with a price and a purchase method."""

    def __init__(self, name, initial_price):
        self.name = name
        self.price_history = [initial_price]  # Track historical prices
        self.current_price = initial_price

    def update_price(self):
        """Simulate price change using a random walk."""
        change_percent = random.uniform(-0.05, 0.05)  # Price can change by -5% to +5%
        self.current_price *= (1 + change_percent)
        self.price_history.append(self.current_price)

class RecurringBuyer:
    """Class to simulate a recurring buying strategy for an asset."""

    def __init__(self, asset, purchase_amount, purchase_interval_days):
        self.asset = asset
        self.purchase_amount = purchase_amount
        self.purchase_interval_days = purchase_interval_days
        self.purchases = []  # To keep track of purchase history
        self.start_date = datetime.now()

    def simulate_purchases(self, total_days):
        """Simulates recurring purchases over a specified total duration."""
        for day in range(total_days):
            # Check if it's time to purchase
            if day % self.purchase_interval_days == 0:
                self.asset.update_price()  # Update asset price before purchasing
                shares_bought = self.purchase_amount / self.asset.current_price
                purchase_date = self.start_date + timedelta(days=day)
                self.purchases.append((purchase_date, shares_bought, self.asset.current_price))
                print(f"Purchased {shares_bought:.4f} shares of {self.asset.name} on {purchase_date.date()} at ${self.asset.current_price:.2f}")

    def get_total_investment(self):
        """Calculates the total investment made."""
        total_investment = sum(amount for _, amount, _ in self.purchases)
        return total_investment

    def get_total_shares(self):
        """Calculates the total shares purchased."""
        total_shares = sum(amount for _, amount, _ in self.purchases)
        return total_shares

    def plot_investment(self):
        """Plots the asset price history and purchase points."""
        dates = [purchase[0] for purchase in self.purchases]
        shares = [purchase[1] for purchase in self.purchases]
        prices = [purchase[2] for purchase in self.purchases]

        # DataFrame for easier plotting
        df = pd.DataFrame({
            'Date': dates,
            'Shares Bought': shares,
            'Price at Purchase': prices
        })
        
        plt.figure(figsize=(14, 7))
        plt.plot(self.asset.price_history, label=f'{self.asset.name} Price History')
        plt.scatter(df['Date'], df['Price at Purchase'], color='red', label='Purchases', zorder=5)
        plt.title(f'{self.asset.name} Price History and Purchase Points')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    """Main function to execute the recurring buying simulation."""
    try:
        # Initialize asset with a starting price
        asset = Asset(name="Sample Asset", initial_price=100.0)

        # Initialize recurring buyer with parameters
        buyer = RecurringBuyer(asset, purchase_amount=100.0, purchase_interval_days=30)

        # Simulate purchases over a year (365 days)
        buyer.simulate_purchases(total_days=365)

        # Output total investment and shares bought
        print(f"\nTotal Investment: ${buyer.get_total_investment():.2f}")
        print(f"Total Shares Bought: {buyer.get_total_shares():.4f} shares")

        # Plot the investment over time
        buyer.plot_investment()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
