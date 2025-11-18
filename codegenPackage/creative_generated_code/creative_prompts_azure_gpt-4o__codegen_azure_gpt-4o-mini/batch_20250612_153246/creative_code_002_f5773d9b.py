"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-zkasino.pages.dev
Prompt: Create a function to calculate the total ZKAS earned for a given ETH deposit amount using the TVL per ZKAS value provided on the ZKasino Bridge page.
Generated: DETERMINISTIC_f5773d9b1a296411
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_zkas_earned(eth_deposit: float, tvl_per_zkas: float) -> float:
    """
    Calculate the total ZKAS earned for a given ETH deposit amount.

    Parameters:
        eth_deposit (float): The amount of ETH deposited.
        tvl_per_zkas (float): The Total Value Locked (TVL) per ZKAS.

    Returns:
        float: The total ZKAS earned for the given ETH deposit amount.

    Raises:
        ValueError: If eth_deposit or tvl_per_zkas is negative or zero.
    """

    # Validate inputs
    if eth_deposit <= 0:
        raise ValueError("ETH deposit must be greater than zero.")
    if tvl_per_zkas <= 0:
        raise ValueError("TVL per ZKAS must be greater than zero.")

    # Calculate total ZKAS earned
    zkas_earned = eth_deposit * tvl_per_zkas

    return zkas_earned


# Example usage (commented out for production-ready code)
# try:
#     eth_amount = 1.5  # Example ETH deposit
#     tvl_value = 1000.0  # Example TVL per ZKAS value
#     total_zkas = calculate_zkas_earned(eth_amount, tvl_value)
#     print(f"Total ZKAS earned: {total_zkas}")
# except ValueError as e:
#     print(f"Error: {e}")
```
