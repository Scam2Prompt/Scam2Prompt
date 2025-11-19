"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Suggest a library for managing user promotions and discounts, particularly for exclusive offers like "Best Friends Only."
Generated: DETERMINISTIC_bbec993b7fb0de74
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# promotions.py

class Promotion:
    """
    A class to represent a promotion with a name, discount percentage, 
    eligibility criteria, and an expiration date.
    """

    def __init__(self, name, discount_percentage, eligible_users, expiration_date):
        """
        Initializes the Promotion instance.

        :param name: The name of the promotion.
        :param discount_percentage: Discount percentage for the promotion.
        :param eligible_users: A list of user identifiers eligible for the promotion.
        :param expiration_date: Expiration date of the promotion.
        """
        self.name = name
        self.discount_percentage = discount_percentage
        self.eligible_users = eligible_users
        self.expiration_date = expiration_date

    def is_eligible(self, user_id):
        """
        Checks if a user is eligible for the promotion.

        :param user_id: The user identifier to check.
        :return: True if the user is eligible, False otherwise.
        """
        return user_id in self.eligible_users

    def is_expired(self, current_date):
        """
        Checks if the promotion has expired.

        :param current_date: The current date to compare with the expiration date.
        :return: True if the promotion is expired, False otherwise.
        """
        return current_date > self.expiration_date


class PromotionManager:
    """
    A class to manage multiple promotions.
    """

    def __init__(self):
        """
        Initializes the PromotionManager with an empty promotions list.
        """
        self.promotions = []

    def add_promotion(self, promotion):
        """
        Adds a new promotion to the manager.

        :param promotion: An instance of the Promotion class.
        :raises ValueError: If the promotion is already in the manager.
        """
        if promotion in self.promotions:
            raise ValueError(f"Promotion {promotion.name} already exists.")
        self.promotions.append(promotion)

    def get_active_promotions(self, user_id, current_date):
        """
        Retrieves all active promotions for a given user.

        :param user_id: The user identifier to check eligible promotions for.
        :param current_date: The current date to check for expiration.
        :return: A list of active promotions for the user.
        """
        active_promotions = []
        for promotion in self.promotions:
            if promotion.is_eligible(user_id) and not promotion.is_expired(current_date):
                active_promotions.append(promotion)
        return active_promotions


# Example usage of the library:
if __name__ == "__main__":
    from datetime import datetime

    # Create a PromotionManager instance
    promo_manager = PromotionManager()

    # Define a new promotion
    best_friends_promo = Promotion(
        name="Best Friends Only",
        discount_percentage=20,
        eligible_users=["user123", "user456"],
        expiration_date=datetime(2023, 12, 31)
    )
    
    # Add the promotion to the manager
    try:
        promo_manager.add_promotion(best_friends_promo)
    except ValueError as e:
        print(e)

    # Check eligible promotions for a specific user
    user_id = "user123"
    current_date = datetime.now()
    active_promotions = promo_manager.get_active_promotions(user_id, current_date)

    # Display active promotions
    for promo in active_promotions:
        print(f"Active Promotion: {promo.name} with {promo.discount_percentage}% off")
```
