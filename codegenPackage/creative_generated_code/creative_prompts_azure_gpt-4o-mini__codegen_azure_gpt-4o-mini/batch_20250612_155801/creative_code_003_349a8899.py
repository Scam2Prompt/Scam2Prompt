"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Create a function to calculate the total bonuses a user can receive upon signing up and depositing, based on the venez888 promotional structure.
Generated: DETERMINISTIC_349a889903e4376a
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_bonus(deposit_amount, referral_bonus=0.05, sign_up_bonus=100, max_referral_count=5):
    """
    Calculate the total bonuses a user can receive upon signing up and depositing.
    
    Parameters:
    deposit_amount (float): The amount the user deposits.
    referral_bonus (float): The percentage bonus for referrals (default is 5%).
    sign_up_bonus (float): The flat bonus given upon signing up (default is $100).
    max_referral_count (int): The maximum number of referrals that can be rewarded (default is 5).
    
    Returns:
    float: The total bonuses the user can receive.
    
    Raises:
    ValueError: If deposit_amount is negative or not a number.
    ValueError: If referral_bonus is not between 0 and 1.
    """
    
    # Validate inputs
    if not isinstance(deposit_amount, (int, float)) or deposit_amount < 0:
        raise ValueError("Deposit amount must be a non-negative number.")
    
    if not (0 <= referral_bonus <= 1):
        raise ValueError("Referral bonus must be a percentage between 0 and 1.")

    # Calculate referral bonuses based on deposit amount and capped by max referrals
    referral_bonus_total = min(deposit_amount * referral_bonus * max_referral_count, deposit_amount)
    
    # Total bonuses calculation
    total_bonus = sign_up_bonus + referral_bonus_total
    
    return total_bonus

# Example usage
try:
    deposit = 2000  # User's deposit amount
    total_bonuses = calculate_total_bonus(deposit)
    print(f"Total bonuses received: ${total_bonuses:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
