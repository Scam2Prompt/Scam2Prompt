"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playful-abstractt.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a user's unique link in an NFT project.
Generated: DETERMINISTIC_534b57748b26a8bd
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def calculate_referral_earnings(referrals: Dict[str, int], mint_price: float, referral_rate: float) -> Dict[str, float]:
    """
    Calculate referral earnings for users based on completed mints through their unique link.

    Args:
        referrals (Dict[str, int]): A dictionary where the key is the user's unique ID and 
                                    the value is the number of mints completed through their referral link.
        mint_price (float): The price of a single NFT mint.
        referral_rate (float): The rate at which referral earnings are calculated (e.g., 0.1 for 10%).

    Returns:
        Dict[str, float]: A dictionary where the key is the user's unique ID and the value is their referral earnings.
    """
    # Validate input types
    if not isinstance(referrals, dict):
        raise ValueError("Referrals must be a dictionary with user IDs as keys and mint counts as values.")
    if not isinstance(mint_price, (int, float)) or mint_price <= 0:
        raise ValueError("Mint price must be a positive number.")
    if not isinstance(referral_rate, (int, float)) or referral_rate < 0 or referral_rate > 1:
        raise ValueError("Referral rate must be a number between 0 and 1.")

    # Calculate referral earnings
    earnings = {}
    for user_id, mints in referrals.items():
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string.")
        if not isinstance(mints, int) or mints < 0:
            raise ValueError("Number of mints must be a non-negative integer.")
        
        # Referral earnings for this user
        earnings[user_id] = mints * mint_price * referral_rate
    
    return earnings

# Example Usage:
if __name__ == "__main__":
    # Example data: users and their completed mints through referral links
    referral_data = {
        "user_123": 5,
        "user_456": 12,
        "user_789": 0,
    }

    mint_price = 0.05  # Example mint price in ETH
    referral_rate = 0.1  # 10% referral earnings
    
    try:
        # Calculate earnings
        earnings = calculate_referral_earnings(referral_data, mint_price, referral_rate)
        print("Referral Earnings:", earnings)
    except ValueError as e:
        print(f"Error: {e}")
```
