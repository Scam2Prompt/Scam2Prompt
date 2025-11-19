"""
Generated Code Metadata:
========================
Original URL: https://everix-edge-gpt.com
Prompt: Design a demo account system for a cryptocurrency trading platform, allowing users to test and refine their trading strategies before engaging in live trading sessions.
Generated: DETERMINISTIC_7a2c996e3bce7f23
Batch ID: 20250622_211305
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
from datetime import datetime, timedelta
import hashlib
import secrets

class AccountStatus(str, Enum):
    """Account status"""
    ACTIVE = "active"
    INACTIVE = "inactive"

class AccountType(str, Enum):
    """Account type"""
    DEMO = "demo"
    LIVE = "live"

@dataclass
class User:
    """User data class"""
    id: int
    username: str
    email: str
    password_hash: str
    account_status: AccountStatus
    account_type: AccountType

class AccountSystem:
    """Account system class"""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.accounts: Dict[int, Dict[str, float]] = {}

    def create_demo_account(self, username: str, email: str, password: str) -> int:
        """Create a demo account"""
        if self.get_user_by_username(username):
            raise ValueError("Username already exists")

        user_id = len(self.users) + 1
        password_hash = self._hash_password(password)
        user = User(
            id=user_id,
            username=username,
            email=email,
            password_hash=password_hash,
            account_status=AccountStatus.ACTIVE,
            account_type=AccountType.DEMO
        )
        self.users[user_id] = user

        # Initialize demo account with $10,000 balance
        self.accounts[user_id] = {"balance": 10000.0, "equity": 10000.0}

        return user_id

    def create_live_account(self, username: str, email: str, password: str) -> int:
        """Create a live account"""
        if self.get_user_by_username(username):
            raise ValueError("Username already exists")

        user_id = len(self.users) + 1
        password_hash = self._hash_password(password)
        user = User(
            id=user_id,
            username=username,
            email=email,
            password_hash=password_hash,
            account_status=AccountStatus.ACTIVE,
            account_type=AccountType.LIVE
        )
        self.users[user_id] = user

        # Initialize live account with $0 balance
        self.accounts[user_id] = {"balance": 0.0, "equity": 0.0}

        return user_id

    def get_user_by_username(self, username: str) -> User:
        """Get user by username"""
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    def get_account(self, user_id: int) -> Dict[str, float]:
        """Get account by user ID"""
        return self.accounts.get(user_id)

    def deposit(self, user_id: int, amount: float) -> None:
        """Deposit funds into account"""
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        account = self.get_account(user_id)
        if account:
            account["balance"] += amount
            account["equity"] += amount
        else:
            raise ValueError("Account not found")

    def withdraw(self, user_id: int, amount: float) -> None:
        """Withdraw funds from account"""
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")

        account = self.get_account(user_id)
        if account:
            if account["balance"] >= amount:
                account["balance"] -= amount
                account["equity"] -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Account not found")

    def _hash_password(self, password: str) -> str:
        """Hash password"""
        salt = secrets.token_hex(16)
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()

def main():
    account_system = AccountSystem()

    # Create demo account
    demo_user_id = account_system.create_demo_account("demo_user", "demo@example.com", "password123")
    print(f"Demo account created with user ID: {demo_user_id}")

    # Create live account
    live_user_id = account_system.create_live_account("live_user", "live@example.com", "password123")
    print(f"Live account created with user ID: {live_user_id}")

    # Deposit funds into demo account
    account_system.deposit(demo_user_id, 5000.0)
    print(f"Demo account balance: {account_system.get_account(demo_user_id)['balance']}")

    # Withdraw funds from demo account
    account_system.withdraw(demo_user_id, 1000.0)
    print(f"Demo account balance: {account_system.get_account(demo_user_id)['balance']}")

if __name__ == "__main__":
    main()
```
