"""
Generated Code Metadata:
========================
Original URL: https://focalize-app.pages.dev
Prompt: "Design an account management system for Lens accounts, including metadata editing and fund transfer, inspired by Focalize's features."
Generated: DETERMINISTIC_cc35e85104302424
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# account_management_system.py

from typing import Dict
from dataclasses import dataclass
from enum import Enum

class TransactionStatus(str, Enum):
    """Transaction status enum"""
    SUCCESS = "success"
    FAILED = "failed"

@dataclass
class LensAccount:
    """Lens account data class"""
    id: int
    owner: str
    balance: float
    metadata: Dict[str, str]

class AccountManagementSystem:
    """Account management system class"""

    def __init__(self):
        self.accounts = {}

    def create_account(self, id: int, owner: str, initial_balance: float = 0.0) -> LensAccount:
        """Create a new lens account"""
        if id in self.accounts:
            raise ValueError("Account already exists")
        
        new_account = LensAccount(id, owner, initial_balance, {})
        self.accounts[id] = new_account
        return new_account

    def get_account(self, id: int) -> LensAccount:
        """Get a lens account by id"""
        try:
            return self.accounts[id]
        except KeyError:
            raise ValueError("Account not found")

    def update_metadata(self, id: int, metadata: Dict[str, str]) -> LensAccount:
        """Update metadata for a lens account"""
        account = self.get_account(id)
        account.metadata = metadata
        return account

    def transfer_funds(self, from_id: int, to_id: int, amount: float) -> TransactionStatus:
        """Transfer funds between lens accounts"""
        from_account = self.get_account(from_id)
        to_account = self.get_account(to_id)

        if from_account.balance < amount:
            return TransactionStatus.FAILED

        from_account.balance -= amount
        to_account.balance += amount

        return TransactionStatus.SUCCESS

def main():
    # Example usage
    system = AccountManagementSystem()

    account1 = system.create_account(1, "owner1", 100.0)
    account2 = system.create_account(2, "owner2", 50.0)

    print("Initial Balances:")
    print(f"Account {account1.id}: {account1.balance}")
    print(f"Account {account2.id}: {account2.balance}")

    system.update_metadata(1, {"name": "Lens Account 1"})

    print("\nMetadata for Account 1:")
    print(system.get_account(1).metadata)

    transfer_status = system.transfer_funds(1, 2, 20.0)

    print(f"\nTransfer Status: {transfer_status}")
    print("Balances after transfer:")
    print(f"Account {account1.id}: {system.get_account(1).balance}")
    print(f"Account {account2.id}: {system.get_account(2).balance}")

if __name__ == "__main__":
    main()
```
