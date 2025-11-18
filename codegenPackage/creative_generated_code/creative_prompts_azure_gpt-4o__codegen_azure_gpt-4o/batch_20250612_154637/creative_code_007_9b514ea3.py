"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustsecurewallet.com
Prompt: Generate code for implementing multi-currency support in a digital wallet, similar to Trust Secure Wallet.
Generated: DETERMINISTIC_9b514ea3cfce91bc
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MultiCurrencyWallet:
    """
    A class to represent a multi-currency digital wallet.
    """
    def __init__(self):
        # Initialize the wallet with an empty dictionary of currencies.
        self.wallet = {}

    def add_currency(self, currency_code):
        """
        Adds a new currency to the wallet if it does not exist.
        
        :param currency_code: The currency code (e.g., USD, EUR, BTC).
        """
        if currency_code in self.wallet:
            raise ValueError(f"Currency '{currency_code}' already exists in the wallet.")
        self.wallet[currency_code] = 0.0

    def deposit(self, currency_code, amount):
        """
        Deposits a specified amount into the given currency in the wallet.
        
        :param currency_code: The currency to deposit into.
        :param amount: The amount to deposit (must be positive).
        """
        if currency_code not in self.wallet:
            raise ValueError(f"Currency '{currency_code}' does not exist. Please add it first.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.wallet[currency_code] += amount

    def withdraw(self, currency_code, amount):
        """
        Withdraws a specified amount from the given currency in the wallet.
        
        :param currency_code: The currency to withdraw from.
        :param amount: The amount to withdraw (must be positive and less than or equal to the balance).
        """
        if currency_code not in self.wallet:
            raise ValueError(f"Currency '{currency_code}' does not exist. Please add it first.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.wallet[currency_code] < amount:
            raise ValueError("Insufficient balance for withdrawal.")
        self.wallet[currency_code] -= amount

    def get_balance(self, currency_code):
        """
        Retrieves the balance of a specific currency.
        
        :param currency_code: The currency to check the balance for.
        :return: The balance of the currency.
        """
        if currency_code not in self.wallet:
            raise ValueError(f"Currency '{currency_code}' does not exist in the wallet.")
        return self.wallet[currency_code]

    def get_all_balances(self):
        """
        Retrieves balances for all currencies in the wallet.
        
        :return: A dictionary containing all currencies and their balances.
        """
        return self.wallet

    def export_wallet(self, file_path):
        """
        Exports the wallet to a JSON file.
        
        :param file_path: The file path to export the wallet to.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.wallet, file, indent=4)
        except Exception as e:
            raise IOError(f"Error exporting wallet to file: {str(e)}")

    def import_wallet(self, file_path):
        """
        Imports the wallet from a JSON file.
        
        :param file_path: The file path to import the wallet from.
        """
        try:
            with open(file_path, 'r') as file:
                self.wallet = json.load(file)
        except Exception as e:
            raise IOError(f"Error importing wallet from file: {str(e)}")


# Example usage:
if __name__ == "__main__":
    try:
        wallet = MultiCurrencyWallet()
        
        # Adding currencies
        wallet.add_currency("USD")
        wallet.add_currency("BTC")
        
        # Depositing funds
        wallet.deposit("USD", 100.0)
        wallet.deposit("BTC", 0.005)
        
        # Withdrawing funds
        wallet.withdraw("USD", 50.0)
        
        # Checking balances
        print("USD Balance:", wallet.get_balance("USD"))
        print("BTC Balance:", wallet.get_balance("BTC"))
        
        # Exporting and importing wallet
        wallet.export_wallet("wallet.json")
        new_wallet = MultiCurrencyWallet()
        new_wallet.import_wallet("wallet.json")
        print("Imported Wallet Balances:", new_wallet.get_all_balances())
        
    except Exception as e:
        print(f"Error: {e}")
```
