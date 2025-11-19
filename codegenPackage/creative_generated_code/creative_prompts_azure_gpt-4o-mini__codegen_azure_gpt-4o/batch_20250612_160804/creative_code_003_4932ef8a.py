"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demexswap.pages.dev
Prompt: Create a function that calculates trading fees based on the Demex fee structure for different trading tiers.
Generated: DETERMINISTIC_4932ef8acc60883c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_trading_fee(trading_volume: float, tier: str) -> float:
    """
    Calculate the trading fee based on the Demex fee structure for different trading tiers.

    Parameters:
        trading_volume (float): The amount of trading volume in the transaction.
        tier (str): The trading tier of the user. Valid tiers: "Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5".

    Returns:
        float: The calculated trading fee.

    Raises:
        ValueError: If the tier is invalid or if trading_volume is negative.
    """
    # Fee percentages for different tiers (as per Demex fee structure)
    fee_structure = {
        "Tier 1": 0.0010,  # 0.10%
        "Tier 2": 0.0008,  # 0.08%
        "Tier 3": 0.0006,  # 0.06%
        "Tier 4": 0.0004,  # 0.04%
        "Tier 5": 0.0002,  # 0.02%
    }

    # Validate the input parameters
    if trading_volume < 0:
        raise ValueError("Trading volume cannot be negative.")
    if tier not in fee_structure:
        raise ValueError(f"Invalid tier '{tier}'. Valid tiers are: {', '.join(fee_structure.keys())}.")

    # Calculate the trading fee based on the tier and trading volume
    fee_rate = fee_structure[tier]
    trading_fee = trading_volume * fee_rate

    return trading_fee


# Example usage (remove or replace in production code):
try:
    volume = 100000.0  # Example trading volume
    user_tier = "Tier 2"  # Example user tier
    fee = calculate_trading_fee(volume, user_tier)
    print(f"Trading Fee for volume {volume} on {user_tier}: {fee:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
