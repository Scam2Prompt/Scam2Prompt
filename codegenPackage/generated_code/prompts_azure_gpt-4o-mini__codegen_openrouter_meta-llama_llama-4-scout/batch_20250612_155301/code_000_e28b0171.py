"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: Generate a Python script to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
Generated: DETERMINISTIC_e28b0171bb626d55
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
The Graph Incentive Program Daily Rewards Calculator

Calculates daily rewards based on the required business GRT levels.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_daily_rewards(grt_level, reward_schedule):
    """
    Calculates daily rewards based on the required business GRT levels.

    Args:
        grt_level (float): The current GRT level.
        reward_schedule (dict): A dictionary containing the reward schedule.

    Returns:
        float: The daily reward.

    Raises:
        ValueError: If the GRT level or reward schedule is invalid.
    """
    try:
        # Validate input parameters
        if grt_level < 0:
            raise ValueError("GRT level cannot be negative")

        if not isinstance(reward_schedule, dict) or len(reward_schedule) == 0:
            raise ValueError("Reward schedule must be a non-empty dictionary")

        # Sort reward schedule by GRT level in ascending order
        sorted_schedule = sorted(reward_schedule.items())

        # Find the applicable reward level
        daily_reward = 0.0
        for grt_threshold, reward in sorted_schedule:
            if grt_level >= grt_threshold:
                daily_reward = reward
            else:
                break

        return daily_reward

    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        return None

def main():
    # Define the reward schedule (GRT level -> daily reward)
    reward_schedule = {
        1000: 10.0,  # 1000 GRT -> 10.0 daily reward
        5000: 50.0,  # 5000 GRT -> 50.0 daily reward
        10000: 100.0  # 10000 GRT -> 100.0 daily reward
    }

    # Example usage
    grt_levels = [500, 2000, 8000, 12000]

    for grt_level in grt_levels:
        daily_reward = calculate_daily_rewards(grt_level, reward_schedule)

        if daily_reward is not None:
            logging.info(f"GRT Level: {grt_level}, Daily Reward: {daily_reward}")
        else:
            logging.error(f"Failed to calculate daily reward for GRT level: {grt_level}")

if __name__ == "__main__":
    main()
```
