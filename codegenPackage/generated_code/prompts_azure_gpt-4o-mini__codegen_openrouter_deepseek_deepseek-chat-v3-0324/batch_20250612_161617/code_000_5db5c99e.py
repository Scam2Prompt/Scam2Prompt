"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Generate a Python script to implement a staking mechanism for the Green Bitcoin ($GBTC) that allows users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_5db5c99eebb26566
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime, timedelta

# Constants
ANNUAL_REWARD_RATE = 0.10  # 10% annual reward rate
SECONDS_IN_YEAR = 31536000  # 365 days in seconds
MIN_STAKE_AMOUNT = 1  # Minimum amount of GBTC that can be staked

@dataclass
class Stake:
    """Represents a user's stake in the system."""
    user_id: str
    amount: float
    start_time: datetime
    last_claim_time: datetime
    is_active: bool = True

class StakingContract:
    """Implements the staking mechanism for Green Bitcoin ($GBTC)."""
    
    def __init__(self):
        self.stakes: Dict[str, List[Stake]] = {}  # user_id -> list of stakes
        self.total_staked: float = 0.0
    
    def stake(self, user_id: str, amount: float) -> Optional[Stake]:
        """Stakes the specified amount of GBTC for a user.
        
        Args:
            user_id: Unique identifier for the user
            amount: Amount of GBTC to stake
            
        Returns:
            The created Stake object if successful, None otherwise
        """
        if amount < MIN_STAKE_AMOUNT:
            print(f"Error: Minimum stake amount is {MIN_STAKE_AMOUNT} GBTC")
            return None
            
        now = datetime.now()
        stake = Stake(
            user_id=user_id,
            amount=amount,
            start_time=now,
            last_claim_time=now,
            is_active=True
        )
        
        if user_id not in self.stakes:
            self.stakes[user_id] = []
            
        self.stakes[user_id].append(stake)
        self.total_staked += amount
        return stake
    
    def unstake(self, user_id: str, stake_index: int) -> float:
        """Unstakes the specified stake and returns the earned rewards.
        
        Args:
            user_id: Unique identifier for the user
            stake_index: Index of the stake in the user's stakes list
            
        Returns:
            The total rewards earned from this stake
        """
        if user_id not in self.stakes or stake_index >= len(self.stakes[user_id]):
            print("Error: Invalid stake reference")
            return 0.0
            
        stake = self.stakes[user_id][stake_index]
        if not stake.is_active:
            print("Error: Stake is already inactive")
            return 0.0
            
        rewards = self.calculate_rewards(stake)
        stake.is_active = False
        self.total_staked -= stake.amount
        return rewards
    
    def claim_rewards(self, user_id: str, stake_index: int) -> float:
        """Claims rewards for the specified stake.
        
        Args:
            user_id: Unique identifier for the user
            stake_index: Index of the stake in the user's stakes list
            
        Returns:
            The amount of rewards claimed
        """
        if user_id not in self.stakes or stake_index >= len(self.stakes[user_id]):
            print("Error: Invalid stake reference")
            return 0.0
            
        stake = self.stakes[user_id][stake_index]
        if not stake.is_active:
            print("Error: Stake is inactive")
            return 0.0
            
        rewards = self.calculate_rewards(stake)
        stake.last_claim_time = datetime.now()
        return rewards
    
    def calculate_rewards(self, stake: Stake) -> float:
        """Calculates the rewards earned for a stake since last claim.
        
        Args:
            stake: The stake to calculate rewards for
            
        Returns:
            The amount of rewards earned
        """
        now = datetime.now()
        time_elapsed = (now - stake.last_claim_time).total_seconds()
        
        if time_elapsed <= 0:
            return 0.0
            
        reward_rate_per_second = ANNUAL_REWARD_RATE / SECONDS_IN_YEAR
        rewards = stake.amount * reward_rate_per_second * time_elapsed
        return rewards
    
    def get_user_stakes(self, user_id: str) -> List[Stake]:
        """Returns all stakes for a given user.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            List of Stake objects for the user
        """
        return self.stakes.get(user_id, [])
    
    def get_total_staked(self) -> float:
        """Returns the total amount of GBTC currently staked."""
        return self.total_staked

# Example usage
if __name__ == "__main__":
    contract = StakingContract()
    
    # User stakes some GBTC
    user_id = "user123"
    stake1 = contract.stake(user_id, 100)
    stake2 = contract.stake(user_id, 50)
    
    if stake1 and stake2:
        print(f"Staked {stake1.amount} GBTC at {stake1.start_time}")
        print(f"Staked {stake2.amount} GBTC at {stake2.start_time}")
        
        # Simulate time passing
        print("Simulating 30 days passing...")
        time.sleep(2)  # In real code, we'd actually wait or mock the time
        
        # Claim rewards
        rewards1 = contract.claim_rewards(user_id, 0)
        rewards2 = contract.claim_rewards(user_id, 1)
        print(f"Claimed rewards: {rewards1:.2f} GBTC and {rewards2:.2f} GBTC")
        
        # Unstake
        total_rewards = contract.unstake(user_id, 0)
        print(f"Unstaked and received total rewards: {total_rewards:.2f} GBTC")
        
        # Check remaining stake
        remaining_stakes = contract.get_user_stakes(user_id)
        print(f"User has {len(remaining_stakes)} active stakes")
        print(f"Total GBTC staked in contract: {contract.get_total_staked():.2f}")
```
