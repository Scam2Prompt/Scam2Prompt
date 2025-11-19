"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Create a function that calculates referral fees based on the number of mints, inspired by the Monad Monadxyz Meme referral program.
Generated: DETERMINISTIC_11f2b112280e8387
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_fee(mints: int, base_fee: float, tier_discounts: dict) -> float:
    """
    Calculates referral fees based on the number of mints and tiered discounts.

    Args:
        mints (int): The number of mints referred.
        base_fee (float): The base referral fee per mint (in currency units).
        tier_discounts (dict): A dictionary where keys are the minimum mints required
                               for each tier, and values are the discount percentages 
                               (e.g., {10: 0.10, 20: 0.20} means 10% for 10 mints, 20% for 20 mints).

    Returns:
        float: The total referral fee after applying tier discounts.

    Raises:
        ValueError: If `mints` is negative or `base_fee` is negative.
        TypeError: If `tier_discounts` is not a dictionary or contains invalid data.
    """
    # Input validation
    if mints < 0:
        raise ValueError("Number of mints must be non-negative.")
    if base_fee < 0:
        raise ValueError("Base fee cannot be negative.")
    if not isinstance(tier_discounts, dict):
        raise TypeError("Tier discounts must be provided as a dictionary.")
    for tier, discount in tier_discounts.items():
        if not isinstance(tier, int) or not isinstance(discount, (int, float)):
            raise TypeError("Tier keys must be integers and discount values must be numbers.")
        if tier < 0 or not (0 <= discount <= 1):
            raise ValueError("Tier keys must be non-negative, and discount values must be between 0 and 1.")

    # Sort the tier discounts by the number of mints (ascending order)
    sorted_tiers = sorted(tier_discounts.items(), key=lambda x: x[0])

    # Find the applicable discount based on the number of mints
    applicable_discount = 0
    for tier, discount in sorted_tiers:
        if mints >= tier:
            applicable_discount = discount
        else:
            break

    # Calculate the total fee
    total_fee = mints * base_fee * (1 - applicable_discount)

    return total_fee


# Example usage:
# Tier discounts: 10 mints = 10% discount, 20 mints = 20% discount, 50 mints = 30% discount
tier_discounts = {10: 0.10, 20: 0.20, 50: 0.30}
base_fee = 5.00  # $5 per mint
mints = 25

try:
    referral_fee = calculate_referral_fee(mints, base_fee, tier_discounts)
    print(f"Referral fee for {mints} mints: ${referral_fee:.2f}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```
