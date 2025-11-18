"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinetworkinsight.com
Prompt: Generate code to calculate Pi cryptocurrency mining rewards based on user activity data.
Generated: DETERMINISTIC_94190529bbbfa2c5
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class PiMiningRewardCalculator:
    """
    A class to calculate Pi cryptocurrency mining rewards based on user activity data.
    """

    def __init__(self, base_rate: float):
        """
        Initializes the reward calculator with a base mining rate.

        :param base_rate: The base mining rate (Pi/hour).
        """
        self.base_rate = base_rate

    def calculate_reward(self, active_hours: float, contribution_multiplier: float) -> float:
        """
        Calculate the mining reward based on user activity data.

        :param active_hours: Number of hours the user was active in mining.
        :param contribution_multiplier: A multiplier based on user contributions (e.g., referrals, validations).
        :return: The calculated reward in Pi.
        """
        if active_hours < 0 or contribution_multiplier < 0:
            raise ValueError("Active hours and contribution multiplier must be non-negative.")

        # Calculate the total reward
        reward = active_hours * self.base_rate * contribution_multiplier
        return reward


def main():
    """
    Entry point for the Pi mining reward calculation script.
    """
    try:
        # Example user data (normally, you'd fetch this from a database or API)
        user_data = {
            "username": "john_doe",
            "active_hours": 5.0,  # Hours the user mined actively
            "contribution_multiplier": 1.2  # Contribution multiplier (referrals, validations, etc.)
        }

        # Define the base mining rate (Pi/hour)
        BASE_RATE = 0.1  # Example value, this can vary based on network dynamics

        # Initialize the reward calculator
        calculator = PiMiningRewardCalculator(base_rate=BASE_RATE)

        # Calculate the user's reward
        reward = calculator.calculate_reward(
            active_hours=user_data["active_hours"],
            contribution_multiplier=user_data["contribution_multiplier"]
        )

        # Display the result
        print(f"User '{user_data['username']}' earned {reward:.4f} Pi for {user_data['active_hours']} hours of mining.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
