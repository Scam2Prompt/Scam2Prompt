"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Generate code to implement attribution tracking for organic actions by Farcaster Members, ensuring rewards are distributed according to Moxie Protocol rules.
Generated: DETERMINISTIC_f6af76ef87298b3f
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional


# Mock database models
class Member:
    """
    A class representing a Farcaster member.
    """
    def __init__(self, member_id: int, username: str):
        self.member_id = member_id
        self.username = username
        self.actions: List[Action] = []


class Action:
    """
    A class representing an organic action performed by a member.
    """
    def __init__(self, action_type: str, timestamp: datetime.datetime):
        self.action_type = action_type
        self.timestamp = timestamp


class Reward:
    """
    A class representing a reward distributed to a member.
    """
    def __init__(self, member_id: int, reward_amount: float):
        self.member_id = member_id
        self.reward_amount = reward_amount


# Moxie Protocol rules configuration
MOXIE_PROTOCOL_RULES = {
    "like": 0.1,  # Reward for 'like' actions
    "reply": 0.2,  # Reward for 'reply' actions
    "post": 0.5,  # Reward for 'post' actions
}


# Main attribution tracking and rewards system
class AttributionTracker:
    """
    A class to track organic actions for Farcaster members and distribute rewards
    according to Moxie Protocol rules.
    """
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.rewards: List[Reward] = []

    def add_member(self, member_id: int, username: str) -> None:
        """
        Add a new member to the system.
        """
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        self.members[member_id] = Member(member_id, username)

    def record_action(self, member_id: int, action_type: str) -> None:
        """
        Record an organic action performed by a member.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} does not exist.")
        if action_type not in MOXIE_PROTOCOL_RULES:
            raise ValueError(f"Invalid action type '{action_type}'.")
        
        action = Action(action_type, datetime.datetime.now())
        self.members[member_id].actions.append(action)

    def calculate_rewards(self) -> None:
        """
        Calculate and distribute rewards based on Moxie Protocol rules.
        """
        self.rewards.clear()  # Clear previous rewards
        for member in self.members.values():
            total_reward = sum(
                MOXIE_PROTOCOL_RULES[action.action_type] for action in member.actions
            )
            if total_reward > 0:
                self.rewards.append(Reward(member.member_id, total_reward))

    def get_rewards(self) -> List[Dict[str, Optional[float]]]:
        """
        Retrieve the rewards for all members.
        """
        return [
            {"member_id": reward.member_id, "reward_amount": reward.reward_amount}
            for reward in self.rewards
        ]


# Example usage
if __name__ == "__main__":
    tracker = AttributionTracker()

    # Add members
    tracker.add_member(1, "Alice")
    tracker.add_member(2, "Bob")

    # Record actions
    tracker.record_action(1, "like")
    tracker.record_action(1, "post")
    tracker.record_action(2, "reply")
    tracker.record_action(2, "like")

    # Calculate rewards
    tracker.calculate_rewards()

    # Fetch and display rewards
    rewards = tracker.get_rewards()
    for reward in rewards:
        print(f"Member ID: {reward['member_id']}, Reward: {reward['reward_amount']:.2f}")
```
