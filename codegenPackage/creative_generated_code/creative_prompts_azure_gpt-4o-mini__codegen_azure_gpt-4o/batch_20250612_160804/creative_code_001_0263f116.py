"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pufferr.pages.dev
Prompt: Write a code snippet to calculate staking multipliers based on user registration, inspired by the Puffer rewards system.
Generated: DETERMINISTIC_0263f116c3f1fd73
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class StakingMultiplierCalculator:
    """
    A class to calculate staking multipliers for users based on their registration date.

    Attributes:
        base_multiplier (float): The base multiplier applied to all users.
        bonus_multiplier (float): The bonus multiplier for early registrants.
        threshold_date (datetime.date): The cutoff date for early registration eligibility.
    """

    def __init__(self, base_multiplier=1.0, bonus_multiplier=0.2, threshold_date=datetime.date(2022, 1, 1)):
        """
        Initialize the calculator with customizable parameters.
        """
        self.base_multiplier = base_multiplier
        self.bonus_multiplier = bonus_multiplier
        self.threshold_date = threshold_date

    def calculate_multiplier(self, registration_date):
        """
        Calculate the staking multiplier for a user based on their registration date.

        Args:
            registration_date (datetime.date): The registration date of the user.

        Returns:
            float: The staking multiplier for the user.
        """
        if not isinstance(registration_date, datetime.date):
            raise ValueError("registration_date must be a datetime.date object")

        # Provide bonus multiplier for users who registered before the threshold date
        if registration_date < self.threshold_date:
            return self.base_multiplier + self.bonus_multiplier
        return self.base_multiplier


if __name__ == "__main__":
    try:
        # Example usage of the calculator
        calculator = StakingMultiplierCalculator()

        # Sample user registration dates
        user_1_date = datetime.date(2021, 12, 15)
        user_2_date = datetime.date(2022, 5, 10)

        # Calculate staking multipliers
        user_1_multiplier = calculator.calculate_multiplier(user_1_date)
        user_2_multiplier = calculator.calculate_multiplier(user_2_date)

        print(f"User 1 Multiplier: {user_1_multiplier}")  # Output: 1.2
        print(f"User 2 Multiplier: {user_2_multiplier}")  # Output: 1.0

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
