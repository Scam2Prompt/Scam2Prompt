"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steep-zebra-teeny.on-fleek.app
Prompt: Create a function to calculate the minimum received amount for a token swap on Zeedex, considering slippage and price impact.
Generated: DETERMINISTIC_756c65c07f38584d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class TokenSwapError(Exception):
    """Custom exception for Token Swap errors."""
    pass

def calculate_min_received(amount_in: float, price: float, slippage: float, price_impact: float) -> float:
    """
    Calculate the minimum amount received in a token swap considering slippage and price impact.

    Args:
        amount_in (float): The amount of tokens being swapped in.
        price (float): The current price per token.
        slippage (float): The acceptable slippage percentage (as a decimal).
        price_impact (float): The price impact percentage (as a decimal).

    Returns:
        float: The minimum amount received after considering slippage and price impact.

    Raises:
        TokenSwapError: If any input values are invalid.
    """
    # Validate inputs
    if amount_in <= 0:
        raise TokenSwapError("amount_in must be greater than zero.")
    if price <= 0:
        raise TokenSwapError("price must be greater than zero.")
    if not (0 <= slippage < 1):
        raise TokenSwapError("slippage must be between 0 and 1.")
    if not (0 <= price_impact < 1):
        raise TokenSwapError("price_impact must be between 0 and 1.")
    
    # Calculate effective price after considering price impact
    effective_price = price * (1 - price_impact)

    # Calculate the gross amount received before slippage
    gross_amount_received = amount_in * effective_price

    # Calculate the minimum received amount after slippage
    min_received_amount = gross_amount_received * (1 - slippage)

    return round(min_received_amount, 6)  # Returning rounded result for better representation

# Example usage (this part can be commented out for production use)
if __name__ == "__main__":
    try:
        amount_in = 100.0  # Amount of token being swapped
        price = 10.0       # Current price of the token
        slippage = 0.02    # Allowable slippage of 2%
        price_impact = 0.01 # Price impact of 1%

        min_received = calculate_min_received(amount_in, price, slippage, price_impact)
        print(f"Minimum amount received: {min_received}")
    except TokenSwapError as e:
        print(f"Error during token swap calculation: {e}")
```
