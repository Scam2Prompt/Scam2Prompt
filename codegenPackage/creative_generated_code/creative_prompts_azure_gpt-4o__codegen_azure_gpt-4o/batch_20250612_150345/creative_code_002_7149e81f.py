"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Create a script to implement a referral bonus system with multiple levels, as outlined in the Hyiprio referral level system.
Generated: DETERMINISTIC_7149e81f6f37ddc2
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Bonus System Implementation

This script implements a multi-level referral bonus system inspired by the Hyiprio referral level system.
The system supports configurable bonus percentages for each level and includes error handling and validations.

Author: Expert Programmer
"""

class ReferralBonusSystem:
    def __init__(self, level_percentages):
        """
        Initializes the referral bonus system.

        :param level_percentages: A dictionary specifying bonus percentages for each referral level.
                                  Example: {1: 10, 2: 5, 3: 2} (Level 1: 10%, Level 2: 5%, Level 3: 2%)
        """
        if not isinstance(level_percentages, dict) or not all(
            isinstance(level, int) and isinstance(percent, (int, float)) for level, percent in level_percentages.items()
        ):
            raise ValueError("Invalid level_percentages format. Must be a dictionary of levels and percentages.")
        
        self.level_percentages = level_percentages

    def calculate_bonus(self, transaction_amount, referral_chain):
        """
        Calculates referral bonuses for a transaction across multiple levels.

        :param transaction_amount: The transaction amount (float or int).
        :param referral_chain: A list of referral IDs in order of levels. Level 1 is the direct referrer, Level 2 is the
                               referrer of Level 1, and so on.
                               Example: ["referrer1", "referrer2", "referrer3"]
        :return: A dictionary mapping referral IDs to their calculated bonuses.
                 Example: {"referrer1": 100.0, "referrer2": 50.0, "referrer3": 20.0}
        """
        if not isinstance(transaction_amount, (int, float)) or transaction_amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")
        
        if not isinstance(referral_chain, list) or not all(isinstance(referrer, str) for referrer in referral_chain):
            raise ValueError("Referral chain must be a list of string referral IDs.")

        bonuses = {}
        for level, referrer in enumerate(referral_chain, start=1):
            if level in self.level_percentages:
                bonus_percentage = self.level_percentages[level]
                bonus_amount = (transaction_amount * bonus_percentage) / 100
                bonuses[referrer] = round(bonus_amount, 2)  # Round to 2 decimal places for currency representation
        
        return bonuses

# Example usage
if __name__ == "__main__":
    try:
        # Define referral level percentages
        level_percentages = {1: 10, 2: 5, 3: 2}

        # Initialize the referral bonus system
        referral_system = ReferralBonusSystem(level_percentages)

        # Simulate a transaction
        transaction_amount = 1000.0
        referral_chain = ["referrer1", "referrer2", "referrer3"]

        # Calculate bonuses
        bonuses = referral_system.calculate_bonus(transaction_amount, referral_chain)
        
        # Output the results
        print("Referral Bonuses:")
        for referrer, bonus in bonuses.items():
            print(f"{referrer}: ${bonus}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
