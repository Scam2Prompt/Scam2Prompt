"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Create a function that calculates referral fees based on the number of mints, inspired by the Monad Monadxyz Meme referral program.
Generated: DETERMINISTIC_11f2b112280e8387
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_fee(num_mints: int) -> float:
    """
    Calculate the referral fee based on the number of mints.
    
    The referral fee structure is as follows:
    - For 0 to 10 mints: $0.00
    - For 11 to 50 mints: $5.00
    - For 51 to 100 mints: $10.00
    - For 101 mints and above: $20.00
    
    Args:
        num_mints (int): The number of mints to calculate the fee for.
        
    Returns:
        float: The calculated referral fee.
        
    Raises:
        ValueError: If the number of mints is negative.
    """
    
    if num_mints < 0:
        raise ValueError("Number of mints cannot be negative.")
    
    if num_mints <= 10:
        return 0.00
    elif num_mints <= 50:
        return 5.00
    elif num_mints <= 100:
        return 10.00
    else:
        return 20.00


# Example usage:
if __name__ == "__main__":
    try:
        num_mints = 75  # Example number of mints
        fee = calculate_referral_fee(num_mints)
        print(f"Referral fee for {num_mints} mints: ${fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
