"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-pass.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a unique referral link for an NFT project.
Generated: DETERMINISTIC_6283f14cddd54fb0
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_earnings(mints_completed: int, earnings_per_mint: float) -> float:
    """
    Calculate the total earnings from referrals based on the number of mints completed.

    Parameters:
    mints_completed (int): The number of mints completed through the referral link.
    earnings_per_mint (float): The earnings generated per mint.

    Returns:
    float: The total earnings from the referral.

    Raises:
    ValueError: If mints_completed is negative or earnings_per_mint is negative.
    TypeError: If mints_completed is not an integer or earnings_per_mint is not a float.
    """
    
    # Validate inputs
    if not isinstance(mints_completed, int):
        raise TypeError("mints_completed must be an integer.")
    if not isinstance(earnings_per_mint, float):
        raise TypeError("earnings_per_mint must be a float.")
    if mints_completed < 0:
        raise ValueError("mints_completed cannot be negative.")
    if earnings_per_mint < 0:
        raise ValueError("earnings_per_mint cannot be negative.")
    
    # Calculate total earnings
    total_earnings = mints_completed * earnings_per_mint
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        mints = 50           # Example number of mints
        earnings = 0.02     # Example earnings per mint (in ETH or USD)
        total = calculate_referral_earnings(mints, earnings)
        print(f"Total earnings from referrals: ${total:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating earnings: {e}")
```
