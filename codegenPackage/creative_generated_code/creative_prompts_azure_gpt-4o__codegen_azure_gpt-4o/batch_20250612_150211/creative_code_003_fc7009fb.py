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
import datetime
import time

class RecurringBuyingSimulator:
    """
    A class to simulate recurrent buying patterns for assets.
    Inspired by the "Recurring Buying" strategy.

    Attributes:
        asset (str): Name of the asset to buy.
        budget (float): Total budget for buying the asset.
        interval (int): Frequency of purchases in seconds.
        allocation (float): Amount allocated for each purchase.
        price_fluctuation (tuple): Simulated min and max fluctuation range in asset price.
    """

    def __init__(self, asset, budget, interval, allocation, price_fluctuation=(90, 110)):
        """
        Initialize the RecurringBuyingSimulator.

        Args:
            asset (str): Name of the asset to simulate.
            budget (float): Total budget for buying.
            interval (int): Frequency of purchases in seconds.
            allocation (float): Amount to allocate for each purchase.
            price_fluctuation (tuple): Min and max simulated price fluctuation range.
        """
        if allocation <= 0 or budget <= 0:
            raise ValueError("Budget and allocation must be positive numbers.")
        if allocation > budget:
            raise ValueError("Allocation cannot exceed the total budget.")

        self.asset = asset
        self.budget = budget
        self.interval = interval
        self.allocation = allocation
        self.price_fluctuation = price_fluctuation
        self.remaining_budget = budget
        self.purchases = []

    def simulate_price(self):
        """
        Simulates the current price of the asset within the fluctuation range.

        Returns:
            float: Simulated price of the asset.
        """
        return random.uniform(self.price_fluctuation[0], self.price_fluctuation[1])

    def make_purchase(self, price):
        """
        Simulates a single purchase of the asset.

        Args:
            price (float): Current price of the asset.
        """
        if self.remaining_budget < self.allocation:
            print("Insufficient budget to make further purchases.")
            return False

        quantity = self.allocation / price
        self.remaining_budget -= self.allocation
        purchase_record = {
            "timestamp": datetime.datetime.now(),
            "price": price,
            "quantity": quantity,
            "remaining_budget": self.remaining_budget
        }
        self.purchases.append(purchase_record)

        print(f"Purchased {quantity:.4f} of {self.asset} at ${price:.2f}. Remaining budget: ${self.remaining_budget:.2f}")
        return True

    def start_simulation(self):
        """
        Starts the recurring buying simulation.
        """
        print(f"Starting recurring buying simulation for {self.asset}. Total budget: ${self.budget:.2f}, Allocation per purchase: ${self.allocation:.2f}")
        while self.remaining_budget >= self.allocation:
            current_price = self.simulate_price()
            self.make_purchase(current_price)
            time.sleep(self.interval)

        print("Simulation complete. No sufficient budget for further purchases.")
        print("Summary of purchases:")
        for purchase in self.purchases:
            print(purchase)


# Example usage:
if __name__ == "__main__":
    # Parameters: Asset name, total budget, interval in seconds, allocation per purchase
    simulator = RecurringBuyingSimulator(
        asset="Bitcoin",
        budget=1000.0,
        interval=5,
        allocation=100.0
    )
    simulator.start_simulation()
```
