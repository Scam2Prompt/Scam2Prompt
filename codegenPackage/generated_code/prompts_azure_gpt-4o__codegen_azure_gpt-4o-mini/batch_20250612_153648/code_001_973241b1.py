"""
Generated Code Metadata:
========================
Original URL: https://lanimal443331.github.io
Prompt: Generate code to simulate the high-to-low pricing mechanism used in Fjord Foundry's LBPs for community-driven price discovery.
Generated: DETERMINISTIC_973241b1f0c69876
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Tuple

class LBP:
    """
    A class to simulate the high-to-low pricing mechanism used in Liquidity Bootstrapping Pools (LBPs).
    """

    def __init__(self, initial_price: float, price_decay_rate: float, total_supply: int):
        """
        Initializes the LBP with the given parameters.

        :param initial_price: The starting price of the asset.
        :param price_decay_rate: The rate at which the price decreases over time.
        :param total_supply: The total supply of the asset available for trading.
        """
        if initial_price <= 0:
            raise ValueError("Initial price must be greater than zero.")
        if price_decay_rate <= 0 or price_decay_rate >= 1:
            raise ValueError("Price decay rate must be between 0 and 1.")
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")

        self.initial_price = initial_price
        self.price_decay_rate = price_decay_rate
        self.total_supply = total_supply
        self.current_price = initial_price
        self.sold_supply = 0

    def simulate_trade(self, amount: int) -> Tuple[float, float]:
        """
        Simulates a trade in the LBP.

        :param amount: The amount of asset to trade.
        :return: A tuple containing the price at which the trade occurred and the total cost of the trade.
        """
        if amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")
        if self.sold_supply + amount > self.total_supply:
            raise ValueError("Trade amount exceeds available supply.")

        # Calculate the cost of the trade based on the current price
        cost = self.current_price * amount
        self.sold_supply += amount

        # Update the price based on the decay rate
        self.current_price *= (1 - self.price_decay_rate)

        return self.current_price, cost

    def reset(self):
        """
        Resets the LBP to its initial state.
        """
        self.current_price = self.initial_price
        self.sold_supply = 0

    def get_status(self) -> dict:
        """
        Returns the current status of the LBP.

        :return: A dictionary containing the current price, total supply, and sold supply.
        """
        return {
            "current_price": self.current_price,
            "total_supply": self.total_supply,
            "sold_supply": self.sold_supply
        }

def main():
    """
    Main function to demonstrate the LBP simulation.
    """
    try:
        # Initialize the LBP with example parameters
        lbp = LBP(initial_price=10.0, price_decay_rate=0.05, total_supply=1000)

        # Simulate a series of trades
        for _ in range(10):
            trade_amount = random.randint(1, 100)  # Random trade amount between 1 and 100
            current_price, cost = lbp.simulate_trade(trade_amount)
            print(f"Traded {trade_amount} units at price {current_price:.2f}, total cost: {cost:.2f}")

        # Print the final status of the LBP
        print("Final LBP Status:", lbp.get_status())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
