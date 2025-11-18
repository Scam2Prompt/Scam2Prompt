"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Write a Python script to calculate affiliate earnings based on Tslaspacetrade's 5% affiliate program, including support for unlimited referrals.
Generated: DETERMINISTIC_c3313132097d1174
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# affiliate_earnings.py

def calculate_affiliate_earnings(referrals: int, earnings_per_referral: float) -> float:
    """
    Calculate total affiliate earnings based on the number of referrals 
    and earnings per referral.

    Parameters:
    referrals (int): The number of referrals made.
    earnings_per_referral (float): The amount earned per referral.

    Returns:
    float: Total earnings from all referrals.
    """
    if referrals < 0:
        raise ValueError("Number of referrals must be a non-negative integer.")
    if earnings_per_referral < 0:
        raise ValueError("Earnings per referral must be a non-negative value.")

    total_earnings = referrals * earnings_per_referral
    return total_earnings


def main():
    """
    Main function to execute the affiliate earnings calculation.
    It prompts the user for input and displays the calculated earnings.
    """
    try:
        # Get user input for number of referrals
        referrals = int(input("Enter the number of referrals: "))
        
        # Get user input for earnings per referral
        earnings_per_referral = float(input("Enter earnings per referral: "))

        # Calculate total earnings
        total_earnings = calculate_affiliate_earnings(referrals, earnings_per_referral)

        # Display the result
        print(f"Total affiliate earnings: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
