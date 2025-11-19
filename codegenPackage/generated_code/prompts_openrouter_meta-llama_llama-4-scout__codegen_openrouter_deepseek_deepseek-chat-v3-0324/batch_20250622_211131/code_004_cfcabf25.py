"""
Generated Code Metadata:
========================
Original URL: https://chitzoinu.pages.dev
Prompt: "Design a staking system for a cryptocurrency platform, incorporating features like automatic token locking and yield farming."
Generated: DETERMINISTIC_cfcabf25a8b3b51f
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from datetime import datetime, timedelta

# Constants
STAKE_MIN_AMOUNT = 1  # Minimum staking amount in tokens
STAKE_LOCK_PERIOD = 7 * 24 * 60 * 60  # Default lock period (7 days in seconds)
APY = 0.1  # Annual Percentage Yield (10%)

class StakeStatus(Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    WITHDRAWN = "WITHDRAWN"

@dataclass
class Stake:
    stake_id: str
    user_id: str
    amount: float
    start_time: float
    end_time: float
    status: StakeStatus
    apy: float

class StakingSystem:
    def __init__(self):
        self.stakes: Dict[str, Stake] = {}
        self.token_balances: Dict[str, float] = {}

    def _generate_stake_id(self, user_id: str, amount: float) -> str:
        """Generate a unique stake ID using user ID and timestamp."""
        timestamp = str(time.time()).encode('utf-8')
        unique_str = f"{user_id}{amount}{timestamp}".encode('utf-8')
        return hashlib.sha256(unique_str).hexdigest()

    def deposit_tokens(self, user_id: str, amount: float) -> bool:
        """Deposit tokens into the user's balance."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if user_id not in self.token_balances:
            self.token_balances[user_id] = 0.0
        
        self.token_balances[user_id] += amount
        return True

    def stake_tokens(self, user_id: str, amount: float, lock_period: int = STAKE_LOCK_PERIOD) -> Stake:
        """Stake tokens for a given lock period."""
        if user_id not in self.token_balances or self.token_balances[user_id] < amount:
            raise ValueError("Insufficient balance")
        
        if amount < STAKE_MIN_AMOUNT:
            raise ValueError(f"Amount must be at least {STAKE_MIN_AMOUNT}")
        
        stake_id = self._generate_stake_id(user_id, amount)
        start_time = time.time()
        end_time = start_time + lock_period
        
        stake = Stake(
            stake_id=stake_id,
            user_id=user_id,
            amount=amount,
            start_time=start_time,
            end_time=end_time,
            status=StakeStatus.ACTIVE,
            apy=APY
        )
        
        self.stakes[stake_id] = stake
        self.token_balances[user_id] -= amount
        
        return stake

    def calculate_rewards(self, stake_id: str) -> float:
        """Calculate rewards for a stake."""
        if stake_id not in self.stakes:
            raise ValueError("Stake not found")
        
        stake = self.stakes[stake_id]
        
        if stake.status != StakeStatus.ACTIVE:
            return 0.0
        
        current_time = time.time()
        if current_time < stake.end_time:
            staked_duration = current_time - stake.start_time
        else:
            staked_duration = stake.end_time - stake.start_time
        
        staked_years = staked_duration / (365 * 24 * 60 * 60)
        return stake.amount * stake.apy * staked_years

    def withdraw_stake(self, stake_id: str) -> Tuple[float, float]:
        """Withdraw staked tokens and rewards."""
        if stake_id not in self.stakes:
            raise ValueError("Stake not found")
        
        stake = self.stakes[stake_id]
        
        if stake.status != StakeStatus.ACTIVE:
            raise ValueError("Stake is not active")
        
        current_time = time.time()
        if current_time < stake.end_time:
            raise ValueError("Stake is still locked")
        
        rewards = self.calculate_rewards(stake_id)
        total_amount = stake.amount + rewards
        
        stake.status = StakeStatus.WITHDRAWN
        self.token_balances[stake.user_id] += total_amount
        
        return stake.amount, rewards

    def get_active_stakes(self, user_id: str) -> List[Stake]:
        """Get all active stakes for a user."""
        return [
            stake for stake in self.stakes.values()
            if stake.user_id == user_id and stake.status == StakeStatus.ACTIVE
        ]

    def get_stake_info(self, stake_id: str) -> Stake:
        """Get stake information by ID."""
        if stake_id not in self.stakes:
            raise ValueError("Stake not found")
        return self.stakes[stake_id]

    def get_user_balance(self, user_id: str) -> float:
        """Get user's available token balance."""
        return self.token_balances.get(user_id, 0.0)

# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # Deposit tokens
    user_id = "user123"
    staking_system.deposit_tokens(user_id, 100.0)
    
    # Stake tokens
    stake = staking_system.stake_tokens(user_id, 50.0)
    print(f"Staked: {stake}")
    
    # Get active stakes
    active_stakes = staking_system.get_active_stakes(user_id)
    print(f"Active stakes: {active_stakes}")
    
    # Calculate rewards (after some time)
    time.sleep(2)  # Simulate time passing
    rewards = staking_system.calculate_rewards(stake.stake_id)
    print(f"Rewards: {rewards}")
    
    # Withdraw (would fail if lock period hasn't expired)
    try:
        amount, rewards = staking_system.withdraw_stake(stake.stake_id)
        print(f"Withdrawn: {amount} + {rewards} rewards")
    except ValueError as e:
        print(f"Cannot withdraw yet: {e}")
```
