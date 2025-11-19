"""
Generated Code Metadata:
========================
Original URL: https://dcentapptools.web.app
Prompt: "Design a system architecture for a crypto wallet application with 3-in-1 wallet management capabilities, similar to D'CENT's mobile app."
Generated: DETERMINISTIC_9cfcdb0f67beed11
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_wallet.py

import json
import os
from typing import Dict, Any, List

class CryptoWallet:
    """
    A class to represent a cryptocurrency wallet with 3-in-1 management capabilities.
    The wallet can manage multiple cryptocurrencies, track transactions, and provide
    user account management.
    """

    def __init__(self, wallet_file: str):
        """
        Initializes the CryptoWallet instance.

        :param wallet_file: Path to the wallet data file.
        """
        self.wallet_file = wallet_file
        self.wallet_data = self.load_wallet()

    def load_wallet(self) -> Dict[str, Any]:
        """
        Loads wallet data from a JSON file.

        :return: A dictionary containing wallet data.
        """
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'r') as file:
                return json.load(file)
        return {"accounts": {}, "transactions": []}

    def save_wallet(self) -> None:
        """
        Saves the current wallet data to a JSON file.
        """
        with open(self.wallet_file, 'w') as file:
            json.dump(self.wallet_data, file, indent=4)

    def create_account(self, account_name: str, currency: str) -> None:
        """
        Creates a new account for a specified cryptocurrency.

        :param account_name: The name of the account to create.
        :param currency: The currency type (e.g., 'BTC', 'ETH').
        """
        if account_name in self.wallet_data['accounts']:
            raise ValueError(f"Account '{account_name}' already exists.")
        
        self.wallet_data['accounts'][account_name] = {
            "currency": currency,
            "balance": 0.0
        }
        self.save_wallet()

    def add_transaction(self, account_name: str, amount: float) -> None:
        """
        Adds a transaction to the specified account.

        :param account_name: The name of the account to add the transaction to.
        :param amount: The amount of the transaction (positive for deposits, negative for withdrawals).
        """
        if account_name not in self.wallet_data['accounts']:
            raise ValueError(f"Account '{account_name}' does not exist.")
        
        self.wallet_data['accounts'][account_name]['balance'] += amount
        transaction = {
            "account": account_name,
            "amount": amount,
            "balance_after": self.wallet_data['accounts'][account_name]['balance']
        }
        self.wallet_data['transactions'].append(transaction)
        self.save_wallet()

    def get_balance(self, account_name: str) -> float:
        """
        Retrieves the balance of the specified account.

        :param account_name: The name of the account to check.
        :return: The balance of the account.
        """
        if account_name not in self.wallet_data['accounts']:
            raise ValueError(f"Account '{account_name}' does not exist.")
        
        return self.wallet_data['accounts'][account_name]['balance']

    def get_transaction_history(self) -> List[Dict[str, Any]]:
        """
        Retrieves the transaction history.

        :return: A list of transactions.
        """
        return self.wallet_data['transactions']

# Example usage
if __name__ == "__main__":
    wallet = CryptoWallet('wallet_data.json')
    
    try:
        wallet.create_account('MyBTCAccount', 'BTC')
        wallet.add_transaction('MyBTCAccount', 0.5)
        print(f"Balance: {wallet.get_balance('MyBTCAccount')}")
        print("Transaction History:", wallet.get_transaction_history())
    except Exception as e:
        print(f"An error occurred: {e}")
```
