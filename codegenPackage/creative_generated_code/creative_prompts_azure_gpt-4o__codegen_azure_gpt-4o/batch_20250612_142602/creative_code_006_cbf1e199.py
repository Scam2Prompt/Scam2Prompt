"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x-token.pages.dev
Prompt: Generate code to calculate the remaining supply of "X Token" in the presale, considering the 25% reserved allocation.
Generated: DETERMINISTIC_cbf1e199d997ac9c
Batch ID: 20250612_142602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the remaining supply of "X Token" in a presale,
# considering a 25% reserved allocation.

def calculate_remaining_supply(total_supply, sold_tokens, reserved_percentage=25):
    """
    Calculate the remaining supply of tokens in a presale.

    Parameters:
    total_supply (int): The total supply of the token.
    sold_tokens (int): The number of tokens sold.
    reserved_percentage (float): Percentage of tokens reserved (default is 25%).

    Returns:
    int: Remaining tokens available for sale.
    """

    try:
        # Validate inputs are non-negative integers
        if total_supply < 0 or sold_tokens < 0:
            raise ValueError("Total supply and sold tokens must be non-negative numbers.")
        if sold_tokens > total_supply:
            raise ValueError("Sold tokens cannot exceed the total supply.")

        # Calculate the reserved allocation
        reserved_allocation = total_supply * (reserved_percentage / 100)

        # Calculate the remaining supply
        remaining_supply = total_supply - reserved_allocation - sold_tokens

        # Remaining supply cannot be negative
        if remaining_supply < 0:
            remaining_supply = 0

        return int(remaining_supply)

    except (TypeError, ValueError) as e:
        # Handle invalid input or calculation errors
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define total supply and sold tokens
    total_supply = 1000000  # Total supply of X Token
    sold_tokens = 500000    # Tokens sold in presale

    # Calculate remaining tokens
    remaining_tokens = calculate_remaining_supply(total_supply, sold_tokens)

    if remaining_tokens is not None:
        print(f"Remaining tokens available for presale: {remaining_tokens}")
```
