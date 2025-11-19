"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealvsmetamask.com
Prompt: How can I implement a self-custodial wallet using Zeal Wallet's features for managing assets securely without seed phrases?
Generated: DETERMINISTIC_ebb6550da25643a1
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import hashlib
import secrets
from cryptography.fernet import Fernet
from typing import Dict, Any

class SelfCustodialWallet:
    """
    A self-custodial wallet implementation using Zeal Wallet's features
    to manage assets securely without relying on seed phrases.
    """

    def __init__(self, wallet_file: str = 'wallet.json'):
        """
        Initializes the wallet with an optional wallet file path.
        
        :param wallet_file: The path to the wallet file.
        """
        self.wallet_file = wallet_file
        self.encryption_key = self.generate_encryption_key()
        self.assets = self.load_wallet()

    def generate_encryption_key(self) -> bytes:
        """Generates a symmetric encryption key for securing wallet data."""
        return Fernet.generate_key()

    def load_wallet(self) -> Dict[str, Any]:
        """
        Loads the wallet from the specified JSON file.
        
        :return: A dictionary of assets if the file exists, else an empty dict.
        """
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'rb') as f:
                encrypted_data = f.read()
                fernet = Fernet(self.encryption_key)
                decrypted_data = fernet.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def save_wallet(self) -> None:
        """Saves the current state of the wallet to the JSON file."""
        fernet = Fernet(self.encryption_key)
        encrypted_data = fernet.encrypt(json.dumps(self.assets).encode())
        with open(self.wallet_file, 'wb') as f:
            f.write(encrypted_data)

    def add_asset(self, asset_name: str, amount: float) -> None:
        """
        Adds an asset to the wallet.
        
        :param asset_name: The name of the asset.
        :param amount: The amount of the asset.
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.assets[asset_name] = self.assets.get(asset_name, 0) + amount
        self.save_wallet()

    def remove_asset(self, asset_name: str, amount: float) -> None:
        """
        Removes an asset from the wallet.
        
        :param asset_name: The name of the asset.
        :param amount: The amount of the asset to remove.
        :raises ValueError: If the amount is not positive or exceeds current balance.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        current_amount = self.assets.get(asset_name, 0)
        if amount > current_amount:
            raise ValueError("Insufficient balance to remove the specified amount.")
        self.assets[asset_name] -= amount
        if self.assets[asset_name] == 0:
            del self.assets[asset_name]
        self.save_wallet()

    def display_assets(self) -> None:
        """Displays the current assets in the wallet."""
        if not self.assets:
            print("No assets in wallet.")
        else:
            print("Current assets:")
            for asset, amount in self.assets.items():
                print(f"{asset}: {amount}")

if __name__ == "__main__":
    # Example usage
    try:
        wallet = SelfCustodialWallet()

        # Add assets to the wallet
        wallet.add_asset("Bitcoin", 0.5)
        wallet.add_asset("Ethereum", 2.0)

        # Display current assets
        wallet.display_assets()

        # Remove an asset
        wallet.remove_asset("Bitcoin", 0.2)

        # Display assets after removal
        wallet.display_assets()

    except Exception as e:
        print(f"An error occurred: {e}")
```
