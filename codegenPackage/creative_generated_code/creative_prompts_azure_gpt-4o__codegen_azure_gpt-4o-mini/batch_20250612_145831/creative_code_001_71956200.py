"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacem-world.vercel.app
Prompt: Generate code to implement a reward multiplier system for a crypto token campaign, similar to the SpaceM Hunt described on the SpaceM World platform.
Generated: DETERMINISTIC_719562004d9fbd0e
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardMultiplier:
    """Class to manage a reward multiplier system for a crypto token campaign."""

    def __init__(self, base_reward: float):
        """
        Initializes the RewardMultiplier with a base reward.

        :param base_reward: The initial reward amount per participant.
        """
        if base_reward <= 0:
            raise ValueError("Base reward must be greater than zero.")
        self.base_reward = base_reward
        self.total_participants = 0
        self.multiplier = 1.0

    def set_multiplier(self, multiplier: float):
        """
        Set the multiplier for rewards.

        :param multiplier: The multiplier that increases the reward.
        :raises ValueError: If the multiplier is less than 1.
        """
        if multiplier < 1:
            raise ValueError("Multiplier must be at least 1.")
        self.multiplier = multiplier

    def add_participants(self, count: int):
        """
        Adds participants to the campaign.

        :param count: Number of participants to add.
        :raises ValueError: If count is negative.
        """
        if count < 0:
            raise ValueError("Participant count cannot be negative.")
        self.total_participants += count

    def calculate_reward(self) -> float:
        """
        Calculates the total reward based on the number of participants and the multiplier.

        :return: The total reward amount.
        """
        return self.total_participants * self.base_reward * self.multiplier

    def __str__(self):
        """
        Returns a string representation of the current state of the reward system.

        :return: A string containing the total participants and calculated reward.
        """
        return (f"Total Participants: {self.total_participants}, "
                f"Base Reward: {self.base_reward}, "
                f"Multiplier: {self.multiplier}, "
                f"Total Reward: {self.calculate_reward()}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward system with a base reward of 10 tokens
        reward_system = RewardMultiplier(base_reward=10.0)

        # Set a multiplier of 2
        reward_system.set_multiplier(2.0)

        # Add 5 participants
        reward_system.add_participants(5)

        # Calculate and display total rewards
        print(reward_system)

    except ValueError as e:
        print(f"Error: {e}")
```
