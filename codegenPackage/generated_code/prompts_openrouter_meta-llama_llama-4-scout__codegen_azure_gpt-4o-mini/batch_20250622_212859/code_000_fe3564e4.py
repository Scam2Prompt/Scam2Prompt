"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: What are the key features of an IT ledger system, and how can they be implemented in a small business setting?
Generated: DETERMINISTIC_fe3564e4fb38d6b1
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class ITLedger:
    """
    A class to represent an IT ledger system for tracking IT assets and transactions.
    """

    def __init__(self, ledger_file='ledger.json'):
        """
        Initializes the IT ledger with a specified file to store data.
        
        :param ledger_file: The file where the ledger data will be stored.
        """
        self.ledger_file = ledger_file
        self.ledger_data = self.load_ledger()

    def load_ledger(self):
        """
        Loads the ledger data from a JSON file.
        
        :return: A dictionary containing the ledger data.
        """
        if os.path.exists(self.ledger_file):
            with open(self.ledger_file, 'r') as file:
                return json.load(file)
        return {"assets": [], "transactions": []}

    def save_ledger(self):
        """
        Saves the current ledger data to a JSON file.
        """
        with open(self.ledger_file, 'w') as file:
            json.dump(self.ledger_data, file, indent=4)

    def add_asset(self, asset_name, asset_type, purchase_date, value):
        """
        Adds a new asset to the ledger.
        
        :param asset_name: The name of the asset.
        :param asset_type: The type of the asset (e.g., hardware, software).
        :param purchase_date: The purchase date of the asset.
        :param value: The value of the asset.
        """
        asset = {
            "name": asset_name,
            "type": asset_type,
            "purchase_date": purchase_date,
            "value": value
        }
        self.ledger_data['assets'].append(asset)
        self.save_ledger()

    def record_transaction(self, asset_name, transaction_type, transaction_date, amount):
        """
        Records a transaction related to an asset.
        
        :param asset_name: The name of the asset involved in the transaction.
        :param transaction_type: The type of transaction (e.g., purchase, sale).
        :param transaction_date: The date of the transaction.
        :param amount: The amount involved in the transaction.
        """
        transaction = {
            "asset_name": asset_name,
            "type": transaction_type,
            "date": transaction_date,
            "amount": amount
        }
        self.ledger_data['transactions'].append(transaction)
        self.save_ledger()

    def get_assets(self):
        """
        Retrieves the list of assets in the ledger.
        
        :return: A list of assets.
        """
        return self.ledger_data['assets']

    def get_transactions(self):
        """
        Retrieves the list of transactions in the ledger.
        
        :return: A list of transactions.
        """
        return self.ledger_data['transactions']

    def find_asset(self, asset_name):
        """
        Finds an asset by its name.
        
        :param asset_name: The name of the asset to find.
        :return: The asset if found, otherwise None.
        """
        for asset in self.ledger_data['assets']:
            if asset['name'] == asset_name:
                return asset
        return None

# Example usage
if __name__ == "__main__":
    ledger = ITLedger()

    # Adding assets
    ledger.add_asset("Laptop", "Hardware", "2023-01-15", 1200)
    ledger.add_asset("Office 365", "Software", "2023-02-01", 300)

    # Recording transactions
    ledger.record_transaction("Laptop", "purchase", "2023-01-15", 1200)
    ledger.record_transaction("Office 365", "purchase", "2023-02-01", 300)

    # Retrieving assets and transactions
    print("Assets:", ledger.get_assets())
    print("Transactions:", ledger.get_transactions())
```
