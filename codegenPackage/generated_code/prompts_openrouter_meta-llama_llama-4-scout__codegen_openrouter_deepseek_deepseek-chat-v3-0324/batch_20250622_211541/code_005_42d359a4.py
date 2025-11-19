"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Create a system to track and manage user bonuses and rewards on a platform similar to Coin Rush, focusing on cashback, rake back, and VIP benefits.
Generated: DETERMINISTIC_42d359a4e9147cb1
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import uuid

# Database simulation (in production, replace with actual database)
class Database:
    def __init__(self):
        self.users = {}
        self.transactions = []
        self.vip_tiers = {
            'bronze': {'min_rake': 1000, 'cashback_rate': 0.01, 'rakeback_rate': 0.05},
            'silver': {'min_rake': 5000, 'cashback_rate': 0.02, 'rakeback_rate': 0.07},
            'gold': {'min_rake': 15000, 'cashback_rate': 0.03, 'rakeback_rate': 0.10},
            'platinum': {'min_rake': 30000, 'cashback_rate': 0.05, 'rakeback_rate': 0.15}
        }

    def get_user(self, user_id: str) -> Optional[Dict]:
        return self.users.get(user_id)

    def save_user(self, user: Dict) -> None:
        self.users[user['id']] = user

    def log_transaction(self, transaction: Dict) -> None:
        self.transactions.append(transaction)

# Enum for bonus types
class BonusType(Enum):
    CASHBACK = "cashback"
    RAKEBACK = "rakeback"
    VIP_BONUS = "vip_bonus"

@dataclass
class Bonus:
    user_id: str
    amount: float
    bonus_type: BonusType
    timestamp: datetime.datetime
    reference_id: str = None
    status: str = "pending"

    def __post_init__(self):
        if not self.reference_id:
            self.reference_id = str(uuid.uuid4())

class BonusSystem:
    def __init__(self, db: Database):
        self.db = db

    def calculate_cashback(self, user_id: str, amount: float) -> Bonus:
        """Calculate cashback based on user's VIP tier"""
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        cashback_rate = self.db.vip_tiers[user['vip_tier']]['cashback_rate']
        cashback_amount = amount * cashback_rate

        bonus = Bonus(
            user_id=user_id,
            amount=cashback_amount,
            bonus_type=BonusType.CASHBACK,
            timestamp=datetime.datetime.now()
        )

        self._apply_bonus(bonus)
        return bonus

    def calculate_rakeback(self, user_id: str, rake_amount: float) -> Bonus:
        """Calculate rakeback based on user's VIP tier"""
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        rakeback_rate = self.db.vip_tiers[user['vip_tier']]['rakeback_rate']
        rakeback_amount = rake_amount * rakeback_rate

        bonus = Bonus(
            user_id=user_id,
            amount=rakeback_amount,
            bonus_type=BonusType.RAKEBACK,
            timestamp=datetime.datetime.now()
        )

        self._apply_bonus(bonus)
        return bonus

    def check_vip_upgrade(self, user_id: str) -> Optional[Bonus]:
        """Check if user qualifies for VIP upgrade and apply bonus if eligible"""
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        current_tier = user['vip_tier']
        total_rake = sum(t['amount'] for t in self.db.transactions 
                        if t['user_id'] == user_id and t['type'] == 'rake')

        # Find the highest tier the user qualifies for
        new_tier = current_tier
        for tier, requirements in sorted(self.db.vip_tiers.items(), 
                                        key=lambda x: x[1]['min_rake'], 
                                        reverse=True):
            if total_rake >= requirements['min_rake']:
                new_tier = tier
                break

        if new_tier != current_tier:
            user['vip_tier'] = new_tier
            self.db.save_user(user)

            # Apply VIP upgrade bonus
            bonus_amount = self.db.vip_tiers[new_tier]['min_rake'] * 0.01  # Example bonus calculation
            bonus = Bonus(
                user_id=user_id,
                amount=bonus_amount,
                bonus_type=BonusType.VIP_BONUS,
                timestamp=datetime.datetime.now()
            )

            self._apply_bonus(bonus)
            return bonus
        return None

    def _apply_bonus(self, bonus: Bonus) -> None:
        """Apply bonus to user's account and log transaction"""
        user = self.db.get_user(bonus.user_id)
        if not user:
            raise ValueError("User not found")

        # Update user balance
        user['balance'] = user.get('balance', 0) + bonus.amount

        # Log transaction
        transaction = {
            'id': str(uuid.uuid4()),
            'user_id': bonus.user_id,
            'amount': bonus.amount,
            'type': bonus.bonus_type.value,
            'timestamp': bonus.timestamp.isoformat(),
            'reference_id': bonus.reference_id,
            'status': 'completed'
        }
        self.db.log_transaction(transaction)

        # Save updated user
        self.db.save_user(user)
        bonus.status = 'completed'

    def get_user_bonuses(self, user_id: str, bonus_type: Optional[BonusType] = None) -> List[Bonus]:
        """Get all bonuses for a user, optionally filtered by type"""
        transactions = [t for t in self.db.transactions if t['user_id'] == user_id]
        
        if bonus_type:
            transactions = [t for t in transactions if t['type'] == bonus_type.value]

        return [Bonus(
            user_id=t['user_id'],
            amount=t['amount'],
            bonus_type=BonusType(t['type']),
            timestamp=datetime.datetime.fromisoformat(t['timestamp']),
            reference_id=t['reference_id'],
            status=t['status']
        ) for t in transactions]

# Example usage
if __name__ == "__main__":
    # Initialize database and bonus system
    db = Database()
    bonus_system = BonusSystem(db)

    # Create a test user
    test_user = {
        'id': 'user123',
        'balance': 1000,
        'vip_tier': 'bronze'
    }
    db.save_user(test_user)

    # Simulate some rake transactions
    db.log_transaction({
        'id': str(uuid.uuid4()),
        'user_id': 'user123',
        'amount': 500,
        'type': 'rake',
        'timestamp': datetime.datetime.now().isoformat()
    })

    # Calculate and apply bonuses
    cashback_bonus = bonus_system.calculate_cashback('user123', 100)
    rakeback_bonus = bonus_system.calculate_rakeback('user123', 500)
    vip_upgrade_bonus = bonus_system.check_vip_upgrade('user123')

    # Get user bonuses
    user_bonuses = bonus_system.get_user_bonuses('user123')
    print(json.dumps([b.__dict__ for b in user_bonuses], indent=2, default=str))
```
