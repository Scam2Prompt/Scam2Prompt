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
# referral_bonus_calculator.py

class ReferralProgram:
    """
    Calculates referral bonuses for Wildhorse LLC's 4-step referral program.
    """

    def __init__(self):
        # Define referral levels and corresponding percentages
        self.referral_levels = {
            1: 0.05,  # 5%
            2: 0.10,  # 10%
            3: 0.15,  # 15%
            4: 0.20   # 20%
        }

    def calculate_bonus(self, level, amount):
        """
        Calculates the referral bonus for a given level and amount.

        Args:
            level (int): The referral level (1-4).
            amount (float): The amount to calculate the bonus for.

        Returns:
            float: The calculated referral bonus.

        Raises:
            ValueError: If the level is not in the range 1-4.
            TypeError: If the amount is not a positive number.
        """
        if not isinstance(level, int) or level < 1 or level > 4:
            raise ValueError("Invalid referral level. Must be between 1 and 4.")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TypeError("Invalid amount. Must be a positive number.")

        percentage = self.referral_levels.get(level)
        if percentage is None:
            raise ValueError("Invalid referral level. Must be between 1 and 4.")

        return amount * percentage

    def calculate_bonuses(self, referrals):
        """
        Calculates referral bonuses for multiple referrals.

        Args:
            referrals (list): A list of tuples containing the referral level and amount.

        Returns:
            dict: A dictionary with the referral level and amount as keys and the calculated bonus as value.

        Raises:
            ValueError: If the referrals list is empty.
        """
        if not referrals:
            raise ValueError("No referrals provided.")

        bonuses = {}
        for level, amount in referrals:
            try:
                bonus = self.calculate_bonus(level, amount)
                bonuses[(level, amount)] = bonus
            except (ValueError, TypeError) as e:
                print(f"Error calculating bonus for level {level} and amount {amount}: {str(e)}")

        return bonuses


def main():
    referral_program = ReferralProgram()

    # Example usage
    referrals = [
        (1, 1000.0),
        (2, 500.0),
        (3, 2000.0),
        (4, 1500.0),
        (5, 1000.0),  # Invalid level
        (1, -500.0),   # Invalid amount
    ]

    bonuses = referral_program.calculate_bonuses(referrals)

    print("Referral Bonuses:")
    for (level, amount), bonus in bonuses.items():
        print(f"Level {level}: ${amount:.2f} = ${bonus:.2f}")


if __name__ == "__main__":
    main()
```
