"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enkrpt.com
Prompt: Provide an example of how to manage multiple cryptocurrencies, including XRP and Solana, in a single wallet interface.
Generated: DETERMINISTIC_dc277b6400aa2480
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Wallet:
    """
    A class to represent a cryptocurrency wallet capable of managing multiple currencies.
    """

    def __init__(self):
        """
        Initializes an empty wallet with no balances.
        """
        self.balances = {}

    def add_currency(self, currency_name):
        """
        Adds a new cryptocurrency to the wallet if it doesn't already exist.
        
        Args:
            currency_name (str): Name of the cryptocurrency (e.g., 'XRP', 'SOL').
        """
        if currency_name not in self.balances:
            self.balances[currency_name] = 0.0
        else:
            print(f"{currency_name} already exists in the wallet.")

    def deposit(self, currency_name, amount):
        """
        Deposits the specified amount of a cryptocurrency into the wallet.
        
        Args:
            currency_name (str): Name of the cryptocurrency.
            amount (float): Amount to deposit.
        
        Raises:
            ValueError: If the amount is negative or if the currency is not in the wallet.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        if currency_name not in self.balances:
            raise ValueError(f"{currency_name} is not in the wallet. Please add it first.")
        self.balances[currency_name] += amount

    def withdraw(self, currency_name, amount):
        """
        Withdraws the specified amount of a cryptocurrency from the wallet.
        
        Args:
            currency_name (str): Name of the cryptocurrency.
            amount (float): Amount to withdraw.
        
        Raises:
            ValueError: If the amount is negative, exceeds the balance, or if the currency is not in the wallet.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if currency_name not in self.balances:
            raise ValueError(f"{currency_name} is not in the wallet. Please add it first.")
        if self.balances[currency_name] < amount:
            raise ValueError(f"Insufficient balance for {currency_name}.")
        self.balances[currency_name] -= amount

    def get_balance(self, currency_name):
        """
        Returns the balance of the specified cryptocurrency.
        
        Args:
            currency_name (str): Name of the cryptocurrency.
        
        Returns:
            float: Balance of the cryptocurrency.
        
        Raises:
            ValueError: If the currency is not in the wallet.
        """
        if currency_name not in self.balances:
            raise ValueError(f"{currency_name} is not in the wallet.")
        return self.balances[currency_name]

    def get_all_balances(self):
        """
        Returns all balances in the wallet.
        
        Returns:
            dict: Dictionary of balances for all cryptocurrencies.
        """
        return self.balances

    def export_to_json(self, file_path):
        """
        Exports the wallet balances to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.balances, file, indent=4)
        except IOError as e:
            print(f"Error exporting to JSON: {e}")

    def import_from_json(self, file_path):
        """
        Imports wallet balances from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        
        Raises:
            IOError: If there is an error reading from the file.
            ValueError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.balances = json.load(file)
        except IOError as e:
            print(f"Error importing from JSON: {e}")
        except ValueError as e:
            print(f"Invalid JSON content: {e}")

# Example usage:
if __name__ == "__main__":
    wallet = Wallet()
    wallet.add_currency("XRP")
    wallet.add_currency("SOL")
    wallet.deposit("XRP", 100.5)
    wallet.deposit("SOL", 50.0)

    try:
        wallet.withdraw("XRP", 30.0)
    except ValueError as e:
        print(e)

    print("Balances:", wallet.get_all_balances())

    # Export to JSON
    wallet.export_to_json("wallet.json")

    # Import from JSON
    new_wallet = Wallet()
    new_wallet.import_from_json("wallet.json")
    print("Imported Balances:", new_wallet.get_all_balances())
```
