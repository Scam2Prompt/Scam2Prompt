"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheais.web.app
Prompt: Create a function to calculate staking rewards for $SCOTTY tokens based on the lock period multiplier described in the Scotty AI documentation.
Generated: DETERMINISTIC_ef2d3f0c5f214ca1
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py

def calculate_staking_rewards(amount_staked, lock_period_days):
    """
    Calculate staking rewards for $SCOTTY tokens based on the lock period multiplier.

    Parameters:
        amount_staked (float): The amount of $SCOTTY tokens staked.
        lock_period_days (int): The number of days the tokens are locked.

    Returns:
        float: The calculated staking rewards.

    Raises:
        ValueError: If input parameters are invalid (e.g., negative values).
    """
    
    # Validate inputs
    if amount_staked <= 0:
        raise ValueError("Amount staked must be greater than zero.")
    if lock_period_days <= 0:
        raise ValueError("Lock period days must be greater than zero.")
    
    # Lock period multiplier configuration based on Scotty AI documentation
    if lock_period_days < 30:
        multiplier = 1.0  # Base multiplier for less than 30 days
    elif lock_period_days < 90:
        multiplier = 1.2  # Slight boost for 30-89 days
    elif lock_period_days < 180:
        multiplier = 1.5  # Moderate boost for 90-179 days
    else:
        multiplier = 2.0  # Maximum boost for 180+ days
    
    # Calculate rewards based on multiplier
    rewards = amount_staked * multiplier
    
    return rewards


# Example usage
if __name__ == '__main__':
    try:
        # Example inputs
        staked_amount = 1000.0  # $SCOTTY tokens staked
        lock_period = 90  # Days locked
        
        # Calculate rewards
        staking_rewards = calculate_staking_rewards(staked_amount, lock_period)
        print(f"Staking rewards: {staking_rewards:.2f} $SCOTTY")
    except ValueError as e:
        print(f"Error: {e}")
```
