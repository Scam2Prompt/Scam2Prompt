"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: "Design a system for secure and transparent investment opportunities, similar to Exytrade's share trading and mutual fund services."
Generated: DETERMINISTIC_09ba3743a61352d8
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from abc import ABC, abstractmethod

# Database simulation (in production, replace with actual database)
class Database:
    def __init__(self):
        self.users = {}
        self.investments = {}
        self.transactions = {}
    
    def add_user(self, user: 'User') -> bool:
        if user.user_id in self.users:
            return False
        self.users[user.user_id] = user
        return True
    
    def add_investment(self, investment: 'Investment') -> bool:
        if investment.investment_id in self.investments:
            return False
        self.investments[investment.investment_id] = investment
        return True
    
    def add_transaction(self, transaction: 'Transaction') -> bool:
        if transaction.transaction_id in self.transactions:
            return False
        self.transactions[transaction.transaction_id] = transaction
        return True

# Singleton database instance
db = Database()

class InvestmentType(Enum):
    STOCK = "STOCK"
    MUTUAL_FUND = "MUTUAL_FUND"
    BOND = "BOND"
    ETF = "ETF"

class TransactionType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    DIVIDEND = "DIVIDEND"
    INTEREST = "INTEREST"

class User:
    def __init__(self, name: str, email: str, password: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password_hash = self._hash_password(password)
        self.portfolio: Dict[str, float] = {}  # investment_id: quantity
        self.created_at = datetime.utcnow()
    
    def _hash_password(self, password: str) -> str:
        """Securely hash the user's password."""
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    def verify_password(self, password: str) -> bool:
        """Verify the user's password against the stored hash."""
        hashed_password, salt = self.password_hash.split(':')
        return hashed_password == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    
    def add_to_portfolio(self, investment_id: str, quantity: float) -> bool:
        """Add an investment to the user's portfolio."""
        if investment_id not in db.investments:
            return False
        
        if investment_id in self.portfolio:
            self.portfolio[investment_id] += quantity
        else:
            self.portfolio[investment_id] = quantity
        return True
    
    def remove_from_portfolio(self, investment_id: str, quantity: float) -> bool:
        """Remove an investment from the user's portfolio."""
        if investment_id not in self.portfolio or self.portfolio[investment_id] < quantity:
            return False
        
        self.portfolio[investment_id] -= quantity
        if self.portfolio[investment_id] == 0:
            del self.portfolio[investment_id]
        return True

class Investment:
    def __init__(self, name: str, investment_type: InvestmentType, price: float, description: str = ""):
        self.investment_id = str(uuid.uuid4())
        self.name = name
        self.type = investment_type
        self.price = price
        self.description = description
        self.created_at = datetime.utcnow()
        self.historical_prices: List[Dict[str, float]] = [{"timestamp": self.created_at, "price": price}]
    
    def update_price(self, new_price: float) -> None:
        """Update the current price and record historical data."""
        self.price = new_price
        self.historical_prices.append({"timestamp": datetime.utcnow(), "price": new_price})

class Transaction:
    def __init__(self, user_id: str, investment_id: str, transaction_type: TransactionType, quantity: float, price: float):
        self.transaction_id = str(uuid.uuid4())
        self.user_id = user_id
        self.investment_id = investment_id
        self.type = transaction_type
        self.quantity = quantity
        self.price = price
        self.timestamp = datetime.utcnow()
        self.status = "PENDING"
    
    def execute(self) -> bool:
        """Execute the transaction and update user portfolio."""
        if self.status != "PENDING":
            return False
        
        user = db.users.get(self.user_id)
        investment = db.investments.get(self.investment_id)
        
        if not user or not investment:
            self.status = "FAILED"
            return False
        
        if self.type == TransactionType.BUY:
            success = user.add_to_portfolio(self.investment_id, self.quantity)
        elif self.type == TransactionType.SELL:
            success = user.remove_from_portfolio(self.investment_id, self.quantity)
        else:
            success = True  # For dividends/interest, just record the transaction
        
        if success:
            self.status = "COMPLETED"
            db.add_transaction(self)
            return True
        
        self.status = "FAILED"
        return False

class InvestmentPlatform(ABC):
    @abstractmethod
    def create_investment(self, name: str, investment_type: InvestmentType, price: float, description: str) -> Optional[Investment]:
        pass
    
    @abstractmethod
    def register_user(self, name: str, email: str, password: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def execute_transaction(self, user_id: str, investment_id: str, transaction_type: TransactionType, quantity: float) -> Optional[Transaction]:
        pass

class ExyTradePlatform(InvestmentPlatform):
    def create_investment(self, name: str, investment_type: InvestmentType, price: float, description: str = "") -> Optional[Investment]:
        """Create a new investment opportunity."""
        if price <= 0:
            return None
        
        investment = Investment(name, investment_type, price, description)
        if not db.add_investment(investment):
            return None
        return investment
    
    def register_user(self, name: str, email: str, password: str) -> Optional[User]:
        """Register a new user to the platform."""
        if not name or not email or not password:
            return None
        
        user = User(name, email, password)
        if not db.add_user(user):
            return None
        return user
    
    def execute_transaction(self, user_id: str, investment_id: str, transaction_type: TransactionType, quantity: float) -> Optional[Transaction]:
        """Execute a buy/sell transaction for a user."""
        if quantity <= 0:
            return None
        
        user = db.users.get(user_id)
        investment = db.investments.get(investment_id)
        
        if not user or not investment:
            return None
        
        transaction = Transaction(user_id, investment_id, transaction_type, quantity, investment.price)
        if not transaction.execute():
            return None
        return transaction
    
    def get_investment_history(self, investment_id: str) -> Optional[List[Dict[str, float]]]:
        """Get historical price data for an investment."""
        investment = db.investments.get(investment_id)
        if not investment:
            return None
        return investment.historical_prices
    
    def get_user_portfolio(self, user_id: str) -> Optional[Dict[str, float]]:
        """Get a user's current portfolio."""
        user = db.users.get(user_id)
        if not user:
            return None
        return user.portfolio

# Example usage
if __name__ == "__main__":
    platform = ExyTradePlatform()
    
    # Register a user
    user = platform.register_user("John Doe", "john@example.com", "securepassword123")
    if not user:
        print("Failed to register user")
        exit(1)
    
    # Create an investment
    investment = platform.create_investment("Tech Stock", InvestmentType.STOCK, 150.50, "Leading tech company")
    if not investment:
        print("Failed to create investment")
        exit(1)
    
    # Execute a buy transaction
    transaction = platform.execute_transaction(user.user_id, investment.investment_id, TransactionType.BUY, 10)
    if not transaction:
        print("Failed to execute transaction")
        exit(1)
    
    print(f"User portfolio: {platform.get_user_portfolio(user.user_id)}")
    print(f"Investment history: {platform.get_investment_history(investment.investment_id)}")
```
