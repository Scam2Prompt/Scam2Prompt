"""
Generated Code Metadata:
========================
Original URL: https://satyloud.io
Prompt: Write a Python script to calculate weekly rewards in SOL for top contributors on Loud, assuming a 4% fee split and a specific mindshare distribution.
Generated: DETERMINISTIC_5befe6a0d938fcb8
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Tuple

def calculate_rewards(
    total_rewards_pool: float,
    fee_split_percentage: float,
    mindshare_distribution: Dict[str, float],
    contributors: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate weekly rewards for top contributors based on mindshare distribution and fee split.
    
    Args:
        total_rewards_pool: Total SOL rewards pool
        fee_split_percentage: Percentage of rewards allocated to fee split (e.g., 4%)
        mindshare_distribution: Dictionary mapping contributor types to their mindshare percentage
        contributors: Dictionary mapping contributor addresses to their contribution scores
        
    Returns:
        Dictionary mapping contributor addresses to their reward amounts in SOL
    """
    # Validate inputs
    if not (0 <= fee_split_percentage <= 100):
        raise ValueError("Fee split percentage must be between 0 and 100")
    
    if not contributors:
        raise ValueError("Contributors dictionary cannot be empty")
    
    total_mindshare = sum(mindshare_distribution.values())
    if not (99.9 <= total_mindshare <= 100.1):  # Allow for floating point rounding
        raise ValueError("Mindshare distribution must sum to 100%")
    
    # Calculate fee split allocation
    fee_split_allocation = total_rewards_pool * (fee_split_percentage / 100)
    remaining_allocation = total_rewards_pool - fee_split_allocation
    
    # Normalize contributor scores to get weights
    total_contributions = sum(contributors.values())
    if total_contributions <= 0:
        raise ValueError("Total contributions must be positive")
    
    contributor_weights = {
        addr: score / total_contributions 
        for addr, score in contributors.items()
    }
    
    # Calculate rewards for each contributor
    rewards = {}
    for addr, weight in contributor_weights.items():
        # Split reward between fee split and mindshare portions
        fee_split_portion = fee_split_allocation * weight
        mindshare_portion = remaining_allocation * mindshare_distribution.get(addr, 0) / 100
        rewards[addr] = fee_split_portion + mindshare_portion
    
    return rewards

def format_rewards(rewards: Dict[str, float], sol_price: float = None) -> List[Dict]:
    """
    Format rewards into a more readable structure, optionally converting to USD.
    
    Args:
        rewards: Dictionary of rewards in SOL
        sol_price: Optional SOL to USD conversion rate
        
    Returns:
        List of dictionaries with formatted reward information
    """
    formatted = []
    for addr, sol_amount in rewards.items():
        entry = {
            "address": addr,
            "reward_sol": round(sol_amount, 6)
        }
        if sol_price is not None:
            entry["reward_usd"] = round(sol_amount * sol_price, 2)
        formatted.append(entry)
    return formatted

def main():
    # Example configuration
    config = {
        "total_rewards_pool": 1000.0,  # 1000 SOL
        "fee_split_percentage": 4.0,   # 4%
        "mindshare_distribution": {
            "addr1": 30.0,
            "addr2": 25.0,
            "addr3": 20.0,
            "addr4": 15.0,
            "addr5": 10.0
        },
        "contributors": {
            "addr1": 5000,
            "addr2": 3000,
            "addr3": 2000,
            "addr4": 1000,
            "addr5": 500
        },
        "sol_price": 20.0  # $20 per SOL
    }
    
    try:
        # Calculate rewards
        rewards = calculate_rewards(
            config["total_rewards_pool"],
            config["fee_split_percentage"],
            config["mindshare_distribution"],
            config["contributors"]
        )
        
        # Format results
        formatted_rewards = format_rewards(rewards, config.get("sol_price"))
        
        # Output results
        print("Weekly Rewards Distribution:")
        print(json.dumps(formatted_rewards, indent=2))
        
    except Exception as e:
        print(f"Error calculating rewards: {str(e)}")

if __name__ == "__main__":
    main()
```
