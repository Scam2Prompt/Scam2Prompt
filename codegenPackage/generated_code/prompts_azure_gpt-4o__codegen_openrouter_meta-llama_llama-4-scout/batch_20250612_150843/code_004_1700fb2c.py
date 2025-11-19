"""
Generated Code Metadata:
========================
Original URL: https://theimmediateifexai.com
Prompt: Implement a demo account feature in a cryptocurrency trading application that allows users to test strategies in a risk-free environment, similar to Immediate Ifex Ai's demo account offering.
Generated: DETERMINISTIC_1700fb2cf94ff464
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# demo_account.py

import logging
from typing import Dict

class DemoAccount:
    """
    A demo account class for testing trading strategies in a risk-free environment.
    """

    def __init__(self, user_id: int, initial_balance: float = 10000.0):
        """
        Initializes a demo account for a user.

        Args:
        - user_id (int): The ID of the user.
        - initial_balance (float): The initial balance of the demo account (default: 10000.0).
        """
        self.user_id = user_id
        self.balance = initial_balance
        self.positions: Dict[str, float] = {}  # asset: quantity

    def get_balance(self) -> float:
        """
        Retrieves the current balance of the demo account.

        Returns:
        - float: The current balance.
        """
        return self.balance

    def get_positions(self) -> Dict[str, float]:
        """
        Retrieves the current positions of the demo account.

        Returns:
        - Dict[str, float]: A dictionary of assets and their quantities.
        """
        return self.positions.copy()

    def place_order(self, asset: str, quantity: float, side: str) -> bool:
        """
        Places an order on the demo account.

        Args:
        - asset (str): The asset to trade.
        - quantity (float): The quantity to trade.
        - side (str): The side of the trade (buy/sell).

        Returns:
        - bool: True if the order was successful, False otherwise.
        """
        try:
            if side not in ['buy', 'sell']:
                raise ValueError("Invalid side. Must be 'buy' or 'sell'.")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0.")

            if asset not in self.positions:
                self.positions[asset] = 0.0

            if side == 'buy':
                cost = quantity * 100.0  # assume $100.0 per unit for simplicity
                if cost > self.balance:
                    raise ValueError("Insufficient balance.")
                self.balance -= cost
                self.positions[asset] += quantity
            elif side == 'sell':
                if self.positions[asset] < quantity:
                    raise ValueError("Insufficient quantity to sell.")
                self.positions[asset] -= quantity
                self.balance += quantity * 90.0  # assume $90.0 per unit for simplicity

            return True

        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return False

    def reset_account(self) -> None:
        """
        Resets the demo account to its initial state.
        """
        self.balance = 10000.0
        self.positions.clear()


# Example usage:
if __name__ == "__main__":
    demo_account = DemoAccount(1)

    print(f"Initial balance: ${demo_account.get_balance():.2f}")
    print("Initial positions:", demo_account.get_positions())

    demo_account.place_order('BTC', 1.0, 'buy')
    print(f"Balance after buying 1 BTC: ${demo_account.get_balance():.2f}")
    print("Positions after buying 1 BTC:", demo_account.get_positions())

    demo_account.place_order('BTC', 0.5, 'sell')
    print(f"Balance after selling 0.5 BTC: ${demo_account.get_balance():.2f}")
    print("Positions after selling 0.5 BTC:", demo_account.get_positions())

    demo_account.reset_account()
    print(f"Balance after reset: ${demo_account.get_balance():.2f}")
    print("Positions after reset:", demo_account.get_positions())
```
