"""
Generated Code Metadata:
========================
Original URL: https://presale-apedinbase.pages.dev
Prompt: Write a function that calculates the minimum and maximum contribution amounts for the APED token presale based on the provided ETH limits.
Generated: DETERMINISTIC_cf37a2a7a539328e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_contribution_limits(min_eth: float, max_eth: float, token_price: float) -> dict:
    """
    Calculate the minimum and maximum contribution amounts for the APED token presale.

    Parameters:
    min_eth (float): The minimum amount of ETH that can be contributed.
    max_eth (float): The maximum amount of ETH that can be contributed.
    token_price (float): The price of one APED token in ETH.

    Returns:
    dict: A dictionary containing the minimum and maximum contribution amounts in APED tokens.
    """
    # Validate input types
    if not (isinstance(min_eth, (int, float)) and isinstance(max_eth, (int, float)) and isinstance(token_price, (int, float))):
        raise ValueError("min_eth, max_eth, and token_price must be numeric values.")

    # Validate that ETH limits are non-negative
    if min_eth < 0 or max_eth < 0:
        raise ValueError("min_eth and max_eth must be non-negative values.")

    # Validate that the token price is positive
    if token_price <= 0:
        raise ValueError("token_price must be a positive value.")

    # Calculate minimum and maximum contributions in APED tokens
    min_contribution = min_eth / token_price
    max_contribution = max_eth / token_price

    # Return results as a dictionary
    return {
        "min_contribution": min_contribution,
        "max_contribution": max_contribution
    }

# Example usage
if __name__ == "__main__":
    try:
        limits = calculate_contribution_limits(0.1, 5.0, 0.01)
        print(f"Minimum Contribution: {limits['min_contribution']} APED tokens")
        print(f"Maximum Contribution: {limits['max_contribution']} APED tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
