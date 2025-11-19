"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Write a Python script that simulates the weekly distribution of SOL rewards to top contributors on Loud, based on their mindshare rankings.
Generated: DETERMINISTIC_07148073d3c3ed29
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Contributor:
    """Class representing a contributor with a name and mindshare ranking."""
    
    def __init__(self, name: str, mindshare: float):
        self.name = name
        self.mindshare = mindshare

    def __repr__(self):
        return f"{self.name} (Mindshare: {self.mindshare})"

def distribute_rewards(contributors: List[Contributor], total_rewards: float) -> Dict[str, float]:
    """
    Distributes SOL rewards to contributors based on their mindshare rankings.

    Args:
        contributors (List[Contributor]): List of contributors.
        total_rewards (float): Total SOL rewards to be distributed.

    Returns:
        Dict[str, float]: A dictionary mapping contributor names to their respective rewards.
    """
    if total_rewards <= 0:
        raise ValueError("Total rewards must be greater than zero.")
    
    if not contributors:
        raise ValueError("Contributor list cannot be empty.")

    # Calculate total mindshare
    total_mindshare = sum(contributor.mindshare for contributor in contributors)
    
    if total_mindshare == 0:
        raise ValueError("Total mindshare cannot be zero.")

    # Distribute rewards based on mindshare
    rewards_distribution = {}
    for contributor in contributors:
        # Calculate reward based on the proportion of mindshare
        reward = (contributor.mindshare / total_mindshare) * total_rewards
        rewards_distribution[contributor.name] = round(reward, 2)  # Round to 2 decimal places

    return rewards_distribution

def main():
    """Main function to simulate the reward distribution."""
    # Sample contributors with their mindshare rankings
    contributors = [
        Contributor("Alice", 150.0),
        Contributor("Bob", 100.0),
        Contributor("Charlie", 50.0),
        Contributor("Diana", 200.0)
    ]

    # Total SOL rewards to distribute
    total_rewards = 500.0

    try:
        rewards = distribute_rewards(contributors, total_rewards)
        print("Rewards Distribution:")
        for name, reward in rewards.items():
            print(f"{name}: {reward} SOL")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
