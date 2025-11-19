"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Provide code examples for implementing a bonus system that matches Parimatch's +100% first deposit bonus with conditions like wagering requirements and expiration periods.
Generated: DETERMINISTIC_0b27f58b5ab0f786
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BonusSystem:
    def __init__(self, bonus_percentage=100, wagering_requirement=5, expiration_days=30):
        """
        Initializes the BonusSystem with default values.
        
        :param bonus_percentage: Percentage of the first deposit bonus (default is 100%)
        :param wagering_requirement: Multiplier for the bonus amount to be wagered (default is 5)
        :param expiration_days: Number of days until the bonus expires (default is 30 days)
        """
        self.bonus_percentage = bonus_percentage
        self.wagering_requirement = wagering_requirement
        self.expiration_days = expiration_days
        self.bonus_amount = 0
        self.deposit_amount = 0
        self.wagered_amount = 0
        self.is_active = False

    def activate_bonus(self, deposit_amount):
        """
        Activates the bonus based on the user's first deposit.
        
        :param deposit_amount: The amount of the first deposit
        :raises ValueError: If the deposit amount is less than or equal to zero
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.deposit_amount = deposit_amount
        self.bonus_amount = (self.bonus_percentage / 100) * deposit_amount
        self.is_active = True

    def wager(self, amount):
        """
        Wagers a specified amount against the bonus.
        
        :param amount: The amount to wager
        :raises ValueError: If the amount is less than or equal to zero or exceeds the available bonus
        """
        if amount <= 0:
            raise ValueError("Wager amount must be greater than zero.")
        if amount > self.bonus_amount - self.wagered_amount:
            raise ValueError("Wager amount exceeds available bonus.")
        
        self.wagered_amount += amount

    def is_bonus_fulfilled(self):
        """
        Checks if the wagering requirement has been fulfilled.
        
        :return: True if the wagering requirement is met, False otherwise
        """
        return self.wagered_amount >= (self.bonus_amount * self.wagering_requirement)

    def expire_bonus(self):
        """
        Expires the bonus after the specified expiration period.
        This method should be called after the expiration period has passed.
        """
        self.is_active = False
        self.bonus_amount = 0
        self.wagered_amount = 0
        self.deposit_amount = 0

    def get_bonus_info(self):
        """
        Returns the current status of the bonus.
        
        :return: A dictionary containing bonus information
        """
        return {
            "is_active": self.is_active,
            "deposit_amount": self.deposit_amount,
            "bonus_amount": self.bonus_amount,
            "wagered_amount": self.wagered_amount,
            "wagering_requirement": self.wagering_requirement,
            "bonus_fulfilled": self.is_bonus_fulfilled()
        }


# Example usage
if __name__ == "__main__":
    try:
        bonus_system = BonusSystem()
        bonus_system.activate_bonus(100)  # User deposits $100
        bonus_system.wager(200)  # User wagers $200
        print(bonus_system.get_bonus_info())  # Check bonus status
    except ValueError as e:
        print(f"Error: {e}")
```
