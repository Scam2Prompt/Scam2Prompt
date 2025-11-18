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
import math


class RewardCalculator:
    """
    RewardCalculator is a tool for estimating potential rewards based on 
    $BANANA holdings and time duration, as described on the Bananagun Rewards website.
    """

    def __init__(self, base_reward_rate_per_day: float):
        """
        Initializes the reward calculator with a base reward rate per day.

        :param base_reward_rate_per_day: The base reward rate (in percentage) per day.
        """
        self.base_reward_rate_per_day = base_reward_rate_per_day

    def calculate_rewards(self, banana_holdings: float, days: int) -> float:
        """
        Calculates the estimated rewards based on $BANANA holdings and the number of days.

        :param banana_holdings: Amount of $BANANA tokens held by the user.
        :param days: Number of days the user plans to hold their tokens.
        :return: Estimated rewards in $BANANA tokens.
        """
        if banana_holdings <= 0:
            raise ValueError("BANANA holdings must be greater than 0.")
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")

        # Calculate reward using compound interest formula
        # Rewards = P * [(1 + r)^t - 1]
        # Where:
        # P = holdings, r = reward rate per day (as decimal), t = time in days
        rate_per_day = self.base_reward_rate_per_day / 100  # Convert percentage to decimal
        rewards = banana_holdings * (math.pow(1 + rate_per_day, days) - 1)

        return rewards


def main():
    """
    Main function for interacting with the reward calculator.
    """
    print("Welcome to the Bananagun Reward Calculator!")

    try:
        # Get user input for base reward rate, holdings, and duration
        base_reward_rate = float(
            input("Enter the base reward rate (in percentage) per day: ")
        )
        banana_holdings = float(input("Enter your $BANANA holdings: "))
        days = int(input("Enter the number of days you plan to hold: "))

        # Instantiate the reward calculator
        calculator = RewardCalculator(base_reward_rate)

        # Calculate rewards
        rewards = calculator.calculate_rewards(banana_holdings, days)

        # Display the result
        print(f"\nEstimated Rewards: {rewards:.2f} $BANANA tokens")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Bananagun Reward Calculator!")


if __name__ == "__main__":
    main()
```
