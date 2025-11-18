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
    the provided Total Value Locked (TVL) and Market Capitalization (MCap).

    Args:
        tvl (float): The Total Value Locked in the Level platform (in USD).
        mcap (float): The Market Capitalization of Level (in USD).

    Returns:
        float: The calculated APY as a percentage.

    Raises:
        ValueError: If TVL or MCap is non-positive.
    """
    # Validate inputs
    if tvl <= 0:
        raise ValueError("TVL must be a positive number.")
    if mcap <= 0:
        raise ValueError("MCap must be a positive number.")

    try:
        # APY calculation formula: APY = (MCap / TVL) * 100
        apy = (mcap / tvl) * 100
        return round(apy, 2)  # Return APY rounded to two decimal places
    except Exception as e:
        # Log and raise unexpected errors
        raise RuntimeError(f"An error occurred during APY calculation: {str(e)}")

# Example usage:
# tvl = 500000  # Total Value Locked (USD)
# mcap = 25000000  # Market Capitalization (USD)
# print(calculate_apy(tvl, mcap))  # Output: 5000.0
```
