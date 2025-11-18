"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprofit-bitcoin.com
Prompt: Write code to simulate a demo account for a decentralized finance platform, allowing users to test peer-to-peer transactions without intermediaries, as described on Profit Bitcoin.
Generated: DETERMINISTIC_bdc0dc07dbcdebc6
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import decimal
from typing import Dict, Optional

# Constants for demo purposes
INITIAL_BALANCE = decimal.Decimal("1000.00")  # Initial balance for demo accounts

class DemoAccount:
    """
    Represents a demo account for a decentralized finance platform.
    Allows users to test peer-to-peer transactions without intermediaries.
    """

    def __init__(self, username: str):
        """
        Initialize a demo account with a unique ID and initial balance.
        
        Args:
            username (str): The username of the account holder.
        """
        self.account_id = str(uuid.uuid4())  # Generate unique account ID
        self.username = username
        self.balance = INITIAL_BALANCE

    def deposit(self, amount: decimal.Decimal):
        """
        Deposit funds into the demo account.
        
        Args:
            amount (decimal.Decimal): The amount to deposit.
        
        Raises:
            ValueError: If the deposit amount is invalid.
        """
        if amount <= decimal.Decimal("0"):
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: decimal.Decimal):
        """
        Withdraw funds from the demo account.
        
        Args:
            amount (decimal.Decimal): The amount to withdraw.
        
        Raises:
            ValueError: If the withdrawal amount is invalid or exceeds balance.
        """
        if amount <= decimal.Decimal("0"):
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, recipient_account, amount: decimal.Decimal):
        """
        Transfer funds to another demo account.
        
        Args:
            recipient_account (DemoAccount): The recipient demo account.
            amount (decimal.Decimal): The amount to transfer.
        
        Raises:
            ValueError: If the transfer amount is invalid or exceeds balance.
        """
        if not isinstance(recipient_account, DemoAccount):
            raise ValueError("Recipient must be a valid DemoAccount instance.")
        if amount <= decimal.Decimal("0"):
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        # Perform the transfer
        self.withdraw(amount)
        recipient_account.deposit(amount)

    def get_balance(self) -> decimal.Decimal:
        """
        Get the current account balance.
        
        Returns:
            decimal.Decimal: The current balance.
        """
        return self.balance

    def __str__(self):
        """
        Return a string representation of the DemoAccount instance.
        
        Returns:
            str: Account details.
        """
        return f"DemoAccount(username='{self.username}', account_id='{self.account_id}', balance={self.balance})"


# Example Usage
if __name__ == "__main__":
    try:
        # Create demo accounts
        user1 = DemoAccount("Alice")
        user2 = DemoAccount("Bob")
        
        print("Initial State:")
        print(user1)
        print(user2)

        # Perform transactions
        print("\nAlice deposits 500:")
        user1.deposit(decimal.Decimal("500"))
        print(user1)

        print("\nAlice transfers 300 to Bob:")
        user1.transfer(user2, decimal.Decimal("300"))
        print(user1)
        print(user2)

        print("\nBob withdraws 100:")
        user2.withdraw(decimal.Decimal("100"))
        print(user2)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
