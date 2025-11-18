"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-pass.nfts2.me
Prompt: Create a function to calculate the total referral fees earned based on the number of mints completed through a referral link on the Unichain Pass platform.
Generated: DETERMINISTIC_8054dd513df5f74d
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_fees(mints_completed, fee_per_mint):
    """
    Calculate the total referral fees earned based on the number of mints
    completed through a referral link on the Unichain Pass platform.
    
    Args:
        mints_completed (int): The number of mints completed through the referral link.
        fee_per_mint (float): The referral fee earned for each mint completed.

    Returns:
        float: The total referral fees earned.

    Raises:
        ValueError: If mints_completed is negative or if fee_per_mint is negative.
    """
    
    # Validate input parameters
    if mints_completed < 0:
        raise ValueError("Number of mints completed cannot be negative.")
    if fee_per_mint < 0:
        raise ValueError("Fee per mint cannot be negative.")
    
    # Calculate total referral fees
    total_fees = mints_completed * fee_per_mint
    
    return total_fees

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        mints = 100    # Number of mints completed
        fee = 0.5      # Referral fee per mint
        
        # Calculate total referral fees
        total_earned = calculate_referral_fees(mints, fee)
        print(f"Total referral fees earned: ${total_earned:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
