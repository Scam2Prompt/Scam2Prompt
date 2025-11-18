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
def calculate_referral_commission(deposit_amount: float, number_of_referrals: int) -> float:
    """
    Calculate the total referral commission based on a 5% bonus on the deposit amount.

    Parameters:
    deposit_amount (float): The amount deposited by the referred user.
    number_of_referrals (int): The number of referrals made.

    Returns:
    float: The total referral commission earned.
    
    Raises:
    ValueError: If deposit_amount is negative or number_of_referrals is negative.
    """
    
    # Validate inputs
    if deposit_amount < 0:
        raise ValueError("Deposit amount must be non-negative.")
    if number_of_referrals < 0:
        raise ValueError("Number of referrals must be non-negative.")
    
    # Calculate the referral commission (5% of the deposit amount per referral)
    commission_rate = 0.05  # 5%
    total_commission = deposit_amount * commission_rate * number_of_referrals
    
    return total_commission

# Example usage (uncomment to run):
# try:
#     commission = calculate_referral_commission(1000, 3)
#     print(f"Total referral commission: ${commission:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
