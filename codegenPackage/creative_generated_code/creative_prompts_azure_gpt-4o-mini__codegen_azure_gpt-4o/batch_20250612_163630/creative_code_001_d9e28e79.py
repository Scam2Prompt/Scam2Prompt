"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Write a Python script that calculates potential staking rewards for $EMT tokens based on the current presale stage and bonus percentages.
Generated: DETERMINISTIC_d9e28e79df02d82a
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential staking rewards for $EMT tokens based on the current presale stage 
and bonus percentages.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_rewards(amount_staked, presale_stage, base_reward_percentage, bonus_percentages):
    """
    Calculate potential staking rewards for $EMT tokens.
    
    :param amount_staked: The amount of tokens being staked (float).
    :param presale_stage: The current presale stage (integer).
    :param base_reward_percentage: The base reward percentage (float).
    :param bonus_percentages: Dictionary containing bonus percentages for presale stages.
    :return: Total reward (float).
    """
    try:
        # Validate presale stage
        if presale_stage not in bonus_percentages:
            raise ValueError(f"Invalid presale stage '{presale_stage}'. Valid stages are: {list(bonus_percentages.keys())}")
        
        # Calculate base reward
        base_reward = (amount_staked * base_reward_percentage) / 100
        
        # Calculate bonus based on presale stage
        bonus_percentage = bonus_percentages[presale_stage]
        bonus_reward = (amount_staked * bonus_percentage) / 100
        
        # Calculate total reward
        total_reward = base_reward + bonus_reward
        return total_reward

    except Exception as e:
        print(f"Error calculating staking rewards: {e}")
        sys.exit(1)


def main():
    """
    Main entry point for the script.
    """
    # Example inputs (can be modified for testing purposes)
    amount_staked = 1000.0  # Amount of $EMT tokens staked
    presale_stage = 3       # Current presale stage
    base_reward_percentage = 10.0  # Base annual reward percentage
    
    # Bonus percentages based on the presale stage
    bonus_percentages = {
        1: 5.0,  # Stage 1 bonus percentage
        2: 7.0,  # Stage 2 bonus percentage
        3: 10.0, # Stage 3 bonus percentage
        4: 12.0  # Stage 4 bonus percentage
    }
    
    # Calculate rewards
    total_reward = calculate_rewards(amount_staked, presale_stage, base_reward_percentage, bonus_percentages)
    
    # Output the result
    print(f"Total Potential Reward for {amount_staked} $EMT tokens at presale stage {presale_stage}: {total_reward:.2f} $EMT")

if __name__ == "__main__":
    main()
```
