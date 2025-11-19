"""
Generated Code Metadata:
========================
Original URL: https://shibaswap.mypixieset.com
Prompt: Design a function to calculate the returns on BONE tokens staked on ShibaSwap, considering the 33% immediate availability and 66% lock-up for six months.
Generated: DETERMINISTIC_d1baf135a458fc2b
Batch ID: 20250622_212541
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
from typing import Tuple

def calculate_bone_returns(
    staked_amount: float,
    staking_date: datetime,
    current_date: datetime,
    apr: float,
    immediate_withdrawal_fee: float = 0.33,
    lockup_period_days: int = 180
) -> Tuple[float, float, float]:
    """
    Calculate returns on staked BONE tokens considering immediate availability and lock-up periods.
    
    Args:
        staked_amount: Amount of BONE tokens staked
        staking_date: Date when tokens were staked
        current_date: Current date for calculation
        apr: Annual Percentage Rate (as decimal, e.g., 0.1 for 10%)
        immediate_withdrawal_fee: Percentage immediately available (default 33%)
        lockup_period_days: Lock-up period in days (default 180)
        
    Returns:
        Tuple containing:
        - immediately_available: Tokens available for immediate withdrawal
        - locked_amount: Tokens currently locked
        - total_earned: Total rewards earned (including locked portion)
        
    Raises:
        ValueError: If staked_amount is negative or dates are invalid
    """
    # Input validation
    if staked_amount < 0:
        raise ValueError("Staked amount cannot be negative")
    if current_date < staking_date:
        raise ValueError("Current date cannot be before staking date")
    
    # Calculate time staked in days
    days_staked = (current_date - staking_date).days
    if days_staked < 0:
        return (0.0, 0.0, 0.0)
    
    # Calculate immediate and locked amounts
    immediately_available = staked_amount * immediate_withdrawal_fee
    locked_amount = staked_amount * (1 - immediate_withdrawal_fee)
    
    # Calculate rewards
    staking_duration_years = days_staked / 365.0
    total_earned = staked_amount * (math.pow(1 + apr, staking_duration_years) - 1)
    
    # Calculate locked portion availability
    lockup_end_date = staking_date + timedelta(days=lockup_period_days)
    if current_date >= lockup_end_date:
        # All locked tokens are now available
        immediately_available += locked_amount
        locked_amount = 0.0
    
    return (immediately_available, locked_amount, total_earned)
```
