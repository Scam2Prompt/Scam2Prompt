"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Generate a Python script to calculate referral earnings based on the Claim-Bits model of up to 200% of referral gains.
Generated: DETERMINISTIC_eb94622984e28272
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
Referral Earnings Calculator based on the Claim-Bits model.

This script calculates the earnings a user can receive from referrals
based on the percentage of their referral gains. The maximum earning
potential is capped at 200% of the referral gains.
"""

class ReferralEarningsCalculator:
    def __init__(self, referral_gain: float):
        """
        Initializes the calculator with the given referral gain.

        :param referral_gain: The total earnings from referrals.
        """
        self.referral_gain = referral_gain
        self.max_earning_percentage = 2.0  # 200%

    def calculate_earnings(self) -> float:
        """
        Calculates the total referral earnings.

        :return: The calculated earnings, capped at 200% of referral gains.
        """
        if self.referral_gain < 0:
            raise ValueError("Referral gain must be a non-negative value.")

        # Calculate the maximum earnings based on the claim-bits model
        earnings = self.referral_gain * self.max_earning_percentage
        return earnings

def main():
    """
    Main function to execute the referral earnings calculation.
    """
    try:
        # Input: Get the referral gains from the user
        referral_gain_input = input("Enter the total referral gain: ")

        # Convert input to float and create an instance of the calculator
        referral_gain = float(referral_gain_input)
        calculator = ReferralEarningsCalculator(referral_gain)

        # Calculate and display the earnings
        earnings = calculator.calculate_earnings()
        print(f"The total referral earnings are: ${earnings:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
