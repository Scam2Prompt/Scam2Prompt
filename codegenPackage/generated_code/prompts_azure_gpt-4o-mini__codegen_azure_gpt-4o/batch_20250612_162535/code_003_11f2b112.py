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
# Import necessary modules
from typing import Dict

def calculate_referral_fees(mints: int, referral_rate: float = 0.05) -> float:
    """
    Calculate referral fees based on the number of mints.

    Args:
        mints (int): The number of mints made by the referred user.
        referral_rate (float): The percentage of the mint value given as a referral fee. Default is 5% (0.05).

    Returns:
        float: The total referral fee earned.

    Raises:
        ValueError: If mints is negative or referral_rate is not between 0 and 1.
    """
    # Validate inputs
    if mints < 0:
        raise ValueError("Number of mints cannot be negative.")
    if not (0 <= referral_rate <= 1):
        raise ValueError("Referral rate must be between 0 and 1.")

    # Assume each mint has a fixed value (e.g., $10 per mint)
    mint_value = 10.0

    # Calculate the total referral fee
    total_fee = mints * mint_value * referral_rate

    return total_fee


# Example usage
if __name__ == "__main__":
    try:
        # Example input: 20 mints with a 5% referral rate
        mints = 20
        referral_rate = 0.05
        referral_fee = calculate_referral_fees(mints, referral_rate)
        print(f"Referral fee for {mints} mints at {referral_rate*100}% rate: ${referral_fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
