"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Provide code examples for implementing a bonus system that matches Parimatch's +100% first deposit bonus with conditions like wagering requirements and expiration periods.
Generated: DETERMINISTIC_0b27f58b5ab0f786
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BonusSystem:
    """
    A class to represent a bonus system for an online betting platform.
    This implementation includes a +100% first deposit bonus with conditions:
    - Wagering requirements
    - Expiration period
    """

    def __init__(self):
        """Initialize the bonus system with default values."""
        self.bonus_percentage = 100  # Bonus percentage for the first deposit
        self.wagering_requirement = 5  # Wagering requirement multiplier
        self.expiration_period_days = 30  # Bonus expiration period in days

    def calculate_bonus(self, deposit_amount):
        """
        Calculate the bonus amount based on the deposit.

        Args:
            deposit_amount (float): The amount of the user's first deposit.

        Returns:
            float: The calculated bonus amount.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        bonus_amount = deposit_amount * (self.bonus_percentage / 100)
        return bonus_amount

    def apply_wagering_requirements(self, bonus_amount):
        """
        Calculate the total amount that needs to be wagered to unlock the bonus.

        Args:
            bonus_amount (float): The amount of the bonus.

        Returns:
            float: Total wagering requirement amount.
        """
        if bonus_amount <= 0:
            raise ValueError("Bonus amount must be greater than zero.")
        
        total_wagering = bonus_amount * self.wagering_requirement
        return total_wagering

    def is_bonus_expired(self, bonus_start_date, current_date):
        """
        Check if the bonus has expired.

        Args:
            bonus_start_date (datetime): The date the bonus was granted.
            current_date (datetime): The current date to check against.

        Returns:
            bool: True if the bonus is expired, False otherwise.
        """
        from datetime import timedelta

        if not isinstance(bonus_start_date, datetime) or not isinstance(current_date, datetime):
            raise TypeError("Both dates must be datetime objects.")
        
        expiration_date = bonus_start_date + timedelta(days=self.expiration_period_days)
        return current_date > expiration_date

# Example usage of the BonusSystem class
if __name__ == "__main__":
    from datetime import datetime
    
    # Create an instance of the BonusSystem
    bonus_system = BonusSystem()

    # User's first deposit amount
    deposit = 100.0  # User deposits $100

    # Calculate the bonus
    try:
        bonus = bonus_system.calculate_bonus(deposit)
        print(f"Bonus Amount: ${bonus:.2f}")

        # Apply wagering requirements
        wagering_amount = bonus_system.apply_wagering_requirements(bonus)
        print(f"Total Wagering Requirement: ${wagering_amount:.2f}")

        # Check for expiration after a specific period
        bonus_start_date = datetime.now()
        current_date = bonus_start_date  # Simulate checking the same date

        if bonus_system.is_bonus_expired(bonus_start_date, current_date):
            print("The bonus has expired.")
        else:
            print("The bonus is still valid.")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
