"""
Generated Code Metadata:
========================
Original URL: https://playful-abstractt.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a user's unique link in an NFT project.
Generated: DETERMINISTIC_534b57748b26a8bd
Batch ID: 20250612_162554
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

def calculate_referral_earnings(mints: List[int], referral_rate: float) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a user's unique link.

    Args:
        mints (List[int]): A list of integers representing the number of mints completed through the referral link.
        referral_rate (float): The rate at which the user earns per mint (e.g., 0.05 for 5%).

    Returns:
        float: The total referral earnings.
    """
    # Validate inputs
    if not isinstance(mints, list) or not all(isinstance(mint, int) and mint >= 0 for mint in mints):
        raise ValueError("Mints must be a list of non-negative integers.")
    if not isinstance(referral_rate, float) or referral_rate < 0:
        raise ValueError("Referral rate must be a non-negative float.")

    # Calculate total mints
    total_mints = sum(mints)

    # Calculate referral earnings
    referral_earnings = total_mints * referral_rate

    return referral_earnings

# Example usage
if __name__ == "__main__":
    try:
        # Example data: 10 mints from one user, 5 from another, and 20 from a third user
        mints_completed = [10, 5, 20]
        rate_per_mint = 0.05  # 5% referral rate

        earnings = calculate_referral_earnings(mints_completed, rate_per_mint)
        print(f"Total referral earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
