"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Write a Python script to calculate and distribute promotional bonuses based on user deposits, as outlined in VZ99's first deposit promotion.
Generated: DETERMINISTIC_fbbef6ef4ce23420
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BonusCalculator:
    """
    A class to calculate and distribute promotional bonuses based on user deposits.
    """

    def __init__(self, bonus_percentage: float):
        """
        Initializes the BonusCalculator with a specified bonus percentage.

        :param bonus_percentage: The percentage of the deposit to be given as a bonus.
        """
        if not (0 <= bonus_percentage <= 100):
            raise ValueError("Bonus percentage must be between 0 and 100.")
        self.bonus_percentage = bonus_percentage / 100  # Convert to decimal

    def calculate_bonus(self, deposit: float) -> float:
        """
        Calculates the bonus for a given deposit.

        :param deposit: The amount of the deposit.
        :return: The calculated bonus.
        """
        if deposit < 0:
            raise ValueError("Deposit amount cannot be negative.")
        bonus = deposit * self.bonus_percentage
        logging.info(f"Calculated bonus for deposit {deposit}: {bonus}")
        return bonus

    def distribute_bonuses(self, deposits: List[float]) -> Dict[int, float]:
        """
        Distributes bonuses based on a list of deposits.

        :param deposits: A list of user deposits.
        :return: A dictionary mapping deposit index to calculated bonus.
        """
        bonuses = {}
        for index, deposit in enumerate(deposits):
            try:
                bonuses[index] = self.calculate_bonus(deposit)
            except ValueError as e:
                logging.error(f"Error calculating bonus for deposit at index {index}: {e}")
                bonuses[index] = 0  # Assign zero bonus in case of error
        return bonuses

def main():
    """
    Main function to execute the bonus calculation and distribution.
    """
    # Example deposits
    user_deposits = [1000, 2000, 1500, -500, 3000]  # The last deposit is invalid

    # Initialize the bonus calculator with a 10% bonus
    bonus_calculator = BonusCalculator(bonus_percentage=10)

    # Distribute bonuses based on user deposits
    bonuses = bonus_calculator.distribute_bonuses(user_deposits)

    # Output the results
    for index, bonus in bonuses.items():
        print(f"Deposit index {index}: Bonus = {bonus:.2f}")

if __name__ == "__main__":
    main()
```
