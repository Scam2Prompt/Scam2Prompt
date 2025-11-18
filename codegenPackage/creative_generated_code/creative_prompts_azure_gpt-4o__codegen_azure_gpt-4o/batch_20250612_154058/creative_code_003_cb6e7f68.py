"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Generate a Python script to calculate referral bonuses based on a referral code system, where users earn a percentage of their referrals' earnings.
Generated: DETERMINISTIC_cb6e7f688e5f3431
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ReferralBonusCalculator:
    """
    Class to calculate referral bonuses based on a referral code system.
    Users earn a percentage of their referrals' earnings.
    """

    def __init__(self, referral_percentage):
        """
        Initialize the calculator with a referral percentage.

        :param referral_percentage: Percentage of referrals' earnings to be given as a bonus (e.g., 10 for 10%).
        """
        if not (0 <= referral_percentage <= 100):
            raise ValueError("Referral percentage must be between 0 and 100.")
        self.referral_percentage = referral_percentage / 100

    def calculate_bonus(self, referral_earnings):
        """
        Calculate the referral bonus based on the referral earnings.

        :param referral_earnings: Dictionary where keys are user IDs, and values are their earnings.
        :return: Dictionary of referral bonuses for each user.
        """
        if not isinstance(referral_earnings, dict):
            raise TypeError("Referral earnings must be a dictionary.")
        if not all(isinstance(value, (int, float)) and value >= 0 for value in referral_earnings.values()):
            raise ValueError("All earnings must be non-negative numbers.")

        referral_bonuses = {}
        for user, earnings in referral_earnings.items():
            bonus = earnings * self.referral_percentage
            referral_bonuses[user] = round(bonus, 2)  # Round to 2 decimal places for currency-like values
        return referral_bonuses


def main():
    """
    Main function to demonstrate calculating referral bonuses.
    """
    try:
        # Example referral percentage (e.g., users earn 10% of their referrals' earnings)
        referral_percentage = 10  # Modify as needed

        # Example input data: A dictionary of user IDs and their earnings
        referral_earnings = {
            "user1": 5000,
            "user2": 2500,
            "user3": 1200,
            "user4": 800,
        }

        # Initialize the ReferralBonusCalculator
        calculator = ReferralBonusCalculator(referral_percentage)

        # Calculate the referral bonuses
        referral_bonuses = calculator.calculate_bonus(referral_earnings)

        # Display the results
        print("Referral Bonuses:")
        for user, bonus in referral_bonuses.items():
            print(f"{user}: ${bonus}")

    except ValueError as ve:
        print(f"ValueError: {ve}", file=sys.stderr)
    except TypeError as te:
        print(f"TypeError: {te}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
