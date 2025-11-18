"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Write a function in Python to calculate and distribute rewards to Lingo token holders based on their proportional contributions to the RWA pool.
Generated: DETERMINISTIC_7a977b4e874ce3d4
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Tuple

def calculate_rewards(rwa_pool: float, contributions: Dict[str, float], total_rewards: float) -> Dict[str, float]:
    """
    Calculate and distribute rewards to token holders based on their proportional contributions to the RWA pool.

    Args:
        rwa_pool (float): Total value of the Real World Asset (RWA) pool.
        contributions (Dict[str, float]): A dictionary where the key is the token holder's ID and the value is their contribution to the RWA pool.
        total_rewards (float): Total rewards to be distributed among token holders.

    Returns:
        Dict[str, float]: A dictionary with token holder IDs as keys and their corresponding rewards as values.
    """
    if rwa_pool <= 0:
        raise ValueError("RWA pool must be greater than zero.")
    if total_rewards <= 0:
        raise ValueError("Total rewards must be greater than zero.")
    if not contributions:
        raise ValueError("Contributions dictionary cannot be empty.")

    # Calculate total contributions
    total_contributions = sum(contributions.values())
    if total_contributions <= 0:
        raise ValueError("Total contributions must be greater than zero.")

    # Validate contributions
    for holder, contribution in contributions.items():
        if contribution < 0:
            raise ValueError(f"Contribution for holder {holder} cannot be negative.")

    # Calculate rewards for each token holder
    rewards_distribution = {}
    for holder, contribution in contributions.items():
        proportion = contribution / total_contributions
        holder_reward = proportion * total_rewards
        rewards_distribution[holder] = round(holder_reward, 2)  # Round to 2 decimal places for precision

    return rewards_distribution


# Example usage
if __name__ == "__main__":
    # Sample data: Token holders and their contributions
    token_contributions = {
        "holder_1": 1000,
        "holder_2": 2000,
        "holder_3": 1500,
    }
    rwa_pool_value = 4500
    total_reward_amount = 1000

    try:
        rewards = calculate_rewards(rwa_pool_value, token_contributions, total_reward_amount)
        print("Rewards Distribution:")
        for holder, reward in rewards.items():
            print(f"{holder}: {reward} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
