"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai2dai.github.io
Prompt: Using the MakerDAO documentation, create a function to calculate the collateralization ratio of a vault holding Dai stablecoins.
Generated: DETERMINISTIC_4461a5564cb7312c
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vault:
    def __init__(self, collateral_amount: float, debt_amount: float):
        """
        Initialize a Vault with collateral amount and debt amount.
        
        :param collateral_amount: The amount of collateral (in DAI) held in the vault.
        :param debt_amount: The amount of debt (in DAI) owed by the vault.
        """
        self.collateral_amount = collateral_amount
        self.debt_amount = debt_amount

    def calculate_collateralization_ratio(self) -> float:
        """
        Calculate the collateralization ratio of the vault.

        The collateralization ratio is calculated using the formula:
        Collateralization Ratio = (Collateral Amount / Debt Amount) * 100%

        :return: The collateralization ratio as a percentage.
        :raises ValueError: If the debt amount is zero or negative.
        """
        if self.debt_amount <= 0:
            raise ValueError("Debt amount must be greater than zero to calculate the collateralization ratio.")

        collateralization_ratio = (self.collateral_amount / self.debt_amount) * 100
        return collateralization_ratio

# Example usage:
if __name__ == "__main__":
    try:
        # Create a vault with 150 DAI collateral and 100 DAI debt
        vault = Vault(collateral_amount=150.0, debt_amount=100.0)
        
        # Calculate and print the collateralization ratio
        ratio = vault.calculate_collateralization_ratio()
        print(f"The collateralization ratio is {ratio:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
