"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Generate a code snippet that implements a discount feature for a "Best Friends Only" promotion on an e-commerce site.
Generated: DETERMINISTIC_2084d5154017e245
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DiscountManager:
    """
    A class to manage discounts for the "Best Friends Only" promotion.
    """

    def __init__(self, discount_percentage, promotion_end_date):
        """
        Initialize the DiscountManager.

        :param discount_percentage: Percentage of discount (e.g., 20 for 20%).
        :param promotion_end_date: End date of the promotion in 'YYYY-MM-DD' format.
        """
        self.discount_percentage = discount_percentage
        try:
            self.promotion_end_date = datetime.datetime.strptime(promotion_end_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

    def is_promotion_active(self):
        """
        Check if the promotion is still active.

        :return: True if the promotion is active, False otherwise.
        """
        today = datetime.date.today()
        return today <= self.promotion_end_date

    def apply_discount(self, original_price, is_best_friend):
        """
        Apply the discount to the original price if the user qualifies.

        :param original_price: The original price of the item (float).
        :param is_best_friend: Boolean indicating if the user is a "Best Friend".
        :return: The price after the discount is applied (float).
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        
        if not isinstance(is_best_friend, bool):
            raise ValueError("is_best_friend must be a boolean value.")
        
        if not self.is_promotion_active():
            return original_price  # No discount if the promotion is inactive.
        
        if is_best_friend:
            discount_amount = original_price * (self.discount_percentage / 100)
            return round(original_price - discount_amount, 2)  # Return price after discount.
        else:
            return original_price  # No discount for non-best-friend users.


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the "Best Friends Only" promotion with 20% discount, ending on 2023-12-31.
        promotion = DiscountManager(discount_percentage=20, promotion_end_date="2023-12-31")
        
        # Check if the promotion is active.
        print("Is the promotion active?", promotion.is_promotion_active())
        
        # Apply the discount for a "Best Friend" user.
        discounted_price = promotion.apply_discount(original_price=100.0, is_best_friend=True)
        print("Discounted price for Best Friends:", discounted_price)
        
        # Apply the discount for a regular user.
        regular_price = promotion.apply_discount(original_price=100.0, is_best_friend=False)
        print("Price for regular users:", regular_price)
    except Exception as e:
        print("Error:", e)
```
