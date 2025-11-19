"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Generate a Python script to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
Generated: DETERMINISTIC_e28b0171bb626d55
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GraphIncentiveProgram:
    """
    A class to calculate daily rewards based on required GRT levels for The Graph's incentive program.
    """

    def __init__(self, base_reward: float, reward_multiplier: float):
        """
        Initializes the program with base reward and multiplier.

        Parameters:
            base_reward (float): The base reward amount for the incentive.
            reward_multiplier (float): The multiplier applied to the rewards based on GRT levels.
        """
        self.base_reward = base_reward
        self.reward_multiplier = reward_multiplier

    def calculate_daily_reward(self, grt_level: float) -> float:
        """
        Calculates the daily reward based on the GRT level.

        Parameters:
            grt_level (float): The required GRT level for calculating rewards.

        Returns:
            float: The calculated daily reward.

        Raises:
            ValueError: If the GRT level is negative.
        """
        if grt_level < 0:
            logging.error("GRT level cannot be negative.")
            raise ValueError("GRT level must be non-negative.")

        # Calculate daily reward
        daily_reward = self.base_reward + (grt_level * self.reward_multiplier)
        logging.info(f"Calculated daily reward: {daily_reward} for GRT level: {grt_level}")
        return daily_reward


def main():
    """
    The main function to execute the reward calculation.
    """
    try:
        # Example parameters for the incentive program
        base_reward = 10.0  # Base reward amount
        reward_multiplier = 0.05  # Reward multiplier per GRT level

        # Initialize the incentive program
        program = GraphIncentiveProgram(base_reward, reward_multiplier)

        # Example GRT levels for testing
        grt_levels = [100, 200, 300, -50]  # Negative value for error handling demonstration

        for level in grt_levels:
            try:
                reward = program.calculate_daily_reward(level)
                print(f"Daily reward for GRT level {level}: {reward}")
            except ValueError as e:
                print(f"Error calculating reward for GRT level {level}: {e}")

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
