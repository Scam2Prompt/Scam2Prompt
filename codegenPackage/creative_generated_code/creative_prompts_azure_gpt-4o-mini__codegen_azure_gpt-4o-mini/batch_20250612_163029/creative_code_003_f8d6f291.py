"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatealpha.co
Prompt: Generate a code snippet for a demo account feature that allows users to practice trading strategies on Immediate Mentax without financial risk.
Generated: DETERMINISTIC_f8d6f29184bc9e3b
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal

class DemoAccount:
    """
    A class to represent a demo trading account for practicing trading strategies without financial risk.
    """

    def __init__(self, initial_balance: Decimal = Decimal('10000.00')):
        """
        Initializes the demo account with a specified initial balance.

        Args:
            initial_balance (Decimal): The initial balance of the demo account. Default is $10,000.00.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.positions = {}
        print(f"Demo account created with an initial balance of {self.balance:.2f}")

    def buy(self, symbol: str, quantity: int, price: Decimal):
        """
        Simulate buying a stock or asset.

        Args:
            symbol (str): The symbol of the stock or asset to buy.
            quantity (int): The number of units to buy.
            price (Decimal): The price per unit.

        Raises:
            ValueError: If the quantity is less than 1 or if there are insufficient funds.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        total_cost = price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete this purchase.")

        self.balance -= total_cost
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity
        print(f"Bought {quantity} of {symbol} at {price:.2f} each. Remaining balance: {self.balance:.2f}")

    def sell(self, symbol: str, quantity: int, price: Decimal):
        """
        Simulate selling a stock or asset.

        Args:
            symbol (str): The symbol of the stock or asset to sell.
            quantity (int): The number of units to sell.
            price (Decimal): The price per unit.

        Raises:
            ValueError: If the quantity is invalid or there are not enough shares to sell.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if symbol not in self.positions or self.positions[symbol] < quantity:
            raise ValueError("Not enough shares to sell.")

        total_gain = price * quantity
        self.balance += total_gain
        self.positions[symbol] -= quantity

        if self.positions[symbol] == 0:
            del self.positions[symbol]

        print(f"Sold {quantity} of {symbol} at {price:.2f} each. New balance: {self.balance:.2f}")

    def get_balance(self) -> Decimal:
        """
        Retrieve the current balance of the demo account.

        Returns:
            Decimal: The current balance.
        """
        return self.balance

    def get_positions(self) -> dict:
        """
        Retrieve the currently held positions in the demo account.

        Returns:
            dict: A dictionary of positions with symbols as keys and quantities as values.
        """
        return self.positions

    def random_market_update(self):
        """
        Simulate a random market update affecting current positions (for demo purposes only).
        Prices change randomly within a predefined range to simulate market volatility.
        """
        for symbol in self.positions.keys():
            price_change = Decimal(random.uniform(-1.0, 1.0))  # Random price change between -1 and 1
            new_price = Decimal(random.uniform(10.0, 100.0)) + price_change
            print(f"{symbol} new simulated market price: {new_price:.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        demo_account = DemoAccount()
        demo_account.buy('AAPL', 10, Decimal('150.00'))
        demo_account.sell('AAPL', 5, Decimal('155.00'))
        demo_account.random_market_update()

        print(f"Current balance: {demo_account.get_balance():.2f}")
        print(f"Current positions: {demo_account.get_positions()}")
    except ValueError as e:
        print(f"Error: {e}")
```
