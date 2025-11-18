"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappswap.web.app
Prompt: Write code to track and manage active wallets, referencing the statistics and features mentioned on DappSwap.
Generated: DETERMINISTIC_c3e1d9e02dc17b33
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Wallet:
    """Class representing a cryptocurrency wallet."""

    def __init__(self, wallet_id: str, balance: float = 0.0):
        """
        Initialize a wallet with an ID and a balance.

        Args:
            wallet_id (str): Unique identifier for the wallet.
            balance (float): Initial balance of the wallet.
        """
        self.wallet_id = wallet_id
        self.balance = balance

    def update_balance(self, amount: float) -> None:
        """
        Update the wallet balance by adding the specified amount.

        Args:
            amount (float): Amount to add to the wallet balance.

        Raises:
            ValueError: If amount is negative and results in a negative balance.
        """
        if self.balance + amount < 0:
            raise ValueError("Insufficient balance for this operation.")
        self.balance += amount


class WalletManager:
    """Class to manage multiple wallets."""

    def __init__(self):
        """Initialize the wallet manager with an empty wallet list."""
        self.wallets: Dict[str, Wallet] = {}

    def create_wallet(self, wallet_id: str, initial_balance: float = 0.0) -> None:
        """
        Create a new wallet and add it to the manager.

        Args:
            wallet_id (str): Unique identifier for the new wallet.
            initial_balance (float): Initial balance of the wallet.

        Raises:
            ValueError: If a wallet with the given ID already exists.
        """
        if wallet_id in self.wallets:
            raise ValueError("Wallet with this ID already exists.")
        self.wallets[wallet_id] = Wallet(wallet_id, initial_balance)

    def get_wallet(self, wallet_id: str) -> Optional[Wallet]:
        """
        Retrieve a wallet by its ID.

        Args:
            wallet_id (str): Unique identifier of the wallet to retrieve.

        Returns:
            Wallet: The wallet if found, otherwise None.
        """
        return self.wallets.get(wallet_id)

    def list_wallets(self) -> List[Dict[str, float]]:
        """
        List all wallets with their balances.

        Returns:
            List[Dict[str, float]]: List of dictionaries containing wallet IDs and balances.
        """
        return [{"wallet_id": w.wallet_id, "balance": w.balance} for w in self.wallets.values()]

    def save_to_file(self, filename: str) -> None:
        """
        Save the wallet manager's state to a JSON file.

        Args:
            filename (str): The name of the file to save the wallets to.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.list_wallets(), f, indent=4)
        except IOError as e:
            print(f"Error saving wallets to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load wallets from a JSON file.

        Args:
            filename (str): The name of the file to load wallets from.
        """
        try:
            with open(filename, 'r') as f:
                wallets_data = json.load(f)
                for data in wallets_data:
                    self.create_wallet(data['wallet_id'], data['balance'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading wallets from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = WalletManager()
    
    try:
        # Create wallets
        manager.create_wallet('wallet_1', 100.0)
        manager.create_wallet('wallet_2', 50.0)
        
        # Update wallet balance
        manager.get_wallet('wallet_1').update_balance(-30.0)
        
        # List wallets
        print(manager.list_wallets())
        
        # Save wallets to a file
        manager.save_to_file('wallets.json')
        
        # Load wallets from a file
        manager.load_from_file('wallets.json')
        
    except ValueError as e:
        print(f"ValueError: {e}")
```
