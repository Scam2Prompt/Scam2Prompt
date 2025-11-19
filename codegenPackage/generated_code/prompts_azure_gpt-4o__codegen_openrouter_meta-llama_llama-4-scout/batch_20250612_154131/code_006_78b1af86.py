"""
Generated Code Metadata:
========================
Original URL: https://unstaked-token.world
Prompt: Write a script to calculate referral earnings based on the number of referrals and the token purchase amount during the $UNSD presale.
Generated: DETERMINISTIC_78b1af862ba492ea
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_calculator.py

def calculate_referral_earnings(referrals: int, token_purchase_amount: float, referral_rate: float = 0.1) -> float:
    """
    Calculate referral earnings based on the number of referrals and the token purchase amount.

    Args:
    - referrals (int): The number of referrals.
    - token_purchase_amount (float): The token purchase amount during the $UNSD presale.
    - referral_rate (float, optional): The referral rate. Defaults to 0.1 (10%).

    Returns:
    - float: The referral earnings.

    Raises:
    - ValueError: If referrals or token_purchase_amount is negative.
    - TypeError: If referrals is not an integer or token_purchase_amount is not a number.
    """

    # Validate input types
    if not isinstance(referrals, int):
        raise TypeError("Referrals must be an integer.")
    if not isinstance(token_purchase_amount, (int, float)):
        raise TypeError("Token purchase amount must be a number.")

    # Validate input values
    if referrals < 0:
        raise ValueError("Referrals cannot be negative.")
    if token_purchase_amount < 0:
        raise ValueError("Token purchase amount cannot be negative.")

    # Calculate referral earnings
    referral_earnings = referrals * token_purchase_amount * referral_rate

    return referral_earnings


def main():
    try:
        # Example usage
        referrals = 10
        token_purchase_amount = 1000.0

        earnings = calculate_referral_earnings(referrals, token_purchase_amount)
        print(f"Referral earnings: ${earnings:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
