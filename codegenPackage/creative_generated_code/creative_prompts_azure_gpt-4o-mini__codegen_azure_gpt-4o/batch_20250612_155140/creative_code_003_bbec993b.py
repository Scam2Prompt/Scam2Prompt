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
"""
Library Name: PromotionsManager
Description: A Python library for managing user promotions and discounts, including exclusive offers
like "Best Friends Only." This library allows you to create, validate, and apply promotions.

Dependencies:
- Python >= 3.7
"""

import datetime


class PromotionError(Exception):
    """Custom exception for promotion-related errors."""
    pass


class Promotion:
    """
    Represents a single promotion.
    Attributes:
        name (str): The name of the promotion.
        discount_percentage (float): Percentage of discount (0-100).
        expiration_date (datetime.date): Expiration date of the promotion.
        is_exclusive (bool): True if the promotion is exclusive (e.g., "Best Friends Only").
        allowed_users (set): A set of users allowed to use this promotion (for exclusive offers).
    """

    def __init__(self, name, discount_percentage, expiration_date, is_exclusive=False, allowed_users=None):
        if not 0 <= discount_percentage <= 100:
            raise PromotionError("Discount percentage must be between 0 and 100.")
        if expiration_date < datetime.date.today():
            raise PromotionError("Expiration date cannot be in the past.")

        self.name = name
        self.discount_percentage = discount_percentage
        self.expiration_date = expiration_date
        self.is_exclusive = is_exclusive
        self.allowed_users = allowed_users if allowed_users else set()

    def is_valid_for_user(self, user_id):
        """
        Checks if the promotion is valid for the given user.
        Args:
            user_id (str): The user ID to check.
        Returns:
            bool: True if the promotion is valid for the user, False otherwise.
        """
        if self.expiration_date < datetime.date.today():
            return False  # Promotion expired.
        if self.is_exclusive and user_id not in self.allowed_users:
            return False  # User is not allowed to use this exclusive promotion.
        return True

    def apply_discount(self, original_price):
        """
        Applies the discount to the original price.
        Args:
            original_price (float): The original price of the item.
        Returns:
            float: The price after applying the discount.
        """
        if original_price < 0:
            raise PromotionError("Original price cannot be negative.")
        discount = (self.discount_percentage / 100) * original_price
        return round(original_price - discount, 2)


class PromotionsManager:
    """
    Manages a collection of promotions.
    Methods:
        add_promotion(promotion): Adds a promotion to the manager.
        remove_promotion(promotion_name): Removes a promotion by name.
        get_promotion(promotion_name): Retrieves a promotion by name.
        validate_promotion_for_user(promotion_name, user_id): Validates if a promotion is valid for a user.
        apply_promotion(promotion_name, user_id, original_price): Applies a promotion to a price for a user.
    """

    def __init__(self):
        self.promotions = {}

    def add_promotion(self, promotion):
        """
        Adds a promotion to the manager.
        Args:
            promotion (Promotion): The promotion to add.
        """
        if promotion.name in self.promotions:
            raise PromotionError(f"Promotion '{promotion.name}' already exists.")
        self.promotions[promotion.name] = promotion

    def remove_promotion(self, promotion_name):
        """
        Removes a promotion by name.
        Args:
            promotion_name (str): The name of the promotion to remove.
        """
        if promotion_name not in self.promotions:
            raise PromotionError(f"Promotion '{promotion_name}' does not exist.")
        del self.promotions[promotion_name]

    def get_promotion(self, promotion_name):
        """
        Retrieves a promotion by name.
        Args:
            promotion_name (str): The name of the promotion to retrieve.
        Returns:
            Promotion: The requested promotion, or None if not found.
        """
        return self.promotions.get(promotion_name)

    def validate_promotion_for_user(self, promotion_name, user_id):
        """
        Validates if a promotion is valid for a user.
        Args:
            promotion_name (str): The name of the promotion to validate.
            user_id (str): The user ID to validate against.
        Returns:
            bool: True if the promotion is valid for the user, False otherwise.
        """
        promotion = self.get_promotion(promotion_name)
        if not promotion:
            raise PromotionError(f"Promotion '{promotion_name}' does not exist.")
        return promotion.is_valid_for_user(user_id)

    def apply_promotion(self, promotion_name, user_id, original_price):
        """
        Applies a promotion to a price for a user.
        Args:
            promotion_name (str): The name of the promotion to apply.
            user_id (str): The user ID applying the promotion.
            original_price (float): The original price of the item.
        Returns:
            float: The price after applying the promotion.
        """
        promotion = self.get_promotion(promotion_name)
        if not promotion:
            raise PromotionError(f"Promotion '{promotion_name}' does not exist.")
        if not promotion.is_valid_for_user(user_id):
            raise PromotionError(f"Promotion '{promotion_name}' is not valid for user '{user_id}'.")
        return promotion.apply_discount(original_price)


# Example usage:
if __name__ == "__main__":
    # Create a promotions manager
    manager = PromotionsManager()

    # Create a promotion
    best_friends_promo = Promotion(
        name="Best Friends Only",
        discount_percentage=25,
        expiration_date=datetime.date(2023, 12, 31),
        is_exclusive=True,
        allowed_users={"user123", "user456"}
    )

    # Add the promotion to the manager
    manager.add_promotion(best_friends_promo)

    # Validate and apply the promotion
    user_id = "user123"
    original_price = 100.0

    try:
        if manager.validate_promotion_for_user("Best Friends Only", user_id):
            discounted_price = manager.apply_promotion("Best Friends Only", user_id, original_price)
            print(f"Discounted price for user {user_id}: ${discounted_price}")
        else:
            print(f"Promotion is not valid for user {user_id}.")
    except PromotionError as e:
        print(f"Error: {e}")
```
