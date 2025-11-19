"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exoticdao.web.app
Prompt: Develop a script that calculates the total rewards in $TNSR tokens based on user activity on the Exotic DAO platform.
Generated: DETERMINISTIC_97521cbbc7c89270
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ExoticDAORewardsCalculator:
    """
    A class to calculate the total rewards in $TNSR tokens based on user activity
    on the Exotic DAO platform.
    """

    def __init__(self, reward_rate_per_activity: float):
        """
        Initialize the rewards calculator.
        
        :param reward_rate_per_activity: The number of $TNSR tokens rewarded per activity unit (float).
        """
        self.reward_rate_per_activity = reward_rate_per_activity

    def calculate_rewards(self, activity_data: dict) -> float:
        """
        Calculate the total rewards in $TNSR tokens based on user activity data.

        :param activity_data: A dictionary where keys are user IDs and values are activity counts (int).
        :return: Total rewards in $TNSR tokens (float).
        :raises ValueError: If activity_data contains invalid values.
        """
        total_rewards = 0.0

        for user_id, activity_count in activity_data.items():
            if not isinstance(activity_count, int) or activity_count < 0:
                raise ValueError(f"Invalid activity count for user {user_id}: {activity_count}")
            total_rewards += activity_count * self.reward_rate_per_activity

        return total_rewards


def main():
    # Load activity data from a JSON file
    activity_file = "activity_data.json"
    try:
        with open(activity_file, "r") as file:
            activity_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {activity_file} not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse {activity_file} - {e}")
        return

    # Initialize the rewards calculator with a reward rate
    reward_rate_per_activity = 0.5  # Example: 0.5 $TNSR tokens per activity unit
    calculator = ExoticDAORewardsCalculator(reward_rate_per_activity)

    try:
        # Calculate total rewards based on the activity data
        total_rewards = calculator.calculate_rewards(activity_data)
        print(f"Total rewards in $TNSR tokens: {total_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
