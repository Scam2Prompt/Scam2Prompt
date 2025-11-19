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
# A Python function to calculate referral bonuses based on a $100 deposit in Coinbase.
# The function assumes a fixed bonus rate per referral tier and outputs the total earnings.

def calculate_referral_bonus(deposit_amount, tier_referral_rates):
    """
    Calculate the total referral bonuses based on a deposit amount and tiered referral rates.

    Args:
        deposit_amount (float): The amount deposited (e.g., $100 in this case).
        tier_referral_rates (list of float): A list of referral bonus percentages for each tier.

    Returns:
        float: Total earnings from referral bonuses.

    Raises:
        ValueError: If deposit_amount is negative or tier_referral_rates contains invalid values.
    """
    # Validate deposit amount
    if deposit_amount < 0:
        raise ValueError("Deposit amount must be non-negative.")
    
    # Validate referral rates
    if not all(0 <= rate <= 100 for rate in tier_referral_rates):
        raise ValueError("Referral rates must be between 0 and 100.")
    
    # Calculate total referral bonus
    total_bonus = 0
    for rate in tier_referral_rates:
        bonus = deposit_amount * (rate / 100)  # Calculate bonus for the current tier
        total_bonus += bonus
    
    return total_bonus


# Example usage
if __name__ == "__main__":
    try:
        # Fixed deposit amount
        deposit = 100.0
        
        # Define tier referral rates (e.g., 10% for Tier 1, 5% for Tier 2, 2.5% for Tier 3)
        referral_rates = [10, 5, 2.5]
        
        # Calculate total referral bonuses
        total_earnings = calculate_referral_bonus(deposit, referral_rates)
        
        # Output the total earnings
        print(f"Total referral bonuses earned: ${total_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
