"""
Generated Code Metadata:
========================
Original URL: https://syn-future.vercel.app
Prompt: Generate a script to simulate futures trading on SynFutures' platform, including functionality for long and short positions on NFTs with leverage.
Generated: DETERMINISTIC_05c5a095015af7e8
Batch ID: 20250612_150122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SynFutures Trading Simulator

import time
from typing import Dict

class NFT:
    def __init__(self, id: str, price: float):
        """
        Initialize an NFT.

        Args:
        - id (str): Unique identifier for the NFT.
        - price (float): Initial price of the NFT.
        """
        self.id = id
        self.price = price

class TradingAccount:
    def __init__(self, balance: float = 10000.0):
        """
        Initialize a trading account.

        Args:
        - balance (float): Initial account balance. Defaults to 10000.0.
        """
        self.balance = balance
        self.positions: Dict[str, Dict[str, float]] = {}

    def open_position(self, nft: NFT, side: str, leverage: float, amount: float):
        """
        Open a long or short position on an NFT.

        Args:
        - nft (NFT): The NFT to trade.
        - side (str): 'long' or 'short'.
        - leverage (float): Leverage for the position.
        - amount (float): Amount to trade.

        Raises:
        - ValueError: If side is not 'long' or 'short'.
        - ValueError: If leverage is not positive.
        - ValueError: If amount is not positive.
        """
        if side not in ['long', 'short']:
            raise ValueError("Invalid side. Must be 'long' or 'short'.")

        if leverage <= 0:
            raise ValueError("Leverage must be positive.")

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Calculate the notional value of the trade
        notional_value = amount * nft.price

        # Calculate the margin required for the position
        margin = notional_value / leverage

        # Check if the account has sufficient balance
        if self.balance < margin:
            raise ValueError("Insufficient balance.")

        # Open the position
        self.positions[nft.id] = {
            'side': side,
            'leverage': leverage,
            'amount': amount,
            'margin': margin,
            'entry_price': nft.price
        }

        # Deduct the margin from the account balance
        self.balance -= margin

        print(f"Opened {side} position on NFT {nft.id} with leverage {leverage} and amount {amount}.")

    def close_position(self, nft: NFT):
        """
        Close an open position on an NFT.

        Args:
        - nft (NFT): The NFT to close the position on.

        Raises:
        - ValueError: If no position is open on the NFT.
        """
        if nft.id not in self.positions:
            raise ValueError("No open position on this NFT.")

        position = self.positions[nft.id]
        side = position['side']
        amount = position['amount']
        entry_price = position['entry_price']
        margin = position['margin']

        # Calculate the profit/loss
        pnl = (nft.price - entry_price) * amount * (1 if side == 'long' else -1)

        # Close the position
        del self.positions[nft.id]

        # Add the margin back to the account balance
        self.balance += margin

        # Add the profit/loss to the account balance
        self.balance += pnl

        print(f"Closed {side} position on NFT {nft.id} with PNL {pnl}.")

    def update_balance(self, amount: float):
        """
        Update the account balance.

        Args:
        - amount (float): Amount to add to the balance.
        """
        self.balance += amount

def main():
    # Create an NFT
    nft = NFT('nft-1', 1000.0)

    # Create a trading account
    account = TradingAccount()

    try:
        # Open a long position with 2x leverage
        account.open_position(nft, 'long', 2.0, 10.0)

        # Simulate a price increase
        nft.price = 1200.0

        # Close the position
        account.close_position(nft)

        # Print the final account balance
        print(f"Final account balance: {account.balance}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
