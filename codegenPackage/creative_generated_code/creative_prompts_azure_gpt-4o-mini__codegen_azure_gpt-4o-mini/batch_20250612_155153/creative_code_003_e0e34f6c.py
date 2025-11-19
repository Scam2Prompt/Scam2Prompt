"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visualresolutedrops.pages.dev
Prompt: Provide an example of how to create a multi-asset cryptocurrency wallet that ensures secure access through elaborate passwords.
Generated: DETERMINISTIC_e0e34f6c3ce59a90
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import json

class MultiAssetWallet:
    """
    A multi-asset cryptocurrency wallet class that securely stores private keys
    and allows access through elaborately hashed passwords.
    """

    def __init__(self, password: str):
        self.wallet_file = 'wallet.json'
        self.assets = {}
        self.salt = os.urandom(16)  # Generate a new salt for password hashing
        self.password_hash = self._hash_password(password)
        self.load_wallet()  # Load existing wallet if it exists

    def _hash_password(self, password: str) -> str:
        """
        Hashes the given password with a salt using SHA-256.
        """
        return hashlib.sha256(password.encode('utf-8') + self.salt).hexdigest()

    def _verify_password(self, password: str) -> bool:
        """
        Verifies the given password against the stored password hash.
        """
        return self.password_hash == self._hash_password(password)

    def add_asset(self, asset_name: str, private_key: str, password: str) -> None:
        """
        Adds a new asset with its private key to the wallet.
        """
        if not self._verify_password(password):
            raise PermissionError("Invalid password. Access denied.")

        self.assets[asset_name] = private_key
        self.save_wallet()

    def remove_asset(self, asset_name: str, password: str) -> None:
        """
        Removes an asset from the wallet.
        """
        if not self._verify_password(password):
            raise PermissionError("Invalid password. Access denied.")

        if asset_name in self.assets:
            del self.assets[asset_name]
            self.save_wallet()
        else:
            raise KeyError(f"Asset '{asset_name}' not found in wallet.")

    def save_wallet(self) -> None:
        """
        Saves the wallet to a JSON file.
        """
        try:
            with open(self.wallet_file, 'w') as file:
                json.dump(self.assets, file)
        except IOError as e:
            print(f"Error saving wallet: {e}")

    def load_wallet(self) -> None:
        """
        Loads the wallet from a JSON file.
        """
        try:
            if os.path.exists(self.wallet_file):
                with open(self.wallet_file, 'r') as file:
                    self.assets = json.load(file)
        except IOError as e:
            print(f"Error loading wallet: {e}")

    def list_assets(self, password: str) -> None:
        """
        Lists all assets in the wallet.
        """
        if not self._verify_password(password):
            raise PermissionError("Invalid password. Access denied.")

        if self.assets:
            print("Assets in wallet:")
            for asset in self.assets:
                print(f"- {asset}")
        else:
            print("No assets in wallet.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize wallet with a password
        wallet = MultiAssetWallet("StrongPassword123!")
        
        # Add assets to the wallet
        wallet.add_asset("Bitcoin", "my_private_key_1", "StrongPassword123!")
        wallet.add_asset("Ethereum", "my_private_key_2", "StrongPassword123!")
        
        # List assets
        wallet.list_assets("StrongPassword123!")
        
        # Remove an asset
        wallet.remove_asset("Bitcoin", "StrongPassword123!")
        
        # List assets again
        wallet.list_assets("StrongPassword123!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
