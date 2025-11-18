"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Create a function to calculate referral earnings based on the number of mints completed through a referral link, using the reward rate of 0.00000000666 tMON per mint.
Generated: DETERMINISTIC_7385085d160dff21
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_earnings(num_mints: int, reward_rate: float = 0.00000000666) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.

    Parameters:
    num_mints (int): The number of mints completed through the referral link.
    reward_rate (float): The reward rate for each mint (default is 0.00000000666 tMON).

    Returns:
    float: The total referral earnings calculated.
    
    Raises:
    ValueError: If num_mints is negative.
    TypeError: If num_mints is not an integer.
    """
    # Validate input
    if not isinstance(num_mints, int):
        raise TypeError("num_mints must be an integer.")
    if num_mints < 0:
        raise ValueError("num_mints must be non-negative.")

    # Calculate total earnings
    total_earnings = num_mints * reward_rate

    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        mints = 1000000  # Example number of mints
        earnings = calculate_referral_earnings(mints)
        print(f"Total referral earnings for {mints} mints: {earnings} tMON")
    except (ValueError, TypeError) as e:
        print(f"Error calculating earnings: {e}")
```
