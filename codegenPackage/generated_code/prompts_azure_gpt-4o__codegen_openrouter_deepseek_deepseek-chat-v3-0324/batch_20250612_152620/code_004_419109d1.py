"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Develop a Python script to calculate the rewards pool distribution for $QUBE token staking, based on the 5% sell tax described in InQubeta's tokenomics.
Generated: DETERMINISTIC_419109d16e3ce6f9
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Staker:
    """Represents a staker with their staked amount and duration."""
    address: str
    staked_amount: float
    staking_duration_days: int

class RewardCalculator:
    """
    A class to calculate the distribution of rewards from the QUBE staking pool.
    The rewards pool is funded by a 5% sell tax on QUBE token transactions.
    """
    
    def __init__(self, stakers: List[Staker], total_sell_volume: float):
        """
        Initialize the RewardCalculator with stakers and total sell volume.
        
        Args:
            stakers: List of Staker objects
            total_sell_volume: Total volume of QUBE tokens sold (used to calculate 5% tax)
        """
        self.stakers = stakers
        self.total_sell_volume = total_sell_volume
        self.rewards_pool = total_sell_volume * 0.05  # 5% sell tax
        
    def calculate_weight(self, staker: Staker) -> float:
        """
        Calculate the weight of a staker based on amount and duration.
        
        Args:
            staker: Staker object
            
        Returns:
            float: Calculated weight for reward distribution
        """
        # Weight is proportional to both amount and duration
        return staker.staked_amount * math.log(1 + staker.staking_duration_days)
    
    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculate rewards for all stakers based on their weights.
        
        Returns:
            Dict[str, float]: Mapping of staker addresses to their reward amounts
            
        Raises:
            ValueError: If no stakers are provided
        """
        if not self.stakers:
            raise ValueError("No stakers provided for reward calculation")
        
        total_weight = sum(self.calculate_weight(staker) for staker in self.stakers)
        if total_weight <= 0:
            return {staker.address: 0.0 for staker in self.stakers}
            
        rewards = {}
        for staker in self.stakers:
            weight = self.calculate_weight(staker)
            reward = (weight / total_weight) * self.rewards_pool
            rewards[staker.address] = reward
            
        return rewards
    
    def get_rewards_distribution(self) -> Tuple[Dict[str, float], float]:
        """
        Get the rewards distribution and total rewards pool.
        
        Returns:
            Tuple[Dict[str, float], float]: (rewards distribution, total rewards pool)
        """
        rewards = self.calculate_rewards()
        return rewards, self.rewards_pool

# Example usage
if __name__ == "__main__":
    # Sample stakers
    stakers = [
        Staker("0x123...", 1000.0, 30),   # 1000 QUBE staked for 30 days
        Staker("0x456...", 5000.0, 60),   # 5000 QUBE staked for 60 days
        Staker("0x789...", 2500.0, 90)    # 2500 QUBE staked for 90 days
    ]
    
    # Total sell volume in QUBE tokens
    total_sell_volume = 100000.0  # 100,000 QUBE sold
    
    try:
        calculator = RewardCalculator(stakers, total_sell_volume)
        rewards, pool = calculator.get_rewards_distribution()
        
        print(f"Total Rewards Pool: {pool:.2f} QUBE")
        print("Rewards Distribution:")
        for address, reward in rewards.items():
            print(f"{address}: {reward:.2f} QUBE")
            
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
