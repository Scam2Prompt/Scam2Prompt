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
def calculate_referral_earnings(num_mints: int, reward_rate: float = 6.66e-9) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.
    
    Args:
        num_mints (int): Number of mints completed through the referral link.
        reward_rate (float, optional): Reward rate per mint in tMON. Defaults to 0.00000000666.
    
    Returns:
        float: Total referral earnings in tMON.
    
    Raises:
        ValueError: If num_mints is negative or reward_rate is negative.
    """
    if num_mints < 0:
        raise ValueError("Number of mints cannot be negative.")
    if reward_rate < 0:
        raise ValueError("Reward rate cannot be negative.")
    
    return num_mints * reward_rate
```
