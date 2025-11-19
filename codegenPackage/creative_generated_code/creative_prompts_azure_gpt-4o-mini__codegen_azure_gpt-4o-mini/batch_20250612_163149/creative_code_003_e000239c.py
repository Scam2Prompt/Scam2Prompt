"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-pro.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a user's referral link in an NFT project.
Generated: DETERMINISTIC_e000239c9bb02b76
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_earnings(referrals: int, earnings_per_mint: float) -> float:
    """
    Calculate total referral earnings based on the number of mints completed
    through a user's referral link in an NFT project.

    Args:
        referrals (int): The number of mints completed through the referral link.
        earnings_per_mint (float): The earnings received for each mint.

    Returns:
        float: Total referral earnings.

    Raises:
        ValueError: If the number of referrals is negative or if earnings_per_mint is negative.
    """
    
    # Validate input parameters
    if referrals < 0:
        raise ValueError("Number of referrals cannot be negative.")
    
    if earnings_per_mint < 0:
        raise ValueError("Earnings per mint cannot be negative.")

    # Calculate total earnings
    total_earnings = referrals * earnings_per_mint

    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        referrals = 10  # Number of mints through referral link
        earnings_per_mint = 0.05  # Earnings per mint in the NFT project

        total = calculate_referral_earnings(referrals, earnings_per_mint)
        print(f"Total referral earnings: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
