"""
Generated Code Metadata:
========================
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings for a user based on the number of mints completed through their referral link, inspired by Monadverse2's model.
Generated: DETERMINISTIC_e3f6de2315dfd89a
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_earnings(mints_completed, base_rate=0.1, tier_thresholds=[10, 50, 100], tier_multipliers=[1.0, 1.5, 2.0]):
    """
    Calculate referral earnings based on the number of mints completed through a referral link.
    
    Args:
        mints_completed (int): Number of mints completed through the referral link.
        base_rate (float, optional): Base earnings per mint. Defaults to 0.1.
        tier_thresholds (list, optional): List of mint thresholds for different tiers. Defaults to [10, 50, 100].
        tier_multipliers (list, optional): List of multipliers corresponding to each tier. Defaults to [1.0, 1.5, 2.0].
    
    Returns:
        float: Total referral earnings.
    
    Raises:
        ValueError: If mints_completed is negative or if tier_thresholds and tier_multipliers lengths don't match.
    """
    # Validate inputs
    if mints_completed < 0:
        raise ValueError("mints_completed cannot be negative")
    if len(tier_thresholds) != len(tier_multipliers):
        raise ValueError("tier_thresholds and tier_multipliers must have the same length")
    
    # Sort thresholds and multipliers in ascending order (just in case)
    sorted_tiers = sorted(zip(tier_thresholds, tier_multipliers), key=lambda x: x[0])
    tier_thresholds = [t[0] for t in sorted_tiers]
    tier_multipliers = [t[1] for t in sorted_tiers]
    
    total_earnings = 0.0
    previous_threshold = 0
    
    # Calculate earnings for each tier
    for threshold, multiplier in zip(tier_thresholds, tier_multipliers):
        if mints_completed <= previous_threshold:
            break
        
        mints_in_tier = min(mints_completed, threshold) - previous_threshold
        tier_earnings = mints_in_tier * base_rate * multiplier
        total_earnings += tier_earnings
        previous_threshold = threshold
    
    # Calculate earnings for any mints above the highest tier
    if mints_completed > previous_threshold:
        mints_above = mints_completed - previous_threshold
        if tier_multipliers:  # Use the highest multiplier if there are any tiers
            highest_multiplier = max(tier_multipliers)
        else:  # No tiers, just use base rate
            highest_multiplier = 1.0
        total_earnings += mints_above * base_rate * highest_multiplier
    
    return total_earnings
```
