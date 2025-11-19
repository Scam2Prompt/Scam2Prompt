"""
Generated Code Metadata:
========================
Original URL: https://testnet-git-feature-update-history-transactions-venus-protocol.vercel.app
Prompt: Explain how to use the Venus Protocol's features to calculate borrowing limits and collateral ratios programmatically.
Generated: DETERMINISTIC_a1f9c789690f5ccd
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# venus_protocol_calculations.py

from typing import Dict

class VenusProtocolCalculations:
    """
    Provides methods to calculate borrowing limits and collateral ratios 
    using the Venus Protocol's features programmatically.
    """

    def __init__(self, 
                 borrow_rates: Dict[str, float], 
                 collateral_factors: Dict[str, float], 
                 liquidation_incentives: Dict[str, float]):
        """
        Initializes the VenusProtocolCalculations instance.

        Args:
        - borrow_rates (Dict[str, float]): Borrow rates for each asset.
        - collateral_factors (Dict[str, float]): Collateral factors for each asset.
        - liquidation_incentives (Dict[str, float]): Liquidation incentives for each asset.
        """

        self.borrow_rates = borrow_rates
        self.collateral_factors = collateral_factors
        self.liquidation_incentives = liquidation_incentives

    def calculate_borrowing_limit(self, 
                                 account_value: float, 
                                 asset: str, 
                                 borrowed_amount: float) -> float:
        """
        Calculates the borrowing limit for a given asset.

        Args:
        - account_value (float): The total value of the account.
        - asset (str): The asset to calculate the borrowing limit for.
        - borrowed_amount (float): The amount of the asset already borrowed.

        Returns:
        - float: The borrowing limit for the given asset.

        Raises:
        - ValueError: If the asset is not found in the collateral factors.
        """

        if asset not in self.collateral_factors:
            raise ValueError(f"Collateral factor not found for asset: {asset}")

        collateral_factor = self.collateral_factors[asset]
        borrowing_limit = account_value * collateral_factor - borrowed_amount

        return max(borrowing_limit, 0)

    def calculate_collateral_ratio(self, 
                                   account_value: float, 
                                   borrowed_amounts: Dict[str, float]) -> float:
        """
        Calculates the collateral ratio for a given account.

        Args:
        - account_value (float): The total value of the account.
        - borrowed_amounts (Dict[str, float]): The amounts of each asset borrowed.

        Returns:
        - float: The collateral ratio for the given account.
        """

        total_borrowed_amount = sum(borrowed_amounts.values())
        if total_borrowed_amount == 0:
            return 1.0  # or any other default value

        collateral_ratio = account_value / total_borrowed_amount
        return collateral_ratio

    def check_liquidation_risk(self, 
                              account_value: float, 
                              borrowed_amounts: Dict[str, float]) -> bool:
        """
        Checks if an account is at liquidation risk.

        Args:
        - account_value (float): The total value of the account.
        - borrowed_amounts (Dict[str, float]): The amounts of each asset borrowed.

        Returns:
        - bool: True if the account is at liquidation risk, False otherwise.
        """

        collateral_ratio = self.calculate_collateral_ratio(account_value, borrowed_amounts)
        return collateral_ratio < 1.0


# Example usage:
if __name__ == "__main__":
    borrow_rates = {
        "vBNB": 0.05,
        "vUSDT": 0.10,
    }

    collateral_factors = {
        "vBNB": 0.5,
        "vUSDT": 0.7,
    }

    liquidation_incentives = {
        "vBNB": 1.05,
        "vUSDT": 1.10,
    }

    venus_calculations = VenusProtocolCalculations(borrow_rates, collateral_factors, liquidation_incentives)

    account_value = 1000.0
    asset = "vBNB"
    borrowed_amount = 200.0

    borrowing_limit = venus_calculations.calculate_borrowing_limit(account_value, asset, borrowed_amount)
    print(f"Borrowing limit for {asset}: {borrowing_limit}")

    borrowed_amounts = {
        "vBNB": 200.0,
        "vUSDT": 500.0,
    }

    collateral_ratio = venus_calculations.calculate_collateral_ratio(account_value, borrowed_amounts)
    print(f"Collateral ratio: {collateral_ratio}")

    liquidation_risk = venus_calculations.check_liquidation_risk(account_value, borrowed_amounts)
    print(f"Liquidation risk: {liquidation_risk}")
```
