"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minthidden.web.app
Prompt: Write code to implement dynamic rewards based on user activity or level status, as referenced in the "My rewards" section of the website.
Generated: DETERMINISTIC_e372b497d5b67d48
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: dynamic_rewards.py

import logging

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Reward tiers based on user levels or activity points
REWARD_TIERS = {
    "Bronze": {"min_points": 0, "reward": "5% Discount Coupon"},
    "Silver": {"min_points": 100, "reward": "10% Discount Coupon"},
    "Gold": {"min_points": 500, "reward": "20% Discount Coupon"},
    "Platinum": {"min_points": 1000, "reward": "Free Product"},
}

def get_user_reward(activity_points):
    """
    Determine the reward for a user based on their activity points.

    Args:
        activity_points (int): The user's activity points.

    Returns:
        str: The reward for the user.
    """
    try:
        # Validate input
        if not isinstance(activity_points, int) or activity_points < 0:
            raise ValueError("Activity points must be a non-negative integer.")

        # Determine the appropriate reward tier
        for tier, data in sorted(REWARD_TIERS.items(), key=lambda x: x[1]["min_points"], reverse=True):
            if activity_points >= data["min_points"]:
                logging.info(f"User qualifies for {tier} tier with {activity_points} points.")
                return data["reward"]

        # Default case: No reward
        return "No Reward"
    except Exception as e:
        logging.error(f"Error determining user reward: {e}")
        return "Error: Unable to determine reward."

def main():
    """
    Main function to demonstrate dynamic reward allocation.
    """
    try:
        # Simulated user activity points (this would typically come from a database or API)
        user_points = [50, 150, 600, 1200, -10]

        for points in user_points:
            print(f"Activity Points: {points}, Reward: {get_user_reward(points)}")
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")

# Run the script if executed directly
if __name__ == "__main__":
    main()
```
