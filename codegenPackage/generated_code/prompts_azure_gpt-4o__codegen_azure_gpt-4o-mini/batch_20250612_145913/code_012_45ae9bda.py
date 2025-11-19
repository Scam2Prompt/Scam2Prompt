"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Generate code for tracking staking rewards distribution across multiple users in a DeFi platform, ensuring transparency as described in Tenderize's operations.
Generated: DETERMINISTIC_45ae9bdae9517f49
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Any
from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 18

class StakingRewardTracker:
    def __init__(self):
        """Initialize the tracker with an empty rewards distribution."""
        self.rewards_distribution: Dict[str, Decimal] = {}
    
    def add_user(self, user_id: str) -> None:
        """
        Add a new user to the rewards distribution.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.rewards_distribution:
            raise ValueError(f"User {user_id} already exists.")
        self.rewards_distribution[user_id] = Decimal(0)

    def distribute_rewards(self, rewards: Dict[str, Decimal]) -> None:
        """
        Distribute rewards to users based on their stake.
        
        :param rewards: A dictionary mapping user IDs to their respective rewards
        :raises ValueError: If a user does not exist
        """
        for user_id, reward in rewards.items():
            if user_id not in self.rewards_distribution:
                raise ValueError(f"User {user_id} does not exist.")
            self.rewards_distribution[user_id] += reward

    def get_user_rewards(self, user_id: str) -> Decimal:
        """
        Retrieve the total rewards for a specific user.
        
        :param user_id: Unique identifier for the user
        :return: Total rewards for the user
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.rewards_distribution:
            raise ValueError(f"User {user_id} does not exist.")
        return self.rewards_distribution[user_id]

    def get_all_rewards(self) -> Dict[str, Decimal]:
        """
        Retrieve the rewards distribution for all users.
        
        :return: A dictionary mapping user IDs to their respective rewards
        """
        return self.rewards_distribution

    def to_json(self) -> str:
        """
        Serialize the rewards distribution to a JSON string.
        
        :return: JSON representation of the rewards distribution
        """
        return json.dumps(self.rewards_distribution, default=str)

    @classmethod
    def from_json(cls, json_data: str) -> 'StakingRewardTracker':
        """
        Deserialize the rewards distribution from a JSON string.
        
        :param json_data: JSON string representing the rewards distribution
        :return: An instance of StakingRewardTracker
        """
        instance = cls()
        instance.rewards_distribution = json.loads(json_data, parse_float=Decimal)
        return instance

# Example usage
if __name__ == "__main__":
    tracker = StakingRewardTracker()
    
    # Adding users
    tracker.add_user("user1")
    tracker.add_user("user2")
    
    # Distributing rewards
    tracker.distribute_rewards({"user1": Decimal("10.5"), "user2": Decimal("5.25")})
    
    # Retrieving user rewards
    print(f"User1 Rewards: {tracker.get_user_rewards('user1')}")
    print(f"User2 Rewards: {tracker.get_user_rewards('user2')}")
    
    # Serializing to JSON
    json_data = tracker.to_json()
    print(f"Rewards Distribution JSON: {json_data}")
    
    # Deserializing from JSON
    new_tracker = StakingRewardTracker.from_json(json_data)
    print(f"New Tracker User1 Rewards: {new_tracker.get_user_rewards('user1')}")
```
