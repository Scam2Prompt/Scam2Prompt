"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxgainfinance.com
Prompt: Write a Python script to simulate the referral program, including both Level 1 and Level 2 commissions, and calculate total earnings for a given number of referrals.
Generated: DETERMINISTIC_8931d748543ba9d1
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Simulation

This script calculates the total earnings for a given number of referrals in a referral program.
It includes both Level 1 and Level 2 commissions.

- Level 1 refers to direct referrals by the user.
- Level 2 refers to referrals made by the user's direct referrals.
"""

# Import necessary modules
import sys

def calculate_referral_earnings(level1_referrals, level2_referrals_per_level1, commission_level1, commission_level2):
    """
    Calculate total earnings from Level 1 and Level 2 referrals.

    Parameters:
        level1_referrals (int): Number of direct referrals made by the user.
        level2_referrals_per_level1 (int): Number of referrals made by each Level 1 referral.
        commission_level1 (float): Commission earned per Level 1 referral.
        commission_level2 (float): Commission earned per Level 2 referral.

    Returns:
        float: Total earnings from both Level 1 and Level 2 referrals.
    """
    if level1_referrals < 0 or level2_referrals_per_level1 < 0:
        raise ValueError("Referral numbers must be non-negative.")
    if commission_level1 < 0 or commission_level2 < 0:
        raise ValueError("Commission values must be non-negative.")

    # Calculate earnings from Level 1 referrals
    level1_earnings = level1_referrals * commission_level1

    # Calculate earnings from Level 2 referrals
    total_level2_referrals = level1_referrals * level2_referrals_per_level1
    level2_earnings = total_level2_referrals * commission_level2

    # Total earnings
    total_earnings = level1_earnings + level2_earnings
    return total_earnings

def main():
    """
    Main function to simulate the referral program.
    Prompts the user for input and calculates total earnings.
    """
    try:
        # Prompt user for input
        print("Referral Program Simulation")
        level1_referrals = int(input("Enter the number of Level 1 referrals: "))
        level2_referrals_per_level1 = int(input("Enter the number of Level 2 referrals per Level 1 referral: "))
        commission_level1 = float(input("Enter the commission per Level 1 referral: "))
        commission_level2 = float(input("Enter the commission per Level 2 referral: "))

        # Calculate total earnings
        total_earnings = calculate_referral_earnings(
            level1_referrals, level2_referrals_per_level1, commission_level1, commission_level2
        )

        # Display the result
        print(f"\nTotal earnings: ${total_earnings:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
