"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vlaunch-io.web.app
Prompt: Create a function to calculate VPAD rewards dynamically, factoring in lockup duration and yearly reward percentages as described on VLaunch.
Generated: DETERMINISTIC_17c10fed3dcb61ba
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VPADRewardCalculator:
    """
    A class to calculate VPAD rewards based on lockup duration and yearly reward percentages.
    """

    def __init__(self, yearly_reward_percentage):
        """
        Initializes the calculator with the yearly reward percentage.

        :param yearly_reward_percentage: The percentage of rewards to be given yearly (in decimal form, e.g., 0.10 for 10%)
        """
        if not (0 <= yearly_reward_percentage <= 1):
            raise ValueError("Yearly reward percentage must be between 0 and 1.")
        
        self.yearly_reward_percentage = yearly_reward_percentage

    def calculate_rewards(self, locked_amount, lockup_duration_years):
        """
        Calculate the total rewards based on locked amount and lockup duration.

        :param locked_amount: The amount of VPAD tokens locked.
        :param lockup_duration_years: The duration in years for which the tokens are locked.
        :return: The total rewards earned after the lockup period.
        """
        if locked_amount < 0:
            raise ValueError("Locked amount must be non-negative.")
        if lockup_duration_years < 0:
            raise ValueError("Lockup duration must be non-negative.")

        # Calculate total rewards
        total_rewards = locked_amount * self.yearly_reward_percentage * lockup_duration_years
        return total_rewards

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the reward calculator with a 10% yearly reward
        reward_calculator = VPADRewardCalculator(yearly_reward_percentage=0.10)

        # Example values for locked amount and lockup duration
        locked_amount = 1000  # 1000 VPAD tokens
        lockup_duration_years = 2  # 2 years

        # Calculate the rewards
        rewards = reward_calculator.calculate_rewards(locked_amount, lockup_duration_years)
        print(f"Total rewards earned: {rewards} VPAD tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
