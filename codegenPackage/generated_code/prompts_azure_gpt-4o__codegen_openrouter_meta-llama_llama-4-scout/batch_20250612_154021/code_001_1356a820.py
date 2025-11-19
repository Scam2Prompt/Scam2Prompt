"""
Generated Code Metadata:
========================
Original URL: https://asteerdex.com
Prompt: Generate code to calculate potential APY earnings from staking assets like BNB, USDT, BTC, or CAKE on Aster, assuming a 30% APY.
Generated: DETERMINISTIC_1356a820998d38bf
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# apy_calculator.py

from enum import Enum
from typing import Dict

class Asset(Enum):
    """Supported assets for staking."""
    BNB = "BNB"
    USDT = "USDT"
    BTC = "BTC"
    CAKE = "CAKE"

class APYCalculator:
    """Calculates potential APY earnings from staking assets."""

    def __init__(self, apy: float = 0.3):
        """
        Initializes the APY calculator.

        Args:
        - apy (float): The annual percentage yield (APY). Defaults to 0.3 (30%).
        """
        self.apy = apy

    def calculate_earnings(self, asset: Asset, amount: float, days: int) -> float:
        """
        Calculates the potential earnings from staking an asset.

        Args:
        - asset (Asset): The asset being staked.
        - amount (float): The amount of the asset being staked.
        - days (int): The number of days the asset is staked.

        Returns:
        - float: The potential earnings.

        Raises:
        - ValueError: If the amount or days are not positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if days <= 0:
            raise ValueError("Days must be positive.")

        # Convert APY to a decimal
        apy_decimal = self.apy / 100

        # Calculate the daily interest rate
        daily_interest_rate = apy_decimal / 365

        # Calculate the potential earnings using compound interest formula
        earnings = amount * (1 + daily_interest_rate) ** days - amount

        return earnings

def main():
    calculator = APYCalculator()

    # Example usage:
    assets: Dict[Asset, float] = {
        Asset.BNB: 10,
        Asset.USDT: 1000,
        Asset.BTC: 0.1,
        Asset.CAKE: 100
    }

    days = 30

    for asset, amount in assets.items():
        try:
            earnings = calculator.calculate_earnings(asset, amount, days)
            print(f"Staking {amount} {asset.value} for {days} days: ${earnings:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
