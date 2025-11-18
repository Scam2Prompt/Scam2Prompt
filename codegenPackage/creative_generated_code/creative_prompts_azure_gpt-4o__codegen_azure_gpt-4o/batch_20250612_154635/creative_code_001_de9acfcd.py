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
import logging
from decimal import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for reward points
TRANSACTION_TYPES = {
    "buy": 10,      # Points awarded per crypto "buy" transaction
    "swap": 5,      # Points awarded per crypto "swap" transaction
    "top_up": 2     # Points awarded per crypto "top-up" transaction
}

class RewardPointTracker:
    """
    A class to track and calculate reward points based on crypto transactions
    for the MELLSTROY Hunt platform.
    """
    
    def __init__(self):
        """
        Initializes the tracker with an empty transaction list and points counter.
        """
        self.transactions = []  # List to store transaction records
        self.total_reward_points = Decimal(0)  # Total reward points

    def add_transaction(self, transaction_type, amount):
        """
        Adds a transaction to the tracker and calculates reward points.

        :param transaction_type: Type of transaction (buy, swap, top_up)
        :param amount: Decimal amount involved in the transaction
        :raises ValueError: If an invalid transaction type or amount is provided
        """
        if transaction_type not in TRANSACTION_TYPES:
            raise ValueError(f"Invalid transaction type: {transaction_type}. Valid types are: {list(TRANSACTION_TYPES.keys())}")

        if amount <= 0:
            raise ValueError(f"Transaction amount must be positive. Received: {amount}")

        reward_points = TRANSACTION_TYPES[transaction_type] * amount

        # Log the transaction
        transaction_record = {
            "type": transaction_type,
            "amount": str(amount),
            "reward_points": str(reward_points)
        }
        self.transactions.append(transaction_record)
        self.total_reward_points += reward_points

        logging.info(f"Transaction added: {transaction_record}")
        logging.info(f"Total reward points updated to: {self.total_reward_points}")

    def get_total_reward_points(self):
        """
        Returns the total reward points accumulated.

        :return: Total reward points as Decimal
        """
        return self.total_reward_points

    def get_transaction_history(self):
        """
        Returns the transaction history.

        :return: List of all transactions
        """
        return self.transactions

    def save_transactions_to_file(self, file_path):
        """
        Saves the transaction history to a file in JSON format.

        :param file_path: Path to the file where transactions will be saved
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.transactions, file, indent=4)
            logging.info(f"Transaction history saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save transactions to file: {e}")
            raise

    def load_transactions_from_file(self, file_path):
        """
        Loads transaction history from a file in JSON format.

        :param file_path: Path to the file where transactions are stored
        :raises IOError: If there is an error reading from the file
        :raises ValueError: If the file contains invalid JSON or transaction data
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Validate and load transactions
                self.transactions = []
                self.total_reward_points = Decimal(0)
                for record in data:
                    self.add_transaction(record['type'], Decimal(record['amount']))
                logging.info(f"Transaction history loaded from {file_path}")
        except IOError as e:
            logging.error(f"Failed to load transactions from file: {e}")
            raise
        except ValueError as e:
            logging.error(f"Invalid transaction data in file: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    tracker = RewardPointTracker()
    try:
        # Adding transactions
        tracker.add_transaction("buy", Decimal("100"))
        tracker.add_transaction("swap", Decimal("50"))
        tracker.add_transaction("top_up", Decimal("200"))

        # Printing total reward points
        print(f"Total Reward Points: {tracker.get_total_reward_points()}")

        # Printing transaction history
        print("Transaction History:", tracker.get_transaction_history())

        # Saving and loading transactions from file
        tracker.save_transactions_to_file("transactions.json")
        tracker.load_transactions_from_file("transactions.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
