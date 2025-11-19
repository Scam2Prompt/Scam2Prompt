"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Design a loyalty program, similar to BaxBet's, that rewards users with cashback and bonuses, using a Python-based data analysis tool to track user activity and reward eligibility.
Generated: DETERMINISTIC_c07a7c4cd08c886e
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class RewardType(Enum):
    """Enum for reward types."""
    CASHBACK = 1
    BONUS = 2

class User:
    """Class representing a user in the loyalty program."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.activity_history = []

    def add_activity(self, activity: Dict):
        """Add a new activity to the user's history."""
        self.activity_history.append(activity)

class LoyaltyProgram:
    """Class representing the loyalty program."""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.rewards: Dict[RewardType, Dict] = {
            RewardType.CASHBACK: {'rate': 0.1, 'min_activity': 100},
            RewardType.BONUS: {'amount': 50, 'min_activity': 5}
        }

    def add_user(self, user_id: int):
        """Add a new user to the loyalty program."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def track_activity(self, user_id: int, activity: Dict):
        """Track a user's activity."""
        if user_id in self.users:
            self.users[user_id].add_activity(activity)
            self.check_reward_eligibility(user_id)
        else:
            raise ValueError("User not found in the loyalty program.")

    def check_reward_eligibility(self, user_id: int):
        """Check if a user is eligible for rewards based on their activity."""
        user = self.users[user_id]
        cashback_eligible = self.check_cashback_eligibility(user)
        bonus_eligible = self.check_bonus_eligibility(user)

        if cashback_eligible:
            self.award_cashback(user_id)
        if bonus_eligible:
            self.award_bonus(user_id)

    def check_cashback_eligibility(self, user: User) -> bool:
        """Check if a user is eligible for cashback."""
        total_activity = sum(activity['amount'] for activity in user.activity_history)
        return total_activity >= self.rewards[RewardType.CASHBACK]['min_activity']

    def check_bonus_eligibility(self, user: User) -> bool:
        """Check if a user is eligible for a bonus."""
        return len(user.activity_history) >= self.rewards[RewardType.BONUS]['min_activity']

    def award_cashback(self, user_id: int):
        """Award cashback to a user."""
        user = self.users[user_id]
        total_activity = sum(activity['amount'] for activity in user.activity_history)
        cashback_amount = total_activity * self.rewards[RewardType.CASHBACK]['rate']
        print(f"User {user_id} awarded ${cashback_amount:.2f} cashback.")

    def award_bonus(self, user_id: int):
        """Award a bonus to a user."""
        bonus_amount = self.rewards[RewardType.BONUS]['amount']
        print(f"User {user_id} awarded ${bonus_amount:.2f} bonus.")

def main():
    loyalty_program = LoyaltyProgram()

    # Add users
    loyalty_program.add_user(1)
    loyalty_program.add_user(2)

    # Track user activity
    loyalty_program.track_activity(1, {'amount': 100, 'timestamp': datetime.now()})
    loyalty_program.track_activity(1, {'amount': 200, 'timestamp': datetime.now()})
    loyalty_program.track_activity(2, {'amount': 50, 'timestamp': datetime.now()})

    # Attempt to track activity for non-existent user
    try:
        loyalty_program.track_activity(3, {'amount': 100, 'timestamp': datetime.now()})
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
