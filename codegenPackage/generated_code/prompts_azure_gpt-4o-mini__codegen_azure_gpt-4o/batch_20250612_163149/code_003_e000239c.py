"""
Generated Code Metadata:
========================
Original URL: https://zksync-pro.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a user's referral link in an NFT project.
Generated: DETERMINISTIC_e000239c9bb02b76
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List

def calculate_referral_earnings(mints: List[int], mint_price: float, referral_percentage: float) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a user's referral link.

    Args:
        mints (List[int]): A list of integers representing the number of mints completed per referral.
        mint_price (float): The price of a single mint in the NFT project.
        referral_percentage (float): The percentage of earnings allocated to the referrer (e.g., 0.10 for 10%).

    Returns:
        float: The total referral earnings for the user.
    """
    # Input validation
    if not isinstance(mints, list) or not all(isinstance(mint, int) and mint >= 0 for mint in mints):
        raise ValueError("Mints must be a list of non-negative integers.")
    if not isinstance(mint_price, (int, float)) or mint_price <= 0:
        raise ValueError("Mint price must be a positive number.")
    if not isinstance(referral_percentage, (int, float)) or not (0 <= referral_percentage <= 1):
        raise ValueError("Referral percentage must be a number between 0 and 1.")

    # Calculate total mints
    total_mints = sum(mints)

    # Calculate referral earnings
    referral_earnings = total_mints * mint_price * referral_percentage

    return referral_earnings

# Example usage
if __name__ == "__main__":
    try:
        # Example data
        mints = [5, 10, 3]  # Number of mints completed through referrals
        mint_price = 0.05  # Price of a single mint in ETH
        referral_percentage = 0.10  # Referral percentage (10%)

        # Calculate earnings
        earnings = calculate_referral_earnings(mints, mint_price, referral_percentage)
        print(f"Total referral earnings: {earnings:.4f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
