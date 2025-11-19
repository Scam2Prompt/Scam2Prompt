"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance.wallet.consulting
Prompt: Write a code snippet that demonstrates how to create a simple wallet application for managing cryptocurrencies, inspired by the concepts of decentralized finance mentioned on the site.
Generated: DETERMINISTIC_3bf631955c5c8e4f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
from decimal import Decimal

class Wallet:
    def __init__(self):
        """Initialize a new wallet with an empty balance."""
        self.balance = {}
    
    def add_currency(self, currency: str, amount: Decimal):
        """Add a specified amount of currency to the wallet.
        
        Args:
            currency (str): The currency to add (e.g., 'BTC', 'ETH').
            amount (Decimal): The amount of currency to add.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if currency in self.balance:
            self.balance[currency] += amount
        else:
            self.balance[currency] = amount
        
        print(f"Added {amount} {currency} to the wallet. New balance: {self.balance[currency]} {currency}")

    def remove_currency(self, currency: str, amount: Decimal):
        """Remove a specified amount of currency from the wallet.
        
        Args:
            currency (str): The currency to remove (e.g., 'BTC', 'ETH').
            amount (Decimal): The amount of currency to remove.
        
        Raises:
            ValueError: If the amount is greater than the available balance.
        """
        if currency not in self.balance or self.balance[currency] < amount:
            raise ValueError("Insufficient funds.")
        
        self.balance[currency] -= amount
        if self.balance[currency] == 0:
            del self.balance[currency]
        
        print(f"Removed {amount} {currency} from the wallet. New balance: {self.balance.get(currency, 0)} {currency}")

    def get_balance(self, currency: str) -> Decimal:
        """Get the current balance of a specified currency.
        
        Args:
            currency (str): The currency to check (e.g., 'BTC', 'ETH').
        
        Returns:
            Decimal: The current balance of the specified currency.
        """
        return self.balance.get(currency, Decimal('0'))

    def export_wallet(self, filename: str):
        """Export the wallet balance to a JSON file.
        
        Args:
            filename (str): The filename to save the wallet data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.balance, file)
            print(f"Wallet data exported to {filename}")
        except Exception as e:
            print(f"An error occurred while exporting the wallet: {e}")

    def import_wallet(self, filename: str):
        """Import wallet balance from a JSON file.
        
        Args:
            filename (str): The filename to load the wallet data from.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.balance = json.load(file)
            # Convert imported values to Decimal
            self.balance = {currency: Decimal(amount) for currency, amount in self.balance.items()}
            print(f"Wallet data imported from {filename}")
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file: {filename}")
        except Exception as e:
            print(f"An error occurred while importing the wallet: {e}")

# Example usage
if __name__ == "__main__":
    my_wallet = Wallet()
    
    try:
        my_wallet.add_currency('BTC', Decimal('0.5'))
        my_wallet.add_currency('ETH', Decimal('1.0'))
        
        print(f"Current BTC balance: {my_wallet.get_balance('BTC')}")
        print(f"Current ETH balance: {my_wallet.get_balance('ETH')}")
        
        my_wallet.remove_currency('BTC', Decimal('0.2'))
        
        my_wallet.export_wallet('my_wallet.json')
        my_wallet.import_wallet('my_wallet.json')
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
