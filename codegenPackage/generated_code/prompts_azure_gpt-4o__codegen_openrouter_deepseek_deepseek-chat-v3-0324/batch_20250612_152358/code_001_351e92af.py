"""
Generated Code Metadata:
========================
Original URL: https://largeoptions.org
Prompt: Generate code to simulate the referral commission system described on largeoptions.org, including tiered percentages (e.g., 6%, 8%, 10%, etc.) and instant payouts.
Generated: DETERMINISTIC_351e92af945d48b5
Batch ID: 20250612_152358
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
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 6

class User:
    def __init__(self, user_id: str, name: str, email: str, referrer_id: Optional[str] = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.referrer_id = referrer_id
        self.tier = 1
        self.balance = Decimal('0.00')
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.name}, email={self.email}, tier={self.tier}, balance={self.balance})"

class Transaction:
    def __init__(self, transaction_id: str, user_id: str, amount: Decimal, transaction_type: str, timestamp: datetime):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.type = transaction_type
        self.timestamp = timestamp

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, amount={self.amount}, type={self.type})"

class ReferralSystem:
    TIER_COMMISSIONS = {
        1: Decimal('0.06'),  # 6%
        2: Decimal('0.08'),  # 8%
        3: Decimal('0.10'),  # 10%
        4: Decimal('0.12'),  # 12%
        5: Decimal('0.15')   # 15%
    }
    
    MIN_WITHDRAWAL = Decimal('10.00')
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.transactions: Dict[str, Transaction] = {}
        self.referral_tree: Dict[str, List[str]] = {}  # referrer_id -> list of referred user_ids
    
    def register_user(self, name: str, email: str, referrer_id: Optional[str] = None) -> User:
        """Register a new user with optional referrer."""
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, referrer_id)
        
        if referrer_id and referrer_id in self.users:
            referrer = self.users[referrer_id]
            if referrer_id not in self.referral_tree:
                self.referral_tree[referrer_id] = []
            self.referral_tree[referrer_id].append(user_id)
            user.tier = referrer.tier + 1
        
        self.users[user_id] = user
        return user
    
    def process_trade(self, user_id: str, trade_amount: Decimal) -> bool:
        """Process a trade and distribute referral commissions."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        if trade_amount <= Decimal('0.00'):
            raise ValueError("Trade amount must be positive")
        
        user = self.users[user_id]
        referrer_id = user.referrer_id
        current_tier = 1
        
        while referrer_id and current_tier <= len(self.TIER_COMMISSIONS):
            if referrer_id in self.users:
                referrer = self.users[referrer_id]
                commission_rate = self.TIER_COMMISSIONS.get(current_tier, Decimal('0.00'))
                commission = trade_amount * commission_rate
                
                referrer.balance += commission
                
                # Record transaction
                transaction_id = str(uuid.uuid4())
                transaction = Transaction(
                    transaction_id=transaction_id,
                    user_id=referrer_id,
                    amount=commission,
                    transaction_type="commission",
                    timestamp=datetime.utcnow()
                )
                self.transactions[transaction_id] = transaction
            
            # Move up the referral chain
            referrer_id = self.users[referrer_id].referrer_id if referrer_id in self.users else None
            current_tier += 1
        
        return True
    
    def withdraw_commission(self, user_id: str, amount: Decimal) -> bool:
        """Withdraw commission balance to user's account."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        if amount <= Decimal('0.00'):
            raise ValueError("Withdrawal amount must be positive")
        
        user = self.users[user_id]
        
        if user.balance < amount:
            raise ValueError("Insufficient balance")
        
        if amount < self.MIN_WITHDRAWAL:
            raise ValueError(f"Minimum withdrawal amount is {self.MIN_WITHDRAWAL}")
        
        user.balance -= amount
        
        # Record transaction
        transaction_id = str(uuid.uuid4())
        transaction = Transaction(
            transaction_id=transaction_id,
            user_id=user_id,
            amount=amount,
            transaction_type="withdrawal",
            timestamp=datetime.utcnow()
        )
        self.transactions[transaction_id] = transaction
        
        return True
    
    def get_user_balance(self, user_id: str) -> Decimal:
        """Get user's current commission balance."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].balance
    
    def get_user_transactions(self, user_id: str) -> List[Transaction]:
        """Get all transactions for a user."""
        return [t for t in self.transactions.values() if t.user_id == user_id]
    
    def get_referral_tree(self, user_id: str) -> List[str]:
        """Get all users referred by a given user."""
        return self.referral_tree.get(user_id, [])

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()
    
    # Register users
    user1 = system.register_user("John Doe", "john@example.com")
    user2 = system.register_user("Jane Smith", "jane@example.com", user1.user_id)
    user3 = system.register_user("Bob Johnson", "bob@example.com", user2.user_id)
    
    # Process trades
    system.process_trade(user3.user_id, Decimal('1000.00'))
    
    # Check balances
    print(f"User1 balance: {system.get_user_balance(user1.user_id)}")  # Should be 60 (6% of 1000)
    print(f"User2 balance: {system.get_user_balance(user2.user_id)}")  # Should be 80 (8% of 1000)
    
    # Withdraw commission
    system.withdraw_commission(user1.user_id, Decimal('50.00'))
    print(f"User1 balance after withdrawal: {system.get_user_balance(user1.user_id)}")  # Should be 10
```
