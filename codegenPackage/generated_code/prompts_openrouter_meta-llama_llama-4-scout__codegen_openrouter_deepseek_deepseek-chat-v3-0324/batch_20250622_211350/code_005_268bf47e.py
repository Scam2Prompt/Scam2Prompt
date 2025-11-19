"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Design a function to calculate the $BASED token allocation for a user based on the number of NFTs they redeem and the redemption phase.
Generated: DETERMINISTIC_268bf47e13d21d4e
Batch ID: 20250622_211350
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

class RedemptionPhase(Enum):
    """
    Enum representing the different redemption phases for $BASED token allocation.
    """
    EARLY = 1
    MID = 2
    LATE = 3

def calculate_based_allocation(
    num_nfts_redeemed: int,
    redemption_phase: RedemptionPhase,
    phase_multipliers: Dict[RedemptionPhase, float] = None,
    base_allocation: float = 100.0
) -> float:
    """
    Calculate the $BASED token allocation for a user based on the number of NFTs redeemed and the redemption phase.

    Args:
        num_nfts_redeemed: Number of NFTs redeemed by the user (must be >= 0).
        redemption_phase: The redemption phase (EARLY, MID, LATE).
        phase_multipliers: Optional dictionary mapping redemption phases to multipliers.
                          Defaults to EARLY=1.5, MID=1.2, LATE=1.0.
        base_allocation: Base allocation per NFT. Defaults to 100.0.

    Returns:
        Total $BASED token allocation for the user.

    Raises:
        ValueError: If num_nfts_redeemed is negative or phase_multipliers is invalid.
    """
    # Validate input
    if num_nfts_redeemed < 0:
        raise ValueError("Number of NFTs redeemed cannot be negative.")
    
    # Set default phase multipliers if not provided
    if phase_multipliers is None:
        phase_multipliers = {
            RedemptionPhase.EARLY: 1.5,
            RedemptionPhase.MID: 1.2,
            RedemptionPhase.LATE: 1.0
        }
    
    # Validate phase_multipliers
    if not all(phase in phase_multipliers for phase in RedemptionPhase):
        raise ValueError("phase_multipliers must include all redemption phases.")
    
    # Calculate allocation
    multiplier = phase_multipliers[redemption_phase]
    total_allocation = num_nfts_redeemed * base_allocation * multiplier
    
    return total_allocation
```
