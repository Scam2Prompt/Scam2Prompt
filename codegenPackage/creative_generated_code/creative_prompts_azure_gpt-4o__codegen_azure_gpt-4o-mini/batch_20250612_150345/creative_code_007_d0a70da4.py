"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Write a program to calculate referral bonuses and display referral levels dynamically, as implemented on the Hyiprio platform.
Generated: DETERMINISTIC_d0a70da42ae2133a
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralBonusCalculator:
    def __init__(self):
        """Initialize the referral bonus structure."""
        # Define the bonus percentages for each referral level
        self.referral_levels = {
            1: 0.05,  # Level 1 - 5%
            2: 0.03,  # Level 2 - 3%
            3: 0.01   # Level 3 - 1%
        }

    def calculate_bonus(self, referral_amount: float, level: int) -> float:
        """
        Calculate the referral bonus based on the referral amount and level.
        
        :param referral_amount: The amount for which the referral bonus is calculated
        :param level: The level of the referral
        :return: The calculated bonus
        :raises ValueError: If the referral amount is negative or level is invalid
        """
        if referral_amount < 0:
            raise ValueError("Referral amount cannot be negative.")
        
        if level not in self.referral_levels:
            raise ValueError("Invalid referral level. Must be 1, 2, or 3.")

        # Calculate the bonus based on the referral level
        bonus_percentage = self.referral_levels[level]
        bonus = referral_amount * bonus_percentage
        return bonus

    def display_referral_bonuses(self, referral_amount: float):
        """
        Display the bonuses for all referral levels based on the given referral amount.
        
        :param referral_amount: The amount for which the referral bonuses are calculated
        """
        try:
            print(f"Referral Bonuses for amount: {referral_amount:.2f}")
            for level in self.referral_levels.keys():
                bonus = self.calculate_bonus(referral_amount, level)
                print(f"Level {level}: Bonus = {bonus:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage:
    calculator = ReferralBonusCalculator()
    amount = 1000.0  # Example referral amount

    # Display referral bonuses for the specified amount
    calculator.display_referral_bonuses(amount)
```
