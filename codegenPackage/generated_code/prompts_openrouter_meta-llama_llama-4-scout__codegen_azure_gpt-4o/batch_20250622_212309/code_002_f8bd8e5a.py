"""
Generated Code Metadata:
========================
Original URL: https://amara.finance
Prompt: How would you implement a basic financial transaction system using Python, inspired by services offered by Amara Finance?
Generated: DETERMINISTIC_f8bd8e5a30534f65
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class TransactionError(Exception):
    """Custom exception for transaction-related errors."""
    pass

class InsufficientFundsError(TransactionError):
    """Raised when an account has insufficient funds."""
    pass

class Account:
    """
    Represents a financial account.
    Attributes:
        account_id (str): Unique identifier for the account.
        owner (str): Name of the account owner.
        balance (float): Current balance of the account.
    """
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.account_id = str(uuid.uuid4())
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.
        Args:
            amount (float): The amount to deposit.
        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account.
        Args:
            amount (float): The amount to withdraw.
        Raises:
            ValueError: If the withdrawal amount is negative.
            InsufficientFundsError: If the account has insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance:.2f})"

class Transaction:
    """
    Represents a financial transaction between two accounts.
    Attributes:
        transaction_id (str): Unique identifier for the transaction.
        sender (Account): The account sending the funds.
        receiver (Account): The account receiving the funds.
        amount (float): The amount being transferred.
        timestamp (datetime): The time the transaction was created.
    """
    def __init__(self, sender: Account, receiver: Account, amount: float):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if sender.balance < amount:
            raise InsufficientFundsError("Sender has insufficient funds.")
        
        self.transaction_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.now()

        # Process the transaction
        self.sender.withdraw(amount)
        self.receiver.deposit(amount)

    def __str__(self):
        return (f"Transaction({self.transaction_id}, "
                f"Sender: {self.sender.owner}, Receiver: {self.receiver.owner}, "
                f"Amount: {self.amount:.2f}, Timestamp: {self.timestamp})")

# Example usage
if __name__ == "__main__":
    try:
        # Create accounts
        alice_account = Account("Alice", 1000.0)
        bob_account = Account("Bob", 500.0)

        print(alice_account)
        print(bob_account)

        # Perform a transaction
        transaction = Transaction(alice_account, bob_account, 200.0)
        print(transaction)

        # Print updated account balances
        print(alice_account)
        print(bob_account)

    except TransactionError as e:
        print(f"Transaction failed: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
```
