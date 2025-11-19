"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venusclaim.pages.dev
Prompt: Create a function that calculates the APY for a specific asset pool on the Venus Protocol based on the provided liquidity data.
Generated: DETERMINISTIC_324741312bca3d6a
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def calculate_apy(total_supply: float, total_borrow: float, interest_rate: float, liquidity: float, time_period_days: int = 365) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for a specific asset pool on the Venus Protocol.

    Parameters:
    total_supply (float): Total supply of the asset in the pool.
    total_borrow (float): Total amount borrowed from the asset pool.
    interest_rate (float): Annual interest rate (as a decimal).
    liquidity (float): Available liquidity in the pool.
    time_period_days (int, optional): The time period over which to calculate the APY (default is 365 days).

    Returns:
    float: Calculated APY for the asset pool.
    
    Raises:
    ValueError: If any of the inputs are negative or if total_supply is zero.
    """

    # Input validation
    if total_supply <= 0:
        logging.error("Total supply must be greater than zero.")
        raise ValueError("Total supply must be greater than zero.")
    if total_borrow < 0:
        logging.error("Total borrow cannot be negative.")
        raise ValueError("Total borrow cannot be negative.")
    if interest_rate < 0:
        logging.error("Interest rate cannot be negative.")
        raise ValueError("Interest rate cannot be negative.")
    if liquidity < 0:
        logging.error("Liquidity cannot be negative.")
        raise ValueError("Liquidity cannot be negative.")

    # Calculate the net supply
    net_supply = total_supply - total_borrow

    # Calculate APY using the formula
    apy = (interest_rate * net_supply / liquidity) * (time_period_days / 365)
    
    logging.info(f"Calculated APY: {apy:.4f}")
    return apy

# Example usage
if __name__ == "__main__":
    try:
        apy_result = calculate_apy(total_supply=1000000, total_borrow=200000, interest_rate=0.05, liquidity=800000)
        print(f"Annual Percentage Yield (APY): {apy_result:.4f}")
    except ValueError as e:
        print(f"Error calculating APY: {e}")
```
