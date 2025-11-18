"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Generate a script to track and calculate reward points based on crypto transactions like buying, swapping, and topping up, as outlined in the MELLSTROY Hunt platform.
Generated: DETERMINISTIC_de9acfcd359c79d9
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class RewardPointTracker:
    def __init__(self):
        self.transactions = []
        self.total_points = Decimal('0.00')

    def add_transaction(self, transaction_type, amount):
        """
        Adds a transaction and calculates reward points.
        
        Parameters:
        transaction_type (str): The type of transaction ('buy', 'swap', 'topup').
        amount (Decimal): The amount of the transaction.
        """
        # Validate transaction type
        if transaction_type not in ['buy', 'swap', 'topup']:
            raise ValueError("Invalid transaction type. Must be 'buy', 'swap', or 'topup'.")

        # Validate amount
        if not isinstance(amount, (Decimal, int, float)):
            raise TypeError("Amount must be a Decimal, int, or float.")
        
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate reward points based on transaction type
        points = self.calculate_reward_points(transaction_type, amount)
        
        # Add transaction to the list
        self.transactions.append({
            'type': transaction_type,
            'amount': amount,
            'points': points
        })

        # Update total points
        self.total_points += points

    def calculate_reward_points(self, transaction_type, amount):
        """
        Calculates reward points based on the transaction type and amount.
        
        Parameters:
        transaction_type (str): The type of transaction.
        amount (Decimal): The amount of the transaction.
        
        Returns:
        Decimal: The calculated points.
        """
        if transaction_type == 'buy':
            return amount * Decimal('0.01')  # 1% of the amount as points
        elif transaction_type == 'swap':
            return amount * Decimal('0.005')  # 0.5% of the amount as points
        elif transaction_type == 'topup':
            return amount * Decimal('0.02')  # 2% of the amount as points

    def get_total_points(self):
        """
        Returns the total reward points accumulated.

        Returns:
        Decimal: Total reward points.
        """
        return self.total_points

    def get_transactions(self):
        """
        Returns the list of all transactions.

        Returns:
        list: List of transactions with their details.
        """
        return self.transactions

    def save_to_file(self, file_path):
        """
        Saves the transaction data to a JSON file.

        Parameters:
        file_path (str): The path of the file to save the data.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({
                    'total_points': str(self.total_points),
                    'transactions': self.transactions
                }, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save transactions to file: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = RewardPointTracker()
    
    try:
        tracker.add_transaction('buy', 100)
        tracker.add_transaction('swap', 50)
        tracker.add_transaction('topup', 200)
        
        print(f"Total Points: {tracker.get_total_points()}")
        print("Transactions:", tracker.get_transactions())
        
        # Save transactions to a file
        tracker.save_to_file('transactions.json')
    except Exception as e:
        print(f"An error occurred: {e}")
```
