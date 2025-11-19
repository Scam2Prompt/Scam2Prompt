"""
Generated Code Metadata:
========================
Original URL: https://mywanderloop.com
Prompt: Write code to implement a no-deposit bonus system for an online casino platform, based on the examples provided by myWanderLoop.
Generated: DETERMINISTIC_db96f54f0500dd83
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class NoDepositBonus:
    def __init__(self, bonus_amount, expiration_days):
        """
        Initialize the NoDepositBonus with a specified amount and expiration period.

        :param bonus_amount: The amount of the no-deposit bonus.
        :param expiration_days: The number of days until the bonus expires.
        """
        self.bonus_amount = bonus_amount
        self.expiration_date = datetime.now() + timedelta(days=expiration_days)
        self.is_active = True

    def redeem_bonus(self, user):
        """
        Redeem the no-deposit bonus for a user if eligible.

        :param user: The user object attempting to redeem the bonus.
        :return: A message indicating the result of the redemption attempt.
        """
        if not self.is_active:
            return "Bonus has already been redeemed or is inactive."
        
        if datetime.now() > self.expiration_date:
            self.is_active = False
            return "Bonus has expired."

        if user.has_bonus:
            return "User has already redeemed a bonus."

        user.balance += self.bonus_amount
        user.has_bonus = True
        return f"Bonus of {self.bonus_amount} redeemed successfully!"

class User:
    def __init__(self, username):
        """
        Initialize a user with a username and a starting balance.

        :param username: The username of the user.
        """
        self.username = username
        self.balance = 0.0
        self.has_bonus = False

    def __str__(self):
        return f"User: {self.username}, Balance: {self.balance}, Has Bonus: {self.has_bonus}"

def main():
    # Example usage of the NoDepositBonus system
    try:
        # Create a user
        user1 = User("Player1")

        # Create a no-deposit bonus of $10 that expires in 7 days
        bonus = NoDepositBonus(bonus_amount=10.0, expiration_days=7)

        # Attempt to redeem the bonus
        print(bonus.redeem_bonus(user1))  # Should succeed
        print(user1)  # Check user balance after redemption

        # Attempt to redeem the bonus again
        print(bonus.redeem_bonus(user1))  # Should fail, already redeemed

        # Simulate waiting for the bonus to expire
        bonus.expiration_date = datetime.now() - timedelta(days=1)
        print(bonus.redeem_bonus(user1))  # Should fail, bonus expired

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
