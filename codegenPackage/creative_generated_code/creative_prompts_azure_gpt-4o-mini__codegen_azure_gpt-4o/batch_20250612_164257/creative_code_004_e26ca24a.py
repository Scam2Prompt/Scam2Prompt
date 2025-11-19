"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a code example that demonstrates how to implement a discount system for first-time shoppers in a jewelry e-commerce application, referencing the "5% off" offer from Malkeenz.
Generated: DETERMINISTIC_e26ca24af8433391
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Discount System for First-Time Shoppers
This script implements a 5% discount system for first-time shoppers in a jewelry e-commerce application.
If the user is a first-time shopper, they receive a 5% discount on their purchase.
"""

class DiscountSystem:
    """
    A class to handle discount logic for first-time shoppers.
    """
    def __init__(self):
        # A dictionary simulating a user database with a "first_time_shopper" flag
        self.user_database = {
            "user1@example.com": {"first_time_shopper": True},
            "user2@example.com": {"first_time_shopper": False},
            "user3@example.com": {"first_time_shopper": True}
        }

    def calculate_discount(self, email, total_amount):
        """
        Calculate the final amount after applying the discount (if applicable).

        :param email: Email of the shopper.
        :param total_amount: Total purchase amount before any discounts.
        :return: Tuple (final_amount, discount_applied).
        """
        try:
            # Check if the user exists in the database
            if email not in self.user_database:
                raise ValueError("User not found in the system.")
            
            # Verify if the user is a first-time shopper
            is_first_time_shopper = self.user_database[email]["first_time_shopper"]

            if is_first_time_shopper:
                # Apply 5% discount
                discount = total_amount * 0.05
                final_amount = total_amount - discount
                return round(final_amount, 2), round(discount, 2)
            else:
                # No discount applied
                return round(total_amount, 2), 0.0
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

# Simulate usage of the DiscountSystem
if __name__ == "__main__":
    # Instantiate the discount system
    discount_system = DiscountSystem()

    # Example transaction data
    shopper_email = "user1@example.com"  # First-time shopper
    purchase_amount = 500.00  # Total purchase amount

    # Apply the discount
    final_price, discount_applied = discount_system.calculate_discount(shopper_email, purchase_amount)

    if final_price is not None:
        print(f"Original Price: ${purchase_amount}")
        print(f"Discount Applied: ${discount_applied}")
        print(f"Final Price after Discount: ${final_price}")
    else:
        print("Failed to calculate the discount.")
```
