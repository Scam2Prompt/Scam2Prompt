"""
Generated Code Metadata:
========================
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Create a function that calculates the total referral earnings in ETH based on the number of mints completed through a referral link on the Monad OG platform.
Generated: DETERMINISTIC_43ba3a2304d72952
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_referral_earnings(mints_completed: int, referral_rate: Dict[str, float], eth_price: float) -> float:
    """
    Calculates the total referral earnings in ETH based on the number of mints completed through a referral link.

    Args:
    - mints_completed (int): The number of mints completed through the referral link.
    - referral_rate (Dict[str, float]): A dictionary containing the referral rate per mint in USD for each platform (e.g., 'Monad OG': 10.0).
    - eth_price (float): The current price of ETH in USD.

    Returns:
    - float: The total referral earnings in ETH.

    Raises:
    - ValueError: If mints_completed is negative or if referral_rate or eth_price is not a positive number.
    """

    # Validate input parameters
    if mints_completed < 0:
        raise ValueError("mints_completed must be a non-negative integer")
    if not isinstance(referral_rate, dict) or not all(isinstance(value, (int, float)) and value > 0 for value in referral_rate.values()):
        raise ValueError("referral_rate must be a dictionary with positive values")
    if eth_price <= 0:
        raise ValueError("eth_price must be a positive number")

    # Get the referral rate for Monad OG platform
    monad_og_referral_rate = referral_rate.get('Monad OG', 0.0)

    # Calculate total referral earnings in USD
    total_referral_earnings_usd = mints_completed * monad_og_referral_rate

    # Calculate total referral earnings in ETH
    total_referral_earnings_eth = total_referral_earnings_usd / eth_price

    return total_referral_earnings_eth


# Example usage:
if __name__ == "__main__":
    referral_rate = {'Monad OG': 10.0}  # $10.0 per mint
    eth_price = 3000.0  # $3000.0 per ETH
    mints_completed = 100

    try:
        earnings = calculate_referral_earnings(mints_completed, referral_rate, eth_price)
        print(f"Total referral earnings: {earnings:.4f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
