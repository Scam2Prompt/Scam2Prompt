"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfts.web.app
Prompt: Create a function that calculates rewards in $TNSR tokens based on user activity metrics, as described on the Tensor NFT trading platform.
Generated: DETERMINISTIC_b27b6d0c158ae6ca
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardCalculator:
    """
    A class to calculate rewards in TNSR tokens based on user activity metrics.
    """

    def __init__(self, base_reward: float, activity_weights: dict):
        """
        Initializes the RewardCalculator with a base reward and activity weights.

        :param base_reward: The base reward value for calculations.
        :param activity_weights: A dictionary mapping activity types to their weights.
        """
        self.base_reward = base_reward
        self.activity_weights = activity_weights

    def calculate_rewards(self, user_activity: dict) -> float:
        """
        Calculates the total rewards in TNSR tokens based on user activity.

        :param user_activity: A dictionary containing user activity metrics.
        :return: The calculated rewards in TNSR tokens.
        :raises ValueError: If the user_activity is missing a required activity type.
        """
        total_reward = 0.0

        # Iterate over each activity type and calculate rewards
        for activity_type, count in user_activity.items():
            if activity_type not in self.activity_weights:
                raise ValueError(f"Activity type '{activity_type}' is not recognized.")

            # Calculate reward for the current activity type
            activity_reward = count * self.activity_weights[activity_type] * self.base_reward
            total_reward += activity_reward

        return total_reward


if __name__ == "__main__":
    # Example usage
    # Define the base reward and activity weights
    base_reward = 1.0  # Base reward for each unit of activity
    activity_weights = {
        'buy': 2.0,      # Weight for buy activity
        'sell': 1.5,     # Weight for sell activity
        'trade': 1.2,    # Weight for trade activity
        'hold': 0.5      # Weight for hold activity
    }

    # Create a RewardCalculator instance
    reward_calculator = RewardCalculator(base_reward, activity_weights)

    # Example user activity metrics
    user_activity = {
        'buy': 10,      # User bought 10 NFTs
        'sell': 5,      # User sold 5 NFTs
        'trade': 3      # User traded 3 NFTs
    }

    try:
        # Calculate and print the total rewards
        total_rewards = reward_calculator.calculate_rewards(user_activity)
        print(f"Total TNSR rewards: {total_rewards}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
