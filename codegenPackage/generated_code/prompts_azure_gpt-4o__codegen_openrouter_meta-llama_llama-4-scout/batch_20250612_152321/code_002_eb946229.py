"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: Generate a Python script to calculate referral earnings based on the Claim-Bits model of up to 200% of referral gains.
Generated: DETERMINISTIC_eb94622984e28272
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Referral Earnings Calculator based on Claim-Bits model.

Calculates referral earnings up to 200% of referral gains.
"""

def calculate_referral_earnings(referral_gains, referral_percentage):
    """
    Calculates referral earnings based on referral gains and percentage.

    Args:
        referral_gains (float): The total gains from referrals.
        referral_percentage (float): The percentage of referral gains to earn.

    Returns:
        float: The calculated referral earnings.

    Raises:
        ValueError: If referral gains or referral percentage is negative.
    """
    if referral_gains < 0 or referral_percentage < 0:
        raise ValueError("Referral gains and percentage must be non-negative.")

    # Cap referral percentage at 200%
    referral_percentage = min(referral_percentage, 200)

    # Calculate referral earnings
    referral_earnings = (referral_gains * referral_percentage) / 100

    return referral_earnings


def main():
    try:
        # Example usage
        referral_gains = 1000.0  # Total gains from referrals
        referral_percentage = 150.0  # Percentage of referral gains to earn

        earnings = calculate_referral_earnings(referral_gains, referral_percentage)
        print(f"Referral earnings: ${earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
