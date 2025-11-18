"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: Generate code that calculates weekly SOL rewards distribution based on Loud's fee split mechanics (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_10eec396ae1bcce2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardDistribution:
    """
    A class to handle the distribution of weekly SOL rewards based on Loud's fee split mechanics.
    The distribution percentage is defined as:
    - sKAITO: 72%
    - Creator: 18%
    - Weekly SOL Distribution: 10%
    """

    def __init__(self, total_rewards: float):
        """
        Initializes the RewardDistribution with the total rewards.

        :param total_rewards: The total amount of SOL rewards to be distributed.
        :raises ValueError: If total_rewards is negative.
        """
        if total_rewards < 0:
            raise ValueError("Total rewards must be a non-negative value.")
        self.total_rewards = total_rewards
        self.skaito_percentage = 0.72
        self.creator_percentage = 0.18
        self.weekly_distribution_percentage = 0.10

    def calculate_distribution(self):
        """
        Calculate the distribution of rewards based on the defined percentages.

        :return: A dictionary containing the distribution amounts for sKAITO, Creator, and Weekly SOL.
        """
        ska_to_rewards = self.total_rewards * self.skaito_percentage
        creator_rewards = self.total_rewards * self.creator_percentage
        weekly_sol_distribution = self.total_rewards * self.weekly_distribution_percentage

        return {
            "sKAITO": ska_to_rewards,
            "Creator": creator_rewards,
            "Weekly SOL Distribution": weekly_sol_distribution
        }

    def display_distribution(self):
        """
        Displays the calculated distribution of rewards in a formatted manner.
        """
        try:
            distribution = self.calculate_distribution()
            print("Weekly SOL Rewards Distribution:")
            for key, value in distribution.items():
                print(f"{key}: {value:.2f} SOL")
        except Exception as e:
            print(f"An error occurred while calculating the distribution: {e}")


# Example usage
if __name__ == "__main__":
    try:
        total_rewards = float(input("Enter the total rewards to distribute (in SOL): "))
        rewards_distribution = RewardDistribution(total_rewards)
        rewards_distribution.display_distribution()
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
