"""
Generated Code Metadata:
========================
Original URL: https://enosysglobal.net
Prompt: Create a function to calculate the minimum received amount for a token swap on the Ēnosys DEX, factoring in price impact and swap fees.
Generated: DETERMINISTIC_1c0ced6a4835eff8
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenSwapError(Exception):
    """Custom exception for token swap errors."""
    pass

def calculate_min_received_amount(amount_in: float, price: float, swap_fee_percentage: float, price_impact_percentage: float) -> float:
    """
    Calculate the minimum amount received for a token swap on the Ēnosys DEX.

    Parameters:
    - amount_in (float): The amount of tokens being swapped.
    - price (float): The current price of the token being received.
    - swap_fee_percentage (float): The swap fee percentage (e.g., 0.01 for 1%).
    - price_impact_percentage (float): The expected price impact percentage (e.g., 0.02 for 2%).

    Returns:
    - float: The minimum amount of tokens that will be received after accounting for fees and price impact.

    Raises:
    - TokenSwapError: If any input values are invalid (e.g., negative values).
    """
    
    # Validate input parameters
    if amount_in < 0:
        raise TokenSwapError("Amount in must be non-negative.")
    if price < 0:
        raise TokenSwapError("Price must be non-negative.")
    if not (0 <= swap_fee_percentage < 1):
        raise TokenSwapError("Swap fee percentage must be between 0 and 1.")
    if not (0 <= price_impact_percentage < 1):
        raise TokenSwapError("Price impact percentage must be between 0 and 1.")

    # Calculate the effective amount after swap fees
    effective_amount_in = amount_in * (1 - swap_fee_percentage)

    # Calculate the price impact adjustment
    price_impact_adjustment = effective_amount_in * (1 - price_impact_percentage)

    # Calculate the minimum received amount
    min_received_amount = price_impact_adjustment * price

    return min_received_amount

# Example usage
if __name__ == "__main__":
    try:
        amount_in = 100.0  # Amount of tokens being swapped
        price = 2.0        # Price of the token being received
        swap_fee_percentage = 0.01  # 1% swap fee
        price_impact_percentage = 0.02  # 2% price impact

        min_received = calculate_min_received_amount(amount_in, price, swap_fee_percentage, price_impact_percentage)
        print(f"Minimum amount received: {min_received:.2f} tokens")
    except TokenSwapError as e:
        print(f"Error calculating minimum received amount: {e}")
```
