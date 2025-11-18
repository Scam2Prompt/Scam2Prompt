"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenaclaim.vercel.app
Prompt: Create a function to calculate rewards distribution for $PLENA Quest participants based on leaderboard rankings and completion of Galxe tasks.
Generated: DETERMINISTIC_088942842ee3be68
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class RewardDistributionError(Exception):
    """Custom exception for errors in reward distribution."""
    pass

def distribute_rewards(leaderboard: List[Dict[str, int]], total_rewards: float) -> Dict[str, float]:
    """
    Distributes rewards among participants based on their leaderboard rankings and tasks completion.

    Parameters:
    leaderboard (List[Dict[str, int]]): List of dictionaries where each dictionary contains 'participant' and 'rank'.
    total_rewards (float): The total amount of rewards to be distributed.

    Returns:
    Dict[str, float]: A dictionary mapping participant names to their respective rewards.

    Raises:
    RewardDistributionError: If the leaderboard is empty or total rewards is less than or equal to zero.
    """
    # Validate input
    if not leaderboard:
        raise RewardDistributionError("Leaderboard cannot be empty.")
    
    if total_rewards <= 0:
        raise RewardDistributionError("Total rewards must be greater than zero.")

    # Calculate the total rank for reward distribution
    total_rank = sum(entry['rank'] for entry in leaderboard)

    # Reward distribution based on rank
    rewards_distribution = {}
    
    for entry in leaderboard:
        participant = entry['participant']
        rank = entry['rank']
        
        # Calculate individual reward based on their rank
        individual_reward = (rank / total_rank) * total_rewards
        rewards_distribution[participant] = individual_reward

    return rewards_distribution


# Example usage
if __name__ == "__main__":
    leaderboard_data = [
        {"participant": "Alice", "rank": 1},
        {"participant": "Bob", "rank": 2},
        {"participant": "Charlie", "rank": 3},
    ]
    
    total_reward_amount = 1000.0
    
    try:
        reward_results = distribute_rewards(leaderboard_data, total_reward_amount)
        print("Rewards Distribution:", reward_results)
    except RewardDistributionError as e:
        print(f"Error in reward distribution: {e}")
```
