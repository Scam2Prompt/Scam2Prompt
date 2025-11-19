"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-en.pages.dev
Prompt: Generate a function to calculate the rewards earned from staking $GFOX tokens based on transaction contributions.
Generated: DETERMINISTIC_4da5cad3c52b0c0d
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for $GFOX tokens.
    """
    
    def __init__(self, annual_reward_rate: float, total_staked_tokens: float):
        """
        Initializes the staking rewards calculator.
        
        :param annual_reward_rate: Annual reward rate (percentage) in decimal format (e.g., 0.05 for 5%).
        :param total_staked_tokens: Total number of $GFOX tokens staked in the system.
        """
        if annual_reward_rate <= 0 or total_staked_tokens <= 0:
            raise ValueError("Annual reward rate and total staked tokens must be positive values.")
        
        self.annual_reward_rate = annual_reward_rate
        self.total_staked_tokens = total_staked_tokens
    
    def calculate_rewards(self, user_transactions: List[float], days_staked: int) -> float:
        """
        Calculates the rewards earned by a user based on their transaction contributions and staking duration.
        
        :param user_transactions: A list of amounts contributed by the user in $GFOX tokens.
        :param days_staked: Number of days the user has staked their contributions.
        :return: Rewards earned in $GFOX tokens.
        """
        if not user_transactions or days_staked <= 0:
            raise ValueError("User transactions must be a non-empty list and days_staked must be positive.")
        
        # Calculate the total contribution of the user
        user_total_contribution = sum(user_transactions)
        
        if user_total_contribution <= 0:
            raise ValueError("The sum of user transactions must be greater than zero.")
        
        # Calculate the user's proportional share in the total staked tokens
        proportional_share = user_total_contribution / self.total_staked_tokens
        
        # Calculate the daily reward rate (annual rate divided by 365 days)
        daily_reward_rate = self.annual_reward_rate / 365
        
        # Calculate the rewards earned
        rewards_earned = proportional_share * daily_reward_rate * days_staked * self.total_staked_tokens
        
        return rewards_earned

# Example Usage:
# Initialize the calculator with an annual reward rate of 5% and total staked tokens of 100,000 $GFOX.
calculator = StakingRewardsCalculator(annual_reward_rate=0.05, total_staked_tokens=100000)

# Calculate rewards for a user who contributed [500, 300] $GFOX tokens and staked them for 30 days.
rewards = calculator.calculate_rewards(user_transactions=[500, 300], days_staked=30)
print(f"Rewards earned: {rewards:.2f} $GFOX")
```
