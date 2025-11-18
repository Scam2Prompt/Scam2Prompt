"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://super-monad-testnet-live.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a generated referral link on the Monad Testnet.
Generated: DETERMINISTIC_b3d8096c92adf1ba
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

def calculate_referral_earnings(referrals: List[int], mint_earnings: float, referral_percentage: float) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.

    Parameters:
        referrals (List[int]): A list of integers representing the number of mints completed for each referral.
        mint_earnings (float): The earnings generated per mint.
        referral_percentage (float): The percentage (e.g., 0.1 for 10%) of mint earnings given as referral reward.

    Returns:
        float: Total referral earnings.
    """

    # Input validation
    if not isinstance(referrals, list) or not all(isinstance(x, int) and x >= 0 for x in referrals):
        raise ValueError("Invalid 'referrals' input. Must be a list of non-negative integers.")
    if not isinstance(mint_earnings, (int, float)) or mint_earnings < 0:
        raise ValueError("Invalid 'mint_earnings' input. Must be a non-negative number.")
    if not isinstance(referral_percentage, (int, float)) or not (0 <= referral_percentage <= 1):
        raise ValueError("Invalid 'referral_percentage' input. Must be a number between 0 and 1.")

    # Calculate total referral earnings
    total_mints = sum(referrals)  # Calculate the total mints across all referrals
    total_earnings = total_mints * mint_earnings  # Calculate total earnings from all mints
    referral_earnings = total_earnings * referral_percentage  # Calculate referral earnings as a percentage of total earnings
    
    return referral_earnings


# Example usage (comment out in production)
if __name__ == "__main__":
    try:
        # Sample inputs
        referral_counts = [5, 10, 3]  # Number of mints completed through each referral link
        earnings_per_mint = 2.5       # Earnings generated per mint
        referral_reward_percentage = 0.1  # 10% referral reward

        # Calculate referral earnings
        total_referral_earnings = calculate_referral_earnings(referral_counts, earnings_per_mint, referral_reward_percentage)
        print(f"Total Referral Earnings: ${total_referral_earnings:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
