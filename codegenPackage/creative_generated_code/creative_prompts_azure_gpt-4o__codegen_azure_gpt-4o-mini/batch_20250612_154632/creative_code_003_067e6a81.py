"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levei.money
Prompt: Create a function that calculates the APY for lvlUSD deposits based on the provided TVL and MCap values from the Level platform.
Generated: DETERMINISTIC_067e6a81b650ed9c
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(tvl: float, mcap: float) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for lvlUSD deposits based on
    Total Value Locked (TVL) and Market Capitalization (MCap) values.

    Parameters:
    tvl (float): Total Value Locked in the Level platform (in USD).
    mcap (float): Market Capitalization of the lvlUSD (in USD).

    Returns:
    float: The calculated APY expressed as a percentage.

    Raises:
    ValueError: If tvl or mcap is negative or if mcap is zero.
    """

    # Validate input values
    if tvl < 0:
        raise ValueError("Total Value Locked (TVL) cannot be negative.")
    if mcap <= 0:
        raise ValueError("Market Capitalization (MCap) must be greater than zero.")

    # Calculate APY using the formula: APY = (TVL / MCap) * 100
    apy = (tvl / mcap) * 100

    return apy


# Example usage:
if __name__ == "__main__":
    try:
        tvl_value = 5000000.0  # Example TVL in USD
        mcap_value = 20000000.0  # Example MCap in USD
        apy_value = calculate_apy(tvl_value, mcap_value)
        print(f"The calculated APY is: {apy_value:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
