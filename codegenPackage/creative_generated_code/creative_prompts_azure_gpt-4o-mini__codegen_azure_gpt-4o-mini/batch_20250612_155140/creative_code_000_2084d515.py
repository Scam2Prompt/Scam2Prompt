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
class EcommerceSite:
    def __init__(self):
        # Initialize an empty list to store users who are eligible for the discount
        self.best_friends = []

    def add_best_friend(self, user_email):
        """
        Adds a user to the best friends list for the discount promotion.
        
        :param user_email: str - Email of the user to be added
        """
        if user_email not in self.best_friends:
            self.best_friends.append(user_email)
            print(f"{user_email} has been added to the best friends list.")
        else:
            print(f"{user_email} is already in the best friends list.")

    def remove_best_friend(self, user_email):
        """
        Removes a user from the best friends list.
        
        :param user_email: str - Email of the user to be removed
        """
        try:
            self.best_friends.remove(user_email)
            print(f"{user_email} has been removed from the best friends list.")
        except ValueError:
            print(f"{user_email} is not in the best friends list.")

    def apply_discount(self, user_email, original_price):
        """
        Applies a discount if the user is in the best friends list.
        
        :param user_email: str - Email of the user
        :param original_price: float - Original price of the item
        :return: float - Price after discount or original price if not eligible
        """
        DISCOUNT_RATE = 0.20  # 20% discount rate for best friends
        try:
            if user_email in self.best_friends:
                discount_amount = original_price * DISCOUNT_RATE
                discounted_price = original_price - discount_amount
                print(f"Discount applied: {discount_amount:.2f}. New price: {discounted_price:.2f}.")
                return discounted_price
            else:
                print("No discount applied. User is not a best friend.")
                return original_price
        except TypeError:
            print("Invalid input: original_price must be a number.")
            return None

# Example usage:
if __name__ == "__main__":
    site = EcommerceSite()
    site.add_best_friend("friend@example.com")
    
    # Attempt to apply discount
    final_price = site.apply_discount("friend@example.com", 100.00)
    print(f"Final price is: {final_price:.2f}")
    
    # Attempt to apply discount for a non-friend
    final_price_non_friend = site.apply_discount("nonfriend@example.com", 100.00)
    print(f"Final price is: {final_price_non_friend:.2f}")
    
    # Remove a best friend and attempt to apply discount again
    site.remove_best_friend("friend@example.com")
    final_price_after_removal = site.apply_discount("friend@example.com", 100.00)
    print(f"Final price after removal is: {final_price_after_removal:.2f}")
```
