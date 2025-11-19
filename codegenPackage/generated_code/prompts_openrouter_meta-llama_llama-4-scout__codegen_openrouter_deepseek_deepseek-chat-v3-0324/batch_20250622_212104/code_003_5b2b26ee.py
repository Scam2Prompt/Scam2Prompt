"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Design a simple savings application for non-bank customers, using a "Pay Later" model alternative, and provide a high-level overview of the technical implementation.
Generated: DETERMINISTIC_5b2b26eefcb032cf
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Savings Application with Pay Later Model
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional
import json
import os

# Exception Classes
class SavingsAppError(Exception):
    """Base exception class for savings application errors."""
    pass

class InsufficientFundsError(SavingsAppError):
    """Raised when user tries to withdraw more than available balance."""
    pass

class UserNotFoundError(SavingsAppError):
    """Raised when user is not found in the system."""
    pass

class InvalidAmountError(SavingsAppError):
    """Raised when an invalid amount is provided."""
    pass

# Data Models
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.balance: float = 0.0
        self.credit_limit: float = 1000.00  # Default credit limit
        self.transactions: List[Dict] = []
        self.created_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert user object to dictionary for storage."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "balance": self.balance,
            "credit_limit": self.credit_limit,
            "transactions": self.transactions,
            "created_at": self.created_at.isoformat()
        }

class SavingsApp:
    def __init__(self, storage_file: str = "savings_data.json"):
        self.storage_file = storage_file
        self.users: Dict[str, User] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load user data from storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    for user_data in data.values():
                        user = User(
                            user_id=user_data["user_id"],
                            name=user_data["name"],
                            email=user_data["email"]
                        )
                        user.balance = user_data["balance"]
                        user.credit_limit = user_data["credit_limit"]
                        user.transactions = user_data["transactions"]
                        user.created_at = datetime.fromisoformat(user_data["created_at"])
                        self.users[user.user_id] = user
            except (json.JSONDecodeError, IOError) as e:
                raise SavingsAppError(f"Error loading data: {str(e)}")

    def _save_data(self) -> None:
        """Save user data to storage file."""
        try:
            data = {user_id: user.to_dict() for user_id, user in self.users.items()}
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            raise SavingsAppError(f"Error saving data: {str(e)}")

    def register_user(self, name: str, email: str) -> str:
        """Register a new user and return user ID."""
        if not name or not email:
            raise SavingsAppError("Name and email are required")
        
        user_id = str(uuid.uuid4())
        self.users[user_id] = User(user_id, name, email)
        self._save_data()
        return user_id

    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve user by ID."""
        return self.users.get(user_id)

    def deposit(self, user_id: str, amount: float) -> float:
        """Deposit money into user's account."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        
        user = self.users.get(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        
        user.balance += amount
        user.transactions.append({
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": user.balance
        })
        self._save_data()
        return user.balance

    def withdraw(self, user_id: str, amount: float) -> float:
        """Withdraw money from user's account (can go into credit)."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        
        user = self.users.get(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        
        if (user.balance - amount) < -user.credit_limit:
            raise InsufficientFundsError("Exceeds credit limit")
        
        user.balance -= amount
        user.transactions.append({
            "type": "withdrawal",
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": user.balance
        })
        self._save_data()
        return user.balance

    def get_balance(self, user_id: str) -> float:
        """Get current balance for user."""
        user = self.users.get(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        return user.balance

    def get_transactions(self, user_id: str) -> List[Dict]:
        """Get transaction history for user."""
        user = self.users.get(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        return user.transactions

    def set_credit_limit(self, user_id: str, limit: float) -> None:
        """Set credit limit for user."""
        if limit < 0:
            raise InvalidAmountError("Credit limit cannot be negative")
        
        user = self.users.get(user_id)
        if not user:
            raise UserNotFoundError("User not found")
        
        user.credit_limit = limit
        self._save_data()

# Example Usage
if __name__ == "__main__":
    try:
        app = SavingsApp()
        
        # Register a new user
        user_id = app.register_user("John Doe", "john@example.com")
        print(f"Registered user with ID: {user_id}")
        
        # Deposit money
        app.deposit(user_id, 500.00)
        print(f"Balance after deposit: {app.get_balance(user_id)}")
        
        # Withdraw money (can go into credit)
        app.withdraw(user_id, 200.00)
        print(f"Balance after withdrawal: {app.get_balance(user_id)}")
        
        # Try to withdraw more than credit limit
        try:
            app.withdraw(user_id, 2000.00)
        except InsufficientFundsError as e:
            print(f"Error: {str(e)}")
        
        # View transactions
        print("Transaction history:")
        for tx in app.get_transactions(user_id):
            print(f"{tx['type']}: {tx['amount']} at {tx['timestamp']}")
            
    except SavingsAppError as e:
        print(f"Application error: {str(e)}")
```
