"""
Generated Code Metadata:
========================
Original URL: https://levei.money
Prompt: Create a function that calculates the APY for lvlUSD deposits based on the provided TVL and MCap values from the Level platform.
Generated: DETERMINISTIC_067e6a81b650ed9c
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_apy(tvl: float, mcap: float, days_per_year: int = 365) -> float:
    """
    Calculates the APY (Annual Percentage Yield) for lvlUSD deposits based on TVL and MCap.

    Args:
        tvl (float): Total Value Locked in the Level platform.
        mcap (float): Market Capitalization of the Level platform.
        days_per_year (int, optional): Number of days in a year. Defaults to 365.

    Returns:
        float: The calculated APY as a percentage.

    Raises:
        ValueError: If any of the input values are non-positive or if TVL > MCap.
    """
    # Validate input parameters
    if tvl <= 0 or mcap <= 0:
        raise ValueError("TVL and MCap must be positive values.")
    if tvl > mcap:
        raise ValueError("TVL cannot be greater than MCap.")
    
    try:
        # Calculate daily yield rate (assuming 0.1% of MCap is distributed daily)
        daily_distribution = 0.001 * mcap
        daily_yield = daily_distribution / tvl
        
        # Calculate APY using compound interest formula
        apy = (math.pow(1 + daily_yield, days_per_year) - 1) * 100
        
        return apy
    except Exception as e:
        raise ValueError(f"Error calculating APY: {str(e)}")

# Example usage:
# try:
#     apy = calculate_apy(tvl=1000000, mcap=5000000)
#     print(f"APY: {apy:.2f}%")
# except ValueError as e:
#     print(f"Error: {e}")
```
