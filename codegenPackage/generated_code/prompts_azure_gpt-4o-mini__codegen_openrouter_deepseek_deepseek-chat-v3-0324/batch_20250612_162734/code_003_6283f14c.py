"""
Generated Code Metadata:
========================
Original URL: https://unichain-pass.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a unique referral link for an NFT project.
Generated: DETERMINISTIC_6283f14cddd54fb0
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_earnings(mints: int, base_rate: float, tier_thresholds: list, tier_multipliers: list) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.
    
    Args:
        mints (int): Number of mints completed through the referral link.
        base_rate (float): Base earnings per mint (in the project's currency).
        tier_thresholds (list): List of mint thresholds for each tier (ascending order).
        tier_multipliers (list): List of multipliers corresponding to each tier (same order as thresholds).
        
    Returns:
        float: Total referral earnings.
        
    Raises:
        ValueError: If inputs are invalid (negative values, empty lists, etc.).
        TypeError: If inputs are of incorrect types.
    """
    # Validate input types
    if not isinstance(mints, int) or not isinstance(base_rate, (int, float)):
        raise TypeError("mints must be an integer and base_rate must be a number")
    if not isinstance(tier_thresholds, list) or not isinstance(tier_multipliers, list):
        raise TypeError("tier_thresholds and tier_multipliers must be lists")
    
    # Validate input values
    if mints < 0 or base_rate < 0:
        raise ValueError("mints and base_rate must be non-negative")
    if len(tier_thresholds) != len(tier_multipliers):
        raise ValueError("tier_thresholds and tier_multipliers must have the same length")
    if any(t < 0 for t in tier_thresholds) or any(m < 0 for m in tier_multipliers):
        raise ValueError("tier thresholds and multipliers must be non-negative")
    
    # Ensure tier_thresholds are in ascending order
    for i in range(1, len(tier_thresholds)):
        if tier_thresholds[i] <= tier_thresholds[i-1]:
            raise ValueError("tier_thresholds must be in ascending order")
    
    # Calculate earnings
    earnings = 0.0
    previous_threshold = 0
    
    for threshold, multiplier in zip(tier_thresholds, tier_multipliers):
        if mints <= previous_threshold:
            break
        mints_in_tier = min(mints, threshold) - previous_threshold
        earnings += mints_in_tier * base_rate * multiplier
        previous_threshold = threshold
    
    # Handle mints beyond the highest tier
    if mints > previous_threshold:
        mints_in_top_tier = mints - previous_threshold
        top_multiplier = tier_multipliers[-1] if tier_multipliers else 1.0
        earnings += mints_in_top_tier * base_rate * top_multiplier
    
    return earnings
```
