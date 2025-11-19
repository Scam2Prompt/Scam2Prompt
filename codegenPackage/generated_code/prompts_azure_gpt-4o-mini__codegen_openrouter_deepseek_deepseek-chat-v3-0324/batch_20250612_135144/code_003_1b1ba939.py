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
def calculate_block_rewards(
    total_rewards: float,
    rpg_staked: float,
    total_rpg_staked: float,
    proposal_node_count: int,
    min_reward: float = 0.0
) -> dict:
    """
    Calculate block rewards for proposal nodes based on RPG staking ratio.
    
    Args:
        total_rewards (float): Total rewards to be distributed
        rpg_staked (float): RPG tokens staked by the node
        total_rpg_staked (float): Total RPG tokens staked in the network
        proposal_node_count (int): Number of proposal nodes
        min_reward (float, optional): Minimum reward per node. Defaults to 0.0.
        
    Returns:
        dict: {
            'node_reward': float,  # Reward for this node
            'total_distributed': float,  # Total rewards distributed
            'remaining_rewards': float  # Remaining rewards after distribution
        }
        
    Raises:
        ValueError: If input values are invalid
    """
    # Validate inputs
    if total_rewards <= 0:
        raise ValueError("Total rewards must be positive")
    if rpg_staked < 0:
        raise ValueError("Staked RPG cannot be negative")
    if total_rpg_staked <= 0:
        raise ValueError("Total staked RPG must be positive")
    if proposal_node_count <= 0:
        raise ValueError("Number of proposal nodes must be positive")
    if min_reward < 0:
        raise ValueError("Minimum reward cannot be negative")
    if rpg_staked > total_rpg_staked:
        raise ValueError("Node's staked RPG cannot exceed total staked RPG")
    
    # Calculate staking ratio
    staking_ratio = rpg_staked / total_rpg_staked
    
    # Calculate base reward based on staking ratio
    base_reward = total_rewards * staking_ratio
    
    # Apply minimum reward constraint
    node_reward = max(base_reward, min_reward)
    
    # Calculate total distributed and remaining rewards
    total_distributed = node_reward * proposal_node_count
    remaining_rewards = total_rewards - total_distributed
    
    return {
        'node_reward': node_reward,
        'total_distributed': total_distributed,
        'remaining_rewards': remaining_rewards
    }
```
