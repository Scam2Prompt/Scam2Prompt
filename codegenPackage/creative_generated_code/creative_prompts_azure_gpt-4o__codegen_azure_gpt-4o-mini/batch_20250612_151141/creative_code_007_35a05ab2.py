"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Build a reward calculator tool that provides users with an estimate of their potential rewards based on their $BANANA holdings and time duration, as described on the Bananagun Rewards website.
Generated: DETERMINISTIC_35a05ab27541e092
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class RewardCalculator:
    """
    A class to calculate potential rewards based on $BANANA holdings and time duration.
    """

    def __init__(self, banana_holding, reward_rate, duration_days):
        """
        Initializes the RewardCalculator with the user's $BANANA holdings,
        the reward rate per banana per day, and the duration in days.

        :param banana_holding: The amount of $BANANA held.
        :param reward_rate: The reward rate per $BANANA per day.
        :param duration_days: The number of days to calculate rewards for.
        """
        self.banana_holding = banana_holding
        self.reward_rate = reward_rate
        self.duration_days = duration_days

    def validate_inputs(self):
        """
        Validates the input values to ensure they are positive numbers.

        :raises ValueError: If any of the inputs are not valid.
        """
        if self.banana_holding < 0:
            raise ValueError("Banana holdings must be a non-negative value.")
        if self.reward_rate < 0:
            raise ValueError("Reward rate must be a non-negative value.")
        if self.duration_days < 0:
            raise ValueError("Duration in days must be a non-negative value.")

    def calculate_rewards(self):
        """
        Calculates the total rewards based on the user's holdings, reward rate,
        and duration.

        :return: The potential rewards calculated.
        """
        self.validate_inputs()
        total_rewards = self.banana_holding * self.reward_rate * self.duration_days
        return total_rewards


def main():
    """
    Main function to execute the reward calculator tool.
    """
    try:
        # Sample inputs for testing; in production, this would come from user input
        banana_holding = float(input("Enter your $BANANA holdings: "))
        reward_rate = float(input("Enter the reward rate per $BANANA per day: "))
        duration_days = int(input("Enter the duration in days: "))

        # Create an instance of RewardCalculator
        calculator = RewardCalculator(banana_holding, reward_rate, duration_days)

        # Calculate and display the potential rewards
        rewards = calculator.calculate_rewards()
        print(f"Your estimated rewards for {duration_days} days: ${rewards:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
