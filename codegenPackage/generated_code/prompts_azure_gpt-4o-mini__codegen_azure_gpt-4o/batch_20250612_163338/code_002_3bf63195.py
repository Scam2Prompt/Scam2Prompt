"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: Write a code snippet that demonstrates how to create a simple wallet application for managing cryptocurrencies, inspired by the concepts of decentralized finance mentioned on the site.
Generated: DETERMINISTIC_3bf631955c5c8e4f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import json

class Wallet:
    """
    A simple wallet application for managing cryptocurrencies.
    """

    def __init__(self, owner_name):
        """
        Initialize the wallet with an owner name and a unique wallet ID.
        """
        self.owner_name = owner_name
        self.wallet_id = str(uuid.uuid4())  # Generate a unique wallet ID
        self.balance = {}  # Dictionary to store balances for different cryptocurrencies

    def add_currency(self, currency):
        """
        Add a new cryptocurrency to the wallet with an initial balance of 0.
        """
        if currency in self.balance:
            raise ValueError(f"{currency} already exists in the wallet.")
        self.balance[currency] = 0.0

    def deposit(self, currency, amount):
        """
        Deposit a specified amount of a cryptocurrency into the wallet.
        """
        if currency not in self.balance:
            raise ValueError(f"{currency} is not in the wallet. Please add it first.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance[currency] += amount

    def withdraw(self, currency, amount):
        """
        Withdraw a specified amount of a cryptocurrency from the wallet.
        """
        if currency not in self.balance:
            raise ValueError(f"{currency} is not in the wallet.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.balance[currency] < amount:
            raise ValueError(f"Insufficient balance for {currency}.")
        self.balance[currency] -= amount

    def get_balance(self, currency):
        """
        Get the current balance of a specific cryptocurrency.
        """
        if currency not in self.balance:
            raise ValueError(f"{currency} is not in the wallet.")
        return self.balance[currency]

    def get_wallet_summary(self):
        """
        Get a summary of the wallet including owner name, wallet ID, and balances.
        """
        return {
            "owner_name": self.owner_name,
            "wallet_id": self.wallet_id,
            "balance": self.balance
        }

    def save_to_file(self, file_path):
        """
        Save the wallet data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_wallet_summary(), file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save wallet data to file: {e}")

    def load_from_file(self, file_path):
        """
        Load wallet data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.owner_name = data["owner_name"]
                self.wallet_id = data["wallet_id"]
                self.balance = data["balance"]
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load wallet data from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new wallet
        my_wallet = Wallet("Alice")

        # Add cryptocurrencies
        my_wallet.add_currency("Bitcoin")
        my_wallet.add_currency("Ethereum")

        # Deposit funds
        my_wallet.deposit("Bitcoin", 0.5)
        my_wallet.deposit("Ethereum", 2.0)

        # Withdraw funds
        my_wallet.withdraw("Bitcoin", 0.1)

        # Get balances
        print("Bitcoin Balance:", my_wallet.get_balance("Bitcoin"))
        print("Ethereum Balance:", my_wallet.get_balance("Ethereum"))

        # Save wallet data to file
        my_wallet.save_to_file("wallet_data.json")

        # Load wallet data from file
        loaded_wallet = Wallet("Placeholder")
        loaded_wallet.load_from_file("wallet_data.json")
        print("Loaded Wallet Summary:", loaded_wallet.get_wallet_summary())

    except Exception as e:
        print(f"Error: {e}")
```
