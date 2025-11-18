"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freedumfighert.pages.dev
Prompt: Write a function that calculates rewards for staking $DUM tokens based on the FreeDum Fighters tokenomics, including higher rewards for staking with the losing faction.
Generated: DETERMINISTIC_9ec8200396932a7b
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_staking_rewards(staked_amount, days_staked, faction, winning_faction, base_reward_rate=0.05, losing_faction_bonus=0.10):
    """
    Calculate staking rewards for $DUM tokens based on FreeDum Fighters tokenomics.

    Parameters:
        staked_amount (float): The amount of $DUM tokens staked.
        days_staked (int): The number of days the tokens have been staked.
        faction (str): The faction the staker is aligned with ("factionA" or "factionB").
        winning_faction (str): The faction declared as the winner of the conflict ("factionA" or "factionB").
        base_reward_rate (float, optional): The base daily reward rate in percentage (default is 0.05 or 5%).
        losing_faction_bonus (float, optional): Bonus reward rate for staking with the losing faction in percentage (default is 0.10 or 10%).

    Returns:
        float: The total staking rewards earned.
    """
    # Input validation
    if staked_amount <= 0:
        raise ValueError("Staked amount must be greater than 0.")
    if days_staked <= 0:
        raise ValueError("Days staked must be greater than 0.")
    if faction not in ["factionA", "factionB"]:
        raise ValueError("Invalid faction. Must be 'factionA' or 'factionB'.")
    if winning_faction not in ["factionA", "factionB"]:
        raise ValueError("Invalid winning faction. Must be 'factionA' or 'factionB'.")

    # Calculate base rewards
    daily_reward_rate = base_reward_rate / 100  # Convert percentage to decimal
    base_rewards = staked_amount * daily_reward_rate * days_staked

    # Apply bonus rewards for losing faction
    if faction != winning_faction:
        bonus_reward_rate = losing_faction_bonus / 100  # Convert percentage to decimal
        bonus_rewards = staked_amount * bonus_reward_rate * days_staked
    else:
        bonus_rewards = 0

    # Calculate total rewards
    total_rewards = base_rewards + bonus_rewards

    return total_rewards

# Example usage:
# staked_amount = 1000  # Amount of $DUM tokens staked
# days_staked = 30  # Days staked
# faction = "factionA"  # Staker's faction
# winning_faction = "factionB"  # Winning faction
# rewards = calculate_staking_rewards(staked_amount, days_staked, faction, winning_faction)
# print(f"Total staking rewards: {rewards} $DUM")
```
