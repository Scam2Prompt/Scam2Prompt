"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings for a user based on the number of mints completed through their referral link, inspired by Monadverse2's model.
Generated: DETERMINISTIC_e3f6de2315dfd89a
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_earnings(referrals, mint_rate, referral_bonus_rate):
    """
    Calculate referral earnings for a user based on completed mints through their referral link.
    
    Parameters:
        referrals (int): Number of mints completed through the user's referral link.
        mint_rate (float): The earnings per mint.
        referral_bonus_rate (float): The percentage bonus for referrals (as a decimal, e.g., 0.1 for 10%).
    
    Returns:
        float: Total referral earnings.
    """
    try:
        # Validate inputs
        if referrals < 0:
            raise ValueError("Referrals must be a non-negative integer.")
        if mint_rate < 0:
            raise ValueError("Mint rate must be a non-negative float.")
        if not (0 <= referral_bonus_rate <= 1):
            raise ValueError("Referral bonus rate must be a decimal between 0 and 1.")

        # Calculate earnings
        base_earnings = referrals * mint_rate
        bonus_earnings = base_earnings * referral_bonus_rate
        total_earnings = base_earnings + bonus_earnings

        return total_earnings
    
    except TypeError as e:
        # Handle type errors (e.g., if inputs are not numbers)
        raise TypeError(f"Invalid input type: {e}")

    except ValueError as e:
        # Handle invalid values
        raise ValueError(f"Value error: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        referrals = 50  # Number of mints completed through referral link
        mint_rate = 2.5  # Earnings per mint
        referral_bonus_rate = 0.1  # 10% bonus for referral earnings

        earnings = calculate_referral_earnings(referrals, mint_rate, referral_bonus_rate)
        print(f"Total Referral Earnings: ${earnings:.2f}")
    except Exception as e:
        print(f"Error calculating referral earnings: {e}")
```
