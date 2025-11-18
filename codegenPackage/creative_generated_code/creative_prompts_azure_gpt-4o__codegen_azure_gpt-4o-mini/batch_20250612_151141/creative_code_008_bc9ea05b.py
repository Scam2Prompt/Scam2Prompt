"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Python script to automate the calculation of referral bonuses in CRUDO tokens and USDT, based on the referral program's tiered rewards system.
Generated: DETERMINISTIC_bc9ea05b94b79005
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus_calculator.py

class ReferralProgram:
    def __init__(self):
        # Define the referral bonus tiers in CRUDO and USDT
        self.tiers = {
            1: {'crudo': 100, 'usdt': 10},  # Tier 1
            2: {'crudo': 200, 'usdt': 20},  # Tier 2
            3: {'crudo': 300, 'usdt': 30},  # Tier 3
            4: {'crudo': 400, 'usdt': 40},  # Tier 4
        }

    def calculate_bonus(self, tier, referrals):
        """
        Calculate the total referral bonus based on the tier and the number of referrals.

        :param tier: The tier level (integer)
        :param referrals: The number of referrals (integer)
        :return: A dictionary containing the total CRUDO and USDT bonuses
        :raises ValueError: If the tier is invalid or referrals are negative
        """
        if tier not in self.tiers:
            raise ValueError("Invalid tier provided.")
        if referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")

        # Calculate bonuses
        tier_bonus = self.tiers[tier]
        total_bonus = {
            'crudo': tier_bonus['crudo'] * referrals,
            'usdt': tier_bonus['usdt'] * referrals
        }
        return total_bonus

def main():
    referral_program = ReferralProgram()

    # Example usage
    try:
        user_tier = int(input("Enter your referral tier (1-4): "))
        num_referrals = int(input("Enter the number of referrals: "))

        # Calculate referral bonuses
        bonuses = referral_program.calculate_bonus(user_tier, num_referrals)

        # Display results
        print(f"Total bonus for {num_referrals} referrals at tier {user_tier}:")
        print(f"CRUDO Tokens: {bonuses['crudo']}")
        print(f"USDT: {bonuses['usdt']}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
