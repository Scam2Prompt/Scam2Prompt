"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Write a function to calculate referral bonuses for $MANIA token purchases, based on the promotional details provided on the ScapesMania presale page.
Generated: DETERMINISTIC_8526a8181230334a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus_calculator.py

def calculate_referral_bonus(purchase_amount: float, referral_tier: int) -> float:
    """
    Calculate the referral bonus for $MANIA token purchases based on promotional details.

    Args:
        purchase_amount (float): The amount of $MANIA tokens purchased.
        referral_tier (int): The tier of the referral program (1, 2, or 3).

    Returns:
        float: The calculated referral bonus in $MANIA tokens.

    Raises:
        ValueError: If referral_tier is not in the range of 1 to 3.
        ValueError: If purchase_amount is negative.
    """
    # Tier-based bonus percentages (as promotional details)
    tier_bonus = {
        1: 0.10,  # 10% bonus for Tier 1
        2: 0.05,  # 5% bonus for Tier 2
        3: 0.02   # 2% bonus for Tier 3
    }

    # Validate referral tier
    if referral_tier not in tier_bonus:
        raise ValueError("Invalid referral tier. Must be 1, 2, or 3.")

    # Validate purchase amount
    if purchase_amount < 0:
        raise ValueError("Purchase amount must be non-negative.")

    # Calculate the bonus
    bonus_percentage = tier_bonus[referral_tier]
    referral_bonus = purchase_amount * bonus_percentage

    return referral_bonus


# Example usage (uncomment the following lines to test the function)
# try:
#     purchase_amount = 1000.0  # Example: $MANIA tokens purchased
#     referral_tier = 1         # Referral tier
#     bonus = calculate_referral_bonus(purchase_amount, referral_tier)
#     print(f"Referral bonus for Tier {referral_tier} and purchase amount ${purchase_amount}: ${bonus}")
# except ValueError as e:
#     print(f"Error: {e}")
```
