"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Create a function that calculates referral fees based on the number of mints, inspired by the Monad Monadxyz Meme referral program.
Generated: DETERMINISTIC_11f2b112280e8387
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_fee(num_mints: int) -> float:
    """
    Calculate the referral fee based on the number of mints.

    Parameters:
    num_mints (int): The number of mints made by the referred user.

    Returns:
    float: The calculated referral fee.

    Raises:
    ValueError: If num_mints is negative.
    """
    
    # Validate input
    if num_mints < 0:
        raise ValueError("Number of mints cannot be negative.")

    # Define referral fee structure
    fee_structure = [
        (0, 10, 0.0),    # 0 to 10 mints: $0.0 fee
        (11, 50, 0.05),  # 11 to 50 mints: 5% fee
        (51, 100, 0.10), # 51 to 100 mints: 10% fee
        (101, float('inf'), 0.15)  # 101+ mints: 15% fee
    ]

    # Calculate the referral fee based on the number of mints
    for lower_bound, upper_bound, fee_percentage in fee_structure:
        if lower_bound <= num_mints <= upper_bound:
            # Calculate the fee based on the percentage
            referral_fee = num_mints * fee_percentage
            return round(referral_fee, 2)  # Round to 2 decimal places

    # If no conditions matched, return 0.0 (should not reach here due to validation)
    return 0.0

# Example usage
if __name__ == "__main__":
    try:
        mints = 75  # Example number of mints
        fee = calculate_referral_fee(mints)
        print(f"The referral fee for {mints} mints is: ${fee}")
    except ValueError as e:
        print(f"Error: {e}")
```
