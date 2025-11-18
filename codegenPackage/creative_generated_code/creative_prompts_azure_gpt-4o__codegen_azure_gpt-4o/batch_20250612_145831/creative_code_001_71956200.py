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
import datetime

class RewardMultiplierSystem:
    """
    A class to implement a reward multiplier system for a crypto token campaign.
    """

    def __init__(self, base_reward: float):
        """
        Initialize the reward multiplier system with a base reward.

        :param base_reward: The base reward for the campaign (float).
        """
        if base_reward <= 0:
            raise ValueError("Base reward must be greater than zero.")
        self.base_reward = base_reward
        self.multipliers = []

    def add_multiplier(self, start_date: str, end_date: str, multiplier: float):
        """
        Add a reward multiplier for a specific campaign period.

        :param start_date: The start date of the multiplier period (YYYY-MM-DD).
        :param end_date: The end date of the multiplier period (YYYY-MM-DD).
        :param multiplier: The multiplier value for the reward.
        """
        try:
            start_date_parsed = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_parsed = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in the format YYYY-MM-DD.")
        
        if start_date_parsed >= end_date_parsed:
            raise ValueError("Start date must be before end date.")
        
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than zero.")

        # Store the multiplier configuration
        self.multipliers.append({
            "start_date": start_date_parsed,
            "end_date": end_date_parsed,
            "multiplier": multiplier
        })

    def calculate_reward(self, current_date: str) -> float:
        """
        Calculate the reward for a given date based on the active multipliers.

        :param current_date: The date for which the reward should be calculated (YYYY-MM-DD).
        :return: The calculated reward (float).
        """
        try:
            current_date_parsed = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Current date must be in the format YYYY-MM-DD.")
        
        # Default reward is the base reward
        reward = self.base_reward

        # Check for any active multipliers
        for multiplier in self.multipliers:
            if multiplier["start_date"] <= current_date_parsed <= multiplier["end_date"]:
                reward *= multiplier["multiplier"]
        
        return reward


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the reward system with a base reward of 100 tokens
        reward_system = RewardMultiplierSystem(base_reward=100)

        # Add multipliers for specific campaign periods
        reward_system.add_multiplier("2023-10-01", "2023-10-10", 1.5)  # 50% extra reward
        reward_system.add_multiplier("2023-12-01", "2023-12-25", 2.0)  # Double the reward

        # Calculate reward for a specific date
        current_date = "2023-10-05"
        calculated_reward = reward_system.calculate_reward(current_date)
        print(f"Reward on {current_date}: {calculated_reward} tokens")

        # Test for a date outside of campaign periods
        current_date = "2024-01-01"
        calculated_reward = reward_system.calculate_reward(current_date)
        print(f"Reward on {current_date}: {calculated_reward} tokens")

    except Exception as e:
        print(f"Error: {e}")
```
