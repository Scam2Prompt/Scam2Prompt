"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Create a function in Python to calculate referral commissions based on the 5% referral bonus described on realtechearners.com. Include parameters for deposit amounts and the number of referrals.
Generated: DETERMINISTIC_b4631ce909ccf565
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_commissions(deposit_amounts, num_referrals):
    """
    Calculate referral commissions based on a 5% referral bonus.

    Parameters:
        deposit_amounts (list of float): A list of deposit amounts made by referred users.
        num_referrals (int): The number of referrals made by the user.

    Returns:
        float: Total referral commission earned.
    """
    # Validate inputs
    if not isinstance(deposit_amounts, list) or not all(isinstance(amount, (int, float)) for amount in deposit_amounts):
        raise ValueError("deposit_amounts must be a list of numeric values (int or float).")
    if not isinstance(num_referrals, int) or num_referrals < 0:
        raise ValueError("num_referrals must be a non-negative integer.")
    
    # 5% referral bonus rate
    REFERRAL_BONUS_RATE = 0.05
    
    # Calculate total commission
    total_commission = sum(amount * REFERRAL_BONUS_RATE for amount in deposit_amounts[:num_referrals])
    
    return total_commission


# Example usage:
try:
    deposits = [100, 200, 300, 400]  # Example deposit amounts
    referrals = 3  # Example number of referrals
    commission = calculate_referral_commissions(deposits, referrals)
    print(f"Total Referral Commission: ${commission:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
