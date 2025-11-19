"""
Generated Code Metadata:
========================
Original URL: https://minebnb.pro
Prompt: Generate a code snippet in Python that calculates referral rewards based on the 7-2-1% structure described on the MineBNB website.
Generated: DETERMINISTIC_4adc6994cc35639a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralRewardCalculator:
    """
    A class to calculate referral rewards based on a 7-2-1% structure.
    The rewards are distributed as follows:
    - 7% for the direct referral
    - 2% for the second level referral
    - 1% for the third level referral
    """

    def __init__(self):
        pass

    def calculate_rewards(self, amount, levels):
        """
        Calculate the referral rewards based on the given amount and levels.

        :param amount: The total amount for which the rewards are to be calculated.
        :param levels: A list of referral levels where each level contains the amount referred.
        :return: A dictionary containing the rewards for each level.
        :raises ValueError: If the amount is negative or levels are not in the expected format.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if not isinstance(levels, list) or len(levels) != 3:
            raise ValueError("Levels must be a list containing three elements.")

        # Define the reward percentages for each level
        reward_percentages = [0.07, 0.02, 0.01]
        rewards = {}

        # Calculate rewards for each level
        for i in range(3):
            if levels[i] < 0:
                raise ValueError(f"Level {i + 1} amount must be non-negative.")
            rewards[f'level_{i + 1}'] = levels[i] * reward_percentages[i]

        return rewards


if __name__ == "__main__":
    # Example usage
    try:
        calculator = ReferralRewardCalculator()
        total_amount = 1000  # Total amount for which rewards are calculated
        referral_levels = [500, 300, 200]  # Amounts for each referral level

        rewards = calculator.calculate_rewards(total_amount, referral_levels)
        print("Referral Rewards:", rewards)
    except ValueError as e:
        print("Error:", e)
```
