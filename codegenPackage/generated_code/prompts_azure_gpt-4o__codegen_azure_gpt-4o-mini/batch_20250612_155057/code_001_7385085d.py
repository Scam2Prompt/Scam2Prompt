"""
Generated Code Metadata:
========================
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Create a function to calculate referral earnings based on the number of mints completed through a referral link, using the reward rate of 0.00000000666 tMON per mint.
Generated: DETERMINISTIC_7385085d160dff21
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_earnings(mints_completed: int, reward_rate: float = 0.00000000666) -> float:
    """
    Calculate the referral earnings based on the number of mints completed.

    Parameters:
    mints_completed (int): The number of mints completed through the referral link.
    reward_rate (float): The reward rate per mint. Default is 0.00000000666 tMON.

    Returns:
    float: The total earnings from referrals.
    
    Raises:
    ValueError: If mints_completed is negative.
    TypeError: If mints_completed is not an integer.
    """
    
    # Validate input
    if not isinstance(mints_completed, int):
        raise TypeError("mints_completed must be an integer.")
    if mints_completed < 0:
        raise ValueError("mints_completed cannot be negative.")
    
    # Calculate total earnings
    total_earnings = mints_completed * reward_rate
    
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        mints = 1000  # Example number of mints
        earnings = calculate_referral_earnings(mints)
        print(f"Total referral earnings for {mints} mints: {earnings:.10f} tMON")
    except (ValueError, TypeError) as e:
        print(f"Error calculating earnings: {e}")
```
