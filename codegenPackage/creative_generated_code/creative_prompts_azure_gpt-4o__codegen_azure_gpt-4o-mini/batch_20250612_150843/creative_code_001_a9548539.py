"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-3x-maxair.com
Prompt: Generate a script to simulate trading using Immediate 3X Maxair's demo account feature, allowing users to test strategies without risking real capital.
Generated: DETERMINISTIC_a9548539033fc265
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class TradingSimulation:
    """A class to simulate trading in a demo account for Immediate 3X Maxair."""

    def __init__(self, initial_balance=10000):
        """Initialize the trading simulation with a given initial balance."""
        self.balance = initial_balance
        self.positions = []
        self.is_trading = True

    def get_market_price(self):
        """Simulate the retrieval of the current market price."""
        # This function simulates fluctuating market prices
        price = random.uniform(50, 150)  # Simulated price between 50 and 150
        return round(price, 2)

    def buy(self, quantity):
        """Execute a buy order."""
        market_price = self.get_market_price()
        total_cost = market_price * quantity

        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")

        self.balance -= total_cost
        self.positions.append((quantity, market_price))
        print(f"Bought {quantity} units at {market_price} each. Total cost: {total_cost:.2f}. Remaining balance: {self.balance:.2f}.")

    def sell(self, quantity):
        """Execute a sell order."""
        if not self.positions:
            raise ValueError("No stocks to sell.")

        market_price = self.get_market_price()
        total_sale_price = market_price * quantity
        quantity_owned = sum(q for q, _ in self.positions)

        if quantity > quantity_owned:
            raise ValueError("You cannot sell more than you own.")

        # Remove sold shares from positions
        for i in range(len(self.positions)):
            if self.positions[i][0] >= quantity:
                self.positions[i] = (self.positions[i][0] - quantity, self.positions[i][1])
                break
            else:
                quantity -= self.positions[i][0]
                self.positions[i] = (0, self.positions[i][1])

        self.balance += total_sale_price
        print(f"Sold {quantity} units at {market_price} each. Total sale price: {total_sale_price:.2f}. New balance: {self.balance:.2f}.")

    def show_balance(self):
        """Display the current account balance."""
        print(f"Current balance: {self.balance:.2f}")

    def show_positions(self):
        """Display the current positions held."""
        print("Current positions:")
        for quantity, price in self.positions:
            if quantity > 0:
                print(f" - {quantity} units at {price} each.")

    def simulate_trading(self, trades):
        """Simulate a series of trades."""
        for _ in range(trades):
            action = random.choice(['buy', 'sell'])
            quantity = random.randint(1, 10)

            try:
                if action == 'buy':
                    self.buy(quantity)
                else:
                    self.sell(quantity)
            except ValueError as e:
                print(f"Error during trading: {e}")

            # Pause for a moment to simulate time between trades
            time.sleep(1)

        self.show_balance()
        self.show_positions()

if __name__ == "__main__":
    # Create a trading simulation instance with an initial balance
    sim = TradingSimulation()

    # Simulate trading with 10 trades
    sim.simulate_trading(10)
```
