"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Explain how the QiDao protocol ensures the stability of its MAI stablecoin through collateralization.
Generated: DETERMINISTIC_f0c6a2b8e171ec29
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# QiDao Protocol Stability Explanation

class CollateralizedStablecoin:
    """
    Represents a stablecoin stabilized through collateralization.
    """

    def __init__(self, collateral_ratio: float, liquidation_ratio: float):
        """
        Initializes the stablecoin with collateral and liquidation ratios.

        Args:
        - collateral_ratio (float): The ratio of collateral to stablecoin supply.
        - liquidation_ratio (float): The ratio at which collateral is liquidated.
        """
        self.collateral_ratio = collateral_ratio
        self.liquidation_ratio = liquidation_ratio
        self.collateral_supply = 0
        self.stablecoin_supply = 0

    def add_collateral(self, amount: float):
        """
        Adds collateral to the stablecoin.

        Args:
        - amount (float): The amount of collateral to add.

        Raises:
        - ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Collateral amount cannot be negative")
        self.collateral_supply += amount

    def mint_stablecoin(self, amount: float):
        """
        Mints new stablecoins.

        Args:
        - amount (float): The amount of stablecoins to mint.

        Raises:
        - ValueError: If the amount is negative or exceeds the collateral ratio.
        """
        if amount < 0:
            raise ValueError("Stablecoin amount cannot be negative")
        if amount > self.collateral_supply * self.collateral_ratio:
            raise ValueError("Insufficient collateral for minting")
        self.stablecoin_supply += amount

    def liquidate_collateral(self):
        """
        Liquidates collateral if the collateral ratio falls below the liquidation ratio.

        Returns:
        - bool: Whether liquidation occurred.
        """
        if self.stablecoin_supply > 0 and self.collateral_supply * self.liquidation_ratio < self.stablecoin_supply:
            # Simulate liquidation by reducing collateral and stablecoin supply
            self.collateral_supply -= self.stablecoin_supply / self.liquidation_ratio
            self.stablecoin_supply = 0
            return True
        return False

    def get_stablecoin_supply(self) -> float:
        """
        Gets the current stablecoin supply.

        Returns:
        - float: The stablecoin supply.
        """
        return self.stablecoin_supply

    def get_collateral_supply(self) -> float:
        """
        Gets the current collateral supply.

        Returns:
        - float: The collateral supply.
        """
        return self.collateral_supply


def main():
    # Example usage
    mai_stablecoin = CollateralizedStablecoin(collateral_ratio=1.5, liquidation_ratio=1.2)

    try:
        mai_stablecoin.add_collateral(1000)
        mai_stablecoin.mint_stablecoin(600)
        print(f"Stablecoin supply: {mai_stablecoin.get_stablecoin_supply()}")
        print(f"Collateral supply: {mai_stablecoin.get_collateral_supply()}")

        # Simulate a drop in collateral value
        mai_stablecoin.collateral_supply = 400
        if mai_stablecoin.liquidate_collateral():
            print("Liquidation occurred")
        else:
            print("No liquidation occurred")

        print(f"Stablecoin supply after liquidation: {mai_stablecoin.get_stablecoin_supply()}")
        print(f"Collateral supply after liquidation: {mai_stablecoin.get_collateral_supply()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
