"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vetterplatform.pages.dev
Prompt: Create a function that calculates the total preons earned based on the amount of VSL staked and the user's Vetter tier.
Generated: DETERMINISTIC_31b2958d0808bd44
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VetterTier:
    """Enum for user Vetter tiers."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4

def calculate_preons(staked_amount: float, vetter_tier: int) -> float:
    """
    Calculate the total preons earned based on the amount of VSL staked 
    and the user's Vetter tier.

    Parameters:
    staked_amount (float): The amount of VSL staked by the user.
    vetter_tier (int): The user's Vetter tier. Must be an integer from 1 to 4.

    Returns:
    float: The total preons earned.

    Raises:
    ValueError: If staked_amount is negative or if vetter_tier is not valid.
    """
    # Validate the staked amount
    if staked_amount < 0:
        raise ValueError("Staked amount must be non-negative.")
    
    # Validate the vetter tier
    if vetter_tier not in [VetterTier.BRONZE, VetterTier.SILVER, 
                           VetterTier.GOLD, VetterTier.PLATINUM]:
        raise ValueError("Invalid Vetter tier. Must be one of: 1, 2, 3, 4.")

    # Define the preon multipliers for each tier
    tier_multipliers = {
        VetterTier.BRONZE: 1.0,
        VetterTier.SILVER: 1.5,
        VetterTier.GOLD: 2.0,
        VetterTier.PLATINUM: 3.0
    }

    # Calculate the total preons earned
    preons_earned = staked_amount * tier_multipliers[vetter_tier]
    
    return preons_earned

# Example usage (to be removed or commented out in production)
if __name__ == "__main__":
    try:
        staked = 1000.0  # Example staked amount
        tier = VetterTier.GOLD  # Example user tier
        total_preons = calculate_preons(staked, tier)
        print(f"Total preons earned: {total_preons}")
    except ValueError as e:
        print(f"Error: {e}")
```
