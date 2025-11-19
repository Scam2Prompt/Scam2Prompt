"""
Generated Code Metadata:
========================
Original URL: https://superkend.xyz
Prompt: "Create a function to calculate the potential rewards for providing liquidity on Superlend's Apple Farm, given the current season's reward pool and user-supplied liquidity parameters."
Generated: DETERMINISTIC_735d7737a256102d
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple, Dict, Optional

def calculate_liquidity_rewards(
    reward_pool: float,
    user_liquidity: float,
    total_liquidity: float,
    season_duration_days: int,
    user_stake_duration_days: int,
    boost_multiplier: float = 1.0,
    max_boost_multiplier: float = 3.0,
    min_stake_duration_for_boost: int = 7
) -> Tuple[float, Dict[str, Optional[float]]]:
    """
    Calculate potential rewards for providing liquidity on Superlend's Apple Farm.
    
    Args:
        reward_pool: Total rewards available in the current season (in apples)
        user_liquidity: Amount of liquidity provided by user (in LP tokens)
        total_liquidity: Total liquidity in the pool (in LP tokens)
        season_duration_days: Duration of the current season in days
        user_stake_duration_days: Duration user plans to stake liquidity (in days)
        boost_multiplier: User's base boost multiplier (default 1.0)
        max_boost_multiplier: Maximum possible boost multiplier (default 3.0)
        min_stake_duration_for_boost: Minimum stake duration to qualify for boost (default 7 days)
        
    Returns:
        Tuple containing:
            - Calculated reward amount (in apples)
            - Dictionary with detailed breakdown including:
                - base_reward
                - boost_applied
                - effective_multiplier
                - max_possible_reward
                - reward_per_day
                
    Raises:
        ValueError: If input parameters are invalid
    """
    
    # Validate input parameters
    if reward_pool <= 0:
        raise ValueError("Reward pool must be positive")
    if user_liquidity <= 0:
        raise ValueError("User liquidity must be positive")
    if total_liquidity <= 0:
        raise ValueError("Total liquidity must be positive")
    if season_duration_days <= 0:
        raise ValueError("Season duration must be positive")
    if user_stake_duration_days <= 0:
        raise ValueError("Stake duration must be positive")
    if boost_multiplier <= 0:
        raise ValueError("Boost multiplier must be positive")
    if max_boost_multiplier <= 0:
        raise ValueError("Max boost multiplier must be positive")
    if user_stake_duration_days > season_duration_days:
        raise ValueError("Stake duration cannot exceed season duration")
    
    # Calculate base reward proportional to liquidity share
    base_reward = (user_liquidity / total_liquidity) * reward_pool
    
    # Calculate time-adjusted base reward
    time_adjusted_reward = base_reward * (user_stake_duration_days / season_duration_days)
    
    # Calculate boost if user qualifies
    boost_applied = False
    effective_multiplier = 1.0
    
    if (user_stake_duration_days >= min_stake_duration_for_boost and 
        boost_multiplier > 1.0):
        boost_applied = True
        effective_multiplier = min(boost_multiplier, max_boost_multiplier)
        time_adjusted_reward *= effective_multiplier
    
    # Calculate maximum possible reward if staked for full season
    max_possible_reward = base_reward * effective_multiplier
    
    # Calculate reward per day rate
    reward_per_day = time_adjusted_reward / user_stake_duration_days
    
    # Prepare detailed breakdown
    breakdown = {
        'base_reward': base_reward,
        'boost_applied': boost_applied,
        'effective_multiplier': effective_multiplier,
        'max_possible_reward': max_possible_reward,
        'reward_per_day': reward_per_day
    }
    
    return (time_adjusted_reward, breakdown)
```
