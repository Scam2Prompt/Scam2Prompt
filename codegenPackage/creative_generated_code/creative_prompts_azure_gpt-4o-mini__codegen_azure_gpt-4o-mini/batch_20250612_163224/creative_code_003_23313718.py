"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Create a function that calculates the weekly rewards for top contributors in the Loud platform based on trading volume and fee distribution.
Generated: DETERMINISTIC_233137183c491097
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple

class Contributor:
    def __init__(self, name: str, trading_volume: float):
        """
        Initializes a Contributor instance.

        :param name: The name of the contributor.
        :param trading_volume: The total trading volume for the contributor.
        """
        self.name = name
        self.trading_volume = trading_volume

def calculate_weekly_rewards(contributors: List[Contributor], total_fees: float) -> List[Tuple[str, float]]:
    """
    Calculates the weekly rewards for top contributors based on their trading volume.

    :param contributors: A list of Contributor instances.
    :param total_fees: The total fees collected to distribute among contributors.
    :return: A list of tuples containing the contributor's name and their calculated reward.
    
    :raises ValueError: If total_fees is non-positive or if contributors list is empty.
    """
    if total_fees <= 0:
        raise ValueError("Total fees must be a positive value.")
    
    if not contributors:
        raise ValueError("The contributors list cannot be empty.")

    # Calculate total trading volume
    total_volume = sum(contributor.trading_volume for contributor in contributors)

    # Calculate rewards based on trading volume share
    rewards = []
    for contributor in contributors:
        if total_volume > 0:
            reward = (contributor.trading_volume / total_volume) * total_fees
        else:
            reward = 0
        rewards.append((contributor.name, reward))

    return rewards

# Example usage
if __name__ == "__main__":
    # List of contributors with their trading volumes
    contributors_list = [
        Contributor("Alice", 5000.0),
        Contributor("Bob", 3000.0),
        Contributor("Charlie", 2000.0)
    ]
    
    # Total fees collected in the week
    total_fees_collected = 1000.0
    
    try:
        # Calculate and print weekly rewards
        rewards = calculate_weekly_rewards(contributors_list, total_fees_collected)
        for name, reward in rewards:
            print(f"{name}: ${reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
