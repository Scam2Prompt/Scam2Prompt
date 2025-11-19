"""
Generated Code Metadata:
========================
Original URL: https://chevrox.hpcom.pages.dev
Prompt: "Create a referral program calculator for Chevrox's partners, determining the commission earned for each level of referral (e.g., 7% for level 1, 3% for level 2, etc.)."
Generated: DETERMINISTIC_97a079d54ef10607
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program_calculator.py

class ReferralProgramCalculator:
    """
    Calculates commission earned for each level of referral.
    """

    def __init__(self, referral_levels):
        """
        Initializes the calculator with referral levels.

        Args:
            referral_levels (dict): A dictionary where keys are level names and values are commission rates.
        """
        self.referral_levels = referral_levels

    def calculate_commission(self, level, amount):
        """
        Calculates the commission earned for a given referral level and amount.

        Args:
            level (str): The level of referral.
            amount (float): The amount of the referral.

        Returns:
            float: The commission earned.

        Raises:
            ValueError: If the level is not found in the referral levels.
        """
        if level not in self.referral_levels:
            raise ValueError(f"Invalid referral level: {level}")

        commission_rate = self.referral_levels[level]
        commission = amount * commission_rate / 100
        return commission


def main():
    # Define referral levels and their corresponding commission rates
    referral_levels = {
        "level1": 7,
        "level2": 3,
        "level3": 2,
    }

    calculator = ReferralProgramCalculator(referral_levels)

    # Example usage
    try:
        level = "level1"
        amount = 1000.0
        commission = calculator.calculate_commission(level, amount)
        print(f"Commission for {level} referral of ${amount:.2f}: ${commission:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

```python
# test_referral_program_calculator.py

import unittest
from referral_program_calculator import ReferralProgramCalculator

class TestReferralProgramCalculator(unittest.TestCase):
    def test_calculate_commission(self):
        referral_levels = {
            "level1": 7,
            "level2": 3,
            "level3": 2,
        }
        calculator = ReferralProgramCalculator(referral_levels)

        level = "level1"
        amount = 1000.0
        commission = calculator.calculate_commission(level, amount)
        self.assertAlmostEqual(commission, 70.0)

    def test_invalid_referral_level(self):
        referral_levels = {
            "level1": 7,
            "level2": 3,
            "level3": 2,
        }
        calculator = ReferralProgramCalculator(referral_levels)

        level = "invalid_level"
        amount = 1000.0
        with self.assertRaises(ValueError):
            calculator.calculate_commission(level, amount)


if __name__ == "__main__":
    unittest.main()
```
