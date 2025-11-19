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
class QiDaoProtocol:
    """
    A class to represent the QiDao protocol and its mechanism for ensuring the stability of the MAI stablecoin.
    """

    def __init__(self):
        """
        Initializes the QiDaoProtocol with default parameters.
        """
        self.collateral = 0.0  # Total collateral in the system
        self.mai_supply = 0.0   # Total supply of MAI stablecoin
        self.collateralization_ratio = 1.5  # Required collateralization ratio (150%)

    def deposit_collateral(self, amount: float) -> None:
        """
        Allows users to deposit collateral into the protocol.

        Args:
            amount (float): The amount of collateral to deposit.

        Raises:
            ValueError: If the deposit amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.collateral += amount
        print(f"Deposited collateral: {amount}. Total collateral: {self.collateral}")

    def mint_mai(self, amount: float) -> None:
        """
        Mints MAI stablecoin based on the collateral provided.

        Args:
            amount (float): The amount of MAI to mint.

        Raises:
            ValueError: If the minting amount exceeds the collateralization limit.
        """
        required_collateral = amount * self.collateralization_ratio
        
        if required_collateral > self.collateral:
            raise ValueError("Insufficient collateral to mint the requested amount of MAI.")
        
        self.mai_supply += amount
        self.collateral -= required_collateral
        print(f"Minted MAI: {amount}. Total MAI supply: {self.mai_supply}. Remaining collateral: {self.collateral}")

    def redeem_mai(self, amount: float) -> None:
        """
        Allows users to redeem MAI stablecoin for collateral.

        Args:
            amount (float): The amount of MAI to redeem.

        Raises:
            ValueError: If the redemption amount exceeds the current MAI supply.
        """
        if amount > self.mai_supply:
            raise ValueError("Redemption amount exceeds the current MAI supply.")
        
        collateral_to_return = amount / self.collateralization_ratio
        self.mai_supply -= amount
        self.collateral += collateral_to_return
        print(f"Redeemed MAI: {amount}. Total MAI supply: {self.mai_supply}. Total collateral: {self.collateral}")

    def get_status(self) -> dict:
        """
        Returns the current status of the QiDao protocol.

        Returns:
            dict: A dictionary containing the current collateral, MAI supply, and collateralization ratio.
        """
        return {
            "collateral": self.collateral,
            "mai_supply": self.mai_supply,
            "collateralization_ratio": self.collateralization_ratio
        }


# Example usage
if __name__ == "__main__":
    try:
        qi_dao = QiDaoProtocol()
        qi_dao.deposit_collateral(150)  # Deposit collateral
        qi_dao.mint_mai(100)             # Mint MAI
        print(qi_dao.get_status())       # Get current status
        qi_dao.redeem_mai(50)            # Redeem MAI
        print(qi_dao.get_status())       # Get updated status
    except ValueError as e:
        print(f"Error: {e}")
```
