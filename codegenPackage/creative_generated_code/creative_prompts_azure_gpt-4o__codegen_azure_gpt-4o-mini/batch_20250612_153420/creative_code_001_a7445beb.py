"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropxdao.web.app
Prompt: Create a function that calculates rewards in $TNSR tokens based on user activity metrics on a Solana-based NFT trading platform like the one described on the Tensor webpage.
Generated: DETERMINISTIC_a7445beb3a3f50db
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for monitoring and debugging
logging.basicConfig(level=logging.INFO)

class RewardCalculator:
    """
    A class to calculate rewards in $TNSR tokens based on user activity metrics.
    """

    def __init__(self, base_reward: float, activity_multiplier: float):
        """
        Initializes the RewardCalculator with base reward and activity multiplier.

        Parameters:
        - base_reward (float): The base amount of TNSR tokens rewarded for participation.
        - activity_multiplier (float): Multiplier based on activity metrics (e.g., trades, listings).
        """
        if base_reward < 0 or activity_multiplier < 0:
            raise ValueError("Base reward and activity multiplier must be non-negative.")

        self.base_reward = base_reward
        self.activity_multiplier = activity_multiplier

    def calculate_rewards(self, num_trades: int, num_listings: int) -> float:
        """
        Calculates the total rewards based on user activity metrics.

        Parameters:
        - num_trades (int): Number of trades executed by the user.
        - num_listings (int): Number of NFTs listed by the user.

        Returns:
        - float: Total rewards in $TNSR tokens.

        Raises:
        - ValueError: If the number of trades or listings is negative.
        """
        if num_trades < 0 or num_listings < 0:
            raise ValueError("Number of trades and listings must be non-negative.")
        
        logging.info(f"Calculating rewards for {num_trades} trades and {num_listings} listings.")

        # Calculate activity score based on trades and listings
        activity_score = self.activity_multiplier * (num_trades + num_listings)

        # Calculate total rewards
        total_rewards = self.base_reward + activity_score
        logging.info(f"Total rewards calculated: {total_rewards} TNSR tokens.")

        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the RewardCalculator with sample base reward and multiplier
        reward_calculator = RewardCalculator(base_reward=10.0, activity_multiplier=2.5)

        # Calculate rewards for a user with specific activity
        rewards = reward_calculator.calculate_rewards(num_trades=5, num_listings=3)
        print(f"User is rewarded with {rewards} TNSR tokens.")
    except ValueError as e:
        logging.error(f"Error calculating rewards: {e}")
```
