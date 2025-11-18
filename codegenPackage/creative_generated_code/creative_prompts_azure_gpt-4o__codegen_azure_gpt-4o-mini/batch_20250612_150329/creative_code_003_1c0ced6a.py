"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enosysglobal.net
Prompt: Create a function to calculate the minimum received amount for a token swap on the Ēnosys DEX, factoring in price impact and swap fees.
Generated: DETERMINISTIC_1c0ced6a4835eff8
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DexError(Exception):
    """Custom exception for handling Dex related errors."""
    pass


def calculate_min_received_amount(amount_in: float, price: float, swap_fee: float, price_impact: float) -> float:
    """
    Calculate the minimum amount received from a token swap on the Ēnosys DEX.

    Args:
        amount_in (float): The amount of tokens being swapped.
        price (float): The current price of the token being received.
        swap_fee (float): The fee percentage applied to the swap (0.01 for 1%).
        price_impact (float): The effect on price due to the size of the swap (0.01 for 1% impact).

    Returns:
        float: The minimum amount of tokens expected after the swap.

    Raises:
        DexError: If any input values are negative or invalid.
    """
    # Validate inputs
    if amount_in < 0:
        raise DexError("Input amount cannot be negative.")
    if price < 0:
        raise DexError("Price cannot be negative.")
    if not (0 <= swap_fee < 1):
        raise DexError("Swap fee must be between 0 and 1.")
    if not (0 <= price_impact < 1):
        raise DexError("Price impact must be between 0 and 1.")

    # Calculate the effective amount after considering swap fee
    effective_amount = amount_in * (1 - swap_fee)
    
    # Adjust the effective amount based on price impact
    adjusted_amount = effective_amount * (1 - price_impact)
    
    # Calculate the minimum amount received in terms of tokens
    min_received_amount = adjusted_amount / price
    
    return min_received_amount


# Example usage:
if __name__ == "__main__":
    try:
        amount_in = 1000.0  # Amount to swap
        price = 0.5         # Price of the token received
        swap_fee = 0.01     # 1% swap fee
        price_impact = 0.02  # 2% price impact
        
        min_amount = calculate_min_received_amount(amount_in, price, swap_fee, price_impact)
        print(f"Minimum amount received: {min_amount:.4f} tokens")
    except DexError as e:
        print(f"Error: {e}")
```
