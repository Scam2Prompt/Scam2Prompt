"""
Generated Code Metadata:
========================
Original URL: https://digitalbitbox.com
Prompt: Create a tutorial for using the BitBoxApp to securely store and manage cryptocurrencies offline, leveraging its advanced features for power users.
Generated: DETERMINISTIC_71130bf3efec2206
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BitBoxApp Tutorial: Securely Store and Manage Cryptocurrencies Offline

This script demonstrates how to use the BitBoxApp to securely store and manage cryptocurrencies.
It includes advanced features for power users, such as creating wallets, sending transactions,
and managing multiple accounts.

Requirements:
- BitBoxApp installed
- Python 3.x
- bitbox02 library (install via pip: `pip install bitbox02`)

Note: This is a simplified example for educational purposes. Always refer to the official
documentation for the latest features and security practices.
"""

import time
from bitbox02 import BitBox02, BitBox02Error

class BitBoxApp:
    def __init__(self):
        """Initialize the BitBoxApp with the connected device."""
        try:
            self.device = BitBox02()
            print("BitBoxApp initialized successfully.")
        except BitBox02Error as e:
            print(f"Error initializing BitBoxApp: {e}")
            raise

    def create_wallet(self, wallet_name):
        """Create a new wallet with the given name."""
        try:
            self.device.create_wallet(wallet_name)
            print(f"Wallet '{wallet_name}' created successfully.")
        except BitBox02Error as e:
            print(f"Error creating wallet: {e}")

    def send_transaction(self, wallet_name, recipient_address, amount):
        """Send a transaction from the specified wallet to the recipient address."""
        try:
            self.device.select_wallet(wallet_name)
            self.device.send_transaction(recipient_address, amount)
            print(f"Transaction of {amount} sent to {recipient_address} from wallet '{wallet_name}'.")
        except BitBox02Error as e:
            print(f"Error sending transaction: {e}")

    def list_wallets(self):
        """List all wallets stored in the BitBoxApp."""
        try:
            wallets = self.device.list_wallets()
            print("Available wallets:")
            for wallet in wallets:
                print(f"- {wallet}")
        except BitBox02Error as e:
            print(f"Error listing wallets: {e}")

    def backup_wallet(self, wallet_name):
        """Backup the specified wallet."""
        try:
            backup_file = self.device.backup_wallet(wallet_name)
            print(f"Wallet '{wallet_name}' backed up successfully to {backup_file}.")
        except BitBox02Error as e:
            print(f"Error backing up wallet: {e}")

    def restore_wallet(self, backup_file):
        """Restore a wallet from a backup file."""
        try:
            self.device.restore_wallet(backup_file)
            print(f"Wallet restored successfully from {backup_file}.")
        except BitBox02Error as e:
            print(f"Error restoring wallet: {e}")

if __name__ == "__main__":
    # Example usage of the BitBoxApp class
    app = BitBoxApp()
    
    # Create a new wallet
    app.create_wallet("MyCryptoWallet")
    
    # List all wallets
    app.list_wallets()
    
    # Send a transaction (example values)
    app.send_transaction("MyCryptoWallet", "recipient_address_here", 0.01)
    
    # Backup the wallet
    app.backup_wallet("MyCryptoWallet")
    
    # Restore the wallet from a backup (example backup file)
    app.restore_wallet("backup_file_path_here")
```
