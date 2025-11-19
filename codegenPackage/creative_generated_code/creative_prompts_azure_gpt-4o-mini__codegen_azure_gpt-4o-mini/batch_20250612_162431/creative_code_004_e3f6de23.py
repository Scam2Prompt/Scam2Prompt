"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings for a user based on the number of mints completed through their referral link, inspired by Monadverse2's model.
Generated: DETERMINISTIC_e3f6de2315dfd89a
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_earnings(mints_completed: int, referral_rate: float) -> float:
    """
    Calculate referral earnings based on the number of mints completed.
    
    Parameters:
    mints_completed (int): The number of mints completed through the referral link.
    referral_rate (float): The rate of earnings per mint completed.

    Returns:
    float: Total earnings from referrals.
    
    Raises:
    ValueError: If mints_completed is negative or if referral_rate is negative.
    """
    # Validate input parameters
    if mints_completed < 0:
        raise ValueError("The number of mints completed cannot be negative.")
    if referral_rate < 0:
        raise ValueError("The referral rate cannot be negative.")

    # Calculate total earnings
    total_earnings = mints_completed * referral_rate
    
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        mints = 150  # Number of mints completed
        rate = 0.05  # Referral rate per mint
        earnings = calculate_referral_earnings(mints, rate)
        print(f"Total referral earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error calculating earnings: {e}")
```
