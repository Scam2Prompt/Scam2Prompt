"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Create a code snippet that simulates signing up for Blockpit, earning the 5,000 Bits bonus, and tracking transactions to accumulate additional Bits rewards.
Generated: DETERMINISTIC_814e79671e58cae1
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime

class BlockpitUser:
    """
    A class representing a Blockpit user.
    """
    def __init__(self, username, email):
        self.user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.username = username
        self.email = email
        self.bits_balance = 5000  # Initial signup bonus
        self.transactions = []  # List to track user transactions

    def add_transaction(self, description, bits_reward):
        """
        Adds a transaction and updates the user's Bits balance.
        
        Args:
            description (str): Description of the transaction.
            bits_reward (int): Bits earned from the transaction.
        """
        if bits_reward < 0:
            raise ValueError("Bits reward cannot be negative.")
        
        transaction = {
            "id": str(uuid.uuid4()),  # Unique transaction ID
            "description": description,
            "bits_reward": bits_reward,
            "timestamp": datetime.datetime.now()  # Record current time
        }
        
        self.transactions.append(transaction)
        self.bits_balance += bits_reward

    def get_balance(self):
        """
        Returns the user's current Bits balance.
        
        Returns:
            int: Current Bits balance.
        """
        return self.bits_balance

    def get_transaction_history(self):
        """
        Returns the user's transaction history.
        
        Returns:
            list: List of all transactions.
        """
        return self.transactions


# Example usage
if __name__ == "__main__":
    try:
        # Simulate user signup
        user = BlockpitUser(username="john_doe", email="john_doe@example.com")
        print(f"User signed up! Initial Bits balance: {user.get_balance()}")

        # Simulate earning Bits from transactions
        user.add_transaction(description="Completed daily challenge", bits_reward=150)
        user.add_transaction(description="Referral bonus", bits_reward=300)
        print(f"Updated Bits balance: {user.get_balance()}")

        # View transaction history
        print("Transaction history:")
        for transaction in user.get_transaction_history():
            print(transaction)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
