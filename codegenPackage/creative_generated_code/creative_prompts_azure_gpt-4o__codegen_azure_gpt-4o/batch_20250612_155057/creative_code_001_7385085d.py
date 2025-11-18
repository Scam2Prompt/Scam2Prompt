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
def calculate_referral_earnings(mints_completed, reward_rate=0.00000000666):
    """
    Calculate referral earnings based on the number of mints completed.

    Args:
        mints_completed (int): The number of mints completed through the referral link.
        reward_rate (float): The reward rate in tMON per mint. Defaults to 0.00000000666.

    Returns:
        float: The total referral earnings in tMON.

    Raises:
        ValueError: If mints_completed is negative or not an integer.
    """
    # Input validation
    if not isinstance(mints_completed, int) or mints_completed < 0:
        raise ValueError("mints_completed must be a non-negative integer.")

    # Calculate referral earnings
    referral_earnings = mints_completed * reward_rate

    return referral_earnings


# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual mints completed value
        mints_completed = 5000  
        
        # Calculate earnings
        earnings = calculate_referral_earnings(mints_completed)
        print(f"Referral earnings for {mints_completed} mints: {earnings:.10f} tMON")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
