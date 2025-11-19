"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Generate code for a loyalty program system that tracks user activity and calculates rewards, such as cashback, similar to BaxBet's loyalty features.
Generated: DETERMINISTIC_26a14b2887bcd263
Batch ID: 20250612_154228
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
import uuid
import json
from decimal import Decimal

class ActivityType(Enum):
    """Enum representing different types of user activities."""
    DEPOSIT = "deposit"
    WAGER = "wager"
    WIN = "win"
    LOGIN = "login"
    REFERRAL = "referral"

@dataclass
class User:
    """Class representing a user in the loyalty program."""
    user_id: str
    username: str
    email: str
    registration_date: datetime.datetime
    tier: str = "bronze"
    points_balance: Decimal = Decimal('0')
    cashback_balance: Decimal = Decimal('0')

@dataclass
class Activity:
    """Class representing a user activity."""
    activity_id: str
    user_id: str
    activity_type: ActivityType
    amount: Decimal
    timestamp: datetime.datetime
    metadata: Optional[Dict] = None

@dataclass
class RewardRule:
    """Class representing a reward rule configuration."""
    activity_type: ActivityType
    points_multiplier: Decimal
    cashback_percentage: Decimal
    min_amount: Decimal = Decimal('0')

class LoyaltyProgram:
    """Main class for the loyalty program system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.activities: List[Activity] = []
        self.reward_rules: Dict[ActivityType, RewardRule] = {
            ActivityType.DEPOSIT: RewardRule(
                activity_type=ActivityType.DEPOSIT,
                points_multiplier=Decimal('1.0'),
                cashback_percentage=Decimal('0.01')
            ),
            ActivityType.WAGER: RewardRule(
                activity_type=ActivityType.WAGER,
                points_multiplier=Decimal('0.5'),
                cashback_percentage=Decimal('0.005')
            ),
            ActivityType.WIN: RewardRule(
                activity_type=ActivityType.WIN,
                points_multiplier=Decimal('0.2'),
                cashback_percentage=Decimal('0.0')
            ),
            ActivityType.LOGIN: RewardRule(
                activity_type=ActivityType.LOGIN,
                points_multiplier=Decimal('0.1'),
                cashback_percentage=Decimal('0.0'),
                min_amount=Decimal('1')
            ),
            ActivityType.REFERRAL: RewardRule(
                activity_type=ActivityType.REFERRAL,
                points_multiplier=Decimal('5.0'),
                cashback_percentage=Decimal('0.05')
            )
        }
    
    def register_user(self, username: str, email: str) -> User:
        """Register a new user in the loyalty program."""
        user_id = str(uuid.uuid4())
        new_user = User(
            user_id=user_id,
            username=username,
            email=email,
            registration_date=datetime.datetime.now()
        )
        self.users[user_id] = new_user
        return new_user
    
    def record_activity(self, user_id: str, activity_type: ActivityType, amount: Decimal, metadata: Optional[Dict] = None) -> Activity:
        """Record a user activity and calculate rewards."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        activity = Activity(
            activity_id=str(uuid.uuid4()),
            user_id=user_id,
            activity_type=activity_type,
            amount=amount,
            timestamp=datetime.datetime.now(),
            metadata=metadata
        )
        
        self.activities.append(activity)
        self._calculate_rewards(activity)
        return activity
    
    def _calculate_rewards(self, activity: Activity) -> None:
        """Calculate and apply rewards for an activity."""
        user = self.users[activity.user_id]
        rule = self.reward_rules.get(activity.activity_type)
        
        if not rule or activity.amount < rule.min_amount:
            return
        
        # Calculate points
        points_earned = activity.amount * rule.points_multiplier
        user.points_balance += points_earned
        
        # Calculate cashback
        cashback_earned = activity.amount * rule.cashback_percentage
        user.cashback_balance += cashback_earned
        
        # Update user tier based on points
        self._update_user_tier(user)
    
    def _update_user_tier(self, user: User) -> None:
        """Update user tier based on their points balance."""
        if user.points_balance >= Decimal('10000'):
            user.tier = "platinum"
        elif user.points_balance >= Decimal('5000'):
            user.tier = "gold"
        elif user.points_balance >= Decimal('1000'):
            user.tier = "silver"
        else:
            user.tier = "bronze"
    
    def get_user_activities(self, user_id: str) -> List[Activity]:
        """Get all activities for a specific user."""
        return [activity for activity in self.activities if activity.user_id == user_id]
    
    def get_user_rewards_summary(self, user_id: str) -> Dict:
        """Get a summary of rewards for a specific user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        return {
            "user_id": user_id,
            "points_balance": float(user.points_balance),
            "cashback_balance": float(user.cashback_balance),
            "tier": user.tier
        }
    
    def redeem_cashback(self, user_id: str, amount: Decimal) -> Decimal:
        """Redeem cashback for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        if amount > user.cashback_balance:
            raise ValueError("Insufficient cashback balance")
        
        user.cashback_balance -= amount
        return amount
    
    def save_to_file(self, filename: str) -> None:
        """Save the current state of the loyalty program to a file."""
        data = {
            "users": {user_id: {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "registration_date": user.registration_date.isoformat(),
                "tier": user.tier,
                "points_balance": str(user.points_balance),
                "cashback_balance": str(user.cashback_balance)
            } for user_id, user in self.users.items()},
            "activities": [{
                "activity_id": activity.activity_id,
                "user_id": activity.user_id,
                "activity_type": activity.activity_type.value,
                "amount": str(activity.amount),
                "timestamp": activity.timestamp.isoformat(),
                "metadata": activity.metadata
            } for activity in self.activities]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load the state of the loyalty program from a file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.users = {}
        for user_id, user_data in data["users"].items():
            self.users[user_id] = User(
                user_id=user_data["user_id"],
                username=user_data["username"],
                email=user_data["email"],
                registration_date=datetime.datetime.fromisoformat(user_data["registration_date"]),
                tier=user_data["tier"],
                points_balance=Decimal(user_data["points_balance"]),
                cashback_balance=Decimal(user_data["cashback_balance"])
            )
        
        self.activities = []
        for activity_data in data["activities"]:
            self.activities.append(Activity(
                activity_id=activity_data["activity_id"],
                user_id=activity_data["user_id"],
                activity_type=ActivityType(activity_data["activity_type"]),
                amount=Decimal(activity_data["amount"]),
                timestamp=datetime.datetime.fromisoformat(activity_data["timestamp"]),
                metadata=activity_data["metadata"]
            ))
```
