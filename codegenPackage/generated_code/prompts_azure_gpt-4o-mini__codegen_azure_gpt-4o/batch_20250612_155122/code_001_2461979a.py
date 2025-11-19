"""
Generated Code Metadata:
========================
Original URL: https://enosysglobal.net
Prompt: Write a function that calculates the price impact of a swap transaction on the Ēnosys DEX using FLR and EETH.
Generated: DETERMINISTIC_2461979aa73783b0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 28

def calculate_price_impact(flare_pool: Decimal, eeth_pool: Decimal, swap_amount: Decimal, is_flare_to_eeth: bool) -> Decimal:
    """
    Calculate the price impact of a swap transaction on the Ēnosys DEX.

    Args:
        flare_pool (Decimal): Current liquidity of FLR in the pool.
        eeth_pool (Decimal): Current liquidity of EETH in the pool.
        swap_amount (Decimal): Amount of FLR or EETH being swapped.
        is_flare_to_eeth (bool): True if swapping FLR for EETH, False if swapping EETH for FLR.

    Returns:
        Decimal: Price impact as a percentage (0-100).
    """
    try:
        # Validate inputs
        if flare_pool <= 0 or eeth_pool <= 0 or swap_amount <= 0:
            raise ValueError("Pool balances and swap amount must be positive values.")

        # Calculate the invariant (constant product formula)
        invariant = flare_pool * eeth_pool

        # Determine new pool balances after the swap
        if is_flare_to_eeth:
            new_flare_pool = flare_pool + swap_amount
            new_eeth_pool = invariant / new_flare_pool
        else:
            new_eeth_pool = eeth_pool + swap_amount
            new_flare_pool = invariant / new_eeth_pool

        # Calculate the price before and after the swap
        price_before = eeth_pool / flare_pool
        price_after = new_eeth_pool / new_flare_pool

        # Calculate price impact as a percentage
        price_impact = ((price_after - price_before) / price_before) * 100

        # Return the absolute value of price impact
        return abs(price_impact)

    except Exception as e:
        # Handle unexpected errors gracefully
        raise RuntimeError(f"An error occurred while calculating price impact: {e}")

# Example usage:
if __name__ == "__main__":
    # Example pool balances and swap amount
    flare_pool = Decimal("10000")
    eeth_pool = Decimal("5000")
    swap_amount = Decimal("100")
    is_flare_to_eeth = True

    # Calculate price impact
    try:
        impact = calculate_price_impact(flare_pool, eeth_pool, swap_amount, is_flare_to_eeth)
        print(f"Price Impact: {impact:.6f}%")
    except RuntimeError as error:
        print(error)
```
