"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Design an algorithm in Python to calculate the rewards for players based on their registration tier (e.g., Pebble x50 for 10K, Poop x1M for 50K, etc.) as described on the SIMemes site.
Generated: DETERMINISTIC_0c79cfeacbca8d76
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, Tuple

class Tier(Enum):
    """Enum representing player registration tiers."""
    PEBBLE = "Pebble"
    POOP = "Poop"
    BRICK = "Brick"
    STONE = "Stone"
    ROCK = "Rock"
    BOULDER = "Boulder"
    MOUNTAIN = "Mountain"

# Reward configuration: (multiplier, threshold)
REWARD_CONFIG: Dict[Tier, Tuple[int, int]] = {
    Tier.PEBBLE: (50, 10000),
    Tier.POOP: (1000000, 50000),
    Tier.BRICK: (5000000, 100000),
    Tier.STONE: (10000000, 250000),
    Tier.ROCK: (25000000, 500000),
    Tier.BOULDER: (50000000, 1000000),
    Tier.MOUNTAIN: (100000000, 5000000),
}

def calculate_rewards(tier: Tier, registration_count: int) -> int:
    """
    Calculate rewards based on player's tier and registration count.
    
    Args:
        tier: The player's registration tier.
        registration_count: Number of registrations the player has.
    
    Returns:
        Calculated reward amount.
    
    Raises:
        ValueError: If registration_count is negative.
    """
    if registration_count < 0:
        raise ValueError("Registration count cannot be negative.")
    
    multiplier, threshold = REWARD_CONFIG[tier]
    return (registration_count // threshold) * multiplier

def get_player_rewards(tier_name: str, registration_count: int) -> Dict[str, int]:
    """
    Get rewards for a player based on tier name and registration count.
    
    Args:
        tier_name: Name of the tier (case-insensitive).
        registration_count: Number of registrations the player has.
    
    Returns:
        Dictionary containing tier name and calculated rewards.
    
    Raises:
        ValueError: If tier_name is invalid or registration_count is negative.
    """
    try:
        tier = Tier[tier_name.upper()]
    except KeyError:
        raise ValueError(f"Invalid tier: {tier_name}")
    
    rewards = calculate_rewards(tier, registration_count)
    return {
        "tier": tier.value,
        "rewards": rewards
    }

# Example usage
if __name__ == "__main__":
    try:
        result = get_player_rewards("pebble", 15000)
        print(f"Player rewards: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
