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
"""
WalletManager: A module to track and manage active wallets.
This code is designed to reference statistics and features inspired by DappSwap.

Key Features:
- Add new wallets
- Remove wallets
- Retrieve statistics about active wallets
- Handle errors gracefully
- Follow Python best practices
"""

from typing import Dict, Optional


class WalletManager:
    """
    A class to manage and track active wallets.
    """
    def __init__(self):
        # Initialize an empty dictionary to store wallets and their associated data.
        self.wallets: Dict[str, Dict[str, Optional[int]]] = {}

    def add_wallet(self, wallet_id: str, balance: int = 0) -> None:
        """
        Add a new wallet to the manager.
        :param wallet_id: Unique identifier for the wallet.
        :param balance: Starting balance for the wallet (default is 0).
        :raises ValueError: If the wallet ID already exists.
        """
        if wallet_id in self.wallets:
            raise ValueError(f"Wallet with ID '{wallet_id}' already exists.")
        self.wallets[wallet_id] = {
            "balance": balance,
            "transactions": 0,  # Tracks the number of transactions for the wallet.
        }

    def remove_wallet(self, wallet_id: str) -> None:
        """
        Remove a wallet from the manager.
        :param wallet_id: Unique identifier for the wallet.
        :raises KeyError: If the wallet ID does not exist.
        """
        if wallet_id not in self.wallets:
            raise KeyError(f"Wallet with ID '{wallet_id}' does not exist.")
        del self.wallets[wallet_id]

    def update_balance(self, wallet_id: str, amount: int) -> None:
        """
        Update the balance of a wallet.
        :param wallet_id: Unique identifier for the wallet.
        :param amount: Amount to add (positive) or subtract (negative) from the balance.
        :raises KeyError: If the wallet ID does not exist.
        """
        if wallet_id not in self.wallets:
            raise KeyError(f"Wallet with ID '{wallet_id}' does not exist.")
        self.wallets[wallet_id]["balance"] += amount
        self.wallets[wallet_id]["transactions"] += 1

    def get_wallet_info(self, wallet_id: str) -> Dict[str, Optional[int]]:
        """
        Retrieve information about a specific wallet.
        :param wallet_id: Unique identifier for the wallet.
        :return: A dictionary containing wallet information.
        :raises KeyError: If the wallet ID does not exist.
        """
        if wallet_id not in self.wallets:
            raise KeyError(f"Wallet with ID '{wallet_id}' does not exist.")
        return self.wallets[wallet_id]

    def get_statistics(self) -> Dict[str, int]:
        """
        Retrieve statistics about all active wallets.
        :return: A dictionary containing total wallet count, total balance, and total transactions.
        """
        total_wallets = len(self.wallets)
        total_balance = sum(wallet["balance"] for wallet in self.wallets.values())
        total_transactions = sum(wallet["transactions"] for wallet in self.wallets.values())
        return {
            "total_wallets": total_wallets,
            "total_balance": total_balance,
            "total_transactions": total_transactions,
        }


# Example Usage (uncomment to test):
# manager = WalletManager()
# manager.add_wallet("wallet_1", 100)
# manager.add_wallet("wallet_2", 200)
# manager.update_balance("wallet_1", -50)
# manager.update_balance("wallet_2", 100)
# print(manager.get_wallet_info("wallet_1"))
# print(manager.get_statistics())
# manager.remove_wallet("wallet_2")
# print(manager.get_statistics())
```
