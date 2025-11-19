"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: What is an example of a DeFi algorithmic money market protocol, and how does it function?
Generated: DETERMINISTIC_91876a6c346dc2d1
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, Any

class AlgorithmicMoneyMarket:
    """
    A simple implementation of an algorithmic money market protocol.
    This class allows users to deposit and borrow assets while maintaining
    an algorithmic interest rate based on supply and demand.
    """

    def __init__(self):
        # Initialize the market with empty supply and demand
        self.supply: Dict[str, float] = {}
        self.demand: Dict[str, float] = {}
        self.interest_rate: float = 0.05  # Base interest rate

    def deposit(self, asset: str, amount: float) -> None:
        """
        Allows users to deposit an asset into the money market.

        :param asset: The type of asset being deposited
        :param amount: The amount of asset to deposit
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        # Update the supply for the asset
        if asset in self.supply:
            self.supply[asset] += amount
        else:
            self.supply[asset] = amount

        print(f"Deposited {amount} of {asset}. Total supply: {self.supply[asset]}")

    def borrow(self, asset: str, amount: float) -> None:
        """
        Allows users to borrow an asset from the money market.

        :param asset: The type of asset being borrowed
        :param amount: The amount of asset to borrow
        :raises ValueError: If the amount is non-positive or exceeds supply
        """
        if amount <= 0:
            raise ValueError("Borrow amount must be positive.")
        if asset not in self.supply or self.supply[asset] < amount:
            raise ValueError("Insufficient supply to borrow the requested amount.")

        # Update the demand for the asset
        if asset in self.demand:
            self.demand[asset] += amount
        else:
            self.demand[asset] = amount

        # Decrease the supply of the asset
        self.supply[asset] -= amount

        print(f"Borrowed {amount} of {asset}. Remaining supply: {self.supply[asset]}")

    def calculate_interest(self, asset: str, duration: int) -> float:
        """
        Calculates the interest for a borrowed amount over a specified duration.

        :param asset: The type of asset for which to calculate interest
        :param duration: The duration in days for which interest is calculated
        :return: The calculated interest amount
        :raises ValueError: If the asset is not borrowed
        """
        if asset not in self.demand:
            raise ValueError("No borrowed amount for this asset.")

        borrowed_amount = self.demand[asset]
        interest = borrowed_amount * self.interest_rate * (duration / 365)  # Annual interest
        return interest

    def repay(self, asset: str, amount: float) -> None:
        """
        Allows users to repay borrowed assets.

        :param asset: The type of asset being repaid
        :param amount: The amount of asset to repay
        :raises ValueError: If the amount is non-positive or exceeds borrowed amount
        """
        if amount <= 0:
            raise ValueError("Repayment amount must be positive.")
        if asset not in self.demand or self.demand[asset] < amount:
            raise ValueError("Repayment amount exceeds borrowed amount.")

        # Decrease the demand for the asset
        self.demand[asset] -= amount

        # Increase the supply of the asset
        self.supply[asset] += amount

        print(f"Repaid {amount} of {asset}. Remaining borrowed: {self.demand[asset]}")

# Example usage
if __name__ == "__main__":
    market = AlgorithmicMoneyMarket()
    market.deposit("ETH", 10)
    market.borrow("ETH", 5)
    interest = market.calculate_interest("ETH", 30)
    print(f"Interest for borrowing 5 ETH for 30 days: {interest}")
    market.repay("ETH", 5)
```
