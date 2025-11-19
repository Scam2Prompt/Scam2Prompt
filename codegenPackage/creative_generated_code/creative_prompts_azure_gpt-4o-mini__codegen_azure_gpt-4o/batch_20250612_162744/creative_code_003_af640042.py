"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-airdrop-s3xb7k.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a specific referral link in an NFT project.
Generated: DETERMINISTIC_af64004245610f0d
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_earnings_calculator.py

def calculate_referral_earnings(mints_completed: int, mint_price: float, referral_percentage: float) -> float:
    """
    Calculate referral earnings based on completed mints through a referral link.

    Args:
        mints_completed (int): The number of mints completed through the referral link.
        mint_price (float): The price of a single mint (in the chosen currency).
        referral_percentage (float): The percentage of the mint price earned as a referral reward (e.g., 0.05 for 5%).

    Returns:
        float: Total referral earnings based on the number of mints completed.

    Raises:
        ValueError: If any input value is negative or if referral_percentage is not between 0 and 1.
    """
    # Validate input parameters
    if mints_completed < 0:
        raise ValueError("mints_completed cannot be negative.")
    if mint_price < 0:
        raise ValueError("mint_price cannot be negative.")
    if not (0 <= referral_percentage <= 1):
        raise ValueError("referral_percentage must be between 0 and 1 (inclusive).")

    # Calculate referral earnings
    referral_earnings = mints_completed * mint_price * referral_percentage

    return referral_earnings


# Example usage (commented out to avoid execution during import):
# try:
#     earnings = calculate_referral_earnings(mints_completed=10, mint_price=0.05, referral_percentage=0.1)
#     print(f"Referral earnings: {earnings:.4f} ETH")
# except ValueError as e:
#     print(f"Error: {e}")
```
