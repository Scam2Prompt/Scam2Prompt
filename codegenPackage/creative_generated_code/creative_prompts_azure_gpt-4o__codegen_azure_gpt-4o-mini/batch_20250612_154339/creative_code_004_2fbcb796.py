"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Write a script to calculate and distribute Halo XP and token rewards to users based on their contributions within the halo.social ecosystem.
Generated: DETERMINISTIC_2fbcb796eccddd90
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class User:
    """Represents a user in the halo.social ecosystem."""
    
    def __init__(self, user_id, contributions):
        self.user_id = user_id
        self.contributions = contributions  # Contribution value for XP calculation
        self.xp = 0  # Experience points awarded
        self.tokens = 0  # Tokens awarded

    def calculate_rewards(self):
        """Calculate XP and token rewards based on contributions."""
        try:
            # Example reward calculation logic
            self.xp = int(self.contributions * 10)  # 10 XP per contribution unit
            self.tokens = Decimal(self.contributions) * Decimal('0.5')  # 0.5 tokens per contribution unit
        except (TypeError, ValueError) as e:
            print(f"Error calculating rewards for user {self.user_id}: {e}")

    def __repr__(self):
        return f"User(user_id={self.user_id}, contributions={self.contributions}, xp={self.xp}, tokens={self.tokens})"


class HaloRewardsDistributor:
    """Distributes rewards to users based on their contributions."""
    
    def __init__(self, user_data):
        self.users = self.load_users(user_data)

    def load_users(self, user_data):
        """Load users from provided data."""
        users = []
        for data in user_data:
            try:
                user = User(user_id=data['user_id'], contributions=data['contributions'])
                users.append(user)
            except KeyError as e:
                print(f"Missing key {e} in user data: {data}")
            except Exception as e:
                print(f"Error loading user data {data}: {e}")
        return users

    def distribute_rewards(self):
        """Calculate and distribute rewards to all users."""
        for user in self.users:
            user.calculate_rewards()

    def get_rewards_summary(self):
        """Get a summary of all users' rewards."""
        return [{ "user_id": user.user_id, "xp": user.xp, "tokens": str(user.tokens) } for user in self.users]


def main():
    """Main function to execute the reward distribution process."""
    # Sample user data
    user_data = [
        {"user_id": 1, "contributions": 15},
        {"user_id": 2, "contributions": 20},
        {"user_id": 3, "contributions": 0},  # Test case with zero contributions
        {"user_id": 4, "contributions": "invalid"},  # Test case with invalid contribution
    ]

    distributor = HaloRewardsDistributor(user_data)
    distributor.distribute_rewards()

    # Output the rewards summary
    rewards_summary = distributor.get_rewards_summary()
    print(json.dumps(rewards_summary, indent=2))


if __name__ == "__main__":
    main()
```
