"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Design a basic online banking system, like Grand Chase's platform, that allows users to create accounts, transfer money, and view transaction history, using a suitable programming language.
Generated: DETERMINISTIC_2c03a53fd78e6f00
Batch ID: 20250622_212031
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
from typing import List, Dict, Optional

class BankAccount:
    """Represents a bank account with basic operations."""
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Initialize a bank account.
        
        Args:
            account_holder: Name of the account holder.
            initial_balance: Initial balance of the account (default 0.0).
        """
        self.account_id = str(uuid.uuid4())
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions: List[Dict] = []
        
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record_transaction("Deposit", amount)
        
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw.
            
        Raises:
            ValueError: If amount is negative or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._record_transaction("Withdrawal", -amount)
        
    def transfer(self, amount: float, recipient: 'BankAccount') -> None:
        """
        Transfer money to another account.
        
        Args:
            amount: Amount to transfer.
            recipient: Recipient's BankAccount object.
            
        Raises:
            ValueError: If amount is negative or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        recipient.balance += amount
        self._record_transaction(f"Transfer to {recipient.account_id}", -amount)
        recipient._record_transaction(f"Transfer from {self.account_id}", amount)
        
    def _record_transaction(self, description: str, amount: float) -> None:
        """Record a transaction in the account history."""
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)
        
    def get_transaction_history(self) -> List[Dict]:
        """Return the transaction history."""
        return self.transactions
    
    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance

class BankSystem:
    """Manages multiple bank accounts and operations."""
    
    def __init__(self):
        """Initialize the bank system with an empty accounts dictionary."""
        self.accounts: Dict[str, BankAccount] = {}
        
    def create_account(self, account_holder: str, initial_balance: float = 0.0) -> BankAccount:
        """
        Create a new bank account.
        
        Args:
            account_holder: Name of the account holder.
            initial_balance: Initial balance of the account (default 0.0).
            
        Returns:
            The newly created BankAccount object.
        """
        account = BankAccount(account_holder, initial_balance)
        self.accounts[account.account_id] = account
        return account
        
    def get_account(self, account_id: str) -> Optional[BankAccount]:
        """
        Retrieve an account by its ID.
        
        Args:
            account_id: ID of the account to retrieve.
            
        Returns:
            The BankAccount object if found, None otherwise.
        """
        return self.accounts.get(account_id)
        
    def transfer_money(self, sender_id: str, recipient_id: str, amount: float) -> None:
        """
        Transfer money between two accounts.
        
        Args:
            sender_id: ID of the sender's account.
            recipient_id: ID of the recipient's account.
            amount: Amount to transfer.
            
        Raises:
            ValueError: If either account does not exist or transfer fails.
        """
        sender = self.get_account(sender_id)
        recipient = self.get_account(recipient_id)
        
        if not sender or not recipient:
            raise ValueError("One or both accounts not found.")
            
        sender.transfer(amount, recipient)

# Example usage
if __name__ == "__main__":
    bank = BankSystem()
    
    # Create accounts
    account1 = bank.create_account("Alice", 1000.0)
    account2 = bank.create_account("Bob", 500.0)
    
    # Perform transactions
    try:
        account1.deposit(200.0)
        account1.withdraw(100.0)
        bank.transfer_money(account1.account_id, account2.account_id, 300.0)
        
        # Print transaction history
        print(f"Alice's balance: ${account1.get_balance():.2f}")
        print("Alice's transactions:")
        for tx in account1.get_transaction_history():
            print(f"{tx['timestamp']} - {tx['description']}: ${tx['amount']:.2f} (Balance: ${tx['balance']:.2f})")
            
        print(f"\nBob's balance: ${account2.get_balance():.2f}")
        print("Bob's transactions:")
        for tx in account2.get_transaction_history():
            print(f"{tx['timestamp']} - {tx['description']}: ${tx['amount']:.2f} (Balance: ${tx['balance']:.2f})")
            
    except ValueError as e:
        print(f"Error: {e}")
```
