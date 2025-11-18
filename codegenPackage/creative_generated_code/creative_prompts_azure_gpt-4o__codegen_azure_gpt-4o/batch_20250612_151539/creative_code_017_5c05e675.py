"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Generate a script to calculate the expiration dates for unused bonus funds and free spins, adhering to the rules outlined on Santa Claus Casino.
Generated: DETERMINISTIC_5c05e675fea3c0d3
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ExpirationCalculator:
    """
    A class to calculate expiration dates for unused bonus funds and free spins
    as per rules defined by Santa Claus Casino.
    """

    def __init__(self, bonus_days=30, free_spins_days=7):
        """
        Initializes the ExpirationCalculator.

        :param bonus_days: Number of days bonus funds are valid (default: 30 days).
        :param free_spins_days: Number of days free spins are valid (default: 7 days).
        """
        self.bonus_days = bonus_days
        self.free_spins_days = free_spins_days

    def calculate_expiration(self, start_date, item_type):
        """
        Calculate the expiration date for the given item type starting from the provided date.

        :param start_date: The date the bonus or free spins were granted (datetime object).
        :param item_type: Type of the item ('bonus' or 'free_spins').

        :return: Expiration date as a datetime object.
        :raises ValueError: If an invalid item_type is provided.
        """
        if item_type not in ['bonus', 'free_spins']:
            raise ValueError("Invalid item_type. Must be 'bonus' or 'free_spins'.")

        days_valid = self.bonus_days if item_type == 'bonus' else self.free_spins_days
        expiration_date = start_date + datetime.timedelta(days=days_valid)
        return expiration_date

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator
        calculator = ExpirationCalculator()

        # Define the start date and item types
        start_date = datetime.datetime.now()  # Today's date
        bonus_expiration = calculator.calculate_expiration(start_date, "bonus")
        free_spins_expiration = calculator.calculate_expiration(start_date, "free_spins")

        # Print the expiration dates
        print(f"Bonus funds expiration date: {bonus_expiration}")
        print(f"Free spins expiration date: {free_spins_expiration}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
