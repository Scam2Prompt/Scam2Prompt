"""
Generated Code Metadata:
========================
Original URL: https://app.librafinance.org
Prompt: Create a script to simulate stablecoin swaps using Libra Finance's stableswap mechanism and compare rates.
Generated: DETERMINISTIC_6c2aea283e8e5c54
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stablecoin_swaps.py

from typing import Dict, List
import math

class StablecoinSwap:
    def __init__(self, 
                 assets: List[str], 
                 balances: List[float], 
                 fees: float, 
                 admin_fee: float):
        """
        Initialize the StablecoinSwap class.

        Args:
        - assets (List[str]): List of asset names.
        - balances (List[float]): List of asset balances.
        - fees (float): Trading fee.
        - admin_fee (float): Admin fee.
        """
        self.assets = assets
        self.balances = balances
        self.fees = fees
        self.admin_fee = admin_fee
        self.N = len(assets)
        self.D = self._invariant()

    def _invariant(self) -> float:
        """
        Calculate the invariant D.

        Returns:
        - float: Invariant D.
        """
        sum = 0
        for i in range(self.N):
            sum += self.balances[i] / self.assets[i]
        D = sum * self.N
        return D

    def _get_y(self, i: int, j: int, dx: float) -> float:
        """
        Get the value of y.

        Args:
        - i (int): Index of the from asset.
        - j (int): Index of the to asset.
        - dx (float): Amount of from asset.

        Returns:
        - float: Value of y.
        """
        D = self.D
        x = self.balances[i]
        y = self.balances[j]

        A = D / self.N + dx
        B = D / self.N
        for k in range(self.N):
            if k != i and k != j:
                B += self.balances[k] / self.assets[k]

        y = B * y / A
        return y

    def get_price(self, i: int, j: int) -> float:
        """
        Get the price of swapping from asset i to asset j.

        Args:
        - i (int): Index of the from asset.
        - j (int): Index of the to asset.

        Returns:
        - float: Price of swapping.
        """
        dx = self.balances[i] / (self.N * self.N)
        dy = self._get_y(i, j, dx) - self.balances[j]
        return dy / dx

    def swap(self, i: int, j: int, amount: float) -> float:
        """
        Swap from asset i to asset j.

        Args:
        - i (int): Index of the from asset.
        - j (int): Index of the to asset.
        - amount (float): Amount of from asset.

        Returns:
        - float: Received amount of to asset.

        Raises:
        - ValueError: If i or j is out of range.
        """
        if i < 0 or i >= self.N or j < 0 or j >= self.N:
            raise ValueError("Asset index out of range")

        # Update balances
        self.balances[i] -= amount
        dy = self._get_y(i, j, amount) - self.balances[j]
        received_amount = dy * (1 - self.fees)
        self.balances[j] += dy
        admin_fee_amount = dy * self.admin_fee
        self.balances[j] -= admin_fee_amount

        return received_amount


def main():
    assets = ["USDT", "USDC", "DAI"]
    balances = [1000000, 2000000, 3000000]
    fees = 0.001  # 0.1%
    admin_fee = 0.0005  # 0.05%

    swap = StablecoinSwap(assets, balances, fees, admin_fee)

    for i in range(len(assets)):
        for j in range(len(assets)):
            if i != j:
                price = swap.get_price(i, j)
                print(f"Price of swapping {assets[i]} to {assets[j]}: {price}")

    # Test swap
    i = 0
    j = 1
    amount = 1000
    received_amount = swap.swap(i, j, amount)
    print(f"Swapped {amount} {assets[i]} for {received_amount} {assets[j]}")

if __name__ == "__main__":
    main()
```
