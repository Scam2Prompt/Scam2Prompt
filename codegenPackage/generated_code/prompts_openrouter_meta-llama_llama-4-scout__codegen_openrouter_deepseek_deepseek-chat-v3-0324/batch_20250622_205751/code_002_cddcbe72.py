"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Generate code to implement a reward calculator for $BANANA token holders, taking into account the APR, time ranges, and Solana rewards.
Generated: DETERMINISTIC_cddcbe72c86e19bd
Batch ID: 20250622_205751
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
from typing import Optional, List, Tuple

class BananaRewardCalculator:
    """
    A reward calculator for $BANANA token holders that calculates rewards based on APR,
    staking duration, and Solana rewards distribution.
    """
    
    def __init__(self, apr: float, solana_rewards_per_day: float):
        """
        Initialize the reward calculator with APR and Solana rewards rate.
        
        Args:
            apr: Annual Percentage Rate (e.g., 0.1 for 10%)
            solana_rewards_per_day: Amount of Solana rewards distributed per day
        """
        if apr <= 0:
            raise ValueError("APR must be positive")
        if solana_rewards_per_day < 0:
            raise ValueError("Solana rewards must be non-negative")
            
        self.apr = apr
        self.solana_rewards_per_day = solana_rewards_per_day
    
    def calculate_banana_rewards(
        self,
        stake_amount: float,
        start_date: datetime,
        end_date: datetime,
        current_date: Optional[datetime] = None
    ) -> float:
        """
        Calculate $BANANA rewards for a given stake amount and time period.
        
        Args:
            stake_amount: Amount of $BANANA tokens staked
            start_date: When the stake was initiated
            end_date: When the stake period ends
            current_date: Optional date to calculate rewards up to (defaults to now)
            
        Returns:
            Amount of $BANANA rewards earned
        """
        if stake_amount <= 0:
            raise ValueError("Stake amount must be positive")
        if end_date <= start_date:
            raise ValueError("End date must be after start date")
            
        current_date = current_date or datetime.now()
        if current_date < start_date:
            return 0.0
            
        effective_end_date = min(end_date, current_date)
        days_staked = (effective_end_date - start_date).days
        
        if days_staked <= 0:
            return 0.0
            
        daily_rate = self.apr / 365
        rewards = stake_amount * daily_rate * days_staked
        return rewards
    
    def calculate_solana_rewards(
        self,
        stake_amount: float,
        total_staked: float,
        start_date: datetime,
        end_date: datetime,
        current_date: Optional[datetime] = None
    ) -> float:
        """
        Calculate Solana rewards based on stake proportion and duration.
        
        Args:
            stake_amount: Amount of $BANANA tokens staked
            total_staked: Total amount of $BANANA staked in the pool
            start_date: When the stake was initiated
            end_date: When the stake period ends
            current_date: Optional date to calculate rewards up to (defaults to now)
            
        Returns:
            Amount of Solana rewards earned
        """
        if stake_amount <= 0:
            raise ValueError("Stake amount must be positive")
        if total_staked <= 0:
            raise ValueError("Total staked must be positive")
        if end_date <= start_date:
            raise ValueError("End date must be after start date")
            
        current_date = current_date or datetime.now()
        if current_date < start_date:
            return 0.0
            
        effective_end_date = min(end_date, current_date)
        days_staked = (effective_end_date - start_date).days
        
        if days_staked <= 0:
            return 0.0
            
        stake_proportion = stake_amount / total_staked
        rewards = self.solana_rewards_per_day * days_staked * stake_proportion
        return rewards
    
    def calculate_total_rewards(
        self,
        stake_amount: float,
        total_staked: float,
        start_date: datetime,
        end_date: datetime,
        current_date: Optional[datetime] = None
    ) -> Tuple[float, float]:
        """
        Calculate both $BANANA and Solana rewards.
        
        Args:
            stake_amount: Amount of $BANANA tokens staked
            total_staked: Total amount of $BANANA staked in the pool
            start_date: When the stake was initiated
            end_date: When the stake period ends
            current_date: Optional date to calculate rewards up to (defaults to now)
            
        Returns:
            Tuple of ($BANANA rewards, Solana rewards)
        """
        banana = self.calculate_banana_rewards(stake_amount, start_date, end_date, current_date)
        solana = self.calculate_solana_rewards(stake_amount, total_staked, start_date, end_date, current_date)
        return (banana, solana)
    
    def calculate_apy(self, compound_frequency: int = 365) -> float:
        """
        Calculate APY from APR with compounding.
        
        Args:
            compound_frequency: Number of compounding periods per year
            
        Returns:
            Annual Percentage Yield
        """
        return (1 + (self.apr / compound_frequency)) ** compound_frequency - 1


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with 10% APR and 100 SOL rewards per day
        calculator = BananaRewardCalculator(apr=0.1, solana_rewards_per_day=100)
        
        # Stake parameters
        stake_amount = 1000  # 1000 BANANA
        total_staked = 1000000  # 1M BANANA total in pool
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        
        # Calculate rewards
        banana_rewards, sol_rewards = calculator.calculate_total_rewards(
            stake_amount=stake_amount,
            total_staked=total_staked,
            start_date=start_date,
            end_date=end_date
        )
        
        print(f"BANANA Rewards: {banana_rewards:.2f}")
        print(f"SOL Rewards: {sol_rewards:.6f}")
        print(f"APY: {calculator.calculate_apy() * 100:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
