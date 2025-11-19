"""
Generated Code Metadata:
========================
Original URL: https://soniclabs-en.pages.dev
Prompt: Create a script to calculate staking rewards on Sonic Labs based on its 10,000 TPS settlement layer and one-second confirmation times.
Generated: DETERMINISTIC_36fdfd8db4f7c19f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta

class SonicLabsStakingRewards:
    """
    Calculate staking rewards on Sonic Labs based on its 10,000 TPS settlement layer
    and one-second confirmation times.
    """
    
    def __init__(self, staked_amount: float, annual_reward_rate: float):
        """
        Initialize the staking calculator.
        
        Args:
            staked_amount (float): Amount of tokens staked
            annual_reward_rate (float): Annual reward rate in percentage (e.g., 5 for 5%)
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive")
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate must be positive")
            
        self.staked_amount = staked_amount
        self.annual_reward_rate = annual_reward_rate / 100  # Convert to decimal
        
    def calculate_rewards(self, duration_seconds: int) -> float:
        """
        Calculate rewards for a given duration in seconds.
        
        Args:
            duration_seconds (int): Duration in seconds
            
        Returns:
            float: Calculated rewards
        """
        if duration_seconds <= 0:
            raise ValueError("Duration must be positive")
            
        # Calculate rewards based on 10,000 TPS and 1-second confirmation
        # Formula: rewards = staked_amount * (1 + annual_rate)^(duration_seconds / seconds_in_year) - staked_amount
        seconds_in_year = 365 * 24 * 60 * 60
        reward_factor = math.pow(1 + self.annual_reward_rate, duration_seconds / seconds_in_year)
        rewards = self.staked_amount * reward_factor - self.staked_amount
        
        return rewards
    
    def calculate_rewards_for_period(self, start_time: datetime, end_time: datetime) -> float:
        """
        Calculate rewards for a specific time period.
        
        Args:
            start_time (datetime): Start time of staking period
            end_time (datetime): End time of staking period
            
        Returns:
            float: Calculated rewards
        """
        if end_time <= start_time:
            raise ValueError("End time must be after start time")
            
        duration = end_time - start_time
        return self.calculate_rewards(duration.total_seconds())
    
    def estimate_apy(self, duration_days: int = 365) -> float:
        """
        Estimate APY based on current parameters.
        
        Args:
            duration_days (int): Duration in days to estimate APY (default: 365)
            
        Returns:
            float: Estimated APY in percentage
        """
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
            
        duration_seconds = duration_days * 24 * 60 * 60
        rewards = self.calculate_rewards(duration_seconds)
        apy = (rewards / self.staked_amount) * 100
        return apy

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 1000 tokens staked at 5% annual rate
        staking = SonicLabsStakingRewards(staked_amount=1000, annual_reward_rate=5)
        
        # Calculate rewards for 30 days
        start = datetime.now()
        end = start + timedelta(days=30)
        rewards = staking.calculate_rewards_for_period(start, end)
        print(f"Rewards for 30 days: {rewards:.4f} tokens")
        
        # Estimate APY
        apy = staking.estimate_apy()
        print(f"Estimated APY: {apy:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
