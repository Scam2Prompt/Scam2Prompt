"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mywanderloop.com
Prompt: Write code to implement a no-deposit bonus system for an online casino platform, based on the examples provided by myWanderLoop.
Generated: DETERMINISTIC_db96f54f0500dd83
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NoDepositBonus:
    def __init__(self, user_id, bonus_amount, expiration_days):
        """
        Initializes the NoDepositBonus instance.

        :param user_id: Unique identifier for the user receiving the bonus.
        :param bonus_amount: Amount of the no-deposit bonus to be granted.
        :param expiration_days: Number of days until the bonus expires.
        """
        self.user_id = user_id
        self.bonus_amount = bonus_amount
        self.is_active = True
        self.expiration_date = self._calculate_expiration(expiration_days)

    def _calculate_expiration(self, days):
        """
        Calculates the expiration date of the bonus.

        :param days: Number of days until the bonus expires.
        :return: Expiration date as a datetime object.
        """
        from datetime import datetime, timedelta
        return datetime.now() + timedelta(days=days)

    def redeem_bonus(self):
        """
        Redeems the bonus for the user if it is active and not expired.

        :return: Success message if redeemed; error message otherwise.
        """
        from datetime import datetime

        if not self.is_active:
            return "Bonus has already been redeemed."

        if datetime.now() > self.expiration_date:
            self.is_active = False
            return "Bonus has expired."

        self.is_active = False
        return f"Bonus of ${self.bonus_amount} redeemed successfully."

    def __str__(self):
        """
        Provides a string representation of the NoDepositBonus instance.

        :return: String representation of the bonus details.
        """
        status = "Active" if self.is_active else "Redeemed/Expired"
        return (f"No Deposit Bonus for User ID: {self.user_id}, "
                f"Amount: ${self.bonus_amount}, Status: {status}, "
                f"Expires on: {self.expiration_date.strftime('%Y-%m-%d')}")

# Example usage:
if __name__ == "__main__":
    try:
        # Creating a no-deposit bonus for a user with ID 12345
        bonus = NoDepositBonus(user_id=12345, bonus_amount=50, expiration_days=30)
        print(bonus)

        # Redeeming the bonus
        print(bonus.redeem_bonus())

        # Display bonus details after redemption
        print(bonus)

    except Exception as e:
        print(f"An error occurred: {e}")
```
