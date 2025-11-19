"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Create a Python program to simulate the referral program earnings described on MFX-Online Trade, allowing users to input the number of referrals and their deposit amounts.
Generated: DETERMINISTIC_aa27d527582b368b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    """
    Simulates the referral program earnings on MFX-Online Trade.
    """

    def __init__(self):
        # Commission rates for referrals (assuming these are fixed values)
        self.commission_rates = {
            'direct': 0.1,  # 10% commission on direct referrals
            'level1': 0.05,  # 5% commission on level 1 referrals
            'level2': 0.02  # 2% commission on level 2 referrals
        }

    def calculate_earnings(self, referrals):
        """
        Calculates earnings from referrals.

        Args:
            referrals (list): List of referral deposit amounts.

        Returns:
            float: Total earnings from referrals.
        """
        total_earnings = 0
        for i, deposit in enumerate(referrals):
            if i == 0:
                # Direct referral
                total_earnings += deposit * self.commission_rates['direct']
            elif i == 1:
                # Level 1 referral
                total_earnings += deposit * self.commission_rates['level1']
            elif i >= 2:
                # Level 2 referral
                total_earnings += deposit * self.commission_rates['level2']
        return total_earnings

    def get_referral_input(self):
        """
        Gets user input for number of referrals and their deposit amounts.

        Returns:
            list: List of referral deposit amounts.
        """
        try:
            num_referrals = int(input("Enter the number of referrals: "))
            referrals = []
            for i in range(num_referrals):
                while True:
                    try:
                        deposit = float(input(f"Enter deposit amount for referral {i+1}: $"))
                        if deposit < 0:
                            print("Deposit amount cannot be negative.")
                        else:
                            referrals.append(deposit)
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            return referrals
        except ValueError:
            print("Invalid input. Please enter a valid number for referrals.")
            return self.get_referral_input()

def main():
    program = ReferralProgram()
    referrals = program.get_referral_input()
    earnings = program.calculate_earnings(referrals)
    print(f"Total earnings from referrals: ${earnings:.2f}")

if __name__ == "__main__":
    main()
```
