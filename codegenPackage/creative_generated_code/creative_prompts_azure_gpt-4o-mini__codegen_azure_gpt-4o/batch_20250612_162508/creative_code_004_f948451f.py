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

class WalletManager:
    """
    A class to manage wallet selections for minting NFTs in a project with a whitelist.
    """
    
    def __init__(self, whitelist_file="whitelist.json"):
        """
        Initializes the WalletManager object.
        
        Args:
            whitelist_file (str): Path to the JSON file containing the whitelist of wallets.
        """
        self.whitelist_file = whitelist_file
        self.whitelist = self.load_whitelist()

    def load_whitelist(self):
        """
        Loads the whitelist from a JSON file.

        Returns:
            dict: A dictionary containing wallets in the whitelist.

        Raises:
            FileNotFoundError: If the whitelist file does not exist.
            ValueError: If the JSON file is not properly formatted.
        """
        try:
            with open(self.whitelist_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: Whitelist file '{self.whitelist_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to parse the whitelist file. Ensure it is properly formatted.")
            return {}

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

        Returns:
            bool: True if the wallet was successfully added, False if it already exists.
        """
        if not self.is_wallet_whitelisted(wallet_address):
            self.whitelist[wallet_address] = {"status": "active"}
            self.save_whitelist()
            return True
        else:
            print("Wallet address is already in the whitelist.")
            return False

    def remove_wallet_from_whitelist(self, wallet_address):
        """
        Removes a wallet address from the whitelist.

        Args:
            wallet_address (str): The wallet address to remove.

        Returns:
            bool: True if the wallet was successfully removed, False if it does not exist.
        """
        if self.is_wallet_whitelisted(wallet_address):
            del self.whitelist[wallet_address]
            self.save_whitelist()
            return True
        else:
            print("Wallet address not found in the whitelist.")
            return False

    def save_whitelist(self):
        """
        Saves the current whitelist to the JSON file.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(self.whitelist_file, "w") as file:
                json.dump(self.whitelist, file, indent=4)
        except IOError:
            print("Error: Failed to save the whitelist file.")

    def list_whitelisted_wallets(self):
        """
        Lists all wallets currently in the whitelist.

        Returns:
            list: A list of whitelisted wallet addresses.
        """
        return list(self.whitelist.keys())


# Example usage:
if __name__ == "__main__":
    # Initialize the WalletManager with the path to the whitelist file
    manager = WalletManager("whitelist.json")

    # Add a wallet to the whitelist
    manager.add_wallet_to_whitelist("wallet_address_1")

    # List all whitelisted wallets
    print("Whitelisted wallets:", manager.list_whitelisted_wallets())

    # Check if a wallet is whitelisted
    print("Is wallet_address_1 whitelisted?", manager.is_wallet_whitelisted("wallet_address_1"))

    # Remove a wallet from the whitelist
    manager.remove_wallet_from_whitelist("wallet_address_1")
```
