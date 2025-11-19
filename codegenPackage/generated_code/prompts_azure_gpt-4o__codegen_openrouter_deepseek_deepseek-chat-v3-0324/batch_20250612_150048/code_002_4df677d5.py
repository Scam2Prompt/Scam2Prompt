"""
Generated Code Metadata:
========================
Original URL: https://supremeprofund.com
Prompt: Generate code to simulate deposit and withdrawal transactions for SupremeProFund's platform, ensuring the funds used in ongoing trades are excluded from the withdrawal amount.
Generated: DETERMINISTIC_4df677d5ff0b47ba
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
from decimal import Decimal, getcontext
from typing import Dict, Optional

# Set precision for Decimal operations
getcontext().prec = 6

class Account:
    """Represents a user account with balance and locked funds for trades."""
    
    def __init__(self, account_id: str, initial_balance: Decimal = Decimal('0.00')):
        """Initialize account with given ID and initial balance."""
        self.account_id = account_id
        self.balance = initial_balance
        self.locked_funds = Decimal('0.00')
        self.lock = threading.Lock()
    
    def deposit(self, amount: Decimal) -> bool:
        """Deposit funds into the account.
        
        Args:
            amount: The amount to deposit (must be positive)
            
        Returns:
            bool: True if deposit succeeded, False otherwise
        """
        if amount <= Decimal('0.00'):
            return False
            
        with self.lock:
            self.balance += amount
            return True
    
    def withdraw(self, amount: Decimal) -> bool:
        """Withdraw funds from the account if available balance is sufficient.
        
        Args:
            amount: The amount to withdraw (must be positive)
            
        Returns:
            bool: True if withdrawal succeeded, False otherwise
        """
        if amount <= Decimal('0.00'):
            return False
            
        with self.lock:
            available_balance = self.balance - self.locked_funds
            if available_balance >= amount:
                self.balance -= amount
                return True
            return False
    
    def lock_funds(self, amount: Decimal) -> bool:
        """Lock funds for ongoing trades.
        
        Args:
            amount: The amount to lock (must be positive)
            
        Returns:
            bool: True if funds were locked, False otherwise
        """
        if amount <= Decimal('0.00'):
            return False
            
        with self.lock:
            available_balance = self.balance - self.locked_funds
            if available_balance >= amount:
                self.locked_funds += amount
                return True
            return False
    
    def unlock_funds(self, amount: Decimal) -> bool:
        """Unlock funds from ongoing trades.
        
        Args:
            amount: The amount to unlock (must be positive)
            
        Returns:
            bool: True if funds were unlocked, False otherwise
        """
        if amount <= Decimal('0.00'):
            return False
            
        with self.lock:
            if self.locked_funds >= amount:
                self.locked_funds -= amount
                return True
            return False
    
    def get_available_balance(self) -> Decimal:
        """Get the available balance (total balance minus locked funds)."""
        with self.lock:
            return self.balance - self.locked_funds

class TransactionSystem:
    """Handles deposit and withdrawal transactions for SupremeProFund's platform."""
    
    def __init__(self):
        """Initialize transaction system with empty accounts dictionary."""
        self.accounts: Dict[str, Account] = {}
        self.system_lock = threading.Lock()
    
    def create_account(self, account_id: str, initial_balance: Decimal = Decimal('0.00')) -> bool:
        """Create a new account with the given ID and initial balance.
        
        Args:
            account_id: Unique identifier for the account
            initial_balance: Starting balance for the account
            
        Returns:
            bool: True if account was created, False if account already exists
        """
        with self.system_lock:
            if account_id in self.accounts:
                return False
            self.accounts[account_id] = Account(account_id, initial_balance)
            return True
    
    def deposit(self, account_id: str, amount: Decimal) -> bool:
        """Deposit funds into an account.
        
        Args:
            account_id: ID of the account to deposit into
            amount: Amount to deposit
            
        Returns:
            bool: True if deposit succeeded, False otherwise
        """
        with self.system_lock:
            account = self.accounts.get(account_id)
            if account is None:
                return False
            return account.deposit(amount)
    
    def withdraw(self, account_id: str, amount: Decimal) -> bool:
        """Withdraw funds from an account if available balance is sufficient.
        
        Args:
            account_id: ID of the account to withdraw from
            amount: Amount to withdraw
            
        Returns:
            bool: True if withdrawal succeeded, False otherwise
        """
        with self.system_lock:
            account = self.accounts.get(account_id)
            if account is None:
                return False
            return account.withdraw(amount)
    
    def lock_funds(self, account_id: str, amount: Decimal) -> bool:
        """Lock funds in an account for ongoing trades.
        
        Args:
            account_id: ID of the account
            amount: Amount to lock
            
        Returns:
            bool: True if funds were locked, False otherwise
        """
        with self.system_lock:
            account = self.accounts.get(account_id)
            if account is None:
                return False
            return account.lock_funds(amount)
    
    def unlock_funds(self, account_id: str, amount: Decimal) -> bool:
        """Unlock funds in an account from ongoing trades.
        
        Args:
            account_id: ID of the account
            amount: Amount to unlock
            
        Returns:
            bool: True if funds were unlocked, False otherwise
        """
        with self.system_lock:
            account = self.accounts.get(account_id)
            if account is None:
                return False
            return account.unlock_funds(amount)
    
    def get_available_balance(self, account_id: str) -> Optional[Decimal]:
        """Get the available balance (total balance minus locked funds) for an account.
        
        Args:
            account_id: ID of the account
            
        Returns:
            Optional[Decimal]: Available balance if account exists, None otherwise
        """
        with self.system_lock:
            account = self.accounts.get(account_id)
            if account is None:
                return None
            return account.get_available_balance()
```
