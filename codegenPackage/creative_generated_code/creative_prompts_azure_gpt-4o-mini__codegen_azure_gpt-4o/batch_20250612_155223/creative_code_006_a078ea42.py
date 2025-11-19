"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Create a function to calculate the potential BTC earnings based on the number of mining credits burned in Bitcoin Minetrix.
Generated: DETERMINISTIC_a078ea42d833e999
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_btc_earnings(mining_credits: Union[int, float], conversion_rate: Union[int, float]) -> Union[float, None]:
    """
    Calculate potential BTC earnings based on the number of mining credits burned.

    Parameters:
        mining_credits (int or float): The number of mining credits burned.
        conversion_rate (int or float): The conversion rate of mining credits to BTC (BTC per credit).

    Returns:
        float: The potential BTC earnings.
        None: If the inputs are invalid or an error occurs.

    Raises:
        ValueError: If mining_credits or conversion_rate is negative.
    """
    try:
        # Input validation
        if mining_credits < 0:
            raise ValueError("Mining credits cannot be negative.")
        if conversion_rate < 0:
            raise ValueError("Conversion rate cannot be negative.")

        # Calculate BTC earnings
        btc_earnings = mining_credits * conversion_rate
        return btc_earnings

    except (TypeError, ValueError) as e:
        # Handle invalid inputs gracefully
        print(f"Error: {str(e)}")
        return None


# Example usage:
if __name__ == "__main__":
    # Define the inputs: number of mining credits burned and conversion rate
    mining_credits = 1000  # Example: 1000 mining credits burned
    conversion_rate = 0.0001  # Example: 0.0001 BTC per credit

    # Calculate BTC earnings and print the result
    btc_earnings = calculate_btc_earnings(mining_credits, conversion_rate)
    if btc_earnings is not None:
        print(f"Potential BTC Earnings: {btc_earnings:.8f} BTC")
    else:
        print("Failed to calculate BTC earnings due to invalid inputs.")
```
