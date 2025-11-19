"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Write a code example for a promotional system that offers bonuses and cashback for new users, similar to the incentives provided by 789Club.
Generated: DETERMINISTIC_5841e6c4a3cdebc2
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PromotionalSystem:
    def __init__(self):
        self.user_promotions = {}

    def register_user(self, user_id):
        """
        Register a new user and assign promotional bonuses.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_promotions:
            raise ValueError("User already registered.")

        # Assign a random bonus and cashback percentage for the new user
        self.user_promotions[user_id] = {
            'bonus_amount': self.generate_bonus(),
            'cashback_percentage': self.generate_cashback()
        }
        print(f"User {user_id} registered with bonus {self.user_promotions[user_id]['bonus_amount']} "
              f"and cashback {self.user_promotions[user_id]['cashback_percentage']}%.")

    def generate_bonus(self):
        """
        Generate a random bonus amount for new users.

        :return: Random bonus amount between 10 and 100
        """
        return random.randint(10, 100)

    def generate_cashback(self):
        """
        Generate a random cashback percentage for new users.

        :return: Random cashback percentage between 5 and 20
        """
        return random.randint(5, 20)

    def get_user_promotions(self, user_id):
        """
        Retrieve the promotional details for a specific user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing bonus amount and cashback percentage
        """
        if user_id not in self.user_promotions:
            raise ValueError("User not found.")
        
        return self.user_promotions[user_id]

def main():
    promo_system = PromotionalSystem()

    # Register a few new users to demonstrate the promotional system
    try:
        promo_system.register_user('user_1')
        promo_system.register_user('user_2')
        promo_system.register_user('user_1')  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve and display promotions for a registered user
    try:
        user_promotions = promo_system.get_user_promotions('user_1')
        print(f"Promotions for user_1: {user_promotions}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
