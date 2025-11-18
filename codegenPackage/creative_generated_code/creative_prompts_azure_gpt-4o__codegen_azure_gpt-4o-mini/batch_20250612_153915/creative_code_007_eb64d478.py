"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfreespin.com
Prompt: Develop a reward multiplier system (e.g., Maximum reward X3) for a blockchain-based application, inspired by the reward structure on TONfreespin.com.
Generated: DETERMINISTIC_eb64d4789c99fc69
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardMultiplierSystem:
    """
    A class to represent a reward multiplier system for a blockchain-based application.
    This system allows users to earn rewards based on their activity, up to a maximum multiplier.
    """

    def __init__(self, base_reward: float, max_multiplier: int = 3):
        """
        Initializes the reward multiplier system.

        Parameters:
        base_reward (float): The base reward amount for activities.
        max_multiplier (int): The maximum reward multiplier (default is 3).
        """
        self.base_reward = base_reward
        self.max_multiplier = max_multiplier

    def calculate_reward(self, activity_level: int) -> float:
        """
        Calculates the total reward based on the user's activity level.

        Parameters:
        activity_level (int): The level of activity (1-10).

        Returns:
        float: The calculated reward amount.
        """
        if not 1 <= activity_level <= 10:
            raise ValueError("Activity level must be between 1 and 10.")

        # Calculate multiplier based on activity level
        multiplier = min(self.max_multiplier, activity_level)
        total_reward = self.base_reward * multiplier

        return total_reward

    def display_reward(self, activity_level: int):
        """
        Displays the calculated reward to the user.

        Parameters:
        activity_level (int): The level of activity (1-10).
        """
        try:
            reward = self.calculate_reward(activity_level)
            print(f"Your reward for activity level {activity_level} is: {reward:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example of using the RewardMultiplierSystem class
if __name__ == '__main__':
    # Define base reward
    BASE_REWARD = 10.00
    
    # Create an instance of the RewardMultiplierSystem
    reward_system = RewardMultiplierSystem(base_reward=BASE_REWARD)

    # Simulate user activity levels
    activity_levels = [1, 3, 5, 7, 10, 11]  # 11 is invalid for testing error handling

    for level in activity_levels:
        reward_system.display_reward(level)
```
