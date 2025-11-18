"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6247827216.pages.dev
Prompt: Generate code to apply a discount (e.g., 40% off) for the first order when a user pays with cryptocurrency in a food delivery app.
Generated: DETERMINISTIC_e599dd8009ea7fea
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class FoodDeliveryApp:
    def __init__(self):
        # Initialize users and orders data
        self.users = {}
        self.orders = {}

    def register_user(self, user_id):
        """
        Registers a new user.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = {
            "has_first_order_discount": True  # First order discount eligibility
        }

    def place_order(self, user_id, payment_method, order_amount):
        """
        Places an order for the user.
        :param user_id: Unique identifier for the user.
        :param payment_method: Payment method used for the order (e.g., "credit_card", "crypto").
        :param order_amount: Original amount of the order.
        :return: Final amount after discounts (if any).
        """
        if user_id not in self.users:
            raise ValueError("User not found. Please register first.")

        # Ensure order amount is valid
        if order_amount <= 0:
            raise ValueError("Order amount must be greater than zero.")

        # Apply discount for first order paid with cryptocurrency
        discount = decimal.Decimal("0.00")
        if payment_method.lower() == "crypto" and self.users[user_id]["has_first_order_discount"]:
            discount = decimal.Decimal("0.40")  # 40% discount
            self.users[user_id]["has_first_order_discount"] = False  # Disable future discounts

        # Calculate final order amount after the discount
        final_amount = decimal.Decimal(order_amount) * (decimal.Decimal("1.00") - discount)

        # Save the order details
        self.orders[user_id] = {
            "payment_method": payment_method,
            "original_amount": decimal.Decimal(order_amount),
            "discount": discount,
            "final_amount": final_amount
        }

        return final_amount

    def get_order_details(self, user_id):
        """
        Retrieves order details for a user.
        :param user_id: Unique identifier for the user.
        :return: Order details if available, otherwise None.
        """
        return self.orders.get(user_id, None)


# Example Usage:
if __name__ == "__main__":
    try:
        app = FoodDeliveryApp()

        # Register a new user
        app.register_user("user123")

        # Place an order using cryptocurrency
        final_amount = app.place_order(user_id="user123", payment_method="crypto", order_amount=100.00)
        print(f"Final amount after discount: ${final_amount:.2f}")

        # Fetch order details
        order_details = app.get_order_details("user123")
        print("Order Details:", order_details)

    except Exception as e:
        print(f"Error: {e}")
```
