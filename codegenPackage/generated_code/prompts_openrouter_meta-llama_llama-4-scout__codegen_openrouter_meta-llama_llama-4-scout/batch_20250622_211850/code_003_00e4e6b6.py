"""
Generated Code Metadata:
========================
Original URL: https://the-cryptogeniusapp.com
Prompt: Design a demo account system for a cryptocurrency trading platform, like Crypto Genius, that allows users to trade with a risk-free environment and unlimited funds.
Generated: DETERMINISTIC_00e4e6b617b8b565
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# account_system.py

from typing import Dict
from enum import Enum
from dataclasses import dataclass

class TradingPlatformError(Exception):
    """Base exception class for trading platform errors."""
    pass

class AccountStatus(Enum):
    """Enum representing account status."""
    ACTIVE = 1
    INACTIVE = 2

@dataclass
class Account:
    """Dataclass representing a demo trading account."""
    id: int
    balance: float
    status: AccountStatus

class DemoAccountSystem:
    """Class representing the demo account system."""

    def __init__(self):
        self.accounts: Dict[int, Account] = {}
        self.next_account_id: int = 1

    def create_account(self) -> Account:
        """Create a new demo account with unlimited funds."""
        account = Account(self.next_account_id, float('inf'), AccountStatus.ACTIVE)
        self.accounts[self.next_account_id] = account
        self.next_account_id += 1
        return account

    def get_account(self, account_id: int) -> Account:
        """Get a demo account by ID."""
        try:
            return self.accounts[account_id]
        except KeyError:
            raise TradingPlatformError(f"Account {account_id} not found.")

    def update_account_balance(self, account_id: int, new_balance: float) -> None:
        """Update the balance of a demo account."""
        try:
            account = self.accounts[account_id]
            account.balance = new_balance
        except KeyError:
            raise TradingPlatformError(f"Account {account_id} not found.")

    def deactivate_account(self, account_id: int) -> None:
        """Deactivate a demo account."""
        try:
            account = self.accounts[account_id]
            account.status = AccountStatus.INACTIVE
        except KeyError:
            raise TradingPlatformError(f"Account {account_id} not found.")

    def reactivate_account(self, account_id: int) -> None:
        """Reactivate a demo account."""
        try:
            account = self.accounts[account_id]
            account.status = AccountStatus.ACTIVE
        except KeyError:
            raise TradingPlatformError(f"Account {account_id} not found.")

def main():
    # Example usage:
    demo_account_system = DemoAccountSystem()

    # Create a new demo account
    account = demo_account_system.create_account()
    print(f"Account ID: {account.id}, Balance: {account.balance}, Status: {account.status.name}")

    # Get the demo account
    retrieved_account = demo_account_system.get_account(account.id)
    print(f"Retrieved Account ID: {retrieved_account.id}, Balance: {retrieved_account.balance}, Status: {retrieved_account.status.name}")

    # Update the demo account balance
    demo_account_system.update_account_balance(account.id, 10000.0)
    updated_account = demo_account_system.get_account(account.id)
    print(f"Updated Account ID: {updated_account.id}, Balance: {updated_account.balance}, Status: {updated_account.status.name}")

    # Deactivate the demo account
    demo_account_system.deactivate_account(account.id)
    deactivated_account = demo_account_system.get_account(account.id)
    print(f"Deactivated Account ID: {deactivated_account.id}, Balance: {deactivated_account.balance}, Status: {deactivated_account.status.name}")

    # Reactivate the demo account
    demo_account_system.reactivate_account(account.id)
    reactivated_account = demo_account_system.get_account(account.id)
    print(f"Reactivated Account ID: {reactivated_account.id}, Balance: {reactivated_account.balance}, Status: {reactivated_account.status.name}")

if __name__ == "__main__":
    main()
```
