"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wildhorse-llc.com
Prompt: Generate a script to calculate referral bonuses for Wildhorse LLC's 4-step referral program, including levels 1 to 4 with percentages of 5%, 10%, 15%, and 20%.
Generated: DETERMINISTIC_700172f57879bd5a
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralBonusCalculator:
    """
    A class to calculate referral bonuses for Wildhorse LLC's 4-step referral program.
    Each level has a specific percentage of bonus based on the total sales amount from referrals.
    """

    def __init__(self, sales_amount):
        """
        Initializes the ReferralBonusCalculator with the given sales amount.

        :param sales_amount: Total sales amount generated from referrals
        """
        if sales_amount < 0:
            raise ValueError("Sales amount must be a non-negative value.")
        self.sales_amount = sales_amount

    def calculate_bonus(self):
        """
        Calculate the total referral bonus across all levels of the referral program.

        :return: Total calculated referral bonus
        """
        levels = [0.05, 0.10, 0.15, 0.20]  # Bonus percentages for levels 1 to 4
        total_bonus = 0.0

        # Calculate bonuses for each level
        for level in range(1, 5):
            bonus = self._calculate_level_bonus(level, levels[level - 1])
            total_bonus += bonus
        
        return total_bonus

    def _calculate_level_bonus(self, level, percentage):
        """
        Calculate the bonus for a specific level.

        :param level: The referral level (1 to 4)
        :param percentage: Bonus percentage for the level
        :return: Calculated bonus for the level
        """
        return self.sales_amount * percentage

def main():
    """
    Main function to execute the referral bonus calculation.
    Prompts the user for input and displays the calculated bonus.
    """
    try:
        sales_amount = float(input("Enter the total sales amount generated from referrals: "))
        calculator = ReferralBonusCalculator(sales_amount)
        bonus = calculator.calculate_bonus()
        print(f"The total referral bonus is: ${bonus:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
