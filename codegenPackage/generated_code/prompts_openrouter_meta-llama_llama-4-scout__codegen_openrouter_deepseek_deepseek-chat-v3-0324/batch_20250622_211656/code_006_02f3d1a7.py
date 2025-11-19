"""
Generated Code Metadata:
========================
Original URL: https://orbiters.vercel.app
Prompt: Propose a method to integrate early adopter bonuses into a token distribution system, considering long-term user activity on a platform like Orbiter Finance.
Generated: DETERMINISTIC_02f3d1a759e3b386
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Token Distribution System with Early Adopter Bonuses

This module implements a token distribution system that rewards early adopters
with bonuses while incentivizing long-term platform engagement.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict
import math

@dataclass
class User:
    """Represents a platform user with their activity history."""
    address: str
    join_date: datetime
    activity_points: List[float]  # Weekly activity points over time

class TokenDistributor:
    """
    Handles token distribution with early adopter bonuses and long-term incentives.
    
    Attributes:
        total_supply: Total tokens to distribute
        base_distribution: Base tokens per user
        early_bonus_window: Days considered for early adopter status
        early_bonus_multiplier: Bonus multiplier for early adopters
        activity_decay_rate: Rate at which activity bonuses decay over time
        max_activity_bonus: Maximum bonus from activity
    """
    
    def __init__(
        self,
        total_supply: float,
        base_distribution: float,
        early_bonus_window: int = 30,
        early_bonus_multiplier: float = 1.5,
        activity_decay_rate: float = 0.95,
        max_activity_bonus: float = 2.0
    ):
        self.total_supply = total_supply
        self.base_distribution = base_distribution
        self.early_bonus_window = early_bonus_window
        self.early_bonus_multiplier = early_bonus_multiplier
        self.activity_decay_rate = activity_decay_rate
        self.max_activity_bonus = max_activity_bonus
        
        if total_supply <= 0:
            raise ValueError("Total supply must be positive")
        if base_distribution <= 0:
            raise ValueError("Base distribution must be positive")
        if early_bonus_multiplier < 1:
            raise ValueError("Early bonus multiplier must be >= 1")
        if not (0 < activity_decay_rate <= 1):
            raise ValueError("Activity decay rate must be between 0 and 1")
        if max_activity_bonus < 1:
            raise ValueError("Max activity bonus must be >= 1")

    def calculate_early_adopter_bonus(self, user: User, reference_date: datetime) -> float:
        """Calculate bonus multiplier based on how early the user joined."""
        days_early = (reference_date - user.join_date).days
        if days_early <= 0:
            return 1.0  # No bonus for users joining after reference
        
        # Linear decay of bonus over the early window
        early_factor = min(days_early / self.early_bonus_window, 1.0)
        return 1.0 + (self.early_bonus_multiplier - 1.0) * early_factor

    def calculate_activity_bonus(self, user: User) -> float:
        """Calculate bonus based on sustained activity over time."""
        if not user.activity_points:
            return 1.0
            
        # Calculate weighted average with exponential decay
        total_weight = 0.0
        weighted_sum = 0.0
        
        for i, points in enumerate(reversed(user.activity_points)):
            weight = math.pow(self.activity_decay_rate, i)
            weighted_sum += points * weight
            total_weight += weight
            
        avg_activity = weighted_sum / total_weight if total_weight > 0 else 0
        return min(1.0 + avg_activity, self.max_activity_bonus)

    def distribute_tokens(self, users: List[User], distribution_date: datetime) -> Dict[str, float]:
        """
        Distribute tokens to users considering early adopter and activity bonuses.
        
        Returns:
            Dictionary mapping user addresses to their token allocation
        """
        if not users:
            return {}
            
        allocations = {}
        total_allocated = 0.0
        
        # Calculate raw allocations with bonuses
        for user in users:
            early_bonus = self.calculate_early_adopter_bonus(user, distribution_date)
            activity_bonus = self.calculate_activity_bonus(user)
            
            allocation = self.base_distribution * early_bonus * activity_bonus
            allocations[user.address] = allocation
            total_allocated += allocation
            
        # Normalize allocations to match total supply
        if total_allocated > 0:
            scaling_factor = self.total_supply / total_allocated
            for address in allocations:
                allocations[address] *= scaling_factor
                
        return allocations

# Example usage
if __name__ == "__main__":
    # Configuration
    config = {
        "total_supply": 1_000_000,
        "base_distribution": 1000,
        "early_bonus_window": 30,
        "early_bonus_multiplier": 1.5,
        "activity_decay_rate": 0.95,
        "max_activity_bonus": 2.0
    }
    
    # Create sample users
    now = datetime.now()
    users = [
        User(
            address="0x1",
            join_date=now - timedelta(days=15),  # Early adopter
            activity_points=[0.8, 0.9, 0.85, 0.95]  # High activity
        ),
        User(
            address="0x2",
            join_date=now - timedelta(days=45),  # Not early adopter
            activity_points=[0.5, 0.6, 0.4, 0.3]  # Moderate activity
        ),
        User(
            address="0x3",
            join_date=now - timedelta(days=5),  # Very early adopter
            activity_points=[0.2, 0.1]  # Low activity
        )
    ]
    
    # Distribute tokens
    distributor = TokenDistributor(**config)
    allocations = distributor.distribute_tokens(users, now)
    
    print("Token Allocations:")
    for address, amount in allocations.items():
        print(f"{address}: {amount:.2f} tokens")
```
