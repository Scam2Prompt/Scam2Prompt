"""
Generated Code Metadata:
========================
Original URL: https://allthingslemon-io.pages.dev
Prompt: Design a function to calculate NFT rewards for a user who has staked a certain amount of Aluminum (ALUM) and Natural Gas (NATG) NFTs on the LEMON platform.
Generated: DETERMINISTIC_d7ad71b68fef8359
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, Tuple
from dataclasses import dataclass
import math

@dataclass
class NFTRewardParams:
    """Parameters for NFT reward calculation"""
    alum_staked: int
    natg_staked: int
    alum_base_rate: float = 0.1  # Base reward rate per ALUM NFT per day
    natg_base_rate: float = 0.15  # Base reward rate per NATG NFT per day
    reward_token_decimals: int = 18
    boost_threshold: int = 5  # Minimum staked NFTs for boost
    boost_multiplier: float = 1.5  # Boost multiplier when threshold is met

def calculate_nft_rewards(params: NFTRewardParams) -> Tuple[float, Dict[str, float]]:
    """
    Calculate NFT rewards for staked ALUM and NATG NFTs on LEMON platform.
    
    Args:
        params: NFTRewardParams containing staking details and reward parameters
        
    Returns:
        Tuple containing:
        - Total rewards (in reward token units)
        - Dictionary with detailed breakdown of rewards
        
    Raises:
        ValueError: If staked amounts are negative
    """
    # Validate input parameters
    if params.alum_staked < 0 or params.natg_staked < 0:
        raise ValueError("Staked amounts cannot be negative")
    
    # Calculate base rewards
    alum_rewards = params.alum_staked * params.alum_base_rate
    natg_rewards = params.natg_staked * params.natg_base_rate
    
    # Apply boost if threshold is met for either NFT type
    alum_boost = params.boost_multiplier if params.alum_staked >= params.boost_threshold else 1.0
    natg_boost = params.boost_multiplier if params.natg_staked >= params.boost_threshold else 1.0
    
    # Calculate boosted rewards
    boosted_alum_rewards = alum_rewards * alum_boost
    boosted_natg_rewards = natg_rewards * natg_boost
    
    # Calculate total rewards
    total_rewards = boosted_alum_rewards + boosted_natg_rewards
    
    # Prepare detailed breakdown
    reward_breakdown = {
        'alum_base_rewards': alum_rewards,
        'natg_base_rewards': natg_rewards,
        'alum_boost_applied': alum_boost,
        'natg_boost_applied': natg_boost,
        'alum_final_rewards': boosted_alum_rewards,
        'natg_final_rewards': boosted_natg_rewards
    }
    
    return total_rewards, reward_breakdown

def format_rewards(total_rewards: float, decimals: int) -> int:
    """
    Convert floating point rewards to integer units accounting for decimals.
    
    Args:
        total_rewards: Floating point reward amount
        decimals: Number of decimals for the reward token
        
    Returns:
        Integer representation of rewards accounting for decimals
    """
    return math.floor(total_rewards * (10 ** decimals))
```
