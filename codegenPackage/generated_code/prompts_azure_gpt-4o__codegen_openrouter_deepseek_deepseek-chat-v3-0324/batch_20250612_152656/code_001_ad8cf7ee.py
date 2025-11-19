"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-def.web.app
Prompt: Generate code to calculate staking rewards for $SCOTTY tokens based on the lock period multiplier described in the Scotty AI staking system.
Generated: DETERMINISTIC_ad8cf7eef93f0a40
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Union

# Constants for staking parameters
LOCK_PERIOD_MULTIPLIERS: Dict[int, float] = {
    30: 1.0,    # 30 days lock period
    60: 1.5,    # 60 days lock period
    90: 2.0,    # 90 days lock period
    180: 3.0,   # 180 days lock period
    365: 5.0    # 365 days lock period
}

ANNUAL_REWARD_RATE: float = 0.20  # 20% annual reward rate

def calculate_staking_rewards(
    amount: float, 
    lock_period_days: int, 
    staking_duration_days: int
) -> Union[float, str]:
    """
    Calculate staking rewards for SCOTTY tokens based on lock period multiplier.
    
    Args:
        amount: Amount of SCOTTY tokens staked
        lock_period_days: Number of days tokens are locked (must be one of 30, 60, 90, 180, 365)
        staking_duration_days: Actual number of days tokens are staked
        
    Returns:
        Calculated reward amount in SCOTTY tokens or error message if invalid input
    """
    try:
        # Validate inputs
        if amount <= 0:
            return "Staked amount must be positive"
            
        if staking_duration_days <= 0:
            return "Staking duration must be positive"
            
        if lock_period_days not in LOCK_PERIOD_MULTIPLIERS:
            return "Invalid lock period. Valid options are: 30, 60, 90, 180, 365 days"
            
        if staking_duration_days > lock_period_days:
            return "Staking duration cannot exceed lock period"
        
        # Get the multiplier for the selected lock period
        multiplier = LOCK_PERIOD_MULTIPLIERS[lock_period_days]
        
        # Calculate daily reward rate with multiplier
        daily_rate = (ANNUAL_REWARD_RATE * multiplier) / 365
        
        # Calculate rewards
        rewards = amount * daily_rate * staking_duration_days
        
        # Round to 8 decimal places to avoid floating point precision issues
        return round(rewards, 8)
        
    except Exception as e:
        return f"Error calculating rewards: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (1000, 30, 30),    # 30-day lock, full period
        (5000, 60, 45),    # 60-day lock, partial period
        (2500, 90, 90),    # 90-day lock, full period
        (10000, 180, 120), # 180-day lock, partial period
        (7500, 365, 200),  # 365-day lock, partial period
        (1000, 30, 31),    # Invalid: exceeds lock period
        (-100, 30, 30),    # Invalid: negative amount
        (1000, 45, 30),    # Invalid: lock period not supported
    ]
    
    for amount, lock_days, duration in test_cases:
        result = calculate_staking_rewards(amount, lock_days, duration)
        print(f"Amount: {amount}, Lock: {lock_days}d, Duration: {duration}d → Reward: {result}")
```
