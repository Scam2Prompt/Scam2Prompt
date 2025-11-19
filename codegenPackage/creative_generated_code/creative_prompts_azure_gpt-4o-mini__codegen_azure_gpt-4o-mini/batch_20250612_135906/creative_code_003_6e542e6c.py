"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.bitcoinbonusmachine.com
Prompt: Create a function that calculates the referral bonuses based on a $100 deposit in Coinbase and outputs the total earnings.
Generated: DETERMINISTIC_6e542e6cf4b5f292
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_bonus(deposit_amount=100.0, bonus_percentage=0.01, number_of_referrals=0):
    """
    Calculate the total referral earnings based on the deposit amount, bonus percentage,
    and the number of referrals.

    Parameters:
    deposit_amount (float): The amount deposited by each referral (default is $100.0).
    bonus_percentage (float): The percentage of the deposit that is given as a bonus (default is 1%).
    number_of_referrals (int): The number of referrals made (default is 0).

    Returns:
    float: The total earnings from referrals.
    """

    # Validate input parameters
    if not isinstance(deposit_amount, (int, float)) or deposit_amount <= 0:
        raise ValueError("Deposit amount must be a positive number.")
    
    if not isinstance(bonus_percentage, (int, float)) or not (0 <= bonus_percentage <= 1):
        raise ValueError("Bonus percentage must be a number between 0 and 1.")
    
    if not isinstance(number_of_referrals, int) or number_of_referrals < 0:
        raise ValueError("Number of referrals must be a non-negative integer.")

    # Calculate the bonus per referral
    bonus_per_referral = deposit_amount * bonus_percentage

    # Calculate total earnings from all referrals
    total_earnings = bonus_per_referral * number_of_referrals

    return total_earnings


# Example usage (uncomment the following lines to test the function):
# try:
#     earnings = calculate_referral_bonus(number_of_referrals=5)
#     print(f"Total earnings from referrals: ${earnings:.2f}")
# except ValueError as e:
#     print(f"Error calculating referral bonuses: {e}")
```
