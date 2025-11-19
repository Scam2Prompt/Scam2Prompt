"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-ethereal.trade
Prompt: Write a Python script that calculates the potential rewards for voters in the Ethereal Vote based on the total incentives and asset multipliers mentioned on the site.
Generated: DETERMINISTIC_17ea9fa77001ed7e
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ethereal Vote Reward Calculator

This script calculates the potential rewards for voters participating in Ethereal Vote.
It uses the total incentives and asset multipliers provided by the site.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

def calculate_rewards(total_incentives, asset_multipliers):
    """
    Calculate the rewards for voters based on total incentives and asset multipliers.

    Parameters:
        total_incentives (float): Total incentives for voting.
        asset_multipliers (dict): A dictionary mapping asset names to their respective multipliers.

    Returns:
        dict: A dictionary containing rewards for each asset.
    """
    if total_incentives <= 0:
        raise ValueError("Total incentives must be greater than zero.")
    
    if not asset_multipliers or not isinstance(asset_multipliers, dict):
        raise ValueError("Asset multipliers must be a non-empty dictionary.")
    
    rewards = {}
    total_multiplier = sum(asset_multipliers.values())
    
    if total_multiplier == 0:
        raise ValueError("The sum of asset multipliers cannot be zero.")

    for asset, multiplier in asset_multipliers.items():
        rewards[asset] = (multiplier / total_multiplier) * total_incentives

    return rewards

def get_user_input():
    """
    Get user input for total incentives and asset multipliers.

    Returns:
        tuple: (total_incentives, asset_multipliers)
    """
    try:
        total_incentives = float(input("Enter the total incentives (e.g., 1000.0): "))
        
        asset_multipliers = {}
        print("Enter asset multipliers (e.g., 'ETH:1.5 BTC:2.0'). Type 'done' when finished:")
        while True:
            user_input = input("Asset multiplier (or 'done' to finish): ")
            if user_input.strip().lower() == "done":
                break
            
            asset, multiplier = user_input.split(":")
            asset_multipliers[asset.strip()] = float(multiplier.strip())
        
        return total_incentives, asset_multipliers

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the reward calculation.
    """
    print("Welcome to the Ethereal Vote Reward Calculator!")
    
    try:
        total_incentives, asset_multipliers = get_user_input()
        rewards = calculate_rewards(total_incentives, asset_multipliers)

        print("\nCalculated Rewards:")
        for asset, reward in rewards.items():
            print(f"{asset}: {reward:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
