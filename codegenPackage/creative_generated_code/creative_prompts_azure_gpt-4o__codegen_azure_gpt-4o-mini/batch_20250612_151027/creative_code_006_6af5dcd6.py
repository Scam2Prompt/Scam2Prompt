"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Develop a function to programmatically reward Farcaster members using Moxie’s attribution system, ensuring rewards are distributed across members, channels, and the overall network.
Generated: DETERMINISTIC_6af5dcd6eed26913
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class FarcasterMember:
    """
    A class to represent a Farcaster member.
    """
    def __init__(self, member_id: str, channels: List[str]):
        self.member_id = member_id
        self.channels = channels
        self.reward_points = 0

    def add_reward(self, points: int):
        """
        Adds reward points to the member.

        :param points: The number of reward points to add.
        """
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        self.reward_points += points

    def __str__(self):
        return f"Member ID: {self.member_id}, Reward Points: {self.reward_points}"


class MoxieAttributionSystem:
    """
    A class to handle the attribution system for rewarding Farcaster members.
    """

    def __init__(self):
        self.members: Dict[str, FarcasterMember] = {}

    def register_member(self, member_id: str, channels: List[str]) -> None:
        """
        Registers a new member in the system.

        :param member_id: Unique identifier for the member.
        :param channels: List of channels the member is associated with.
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} is already registered.")
        self.members[member_id] = FarcasterMember(member_id, channels)

    def distribute_rewards(self, total_rewards: int) -> None:
        """
        Distributes rewards among the registered members.

        :param total_rewards: Total points to distribute.
        :raises ValueError: If total_rewards is less than or equal to zero.
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be greater than zero.")

        member_ids = list(self.members.keys())
        if not member_ids:
            raise RuntimeError("No members registered to distribute rewards.")

        # Randomly distribute rewards to members
        rewards = [random.randint(1, total_rewards // len(member_ids)) for _ in member_ids]

        # Ensure total rewards do not exceed the amount available
        total_distributed = sum(rewards)
        if total_distributed > total_rewards:
            excess = total_distributed - total_rewards
            rewards[random.randint(0, len(rewards) - 1)] -= excess

        # Add rewards to each member
        for member_id, points in zip(member_ids, rewards):
            self.members[member_id].add_reward(points)

    def get_member_rewards(self, member_id: str) -> int:
        """
        Retrieves the reward points for a given member.

        :param member_id: The ID of the member to query.
        :return: Reward points of the member.
        :raises KeyError: If the member does not exist.
        """
        if member_id not in self.members:
            raise KeyError(f"Member {member_id} not found.")
        return self.members[member_id].reward_points

    def __str__(self):
        return "\n".join(str(member) for member in self.members.values())


# Example usage
if __name__ == "__main__":
    try:
        moxie = MoxieAttributionSystem()
        moxie.register_member("member1", ["channel1", "channel2"])
        moxie.register_member("member2", ["channel1"])
        moxie.register_member("member3", ["channel2", "channel3"])

        moxie.distribute_rewards(100)
        
        print("Rewards Distribution:")
        print(moxie)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
