"""
Generated Code Metadata:
========================
Original URL: https://srrv2oldmtlx.pages.dev
Prompt: Create a Python script that calculates the daily MTLX rewards for the "Steel Rebar V2" market based on the provided APY and liquidity data.
Generated: DETERMINISTIC_d84769a1ad08bb55
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_daily_rewards(apy: float, liquidity: float) -> float:
    """
    Calculate the daily MTLX rewards based on the provided APY and liquidity.

    Parameters:
    apy (float): The annual percentage yield as a decimal (e.g., 0.05 for 5%).
    liquidity (float): The total liquidity in the market.

    Returns:
    float: The daily MTLX rewards calculated.
    
    Raises:
    ValueError: If APY or liquidity is negative.
    """
    if apy < 0:
        logging.error("APY cannot be negative.")
        raise ValueError("APY cannot be negative.")
    if liquidity < 0:
        logging.error("Liquidity cannot be negative.")
        raise ValueError("Liquidity cannot be negative.")

    # Calculate daily rewards
    daily_rewards = (apy / 365) * liquidity
    logging.info(f"Calculated daily rewards: {daily_rewards} MTLX")
    
    return daily_rewards

def main():
    """
    Main function to execute the daily rewards calculation.
    """
    # Example input values
    apy = 0.05  # 5% APY
    liquidity = 1000000  # $1,000,000 liquidity

    try:
        daily_rewards = calculate_daily_rewards(apy, liquidity)
        print(f"Daily MTLX rewards for the Steel Rebar V2 market: {daily_rewards:.2f} MTLX")
    except ValueError as e:
        logging.error(f"Error calculating daily rewards: {e}")

if __name__ == "__main__":
    main()
```
