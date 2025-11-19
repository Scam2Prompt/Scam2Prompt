"""
Generated Code Metadata:
========================
Original URL: https://mitofi-launchpad.pages.dev
Prompt: What are the key features of Black Panther's vaults in the context of asset management on Injective?
Generated: DETERMINISTIC_d53edc89e136aeb8
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines the key features of Black Panther's vaults in the context of asset management on Injective.
The code is designed to simulate the core functionalities of vaults, including deposit, withdrawal, and asset tracking.
"""

class BlackPantherVault:
    """
    Black Panther Vault class for asset management on Injective.
    """

    def __init__(self, vault_name):
        """
        Initialize the vault with a name and an empty asset pool.
        :param vault_name: Name of the vault.
        """
        self.vault_name = vault_name
        self.assets = {}  # Dictionary to track assets and their quantities

    def deposit(self, asset_name, quantity):
        """
        Deposit assets into the vault.
        :param asset_name: Name of the asset to deposit.
        :param quantity: Quantity of the asset to deposit.
        :raises ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Deposit quantity must be greater than zero.")
        
        # Add asset to the vault or update its quantity
        if asset_name in self.assets:
            self.assets[asset_name] += quantity
        else:
            self.assets[asset_name] = quantity

        print(f"Deposited {quantity} of {asset_name} into {self.vault_name}.")

    def withdraw(self, asset_name, quantity):
        """
        Withdraw assets from the vault.
        :param asset_name: Name of the asset to withdraw.
        :param quantity: Quantity of the asset to withdraw.
        :raises ValueError: If quantity is not positive or exceeds available balance.
        :raises KeyError: If the asset does not exist in the vault.
        """
        if quantity <= 0:
            raise ValueError("Withdrawal quantity must be greater than zero.")
        
        if asset_name not in self.assets:
            raise KeyError(f"{asset_name} does not exist in the vault.")
        
        if self.assets[asset_name] < quantity:
            raise ValueError(f"Insufficient balance for {asset_name}. Available: {self.assets[asset_name]}.")

        # Deduct the asset quantity from the vault
        self.assets[asset_name] -= quantity

        print(f"Withdrew {quantity} of {asset_name} from {self.vault_name}.")

        # Remove the asset from the vault if its quantity becomes zero
        if self.assets[asset_name] == 0:
            del self.assets[asset_name]

    def get_vault_summary(self):
        """
        Get a summary of the assets in the vault.
        :return: Dictionary containing asset names and their quantities.
        """
        return self.assets

    def __str__(self):
        """
        String representation of the vault.
        :return: Summary of the vault's assets.
        """
        return f"Vault '{self.vault_name}' contains: {self.assets}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a vault
        vault = BlackPantherVault("Wakanda Vault")

        # Deposit assets
        vault.deposit("Gold", 100)
        vault.deposit("Vibranium", 50)

        # Withdraw assets
        vault.withdraw("Gold", 30)

        # Print vault summary
        print(vault)

    except Exception as e:
        print(f"Error: {e}")
```
