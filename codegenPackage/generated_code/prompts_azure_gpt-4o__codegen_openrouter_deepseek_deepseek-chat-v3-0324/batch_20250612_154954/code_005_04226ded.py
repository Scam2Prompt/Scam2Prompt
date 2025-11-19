"""
Generated Code Metadata:
========================
Original URL: https://imperial-holding.com.co
Prompt: Write code to implement a feature for managing multiple account types with tailored solutions and innovative approaches, as highlighted by Imperial Capital.
Generated: DETERMINISTIC_04226ded6cb05739
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Account Management System with Multiple Account Types

This module provides a flexible and extensible system for managing multiple account types
with tailored solutions. It follows best practices for clean code, error handling, and
production readiness.

Key Features:
- Support for multiple account types (e.g., Basic, Premium, Enterprise)
- Customizable account solutions
- Extensible architecture for future account types
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Dict, Optional, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AccountType(Enum):
    """Enum representing different account types."""
    BASIC = auto()
    PREMIUM = auto()
    ENTERPRISE = auto()

class Account(ABC):
    """Abstract base class for all account types."""
    
    def __init__(self, account_id: str, owner_name: str):
        """
        Initialize an account with basic information.
        
        Args:
            account_id: Unique identifier for the account
            owner_name: Name of the account owner
        """
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance: float = 0.0
    
    @abstractmethod
    def get_features(self) -> List[str]:
        """Return the list of features available for this account type."""
        pass
    
    @abstractmethod
    def get_limits(self) -> Dict[str, float]:
        """Return the account limits (transactions, transfers, etc.)."""
        pass
    
    def deposit(self, amount: float) -> None:
        """Deposit funds into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        logger.info(f"Deposited {amount} to account {self.account_id}. New balance: {self.balance}")
    
    def withdraw(self, amount: float) -> None:
        """Withdraw funds from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        logger.info(f"Withdrew {amount} from account {self.account_id}. New balance: {self.balance}")
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"Account ID: {self.account_id}, Owner: {self.owner_name}, Balance: {self.balance}"

class BasicAccount(Account):
    """Basic account type with standard features."""
    
    def get_features(self) -> List[str]:
        return [
            "Standard transactions",
            "Basic customer support",
            "Limited transfers"
        ]
    
    def get_limits(self) -> Dict[str, float]:
        return {
            "daily_withdrawal": 1000.00,
            "monthly_transfers": 5,
            "max_balance": 50000.00
        }

class PremiumAccount(Account):
    """Premium account type with enhanced features."""
    
    def get_features(self) -> List[str]:
        return [
            "Unlimited transactions",
            "Priority customer support",
            "Higher transfer limits",
            "Investment options"
        ]
    
    def get_limits(self) -> Dict[str, float]:
        return {
            "daily_withdrawal": 5000.00,
            "monthly_transfers": 20,
            "max_balance": 200000.00
        }

class EnterpriseAccount(Account):
    """Enterprise account type with business features."""
    
    def get_features(self) -> List[str]:
        return [
            "Unlimited transactions",
            "24/7 dedicated support",
            "API access",
            "Multi-user access",
            "Advanced reporting"
        ]
    
    def get_limits(self) -> Dict[str, float]:
        return {
            "daily_withdrawal": 25000.00,
            "monthly_transfers": 100,
            "max_balance": 1000000.00
        }

class AccountFactory:
    """Factory class for creating account instances."""
    
    @staticmethod
    def create_account(account_type: AccountType, account_id: str, owner_name: str) -> Account:
        """
        Create an account of the specified type.
        
        Args:
            account_type: Type of account to create
            account_id: Unique identifier for the account
            owner_name: Name of the account owner
            
        Returns:
            An instance of the requested account type
            
        Raises:
            ValueError: If the account type is not supported
        """
        if account_type == AccountType.BASIC:
            return BasicAccount(account_id, owner_name)
        elif account_type == AccountType.PREMIUM:
            return PremiumAccount(account_id, owner_name)
        elif account_type == AccountType.ENTERPRISE:
            return EnterpriseAccount(account_id, owner_name)
        else:
            raise ValueError(f"Unsupported account type: {account_type}")

class AccountManager:
    """Manager class for handling multiple accounts."""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
    
    def add_account(self, account_type: AccountType, account_id: str, owner_name: str) -> Account:
        """
        Add a new account to the manager.
        
        Args:
            account_type: Type of account to create
            account_id: Unique identifier for the account
            owner_name: Name of the account owner
            
        Returns:
            The created account instance
            
        Raises:
            ValueError: If account ID already exists
        """
        if account_id in self.accounts:
            raise ValueError(f"Account with ID {account_id} already exists")
        
        account = AccountFactory.create_account(account_type, account_id, owner_name)
        self.accounts[account_id] = account
        logger.info(f"Created new {account_type.name} account for {owner_name}")
        return account
    
    def get_account(self, account_id: str) -> Optional[Account]:
        """Retrieve an account by its ID."""
        return self.accounts.get(account_id)
    
    def remove_account(self, account_id: str) -> None:
        """Remove an account from the manager."""
        if account_id not in self.accounts:
            raise ValueError(f"Account with ID {account_id} not found")
        
        del self.accounts[account_id]
        logger.info(f"Removed account {account_id}")
    
    def list_accounts(self) -> List[Account]:
        """Return a list of all managed accounts."""
        return list(self.accounts.values())

# Example usage
if __name__ == "__main__":
    try:
        manager = AccountManager()
        
        # Create accounts
        basic_acc = manager.add_account(AccountType.BASIC, "acc001", "John Doe")
        premium_acc = manager.add_account(AccountType.PREMIUM, "acc002", "Jane Smith")
        enterprise_acc = manager.add_account(AccountType.ENTERPRISE, "acc003", "Acme Corp")
        
        # Perform operations
        basic_acc.deposit(500)
        premium_acc.deposit(2000)
        enterprise_acc.deposit(10000)
        
        # Display account info
        for account in manager.list_accounts():
            print(account)
            print("Features:", account.get_features())
            print("Limits:", account.get_limits())
            print()
            
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```
