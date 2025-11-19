"""
Generated Code Metadata:
========================
Original URL: https://profitproinvest.com
Prompt: Generate code for a referral system that calculates and distributes up to 5% referral commissions, as described in the affiliate program on profitproinvest.com.
Generated: DETERMINISTIC_b3629e62d5dc2633
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal
from typing import List, Dict, Optional
from dataclasses import dataclass

# Set precision for decimal calculations
decimal.getcontext().prec = 6

@dataclass
class User:
    """Represents a user in the referral system."""
    id: str
    referrer_id: Optional[str] = None
    balance: decimal.Decimal = decimal.Decimal('0.00')

@dataclass
class Transaction:
    """Represents a financial transaction."""
    user_id: str
    amount: decimal.Decimal
    type: str  # 'deposit', 'withdrawal', 'commission'
    timestamp: str
    reference: str

class ReferralSystem:
    """Handles referral commissions calculation and distribution."""
    
    def __init__(self, max_levels: int = 5, commission_rate: decimal.Decimal = decimal.Decimal('0.05')):
        """
        Initialize the referral system.
        
        Args:
            max_levels: Maximum referral levels to track (default: 5)
            commission_rate: Commission percentage (default: 5%)
        """
        self.max_levels = max_levels
        self.commission_rate = commission_rate
        self.users: Dict[str, User] = {}
        self.transactions: List[Transaction] = []
    
    def add_user(self, user_id: str, referrer_id: Optional[str] = None) -> None:
        """Add a new user to the system."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
        
        if referrer_id and referrer_id not in self.users:
            raise ValueError(f"Referrer {referrer_id} does not exist")
        
        self.users[user_id] = User(id=user_id, referrer_id=referrer_id)
    
    def record_deposit(self, user_id: str, amount: decimal.Decimal, timestamp: str, reference: str) -> None:
        """Record a deposit and distribute referral commissions."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        # Record the deposit transaction
        deposit_tx = Transaction(
            user_id=user_id,
            amount=amount,
            type='deposit',
            timestamp=timestamp,
            reference=reference
        )
        self.transactions.append(deposit_tx)
        
        # Update user balance
        self.users[user_id].balance += amount
        
        # Distribute referral commissions
        self._distribute_commissions(user_id, amount, timestamp, reference)
    
    def _distribute_commissions(self, user_id: str, amount: decimal.Decimal, timestamp: str, reference: str) -> None:
        """Distribute commissions to referrers up to max_levels."""
        current_user_id = user_id
        level = 1
        
        while level <= self.max_levels:
            referrer = self._get_referrer(current_user_id)
            if not referrer:
                break
            
            commission = amount * self.commission_rate
            
            # Record commission transaction
            commission_tx = Transaction(
                user_id=referrer.id,
                amount=commission,
                type='commission',
                timestamp=timestamp,
                reference=f"{reference}_level_{level}"
            )
            self.transactions.append(commission_tx)
            
            # Update referrer balance
            referrer.balance += commission
            
            current_user_id = referrer.id
            level += 1
    
    def _get_referrer(self, user_id: str) -> Optional[User]:
        """Get the referrer of a user if exists."""
        user = self.users.get(user_id)
        if not user or not user.referrer_id:
            return None
        return self.users.get(user.referrer_id)
    
    def get_user_balance(self, user_id: str) -> decimal.Decimal:
        """Get the current balance of a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist")
        return self.users[user_id].balance
    
    def get_user_transactions(self, user_id: str) -> List[Transaction]:
        """Get all transactions for a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist")
        return [tx for tx in self.transactions if tx.user_id == user_id]

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()
    
    # Add users with referral relationships
    system.add_user("user1")  # Root user
    system.add_user("user2", "user1")
    system.add_user("user3", "user2")
    system.add_user("user4", "user3")
    system.add_user("user5", "user4")
    system.add_user("user6", "user5")
    
    # Record a deposit
    system.record_deposit(
        user_id="user6",
        amount=decimal.Decimal("1000.00"),
        timestamp="2023-01-01T00:00:00Z",
        reference="deposit_001"
    )
    
    # Check balances
    print(f"User1 balance: {system.get_user_balance('user1')}")
    print(f"User2 balance: {system.get_user_balance('user2')}")
    print(f"User3 balance: {system.get_user_balance('user3')}")
    print(f"User4 balance: {system.get_user_balance('user4')}")
    print(f"User5 balance: {system.get_user_balance('user5')}")
    print(f"User6 balance: {system.get_user_balance('user6')}")
```
