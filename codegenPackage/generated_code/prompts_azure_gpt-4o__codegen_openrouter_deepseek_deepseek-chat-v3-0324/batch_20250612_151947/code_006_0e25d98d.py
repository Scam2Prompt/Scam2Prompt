"""
Generated Code Metadata:
========================
Original URL: https://bonk-rewarded.pages.dev
Prompt: Write code to simulate the distribution of fees collected by the BONK Ecosystem into the BONK Rewards Pool, and calculate the user's share based on their locked $BONK and duration multiplier.
Generated: DETERMINISTIC_0e25d98d497d7f5b
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class UserLock:
    """Represents a user's locked BONK tokens and lock duration."""
    user_address: str
    locked_amount: float  # Amount of BONK tokens locked
    lock_duration: int    # Duration in days

class BonkRewardsPool:
    """Simulates the BONK Rewards Pool distribution system."""
    
    def __init__(self):
        """Initialize the rewards pool with empty state."""
        self.total_fees_collected: float = 0.0
        self.user_locks: Dict[str, UserLock] = {}
        self.total_weighted_stake: float = 0.0
        
    def collect_fees(self, amount: float) -> None:
        """Add collected fees to the rewards pool.
        
        Args:
            amount: Amount of fees to add to the pool (in BONK)
        """
        if amount <= 0:
            raise ValueError("Fee amount must be positive")
        self.total_fees_collected += amount
    
    def add_user_lock(self, user_address: str, locked_amount: float, lock_duration: int) -> None:
        """Add or update a user's locked BONK position.
        
        Args:
            user_address: Unique identifier for the user
            locked_amount: Amount of BONK tokens to lock
            lock_duration: Duration in days (minimum 1 day)
        """
        if locked_amount <= 0:
            raise ValueError("Locked amount must be positive")
        if lock_duration < 1:
            raise ValueError("Lock duration must be at least 1 day")
            
        # Remove previous stake if exists
        if user_address in self.user_locks:
            previous_lock = self.user_locks[user_address]
            self.total_weighted_stake -= self._calculate_weighted_stake(
                previous_lock.locked_amount, 
                previous_lock.lock_duration
            )
        
        # Add new stake
        self.user_locks[user_address] = UserLock(
            user_address=user_address,
            locked_amount=locked_amount,
            lock_duration=lock_duration
        )
        
        # Update total weighted stake
        self.total_weighted_stake += self._calculate_weighted_stake(
            locked_amount, 
            lock_duration
        )
    
    def _calculate_weighted_stake(self, amount: float, duration: int) -> float:
        """Calculate the weighted stake based on amount and duration.
        
        Args:
            amount: Amount of BONK tokens
            duration: Lock duration in days
            
        Returns:
            Weighted stake value
        """
        # Linear multiplier: 1x for 1 day, 2x for 365 days, etc.
        duration_multiplier = 1 + (duration / 365)
        return amount * duration_multiplier
    
    def calculate_user_rewards(self, user_address: str) -> float:
        """Calculate the user's share of the rewards pool.
        
        Args:
            user_address: User to calculate rewards for
            
        Returns:
            Amount of rewards the user is entitled to (in BONK)
            
        Raises:
            ValueError: If user has no locked position
        """
        if user_address not in self.user_locks:
            raise ValueError("User has no locked position")
            
        if self.total_weighted_stake == 0:
            return 0.0
            
        user_lock = self.user_locks[user_address]
        user_weight = self._calculate_weighted_stake(
            user_lock.locked_amount,
            user_lock.lock_duration
        )
        
        user_share = user_weight / self.total_weighted_stake
        return user_share * self.total_fees_collected
    
    def distribute_rewards(self) -> Dict[str, float]:
        """Distribute all collected fees to users based on their weighted stake.
        
        Returns:
            Dictionary mapping user addresses to their reward amounts
        """
        if self.total_weighted_stake == 0:
            return {}
            
        rewards = {}
        for user_address, user_lock in self.user_locks.items():
            user_weight = self._calculate_weighted_stake(
                user_lock.locked_amount,
                user_lock.lock_duration
            )
            user_share = user_weight / self.total_weighted_stake
            rewards[user_address] = user_share * self.total_fees_collected
        
        # Reset the collected fees after distribution
        self.total_fees_collected = 0.0
        return rewards
    
    def get_pool_state(self) -> dict:
        """Get the current state of the rewards pool.
        
        Returns:
            Dictionary containing pool statistics
        """
        return {
            "total_fees_collected": self.total_fees_collected,
            "total_weighted_stake": self.total_weighted_stake,
            "total_users": len(self.user_locks),
            "average_lock_duration": (
                sum(lock.lock_duration for lock in self.user_locks.values()) / len(self.user_locks)
                if self.user_locks else 0
            )
        }
```
