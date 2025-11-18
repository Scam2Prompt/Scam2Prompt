"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reyanetwork-4m4.pages.dev
Prompt: Generate code to implement a rewards tracking system for LPs providing liquidity on Reya Network.
Generated: DETERMINISTIC_3e1e4fd019ff0bb5
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Reward:
    """Class to represent a single reward entry."""
    def __init__(self, lp_id: str, amount: float, timestamp: datetime):
        self.lp_id = lp_id
        self.amount = amount
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        """Convert Reward to a dictionary for easy serialization."""
        return {
            'lp_id': self.lp_id,
            'amount': self.amount,
            'timestamp': self.timestamp.isoformat()
        }

class RewardsTracker:
    """Class to manage liquidity provider rewards."""
    
    def __init__(self):
        self.rewards: List[Reward] = []

    def add_reward(self, lp_id: str, amount: float) -> None:
        """Adds a new reward entry to the tracker.
        
        Args:
            lp_id (str): The ID of the liquidity provider.
            amount (float): The reward amount to be added.
        """
        if amount <= 0:
            raise ValueError("Reward amount must be positive.")
        
        new_reward = Reward(lp_id, amount, datetime.now())
        self.rewards.append(new_reward)

    def get_rewards_by_lp(self, lp_id: str) -> List[Reward]:
        """Retrieves all rewards for a specific liquidity provider.
        
        Args:
            lp_id (str): The ID of the liquidity provider.
        
        Returns:
            List[Reward]: A list of Reward objects.
        """
        return [reward for reward in self.rewards if reward.lp_id == lp_id]

    def serialize_rewards(self) -> str:
        """Serializes the rewards to a JSON string.
        
        Returns:
            str: A JSON representation of the rewards.
        """
        return json.dumps([reward.to_dict() for reward in self.rewards], indent=4)

    def load_rewards(self, json_data: str) -> None:
        """Loads rewards from a JSON string.
        
        Args:
            json_data (str): A JSON string representing the rewards.
        """
        try:
            rewards_list = json.loads(json_data)
            for reward_data in rewards_list:
                reward = Reward(
                    lp_id=reward_data['lp_id'],
                    amount=reward_data['amount'],
                    timestamp=datetime.fromisoformat(reward_data['timestamp'])
                )
                self.rewards.append(reward)
        except (ValueError, KeyError) as e:
            raise ValueError("Invalid JSON data for rewards.") from e

# Example use case of the RewardsTracker
if __name__ == "__main__":
    tracker = RewardsTracker()
    
    # Adding rewards
    tracker.add_reward("LP123", 100.0)
    tracker.add_reward("LP456", 150.5)

    # Fetching rewards for a specific liquidity provider
    lp_rewards = tracker.get_rewards_by_lp("LP123")
    print("Rewards for LP123:", [reward.to_dict() for reward in lp_rewards])

    # Serializing rewards to JSON
    json_output = tracker.serialize_rewards()
    print("Serialized Rewards:\n", json_output)

    # Loading rewards from JSON
    try:
        tracker.load_rewards(json_output)
        print("Rewards loaded successfully.")
    except ValueError as e:
        print("Error loading rewards:", e)
```
