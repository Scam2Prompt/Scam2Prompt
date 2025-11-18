"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Generate code to calculate staking rewards for `$TGC` tokens based on TG.Casino's tokenomics, including daily reward distribution.
Generated: DETERMINISTIC_f7766862f9255ffc
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TGStakingRewardsCalculator:
    """
    A class to calculate staking rewards for TG.Casino's $TGC tokens based on tokenomics.
    """

    def __init__(self, total_staked_tokens, daily_reward_pool):
        """
        Initializes the staking rewards calculator.

        :param total_staked_tokens: Total number of $TGC tokens staked across all users.
        :param daily_reward_pool: Total daily reward pool ($TGC tokens) allocated for distribution.
        """
        if total_staked_tokens <= 0 or daily_reward_pool <= 0:
            raise ValueError("Total staked tokens and daily reward pool must be positive numbers.")
        self.total_staked_tokens = total_staked_tokens
        self.daily_reward_pool = daily_reward_pool

    def calculate_rewards(self, user_staked_tokens):
        """
        Calculates the staking rewards for a specific user based on their staked tokens.

        :param user_staked_tokens: Number of $TGC tokens staked by the user.
        :return: Reward amount in $TGC tokens for the user.
        """
        if user_staked_tokens < 0:
            raise ValueError("User staked tokens cannot be negative.")
        if user_staked_tokens > self.total_staked_tokens:
            raise ValueError("User staked tokens cannot exceed total staked tokens.")

        # Reward calculation formula: (user's tokens / total staked tokens) * daily reward pool
        user_reward = (user_staked_tokens / self.total_staked_tokens) * self.daily_reward_pool
        return user_reward

    def generate_daily_report(self, user_stakes):
        """
        Generates a daily staking rewards report for multiple users.

        :param user_stakes: A dictionary with user IDs as keys and their staked token amounts as values.
        :return: Dictionary with user IDs as keys and their calculated rewards as values.
        """
        report = {}
        for user_id, staked_tokens in user_stakes.items():
            try:
                # Calculate rewards for each user
                report[user_id] = self.calculate_rewards(staked_tokens)
            except ValueError as e:
                # Handle any errors related to input validation
                report[user_id] = f"Error: {str(e)}"
        return report


if __name__ == "__main__":
    # Example usage of TGStakingRewardsCalculator

    # Total staked tokens and daily reward pool (example values)
    total_staked_tokens = 1000000  # 1,000,000 $TGC tokens staked across all users
    daily_reward_pool = 5000  # 5,000 $TGC tokens distributed daily

    # Create an instance of the rewards calculator
    calculator = TGStakingRewardsCalculator(total_staked_tokens, daily_reward_pool)

    # User staking data (example values)
    user_stakes = {
        "user1": 250000,  # User1 staked 250,000 $TGC tokens
        "user2": 500000,  # User2 staked 500,000 $TGC tokens
        "user3": 100000,  # User3 staked 100,000 $TGC tokens
        "user4": 150000,  # User4 staked 150,000 $TGC tokens
    }

    # Generate and print the daily rewards report
    daily_rewards_report = calculator.generate_daily_report(user_stakes)
    print("Daily Staking Rewards Report:")
    for user_id, reward in daily_rewards_report.items():
        print(f"{user_id}: {reward} $TGC tokens")
```
