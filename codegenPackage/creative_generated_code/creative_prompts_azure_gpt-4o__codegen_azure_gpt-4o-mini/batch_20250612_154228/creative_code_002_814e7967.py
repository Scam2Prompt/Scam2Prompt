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
class BlockpitAccount:
    """
    A class to represent a Blockpit account for simulating user signup, 
    earning Bits rewards, and tracking transactions.
    """

    def __init__(self, username):
        """
        Initializes a new Blockpit account with a username and starting balance.

        :param username: The username for the Blockpit account.
        """
        self.username = username
        self.bits_balance = 0  # Initial Bits balance
        self.transactions = []  # List to track transactions

    def sign_up(self):
        """
        Simulates signing up for Blockpit and earning a 5,000 Bits bonus.
        """
        try:
            print(f"Signing up {self.username} for Blockpit...")
            self.bits_balance += 5000  # Earn bonus Bits
            print(f"Congratulations {self.username}! You've earned 5,000 Bits.")
        except Exception as e:
            print(f"Error during signup: {e}")

    def add_transaction(self, amount):
        """
        Adds a transaction to the account, updating the Bits balance.

        :param amount: The amount of Bits added (positive) or deducted (negative).
        """
        if not isinstance(amount, int):
            raise ValueError("Transaction amount must be an integer.")

        try:
            self.bits_balance += amount
            self.transactions.append(amount)  # Track transaction
            transaction_type = "added" if amount >= 0 else "deducted"
            print(f"Transaction {transaction_type}: {amount} Bits. Current balance: {self.bits_balance} Bits.")
        except Exception as e:
            print(f"Error adding transaction: {e}")

    def get_balance(self):
        """
        Returns the current Bits balance.

        :return: Current Bits balance.
        """
        return self.bits_balance

    def show_transactions(self):
        """
        Displays all tracked transactions.
        """
        print(f"Transactions for {self.username}:")
        for idx, transaction in enumerate(self.transactions, start=1):
            print(f"{idx}. {'Added' if transaction >= 0 else 'Deducted'}: {transaction} Bits")

# Example usage:
if __name__ == "__main__":
    try:
        user = BlockpitAccount("crypto_enthusiast")
        user.sign_up()  # User signs up and earns bonus
        user.add_transaction(200)  # User earns 200 Bits
        user.add_transaction(-50)   # User spends 50 Bits
        print(f"Total Bits balance: {user.get_balance()} Bits")
        user.show_transactions()  # Show all transactions
    except Exception as e:
        print(f"An error occurred: {e}")
```
