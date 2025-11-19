"""
Generated Code Metadata:
========================
Original URL: https://claimdoge20live.pages.dev
Prompt: "Design a staking rewards calculator for Dogecoin20 that takes into account the user's staked balance, percentage of the pool, and current annual returns percentage."
Generated: DETERMINISTIC_542974c041eccf1c
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Dogecoin20StakingCalculator:
    """
    A calculator for estimating staking rewards in Dogecoin20.
    
    Attributes:
        total_pool_tokens (float): Total tokens staked in the pool.
        annual_return_percent (float): Annual return percentage for staking.
    """
    
    def __init__(self, total_pool_tokens: float, annual_return_percent: float):
        """
        Initialize the staking calculator with pool details.
        
        Args:
            total_pool_tokens: Total tokens staked in the pool.
            annual_return_percent: Annual return percentage (e.g., 5 for 5%).
            
        Raises:
            ValueError: If total_pool_tokens or annual_return_percent is negative.
        """
        if total_pool_tokens < 0:
            raise ValueError("Total pool tokens cannot be negative.")
        if annual_return_percent < 0:
            raise ValueError("Annual return percentage cannot be negative.")
            
        self.total_pool_tokens = total_pool_tokens
        self.annual_return_percent = annual_return_percent
    
    def calculate_daily_rewards(self, user_staked_tokens: float) -> float:
        """
        Calculate daily staking rewards for a user based on their stake.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            
        Returns:
            float: Daily rewards in tokens.
            
        Raises:
            ValueError: If user_staked_tokens is negative.
        """
        if user_staked_tokens < 0:
            raise ValueError("User staked tokens cannot be negative.")
            
        if self.total_pool_tokens == 0:
            return 0.0
            
        user_pool_percentage = user_staked_tokens / self.total_pool_tokens
        annual_rewards = user_pool_percentage * (self.annual_return_percent / 100) * self.total_pool_tokens
        daily_rewards = annual_rewards / 365
        return daily_rewards
    
    def calculate_weekly_rewards(self, user_staked_tokens: float) -> float:
        """
        Calculate weekly staking rewards for a user based on their stake.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            
        Returns:
            float: Weekly rewards in tokens.
        """
        daily_rewards = self.calculate_daily_rewards(user_staked_tokens)
        return daily_rewards * 7
    
    def calculate_monthly_rewards(self, user_staked_tokens: float) -> float:
        """
        Calculate monthly (30-day) staking rewards for a user based on their stake.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            
        Returns:
            float: Monthly rewards in tokens.
        """
        daily_rewards = self.calculate_daily_rewards(user_staked_tokens)
        return daily_rewards * 30
    
    def calculate_annual_rewards(self, user_staked_tokens: float) -> float:
        """
        Calculate annual staking rewards for a user based on their stake.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            
        Returns:
            float: Annual rewards in tokens.
        """
        if user_staked_tokens < 0:
            raise ValueError("User staked tokens cannot be negative.")
            
        if self.total_pool_tokens == 0:
            return 0.0
            
        user_pool_percentage = user_staked_tokens / self.total_pool_tokens
        annual_rewards = user_pool_percentage * (self.annual_return_percent / 100) * self.total_pool_tokens
        return annual_rewards
    
    def calculate_rewards_for_period(self, user_staked_tokens: float, days: int) -> float:
        """
        Calculate staking rewards for a custom period in days.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            days: Number of days to calculate rewards for.
            
        Returns:
            float: Rewards for the specified period in tokens.
            
        Raises:
            ValueError: If days is negative.
        """
        if days < 0:
            raise ValueError("Days cannot be negative.")
            
        daily_rewards = self.calculate_daily_rewards(user_staked_tokens)
        return daily_rewards * days
    
    def get_user_pool_percentage(self, user_staked_tokens: float) -> float:
        """
        Get the user's percentage of the total staking pool.
        
        Args:
            user_staked_tokens: Amount of tokens staked by the user.
            
        Returns:
            float: Percentage of the pool owned by user (0-100).
            
        Raises:
            ValueError: If user_staked_tokens is negative.
        """
        if user_staked_tokens < 0:
            raise ValueError("User staked tokens cannot be negative.")
            
        if self.total_pool_tokens == 0:
            return 0.0
            
        return (user_staked_tokens / self.total_pool_tokens) * 100


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with total pool tokens and annual return percentage
        calculator = Dogecoin20StakingCalculator(
            total_pool_tokens=1000000.0,
            annual_return_percent=5.0
        )
        
        # User's staked tokens
        user_stake = 5000.0
        
        # Calculate and display rewards
        print(f"User's pool percentage: {calculator.get_user_pool_percentage(user_stake):.2f}%")
        print(f"Daily rewards: {calculator.calculate_daily_rewards(user_stake):.2f} DOGE20")
        print(f"Weekly rewards: {calculator.calculate_weekly_rewards(user_stake):.2f} DOGE20")
        print(f"Monthly rewards: {calculator.calculate_monthly_rewards(user_stake):.2f} DOGE20")
        print(f"Annual rewards: {calculator.calculate_annual_rewards(user_stake):.2f} DOGE20")
        print(f"30-day rewards: {calculator.calculate_rewards_for_period(user_stake, 30):.2f} DOGE20")
        
    except ValueError as e:
        print(f"Error: {e}")
```
