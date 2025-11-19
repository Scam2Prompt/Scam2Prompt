"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Design a system to implement a loyalty program for Slots City, tracking user activity and rewarding them with bonuses, free spins, and other perks.
Generated: DETERMINISTIC_a9d79dee73926c81
Batch ID: 20250622_205358
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
    BONUS = 1
    FREE_SPINS = 2
    OTHER_PERKS = 3

class User:
    """Class representing a user in the loyalty program."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.activity_history = []
        self.rewards = []

    def log_activity(self, activity: str):
        """Log user activity."""
        self.activity_history.append({
            'timestamp': datetime.now(),
            'activity': activity
        })

    def add_reward(self, reward: Dict):
        """Add a reward to the user's account."""
        self.rewards.append(reward)

class LoyaltyProgram:
    """Class representing the loyalty program."""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.rewards_config = {
            'bonus': {
                'threshold': 10,
                'reward': {'type': RewardType.BONUS, 'value': 10}
            },
            'free_spins': {
                'threshold': 20,
                'reward': {'type': RewardType.FREE_SPINS, 'value': 5}
            }
        }

    def create_user(self, user_id: int):
        """Create a new user in the loyalty program."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def log_user_activity(self, user_id: int, activity: str):
        """Log activity for a user."""
        try:
            user = self.users[user_id]
            user.log_activity(activity)
            self.check_for_rewards(user)
        except KeyError:
            print(f"User {user_id} not found.")

    def check_for_rewards(self, user: User):
        """Check if a user has earned a reward."""
        activity_count = len(user.activity_history)
        for reward_name, config in self.rewards_config.items():
            if activity_count >= config['threshold'] and not self.has_reward(user, config['reward']):
                user.add_reward(config['reward'])
                print(f"User {user.user_id} earned a {reward_name} reward.")

    def has_reward(self, user: User, reward: Dict):
        """Check if a user has already received a reward."""
        for user_reward in user.rewards:
            if user_reward['type'] == reward['type'] and user_reward['value'] == reward['value']:
                return True
        return False

    def get_user_rewards(self, user_id: int) -> List[Dict]:
        """Get a user's rewards."""
        try:
            user = self.users[user_id]
            return user.rewards
        except KeyError:
            print(f"User {user_id} not found.")
            return []

def main():
    loyalty_program = LoyaltyProgram()
    loyalty_program.create_user(1)

    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')  # Triggers bonus reward
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')
    loyalty_program.log_user_activity(1, 'played_slot')  # Triggers free spins reward

    rewards = loyalty_program.get_user_rewards(1)
    for reward in rewards:
        print(f"Reward: {reward['type'].name}, Value: {reward['value']}")

if __name__ == "__main__":
    main()
```
