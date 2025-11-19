"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: Can you write a function to calculate the block rewards for proposal nodes based on the RPG staking ratio in the Rangers Protocol?
Generated: DETERMINISTIC_1b1ba9393fd37a5e
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

def calculate_block_rewards(staking_ratios: Dict[str, float], total_block_reward: float) -> Dict[str, float]:
    """
    Calculate block rewards for proposal nodes based on the RPG staking ratio.

    Parameters:
        staking_ratios (Dict[str, float]): A dictionary where keys are node IDs and values are their staking ratios.
        total_block_reward (float): The total block reward to be distributed.

    Returns:
        Dict[str, float]: A dictionary where keys are node IDs and values are their respective block rewards.
    """
    # Validate inputs
    if not staking_ratios or total_block_reward <= 0:
        raise ValueError("Invalid input: staking_ratios must be non-empty and total_block_reward must be positive.")

    # Calculate the total staking ratio
    total_staking_ratio = sum(staking_ratios.values())
    if total_staking_ratio <= 0:
        raise ValueError("Invalid staking ratios: Total staking ratio must be positive.")

    # Calculate rewards for each node
    block_rewards = {}
    for node_id, staking_ratio in staking_ratios.items():
        # Ensure staking ratio is non-negative
        if staking_ratio < 0:
            raise ValueError(f"Invalid staking ratio for node {node_id}: Staking ratio must be non-negative.")
        
        # Calculate the reward proportionally based on staking ratio
        block_rewards[node_id] = (staking_ratio / total_staking_ratio) * total_block_reward

    return block_rewards

# Example usage:
if __name__ == "__main__":
    # Example staking ratios for nodes
    staking_ratios_example = {
        "node1": 100.0,
        "node2": 200.0,
        "node3": 300.0
    }
    # Total block reward to distribute
    total_block_reward_example = 600.0

    try:
        rewards = calculate_block_rewards(staking_ratios_example, total_block_reward_example)
        print("Block Rewards:", rewards)
    except ValueError as e:
        print("Error:", e)
```
