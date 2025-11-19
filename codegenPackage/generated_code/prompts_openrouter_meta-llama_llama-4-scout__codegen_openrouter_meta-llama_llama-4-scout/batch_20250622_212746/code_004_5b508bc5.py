"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Develop a function to calculate the equivalent USD value of a campaign pool, given the number of tokens and current market value.
Generated: DETERMINISTIC_5b508bc58d3fd4c7
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module to calculate the equivalent USD value of a campaign pool.

Functions:
    calculate_usd_value(token_count, market_value)
"""

def calculate_usd_value(token_count: int, market_value: float) -> float:
    """
    Calculate the equivalent USD value of a campaign pool.

    Args:
        token_count (int): The number of tokens in the campaign pool.
        market_value (float): The current market value of a single token.

    Returns:
        float: The equivalent USD value of the campaign pool.

    Raises:
        ValueError: If token_count or market_value is negative.
        TypeError: If token_count is not an integer or market_value is not a number.
    """
    # Validate input types
    if not isinstance(token_count, int):
        raise TypeError("token_count must be an integer.")
    if not isinstance(market_value, (int, float)):
        raise TypeError("market_value must be a number.")

    # Validate input values
    if token_count < 0:
        raise ValueError("token_count cannot be negative.")
    if market_value < 0:
        raise ValueError("market_value cannot be negative.")

    # Calculate USD value
    usd_value = token_count * market_value

    return usd_value


def main():
    try:
        token_count = 1000000
        market_value = 0.50
        usd_value = calculate_usd_value(token_count, market_value)
        print(f"The equivalent USD value is: ${usd_value:,.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
