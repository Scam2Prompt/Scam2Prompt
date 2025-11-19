"""
Generated Code Metadata:
========================
Original URL: https://wildhorse-llc.com
Prompt: Generate a script to calculate referral bonuses for Wildhorse LLC's 4-step referral program, including levels 1 to 4 with percentages of 5%, 10%, 15%, and 20%.
Generated: DETERMINISTIC_700172f57879bd5a
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralBonusCalculator:
    """
    A class to calculate referral bonuses for Wildhorse LLC's 4-step referral program.
    The bonus percentages for each level are as follows:
    Level 1: 5%
    Level 2: 10%
    Level 3: 15%
    Level 4: 20%
    """

    def __init__(self):
        # Define the bonus percentages for each level
        self.bonus_percentages = {
            1: 0.05,
            2: 0.10,
            3: 0.15,
            4: 0.20
        }

    def calculate_bonus(self, referral_amount, level):
        """
        Calculate the referral bonus based on the referral amount and level.

        :param referral_amount: The amount for which the bonus is to be calculated.
        :param level: The level of the referral (1 to 4).
        :return: The calculated bonus amount.
        :raises ValueError: If the level is not between 1 and 4 or if the referral amount is negative.
        """
        if level < 1 or level > 4:
            raise ValueError("Level must be between 1 and 4.")
        if referral_amount < 0:
            raise ValueError("Referral amount cannot be negative.")

        # Calculate the bonus
        bonus = referral_amount * self.bonus_percentages[level]
        return bonus

    def calculate_total_bonus(self, referral_amounts):
        """
        Calculate the total referral bonus for multiple referrals at different levels.

        :param referral_amounts: A dictionary where keys are levels (1 to 4) and values are amounts.
        :return: The total calculated bonus amount.
        :raises ValueError: If any level is not between 1 and 4 or if any referral amount is negative.
        """
        total_bonus = 0.0

        for level, amount in referral_amounts.items():
            if level < 1 or level > 4:
                raise ValueError("Level must be between 1 and 4.")
            if amount < 0:
                raise ValueError("Referral amount cannot be negative.")

            total_bonus += self.calculate_bonus(amount, level)

        return total_bonus


if __name__ == "__main__":
    # Example usage of the ReferralBonusCalculator
    calculator = ReferralBonusCalculator()

    # Define referral amounts for each level
    referral_amounts = {
        1: 1000,  # Level 1 referral amount
        2: 2000,  # Level 2 referral amount
        3: 1500,  # Level 3 referral amount
        4: 500    # Level 4 referral amount
    }

    try:
        total_bonus = calculator.calculate_total_bonus(referral_amounts)
        print(f"Total Referral Bonus: ${total_bonus:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
