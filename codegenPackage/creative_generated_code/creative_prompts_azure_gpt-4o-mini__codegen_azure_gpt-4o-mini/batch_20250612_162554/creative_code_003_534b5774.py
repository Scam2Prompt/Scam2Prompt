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
def calculate_referral_earnings(mints_completed, earning_per_mint):
    """
    Calculate the total earnings from referrals based on the number of mints completed.
    
    Parameters:
    mints_completed (int): The number of mints completed through the unique link.
    earning_per_mint (float): The amount earned for each mint completed.

    Returns:
    float: Total earnings from the referrals.

    Raises:
    ValueError: If mints_completed is negative or earning_per_mint is negative.
    """
    # Validate inputs
    if mints_completed < 0:
        raise ValueError("mints_completed must be a non-negative integer.")
    if earning_per_mint < 0:
        raise ValueError("earning_per_mint must be a non-negative float.")

    # Calculate total earnings
    total_earnings = mints_completed * earning_per_mint
    
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        # Sample inputs for testing the function
        mints = 150  # Example number of mints completed
        earning_per_mint = 0.1  # Example earning per mint in dollars
        
        # Calculate earnings
        earnings = calculate_referral_earnings(mints, earning_per_mint)
        
        # Display the result
        print(f"Total referral earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
