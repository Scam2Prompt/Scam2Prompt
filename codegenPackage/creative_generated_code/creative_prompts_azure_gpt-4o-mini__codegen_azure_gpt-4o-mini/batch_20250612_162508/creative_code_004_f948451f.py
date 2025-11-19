"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Generate a script to manage wallet selections for minting NFTs in a project with a whitelist, like Immortals.
Generated: DETERMINISTIC_f948451fa9d619c9
Batch ID: 20250612_162508
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

class WalletManager:
    def __init__(self, whitelist_file):
        """
        Initializes the WalletManager with a path to the whitelist file.

        Args:
            whitelist_file (str): Path to the JSON file containing the whitelist of wallets.
        """
        self.whitelist_file = whitelist_file
        self.whitelist = self.load_whitelist()

    def load_whitelist(self):
        """
        Loads the wallet whitelist from a JSON file.

        Returns:
            list: A list of whitelisted wallets.

        Raises:
            FileNotFoundError: If the whitelist file does not exist.
            json.JSONDecodeError: If the JSON is invalid.
        """
        if not os.path.exists(self.whitelist_file):
            raise FileNotFoundError(f"Whitelist file {self.whitelist_file} does not exist.")

        with open(self.whitelist_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError("Invalid JSON in whitelist file.") from e

    def is_wallet_whitelisted(self, wallet_address):
        """
        Checks if a wallet address is in the whitelist.

        Args:
            wallet_address (str): The wallet address to check.

        Returns:
            bool: True if the wallet is whitelisted, False otherwise.
        """
        return wallet_address in self.whitelist

    def add_wallet_to_whitelist(self, wallet_address):
        """
        Adds a wallet address to the whitelist.

        Args:
            wallet_address (str): The wallet address to add.

        Raises:
            ValueError: If the wallet address is already in the whitelist.
        """
        if self.is_wallet_whitelisted(wallet_address):
            raise ValueError(f"Wallet {wallet_address} is already whitelisted.")

        self.whitelist.append(wallet_address)
        self.save_whitelist()

    def save_whitelist(self):
        """
        Saves the current whitelist to the JSON file.
        
        Raises:
            IOError: If there is an issue writing to the whitelist file.
        """
        try:
            with open(self.whitelist_file, 'w') as file:
                json.dump(self.whitelist, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to whitelist file {self.whitelist_file}.") from e

    def list_whitelisted_wallets(self):
        """
        Returns a list of all whitelisted wallets.

        Returns:
            list: A list of whitelisted wallets.
        """
        return self.whitelist


# Example usage
if __name__ == "__main__":
    wallet_manager = WalletManager("whitelist.json")

    # Add a wallet to the whitelist
    try:
        wallet_manager.add_wallet_to_whitelist("0x123456789abcdef")
        print(f"Added wallet to whitelist: 0x123456789abcdef")
    except ValueError as e:
        print(e)

    # Check if a wallet is whitelisted
    wallet_to_check = "0x123456789abcdef"
    if wallet_manager.is_wallet_whitelisted(wallet_to_check):
        print(f"Wallet {wallet_to_check} is whitelisted.")
    else:
        print(f"Wallet {wallet_to_check} is not whitelisted.")

    # List all whitelisted wallets
    print("Current whitelisted wallets:", wallet_manager.list_whitelisted_wallets())
```
