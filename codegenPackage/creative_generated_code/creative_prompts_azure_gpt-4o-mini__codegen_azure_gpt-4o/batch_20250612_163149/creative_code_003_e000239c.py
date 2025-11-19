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
# Import necessary modules
from typing import Union

def calculate_referral_earnings(referral_count: int, mint_price: Union[int, float], referral_percentage: Union[int, float]) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.
    
    Args:
        referral_count (int): The number of mints completed through the referral link.
        mint_price (Union[int, float]): The price of one mint in the NFT project.
        referral_percentage (Union[int, float]): The percentage of the mint price awarded as referral earnings.
        
    Returns:
        float: The total referral earnings for the user.
    
    Raises:
        ValueError: If any input is invalid (negative values, incorrect types, or percentage out of range).
    """
    
    # Validate inputs
    if referral_count < 0:
        raise ValueError("Referral count must be a non-negative integer.")
    if mint_price <= 0:
        raise ValueError("Mint price must be a positive number.")
    if not (0 <= referral_percentage <= 100):
        raise ValueError("Referral percentage must be between 0 and 100.")
    
    # Calculate referral earnings
    earnings = referral_count * mint_price * (referral_percentage / 100)
    
    return round(earnings, 2)  # Return earnings rounded to 2 decimal places

# Example usage (uncomment to test)
# try:
#     referral_earnings = calculate_referral_earnings(referral_count=10, mint_price=50, referral_percentage=5)
#     print(f"Referral earnings: ${referral_earnings}")
# except ValueError as e:
#     print(f"Error: {e}")
```
