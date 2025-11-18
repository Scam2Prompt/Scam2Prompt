"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: Generate code for tracking user transaction history in a Uniswap clone application.
Generated: DETERMINISTIC_8241dbe5448c3aee
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Dict
import uuid

# Define a Transaction class
class Transaction:
    """
    Represents a single transaction in the Uniswap clone application.
    """
    def __init__(self, user_id: str, transaction_type: str, token_in: str, token_out: str,
                 amount_in: float, amount_out: float):
        """
        Initialize a transaction object.
        
        Args:
            user_id (str): Unique identifier for the user.
            transaction_type (str): Type of transaction ('swap', 'add_liquidity', 'remove_liquidity').
            token_in (str): Token being sold or removed.
            token_out (str): Token being bought or added.
            amount_in (float): Amount of token_in involved in the transaction.
            amount_out (float): Amount of token_out involved in the transaction.
        """
        self.transaction_id = str(uuid.uuid4())  # Unique transaction ID
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.token_in = token_in
        self.token_out = token_out
        self.amount_in = amount_in
        self.amount_out = amount_out
        self.timestamp = datetime.now()  # Timestamp of the transaction

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the transaction object to a dictionary for easier serialization.
        
        Returns:
            dict: Dictionary representation of the transaction.
        """
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "transaction_type": self.transaction_type,
            "token_in": self.token_in,
            "token_out": self.token_out,
            "amount_in": self.amount_in,
            "amount_out": self.amount_out,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }


# Define a TransactionHistory class
class TransactionHistory:
    """
    Manages the transaction history for users in the Uniswap clone application.
    """
    def __init__(self):
        """
        Initialize the transaction history manager.
        """
        self.user_transactions = {}  # Stores a list of transactions for each user

    def add_transaction(self, transaction: Transaction) -> None:
        """
        Add a transaction to the user's transaction history.
        
        Args:
            transaction (Transaction): The transaction to be added.
        """
        if transaction.user_id not in self.user_transactions:
            self.user_transactions[transaction.user_id] = []
        self.user_transactions[transaction.user_id].append(transaction)
        print(f"Transaction added: {transaction.to_dict()}")  # Log the transaction for debug purposes

    def get_transactions(self, user_id: str) -> List[Dict[str, str]]:
        """
        Retrieve the transaction history for a specific user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            list: List of transactions as dictionaries.
        """
        if user_id not in self.user_transactions:
            return []
        return [transaction.to_dict() for transaction in self.user_transactions[user_id]]

    def clear_transactions(self, user_id: str) -> None:
        """
        Clear all transaction history for a specific user.
        
        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.user_transactions:
            del self.user_transactions[user_id]
            print(f"Transaction history cleared for user: {user_id}")  # Log for debug purposes


# Example usage
if __name__ == "__main__":
    # Initialize transaction history manager
    history_manager = TransactionHistory()

    # Create sample transactions
    transaction1 = Transaction(user_id="user1", transaction_type="swap", token_in="ETH", token_out="DAI", amount_in=1.2, amount_out=2400)
    transaction2 = Transaction(user_id="user1", transaction_type="add_liquidity", token_in="DAI", token_out="USDT", amount_in=1000, amount_out=1000)

    # Add transactions to history
    history_manager.add_transaction(transaction1)
    history_manager.add_transaction(transaction2)

    # Retrieve transactions for user
    user1_transactions = history_manager.get_transactions("user1")
    print("User1 Transactions:", user1_transactions)

    # Clear transactions for user
    history_manager.clear_transactions("user1")
```
