"""
Generated Code Metadata:
========================
Original URL: https://onbeam.live
Prompt: Create a function to calculate rewards for staking BEAM and Node Tokens on the Beam Network, considering commission rates and staked amounts.
Generated: DETERMINISTIC_779e77f593195758
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple, Dict

def calculate_staking_rewards(
    beam_staked: float,
    node_staked: float,
    commission_rate: float,
    total_beam_staked: float,
    total_node_staked: float,
    beam_reward_pool: float,
    node_reward_pool: float,
    validator_fee: float = 0.0
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """
    Calculate staking rewards for BEAM and Node tokens considering commission rates.
    
    Args:
        beam_staked: Amount of BEAM tokens staked by user
        node_staked: Amount of Node tokens staked by user
        commission_rate: Validator's commission rate (0-1)
        total_beam_staked: Total BEAM tokens staked in the pool
        total_node_staked: Total Node tokens staked in the pool
        beam_reward_pool: Total BEAM rewards available for distribution
        node_reward_pool: Total Node rewards available for distribution
        validator_fee: Additional validator fee (0-1)
    
    Returns:
        Tuple of dictionaries containing:
        - First dict: User rewards (beam, node)
        - Second dict: Validator rewards (beam, node)
    
    Raises:
        ValueError: If input values are invalid
    """
    # Validate input parameters
    if any(val < 0 for val in [beam_staked, node_staked, total_beam_staked, 
                              total_node_staked, beam_reward_pool, node_reward_pool]):
        raise ValueError("Staked amounts and reward pools must be non-negative")
    
    if not 0 <= commission_rate <= 1:
        raise ValueError("Commission rate must be between 0 and 1")
    
    if not 0 <= validator_fee <= 1:
        raise ValueError("Validator fee must be between 0 and 1")
    
    # Calculate user's share of the staking pool
    beam_share = beam_staked / total_beam_staked if total_beam_staked > 0 else 0
    node_share = node_staked / total_node_staked if total_node_staked > 0 else 0
    
    # Calculate gross rewards before commission
    user_beam_gross = beam_reward_pool * beam_share
    user_node_gross = node_reward_pool * node_share
    
    # Calculate validator commission
    validator_beam_commission = user_beam_gross * commission_rate
    validator_node_commission = user_node_gross * commission_rate
    
    # Calculate validator fee (if any)
    validator_beam_fee = validator_beam_commission * validator_fee
    validator_node_fee = validator_node_commission * validator_fee
    
    # Calculate net rewards for user
    user_beam_net = user_beam_gross - validator_beam_commission
    user_node_net = user_node_gross - validator_node_commission
    
    # Calculate validator total rewards (commission + fee)
    validator_beam_total = validator_beam_commission + validator_beam_fee
    validator_node_total = validator_node_commission + validator_node_fee
    
    # Round to avoid floating point precision issues
    user_rewards = {
        'beam': round(user_beam_net, 8),
        'node': round(user_node_net, 8)
    }
    
    validator_rewards = {
        'beam': round(validator_beam_total, 8),
        'node': round(validator_node_total, 8)
    }
    
    return user_rewards, validator_rewards
```
