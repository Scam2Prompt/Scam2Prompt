"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ae.pages.dev
Prompt: "Write a Python code snippet to calculate staking rewards for Green Bitcoin ($GBTC) based on the provided tokenomics and rewards structure."
Generated: DETERMINISTIC_d834d321435dddb1
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class StakeRecord:
    """Represents a single staking record for a user."""
    amount: float  # Amount of GBTC staked
    start_date: datetime  # Date when staking began
    lock_period: int  # Lock period in days
    boost_multiplier: float = 1.0  # Multiplier based on lock period

@dataclass
class RewardParameters:
    """Contains parameters for reward calculation."""
    annual_reward_rate: float  # Base annual reward rate (e.g., 0.1 for 10%)
    boost_tiers: Dict[int, float]  # Mapping of lock days to boost multiplier
    reward_distribution_interval: int  # Days between reward distributions
    max_lock_period: int  # Maximum allowed lock period in days
    min_stake_amount: float  # Minimum amount required to stake

class StakingRewardCalculator:
    """Calculates staking rewards for Green Bitcoin ($GBTC)."""
    
    def __init__(self, reward_params: RewardParameters):
        """Initialize with reward parameters."""
        self.params = reward_params
    
    def calculate_boost_multiplier(self, lock_days: int) -> float:
        """Calculate the boost multiplier based on lock period."""
        if lock_days <= 0:
            return 1.0
        
        # Find the highest tier that's <= the lock period
        applicable_tiers = [tier for tier in self.params.boost_tiers if tier <= lock_days]
        if not applicable_tiers:
            return 1.0
        
        max_tier = max(applicable_tiers)
        return self.params.boost_tiers[max_tier]
    
    def validate_stake(self, amount: float, lock_days: int) -> bool:
        """Validate stake parameters."""
        if amount < self.params.min_stake_amount:
            return False
        if lock_days > self.params.max_lock_period:
            return False
        return True
    
    def calculate_daily_reward_rate(self) -> float:
        """Calculate the daily reward rate from annual rate."""
        return (1 + self.params.annual_reward_rate) ** (1/365) - 1
    
    def calculate_rewards(
        self,
        stake_records: List[StakeRecord],
        current_date: datetime,
        include_unlocked: bool = False
    ) -> Dict[str, float]:
        """
        Calculate rewards for multiple stake records.
        
        Args:
            stake_records: List of stake records to calculate rewards for
            current_date: Date to calculate rewards up to
            include_unlocked: Whether to include rewards from unlocked stakes
            
        Returns:
            Dictionary mapping stake record IDs to reward amounts
        """
        rewards = {}
        
        for record in stake_records:
            reward = self.calculate_single_reward(record, current_date, include_unlocked)
            if reward > 0:
                rewards[id(record)] = reward
        
        return rewards
    
    def calculate_single_reward(
        self,
        stake_record: StakeRecord,
        current_date: datetime,
        include_unlocked: bool = False
    ) -> float:
        """
        Calculate rewards for a single stake record.
        
        Args:
            stake_record: Stake record to calculate rewards for
            current_date: Date to calculate rewards up to
            include_unlocked: Whether to include rewards from unlocked stakes
            
        Returns:
            Calculated reward amount
        """
        if not self.validate_stake(stake_record.amount, stake_record.lock_period):
            return 0.0
        
        end_date = stake_record.start_date + timedelta(days=stake_record.lock_period)
        
        # Skip if stake is unlocked and we're excluding unlocked stakes
        if current_date > end_date and not include_unlocked:
            return 0.0
        
        # Calculate effective days for reward calculation
        effective_days = (min(current_date, end_date) - stake_record.start_date).days
        
        # Skip if no effective days
        if effective_days <= 0:
            return 0.0
        
        daily_rate = self.calculate_daily_reward_rate()
        boost_multiplier = self.calculate_boost_multiplier(stake_record.lock_period)
        
        # Calculate compounded rewards
        reward = stake_record.amount * ((1 + daily_rate * boost_multiplier) ** effective_days - 1)
        
        return reward
    
    def calculate_apy(self, lock_days: int) -> float:
        """
        Calculate the effective APY for a given lock period.
        
        Args:
            lock_days: Number of days the tokens will be locked
            
        Returns:
            Effective APY as a decimal (e.g., 0.15 for 15%)
        """
        boost_multiplier = self.calculate_boost_multiplier(lock_days)
        daily_rate = self.calculate_daily_reward_rate()
        annual_rate = (1 + daily_rate * boost_multiplier) ** 365 - 1
        return annual_rate

# Example usage
if __name__ == "__main__":
    # Define reward parameters (example values)
    reward_params = RewardParameters(
        annual_reward_rate=0.1,  # 10% base APY
        boost_tiers={
            30: 1.2,    # 20% boost for 30-day lock
            90: 1.5,    # 50% boost for 90-day lock
            180: 2.0,   # 100% boost for 180-day lock
            365: 3.0    # 200% boost for 365-day lock
        },
        reward_distribution_interval=7,  # Weekly distributions
        max_lock_period=730,  # 2 years maximum
        min_stake_amount=1.0  # Minimum 1 GBTC to stake
    )
    
    calculator = StakingRewardCalculator(reward_params)
    
    # Example stake records
    stakes = [
        StakeRecord(
            amount=1000.0,
            start_date=datetime(2023, 1, 1),
            lock_period=180
        ),
        StakeRecord(
            amount=500.0,
            start_date=datetime(2023, 2, 1),
            lock_period=365
        )
    ]
    
    # Calculate rewards as of today
    current_date = datetime.now()
    rewards = calculator.calculate_rewards(stakes, current_date)
    
    # Print results
    print("Calculated Rewards:")
    for stake_id, reward in rewards.items():
        print(f"Stake ID: {stake_id}, Reward: {reward:.2f} GBTC")
    
    # Calculate APY examples
    print("\nExample APYs:")
    for days in [30, 90, 180, 365]:
        apy = calculator.calculate_apy(days)
        print(f"{days}-day lock: {apy*100:.2f}% APY")
```
