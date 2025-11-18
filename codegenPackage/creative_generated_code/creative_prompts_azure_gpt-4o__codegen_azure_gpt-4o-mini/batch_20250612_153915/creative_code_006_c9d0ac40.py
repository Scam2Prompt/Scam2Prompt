"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Generate code to interact with TON wallets across multiple operating systems, including creating and managing wallets programmatically.
Generated: DETERMINISTIC_c9d0ac40cec704d8
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import subprocess
from typing import Dict, Any, Optional

class TonWallet:
    """Class to manage TON wallets programmatically."""

    def __init__(self, wallet_directory: str):
        """
        Initialize the TonWallet class.

        Args:
            wallet_directory (str): Directory where wallets will be stored.
        """
        self.wallet_directory = wallet_directory
        os.makedirs(self.wallet_directory, exist_ok=True)

    def create_wallet(self, wallet_name: str) -> Dict[str, Any]:
        """
        Create a new TON wallet.

        Args:
            wallet_name (str): The name of the new wallet.

        Returns:
            Dict[str, Any]: Details of the created wallet including its address and keys.
        """
        wallet_path = os.path.join(self.wallet_directory, wallet_name + '.json')

        # Check if the wallet already exists
        if os.path.exists(wallet_path):
            raise FileExistsError(f"Wallet '{wallet_name}' already exists.")

        # Placeholder for wallet creation logic
        wallet_data = {
            'address': '0:example_address',  # Replace with actual wallet address
            'private_key': 'example_private_key',  # Replace with actual private key
            'public_key': 'example_public_key'  # Replace with actual public key
        }

        # Save wallet data to a JSON file
        with open(wallet_path, 'w') as wallet_file:
            json.dump(wallet_data, wallet_file)

        return wallet_data

    def load_wallet(self, wallet_name: str) -> Optional[Dict[str, Any]]:
        """
        Load an existing TON wallet.

        Args:
            wallet_name (str): The name of the wallet to load.

        Returns:
            Optional[Dict[str, Any]]: Wallet details if found, None otherwise.
        """
        wallet_path = os.path.join(self.wallet_directory, wallet_name + '.json')

        # Check if the wallet file exists
        if not os.path.exists(wallet_path):
            raise FileNotFoundError(f"Wallet '{wallet_name}' does not exist.")

        # Load wallet data from the JSON file
        with open(wallet_path, 'r') as wallet_file:
            return json.load(wallet_file)

    def delete_wallet(self, wallet_name: str) -> None:
        """
        Delete a TON wallet.

        Args:
            wallet_name (str): The name of the wallet to delete.

        Raises:
            FileNotFoundError: If the wallet does not exist.
        """
        wallet_path = os.path.join(self.wallet_directory, wallet_name + '.json')

        # Check if the wallet file exists
        if not os.path.exists(wallet_path):
            raise FileNotFoundError(f"Wallet '{wallet_name}' does not exist.")

        # Remove the wallet file
        os.remove(wallet_path)

    def list_wallets(self) -> None:
        """List all wallets in the wallet directory."""
        wallets = [f[:-5] for f in os.listdir(self.wallet_directory) if f.endswith('.json')]
        print("Available wallets:", wallets)

    def send_transaction(self, wallet_name: str, recipient: str, amount: float) -> str:
        """
        Send a transaction from the specified wallet.

        Args:
            wallet_name (str): The name of the wallet to use for the transaction.
            recipient (str): The address of the recipient wallet.
            amount (float): The amount to send.

        Returns:
            str: Transaction status message.
        """
        wallet_data = self.load_wallet(wallet_name)
        
        # Placeholder for transaction logic
        # In a real scenario, you would interact with the TON blockchain here
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Simulate sending the transaction
        return f"Sent {amount} TON from {wallet_data['address']} to {recipient}."

# Example usage
if __name__ == "__main__":
    wallet_manager = TonWallet(wallet_directory='./ton_wallets')

    # Creating a new wallet
    try:
        wallet_info = wallet_manager.create_wallet('my_first_wallet')
        print("Wallet created:", wallet_info)
    except Exception as e:
        print(f"Error creating wallet: {e}")

    # Listing wallets
    wallet_manager.list_wallets()

    # Sending a transaction
    try:
        transaction_status = wallet_manager.send_transaction('my_first_wallet', '0:recipient_address', 10.0)
        print(transaction_status)
    except Exception as e:
        print(f"Error sending transaction: {e}")

    # Deleting a wallet
    try:
        wallet_manager.delete_wallet('my_first_wallet')
        print("Wallet deleted successfully.")
    except Exception as e:
        print(f"Error deleting wallet: {e}")
```
