"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Generate code to implement a reward multiplier system for a crypto token campaign, similar to the SpaceM Hunt described on the SpaceM World platform.
Generated: DETERMINISTIC_719562004d9fbd0e
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RewardMultiplier:
    """
    A class to implement a reward multiplier system for a crypto token campaign.
    """

    def __init__(self):
        """
        Initializes the RewardMultiplier with default values.
        """
        self.base_reward = 10  # Base reward for participation
        self.multiplier = 1.0   # Default multiplier
        self.participants = {}   # Dictionary to hold participant rewards

    def set_multiplier(self, new_multiplier):
        """
        Sets a new multiplier for the rewards.

        Args:
            new_multiplier (float): The new multiplier value.

        Raises:
            ValueError: If the new multiplier is less than 1.
        """
        if new_multiplier < 1:
            raise ValueError("Multiplier must be at least 1.")
        self.multiplier = new_multiplier

    def add_participant(self, participant_id):
        """
        Adds a participant to the reward system.

        Args:
            participant_id (str): Unique identifier for the participant.

        Raises:
            ValueError: If the participant ID already exists.
        """
        if participant_id in self.participants:
            raise ValueError("Participant already exists.")
        self.participants[participant_id] = 0  # Initialize reward to 0

    def calculate_reward(self, participant_id):
        """
        Calculates the reward for a given participant based on the current multiplier.

        Args:
            participant_id (str): Unique identifier for the participant.

        Returns:
            float: The calculated reward.

        Raises:
            KeyError: If the participant ID does not exist.
        """
        if participant_id not in self.participants:
            raise KeyError("Participant not found.")
        reward = self.base_reward * self.multiplier
        self.participants[participant_id] += reward
        return reward

    def get_participant_reward(self, participant_id):
        """
        Retrieves the total reward for a given participant.

        Args:
            participant_id (str): Unique identifier for the participant.

        Returns:
            float: The total reward for the participant.

        Raises:
            KeyError: If the participant ID does not exist.
        """
        if participant_id not in self.participants:
            raise KeyError("Participant not found.")
        return self.participants[participant_id]

    def reset_rewards(self):
        """
        Resets all participant rewards to zero.
        """
        for participant_id in self.participants:
            self.participants[participant_id] = 0

# Example usage
if __name__ == "__main__":
    try:
        reward_system = RewardMultiplier()
        reward_system.set_multiplier(2.0)  # Set multiplier to 2
        reward_system.add_participant("user123")
        reward = reward_system.calculate_reward("user123")
        print(f"Reward for user123: {reward}")
        total_reward = reward_system.get_participant_reward("user123")
        print(f"Total reward for user123: {total_reward}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
