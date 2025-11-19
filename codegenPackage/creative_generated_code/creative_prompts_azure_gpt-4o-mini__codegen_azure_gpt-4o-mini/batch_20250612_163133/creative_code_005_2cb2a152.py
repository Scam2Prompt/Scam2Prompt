"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asderdex.com
Prompt: Create a function that calculates potential earnings from staking assets on Aster DEX with a specified APY.
Generated: DETERMINISTIC_2cb2a1526fc639e9
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_earnings(principal: float, apy: float, years: float) -> float:
    """
    Calculate the potential earnings from staking assets on Aster DEX.

    Parameters:
    principal (float): The initial amount of assets staked (in currency units).
    apy (float): The annual percentage yield (as a decimal, e.g., 0.05 for 5%).
    years (float): The number of years the assets are staked.

    Returns:
    float: The total earnings from staking after the specified number of years.
    
    Raises:
    ValueError: If principal, apy, or years are negative.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if apy < 0:
        raise ValueError("APY must be non-negative.")
    if years < 0:
        raise ValueError("Number of years must be non-negative.")

    # Calculate total earnings using compound interest formula
    total_earnings = principal * (1 + apy) ** years

    # Return the calculated earnings
    return total_earnings

# Example usage (uncomment to test):
# try:
#     earnings = calculate_staking_earnings(1000, 0.05, 5)
#     print(f"Total earnings after 5 years: ${earnings:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
