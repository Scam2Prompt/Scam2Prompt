"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedapponlineportal.com
Prompt: Generate code to track active users, supported wallets, and total transactions using metrics similar to those provided on the "Defi Dapp Pages" platform.
Generated: DETERMINISTIC_bdfc4d75c9888407
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from collections import defaultdict

class DAppMetricsTracker:
    """
    A class to track metrics for a DeFi DApp platform, including:
    - Active users
    - Supported wallets
    - Total transactions
    """
    
    def __init__(self):
        """
        Initializes the metrics tracker with default values.
        """
        self.active_users = set()  # Using a set to ensure uniqueness
        self.supported_wallets = set()  # Wallets supported by the DApp
        self.transaction_count = 0  # Total number of transactions
        self.user_transaction_history = defaultdict(list)  # Tracks transactions per user
    
    def user_login(self, user_id: str):
        """
        Adds a user to the set of active users when they log in.
        
        Args:
            user_id (str): A unique identifier for the user.
        """
        if user_id:
            self.active_users.add(user_id)
        else:
            raise ValueError("Invalid user ID provided.")

    def user_logout(self, user_id: str):
        """
        Removes a user from the set of active users when they log out.
        
        Args:
            user_id (str): A unique identifier for the user.
        """
        if user_id in self.active_users:
            self.active_users.remove(user_id)
        else:
            raise ValueError("User ID is not currently active.")

    def add_supported_wallet(self, wallet_name: str):
        """
        Adds a wallet to the set of supported wallets.
        
        Args:
            wallet_name (str): Name of the wallet to be added.
        """
        if wallet_name:
            self.supported_wallets.add(wallet_name)
        else:
            raise ValueError("Wallet name cannot be empty.")

    def remove_supported_wallet(self, wallet_name: str):
        """
        Removes a wallet from the set of supported wallets.
        
        Args:
            wallet_name (str): Name of the wallet to be removed.
        """
        if wallet_name in self.supported_wallets:
            self.supported_wallets.remove(wallet_name)
        else:
            raise ValueError("Wallet is not in the list of supported wallets.")

    def record_transaction(self, user_id: str, transaction_details: dict):
        """
        Records a transaction for a user and increments the transaction count.
        
        Args:
            user_id (str): Identifier for the user making the transaction.
            transaction_details (dict): Details of the transaction.
        """
        if not user_id or not isinstance(transaction_details, dict):
            raise ValueError("Invalid user ID or transaction details.")

        self.transaction_count += 1
        self.user_transaction_history[user_id].append({
            "timestamp": time.time(),
            "details": transaction_details,
        })

    def get_metrics(self) -> dict:
        """
        Retrieves all metrics for the DApp.

        Returns:
            dict: A dictionary containing active users, supported wallets, and total transactions.
        """
        return {
            "active_users": len(self.active_users),
            "supported_wallets": list(self.supported_wallets),
            "total_transactions": self.transaction_count
        }

    def detailed_transaction_history(self) -> dict:
        """
        Retrieves the detailed transaction history for all users.

        Returns:
            dict: A dictionary mapping user IDs to their respective transaction histories.
        """
        return self.user_transaction_history


# Example usage:
if __name__ == "__main__":
    tracker = DAppMetricsTracker()

    # Managing active users
    tracker.user_login("user1")
    tracker.user_login("user2")
    tracker.user_logout("user2")

    # Managing supported wallets
    tracker.add_supported_wallet("Metamask")
    tracker.add_supported_wallet("Coinbase Wallet")
    tracker.remove_supported_wallet("Coinbase Wallet")

    # Recording transactions
    tracker.record_transaction("user1", {"amount": 100, "currency": "ETH"})
    tracker.record_transaction("user1", {"amount": 50, "currency": "BTC"})

    # Retrieving metrics
    print(tracker.get_metrics())
    print(tracker.detailed_transaction_history())
```
