"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a function to calculate the APR for `rsTAO` supply based on the provided percentage (e.g., 13.87%) and update the staking rewards dynamically.
Generated: DETERMINISTIC_2f39fdeee5b26e87
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_apr(current_supply: float, apr_percentage: float, time_period_days: int = 365) -> float:
    """
    Calculate the APR (Annual Percentage Rate) for rsTAO supply based on the given percentage.
    
    Args:
        current_supply (float): Current total supply of rsTAO tokens
        apr_percentage (float): APR percentage (e.g., 13.87 for 13.87%)
        time_period_days (int, optional): Time period in days for APR calculation. Defaults to 365.
    
    Returns:
        float: Total rewards to be distributed over the time period
    """
    if current_supply <= 0:
        raise ValueError("Current supply must be greater than 0")
    if apr_percentage <= 0:
        raise ValueError("APR percentage must be greater than 0")
    if time_period_days <= 0:
        raise ValueError("Time period must be greater than 0 days")
    
    # Convert APR from percentage to decimal
    apr_decimal = apr_percentage / 100
    
    # Calculate rewards for the given time period
    rewards = current_supply * apr_decimal * (time_period_days / 365)
    
    return rewards

def update_staking_rewards(current_supply: float, apr_percentage: float, stakers: dict) -> dict:
    """
    Update staking rewards for each staker based on the current APR.
    
    Args:
        current_supply (float): Current total supply of rsTAO tokens
        apr_percentage (float): APR percentage (e.g., 13.87 for 13.87%)
        stakers (dict): Dictionary of staker addresses and their staked amounts
        
    Returns:
        dict: Updated staker rewards dictionary with new rewards added
    """
    if not stakers:
        raise ValueError("Stakers dictionary cannot be empty")
    
    total_staked = sum(stakers.values())
    if total_staked <= 0:
        raise ValueError("Total staked amount must be greater than 0")
    
    # Calculate total rewards to distribute
    total_rewards = calculate_apr(current_supply, apr_percentage)
    
    # Calculate reward per staked token
    reward_per_token = total_rewards / total_staked
    
    # Update each staker's rewards
    updated_rewards = {}
    for staker, amount in stakers.items():
        updated_rewards[staker] = amount * reward_per_token
    
    return updated_rewards
```
