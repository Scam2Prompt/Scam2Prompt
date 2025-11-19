"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.practisea.com
Prompt: Illustrate how to implement a shopping cart feature that calculates shipping costs for international orders on Practisea's platform, considering the $39.99 free shipping threshold.
Generated: DETERMINISTIC_260fc4f3a191e498
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

import json

class ShoppingCart:
    """
    A class representing a shopping cart.
    """
    def __init__(self, user_country: str):
        """
        Initialize the shopping cart with user country and an empty item list.
        :param user_country: str - Country code of the user (e.g., 'US', 'CA', 'FR', etc.)
        """
        self.user_country = user_country
        self.items = []  # List to store items in the cart

    def add_item(self, name: str, price: float):
        """
        Add an item to the shopping cart.
        :param name: str - Name of the item
        :param price: float - Price of the item
        """
        if price < 0:
            raise ValueError("Price must be non-negative.")
        self.items.append({"name": name, "price": price})

    def calculate_total(self) -> float:
        """
        Calculate the total cost of items in the shopping cart.
        :return: float - Total price of items
        """
        return sum(item["price"] for item in self.items)

    def calculate_shipping_cost(self) -> float:
        """
        Calculate shipping cost based on the total price and user's country.
        Free shipping is applied for orders over $39.99.
        :return: float - Shipping cost
        """
        free_shipping_threshold = 39.99
        international_shipping_rate = 10.00

        total = self.calculate_total()

        # Shipping is free if total exceeds the free shipping threshold
        if total >= free_shipping_threshold:
            return 0.0

        # Apply international shipping rate for orders below the threshold
        if self.user_country != "US":  # Example: Assume 'US' is the local country
            return international_shipping_rate
        return 5.00  # Default local shipping rate for orders below threshold

    def checkout(self):
        """
        Display the final summary of the shopping cart including total and shipping cost.
        """
        try:
            total = self.calculate_total()
            shipping = self.calculate_shipping_cost()
            grand_total = total + shipping

            # Display the summary in JSON format
            summary = {
                "items": self.items,
                "total": round(total, 2),
                "shipping_cost": round(shipping, 2),
                "grand_total": round(grand_total, 2)
            }
            print(json.dumps(summary, indent=4))
        except Exception as e:
            print(f"An error occurred during checkout: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart instance for a user in France
        cart = ShoppingCart(user_country="FR")

        # Add items to the cart
        cart.add_item("T-shirt", 15.99)
        cart.add_item("Jeans", 25.00)

        # Perform checkout
        cart.checkout()
    except Exception as err:
        print(f"Error: {err}")
```
