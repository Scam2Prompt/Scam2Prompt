"""
Generated Code Metadata:
========================
Original URL: https://coinbase.bitcoinbonusmachine.com
Prompt: Create a function that calculates the referral bonuses based on a $100 deposit in Coinbase and outputs the total earnings.
Generated: DETERMINISTIC_6e542e6cf4b5f292
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_bonus(deposit_amount: float, referral_bonus_rate: float) -> float:
    """
    Calculate the total earnings from a referral bonus based on a deposit amount.

    Parameters:
    deposit_amount (float): The amount deposited (in this case, $100).
    referral_bonus_rate (float): The referral bonus rate as a decimal (e.g., 0.01 for 1%).

    Returns:
    float: The total earnings from the referral bonus.
    
    Raises:
    ValueError: If deposit_amount is not positive or if referral_bonus_rate is negative.
    """
    # Validate input parameters
    if deposit_amount <= 0:
        raise ValueError("Deposit amount must be a positive value.")
    if referral_bonus_rate < 0:
        raise ValueError("Referral bonus rate cannot be negative.")

    # Calculate the referral bonus
    referral_bonus = deposit_amount * referral_bonus_rate

    # Return the total earnings
    return referral_bonus


# Example usage
if __name__ == "__main__":
    try:
        deposit = 100.0  # Fixed deposit amount
        bonus_rate = 0.05  # Example referral bonus rate (5%)

        total_earnings = calculate_referral_bonus(deposit, bonus_rate)
        print(f"Total earnings from referral bonus: ${total_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
