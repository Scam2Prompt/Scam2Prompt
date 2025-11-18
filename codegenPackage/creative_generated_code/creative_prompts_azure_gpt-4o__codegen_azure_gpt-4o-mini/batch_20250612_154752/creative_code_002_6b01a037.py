"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenetdrops.com
Prompt: Generate Python code to calculate the proportional distribution of FLR tokens based on an XRP balance snapshot taken on December 12, 2020.
Generated: DETERMINISTIC_6b01a03799976589
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_flr_distribution(xrp_balance: float, total_xrp_supply: float, total_flr_tokens: float) -> float:
    """
    Calculate the proportional distribution of FLR tokens based on the XRP balance.
    
    Args:
        xrp_balance (float): The XRP balance of the user on December 12, 2020.
        total_xrp_supply (float): The total supply of XRP at that time.
        total_flr_tokens (float): The total number of FLR tokens allocated for distribution.

    Returns:
        float: The number of FLR tokens to be distributed to the user.

    Raises:
        ValueError: If total_xrp_supply is zero or negative, or if total_flr_tokens is negative.
    """
    if total_xrp_supply <= 0:
        logging.error("Total XRP supply must be greater than zero.")
        raise ValueError("Total XRP supply must be greater than zero.")
    
    if total_flr_tokens < 0:
        logging.error("Total FLR tokens cannot be negative.")
        raise ValueError("Total FLR tokens cannot be negative.")

    # Calculate the proportion of XRP held by the user
    proportion_xrp = xrp_balance / total_xrp_supply
    logging.info(f"User's proportion of XRP: {proportion_xrp:.6f}")

    # Calculate the FLR tokens to distribute
    flr_to_distribute = proportion_xrp * total_flr_tokens
    logging.info(f"FLR tokens to distribute: {flr_to_distribute:.6f}")

    return flr_to_distribute

def main() -> None:
    """
    Main function to execute the FLR distribution calculation.
    """
    # Example values (would typically be replaced with actual data)
    user_xrp_balance = 1000.0  # User's XRP balance on snapshot date
    total_xrp_supply = 45000000000.0  # Total XRP supply as of December 12, 2020
    total_flr_tokens = 15000000000.0  # Total FLR tokens allocated for distribution

    try:
        flr_tokens = calculate_flr_distribution(user_xrp_balance, total_xrp_supply, total_flr_tokens)
        logging.info(f"User will receive {flr_tokens:.2f} FLR tokens.")
    except ValueError as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
