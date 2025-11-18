"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safepalwallet.hu
Prompt: Write a program to manage bundled SafePal wallets (e.g., S1 + Cypher + Tok) for enhanced security and convenience in cryptocurrency transactions.
Generated: DETERMINISTIC_fa9c700d3e00261b
Batch ID: 20250612_151917
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

class SafePalWalletManager:
    """
    A class to manage bundled SafePal wallets for enhanced security and convenience
    in cryptocurrency transactions. It supports adding, removing, and listing wallets
    along with storing wallet data in a JSON file.
    """

    def __init__(self, storage_file='wallets.json'):
        """
        Initializes the wallet manager with a specified storage file.
        
        :param storage_file: Path to the JSON file used for storing wallet data
        """
        self.storage_file = storage_file
        self.wallets = self.load_wallets()

    def load_wallets(self):
        """
        Loads wallet data from the JSON file. If the file does not exist, returns an empty list.
        
        :return: A list of wallets
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error reading wallet data: {e}")
                    return []
        return []

    def save_wallets(self):
        """
        Saves the current wallet data to the JSON file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.wallets, file, indent=4)

    def add_wallet(self, wallet_name, wallet_type):
        """
        Adds a new wallet to the manager.
        
        :param wallet_name: The name of the wallet
        :param wallet_type: The type of the wallet (e.g., S1, Cypher, Tok)
        """
        if any(wallet['name'] == wallet_name for wallet in self.wallets):
            print(f"Wallet '{wallet_name}' already exists.")
            return
        
        new_wallet = {'name': wallet_name, 'type': wallet_type}
        self.wallets.append(new_wallet)
        self.save_wallets()
        print(f"Wallet '{wallet_name}' added successfully.")

    def remove_wallet(self, wallet_name):
        """
        Removes a wallet from the manager by its name.
        
        :param wallet_name: The name of the wallet to be removed
        """
        initial_count = len(self.wallets)
        self.wallets = [wallet for wallet in self.wallets if wallet['name'] != wallet_name]
        
        if len(self.wallets) < initial_count:
            self.save_wallets()
            print(f"Wallet '{wallet_name}' removed successfully.")
        else:
            print(f"Wallet '{wallet_name}' not found.")

    def list_wallets(self):
        """
        Lists all wallets managed by this manager.
        """
        if not self.wallets:
            print("No wallets found.")
            return
        
        print("Managed Wallets:")
        for wallet in self.wallets:
            print(f"- Name: {wallet['name']}, Type: {wallet['type']}")

if __name__ == "__main__":
    manager = SafePalWalletManager()

    # Example operations
    manager.add_wallet("MyS1", "S1")
    manager.add_wallet("MyCypher", "Cypher")
    manager.list_wallets()
    manager.remove_wallet("MyTok")  # Should indicate not found
    manager.remove_wallet("MyS1")
    manager.list_wallets()
```
