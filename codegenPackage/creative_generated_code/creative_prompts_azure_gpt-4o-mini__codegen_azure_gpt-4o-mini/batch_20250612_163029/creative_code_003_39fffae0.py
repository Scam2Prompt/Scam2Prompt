"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-prime.com
Prompt: Explain how to use the demo account feature of switch hiprex 400 to test trading strategies without financial risk.
Generated: DETERMINISTIC_39fffae0b38905e5
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Hiprex400DemoAccount:
    """
    A class to simulate the usage of a demo account on the Hiprex 400 trading platform.
    This class allows users to test trading strategies without financial risk.
    """

    def __init__(self, initial_balance: float):
        """
        Initializes the demo account with a specified initial balance.

        Args:
            initial_balance (float): The starting balance for the demo account.

        Raises:
            ValueError: If the initial balance is not positive.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be a positive number.")
        self.balance = initial_balance
        self.positions = {}
        print(f"Demo account created with an initial balance of ${self.balance:.2f}.")

    def buy(self, asset: str, amount: float, price: float):
        """
        Simulates buying an asset.

        Args:
            asset (str): The name of the asset to buy.
            amount (float): The quantity of the asset to buy.
            price (float): The price per unit of the asset.

        Raises:
            ValueError: If the buy amount is invalid or if there are insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete the purchase.")
        
        self.balance -= total_cost
        self.positions[asset] = self.positions.get(asset, 0) + amount
        print(f"Bought {amount} of {asset} at ${price:.2f} each. Total cost: ${total_cost:.2f}.")

    def sell(self, asset: str, amount: float, price: float):
        """
        Simulates selling an asset.

        Args:
            asset (str): The name of the asset to sell.
            amount (float): The quantity of the asset to sell.
            price (float): The price per unit of the asset.

        Raises:
            ValueError: If the sell amount is invalid or if the asset is not held in the portfolio.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if asset not in self.positions or self.positions[asset] < amount:
            raise ValueError("Not enough asset held to sell.")

        total_revenue = amount * price
        self.balance += total_revenue
        self.positions[asset] -= amount
        print(f"Sold {amount} of {asset} at ${price:.2f} each. Total revenue: ${total_revenue:.2f}.")

    def check_balance(self):
        """Prints the current balance of the demo account."""
        print(f"Current balance: ${self.balance:.2f}")

    def print_positions(self):
        """Prints the current asset positions held in the demo account."""
        print("Current positions:")
        for asset, amount in self.positions.items():
            print(f"{asset}: {amount}")

# Example usage
if __name__ == "__main__":
    try:
        demo_account = Hiprex400DemoAccount(initial_balance=10000.00)
        demo_account.buy(asset='AAPL', amount=10, price=150.00)
        demo_account.sell(asset='AAPL', amount=5, price=155.00)
        demo_account.check_balance()
        demo_account.print_positions()
    except ValueError as e:
        print(f"Error: {e}")
```
