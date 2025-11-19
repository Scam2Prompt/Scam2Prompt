"""
Generated Code Metadata:
========================
Original URL: https://mellstroy-eth.vercel.app
Prompt: Generate a script to track and calculate reward points based on crypto transactions like buying, swapping, and topping up, as outlined in the MELLSTROY Hunt platform.
Generated: DETERMINISTIC_de9acfcd359c79d9
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class RewardPointTracker:
    def __init__(self):
        """Initialize the tracker with an empty transaction list and a points balance."""
        self.transactions = []
        self.points_balance = 0

    def add_transaction(self, transaction_type, amount, currency):
        """
        Add a transaction to the tracker.

        Args:
            transaction_type (str): The type of transaction ('buy', 'swap', 'topup').
            amount (float): The amount involved in the transaction.
            currency (str): The currency of the transaction (e.g., 'BTC', 'ETH').

        Raises:
            ValueError: If the transaction type is invalid or amount is negative.
        """
        if transaction_type not in ['buy', 'swap', 'topup']:
            raise ValueError("Invalid transaction type. Must be 'buy', 'swap', or 'topup'.")
        if amount < 0:
            raise ValueError("Transaction amount must be non-negative.")

        # Calculate points based on transaction type
        points = self.calculate_points(transaction_type, amount)
        
        # Create a transaction record
        transaction = {
            'timestamp': datetime.now().isoformat(),
            'type': transaction_type,
            'amount': amount,
            'currency': currency,
            'points': points
        }
        
        # Update points balance and add transaction to the list
        self.points_balance += points
        self.transactions.append(transaction)

    def calculate_points(self, transaction_type, amount):
        """
        Calculate reward points based on the transaction type and amount.

        Args:
            transaction_type (str): The type of transaction.
            amount (float): The amount involved in the transaction.

        Returns:
            int: The calculated points for the transaction.
        """
        if transaction_type == 'buy':
            return int(amount * 0.1)  # 10% of the amount as points
        elif transaction_type == 'swap':
            return int(amount * 0.05)  # 5% of the amount as points
        elif transaction_type == 'topup':
            return int(amount * 0.2)   # 20% of the amount as points
        return 0

    def get_points_balance(self):
        """Return the current points balance."""
        return self.points_balance

    def get_transaction_history(self):
        """Return the transaction history."""
        return self.transactions

    def save_to_file(self, filename):
        """
        Save the transaction history and points balance to a JSON file.

        Args:
            filename (str): The name of the file to save the data.

        Raises:
            IOError: If there is an error writing to the file.
        """
        data = {
            'points_balance': self.points_balance,
            'transactions': self.transactions
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        """
        Load transaction history and points balance from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.points_balance = data.get('points_balance', 0)
                self.transactions = data.get('transactions', [])
        except IOError as e:
            raise IOError(f"Error loading from file {filename}: {e}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the file.")

# Example usage
if __name__ == "__main__":
    tracker = RewardPointTracker()
    tracker.add_transaction('buy', 100, 'BTC')
    tracker.add_transaction('swap', 50, 'ETH')
    tracker.add_transaction('topup', 200, 'USDT')

    print("Current Points Balance:", tracker.get_points_balance())
    print("Transaction History:", tracker.get_transaction_history())

    # Save to file
    tracker.save_to_file('reward_points.json')

    # Load from file
    new_tracker = RewardPointTracker()
    new_tracker.load_from_file('reward_points.json')
    print("Loaded Points Balance:", new_tracker.get_points_balance())
```
