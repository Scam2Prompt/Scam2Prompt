"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Design a checkout process that includes a promotional discount feature, reflecting the sitewide sale mentioned on the T-Shirt Store.
Generated: DETERMINISTIC_fb6976d07cb1c832
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CheckoutSystem:
    """
    A class to represent the checkout system for a T-Shirt Store.
    """

    def __init__(self, sale_discount=0.0):
        """
        Initialize the checkout system with an optional sitewide sale discount.
        :param sale_discount: Percentage discount for the sitewide sale (0.0 - 100.0).
        """
        if not (0.0 <= sale_discount <= 100.0):
            raise ValueError("Sale discount must be between 0.0 and 100.0.")
        self.sale_discount = sale_discount
        self.cart = []

    def add_to_cart(self, item_name, price, quantity=1):
        """
        Add an item to the shopping cart.
        :param item_name: Name of the item.
        :param price: Price of the item (per unit).
        :param quantity: Quantity of the item.
        """
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity must be positive.")
        self.cart.append({"item_name": item_name, "price": price, "quantity": quantity})

    def calculate_total(self):
        """
        Calculate the total cost including discounts.
        :return: Total cost after applying the promotional discount.
        """
        total_cost = sum(item["price"] * item["quantity"] for item in self.cart)
        discount_amount = total_cost * (self.sale_discount / 100.0)
        return round(total_cost - discount_amount, 2)

    def display_cart(self):
        """
        Display the items in the cart along with their price and quantity.
        """
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("Items in your cart:")
        for item in self.cart:
            print(f"{item['quantity']}x {item['item_name']} - ${item['price']} each")
        print(f"Sitewide Sale Discount: {self.sale_discount}%")

    def checkout(self):
        """
        Simulate the checkout process.
        """
        if not self.cart:
            print("Your cart is empty. Please add items before proceeding to checkout.")
            return
        
        print("\n--- Checkout Summary ---")
        self.display_cart()
        total_cost = self.calculate_total()
        print(f"\nTotal Cost (after discount): ${total_cost}")
        print("Thank you for shopping at the T-Shirt Store!")


if __name__ == "__main__":
    try:
        # Instantiate the checkout system with a 15% sitewide discount
        checkout = CheckoutSystem(sale_discount=15.0)
        
        # Add items to the cart
        checkout.add_to_cart("Classic T-Shirt", 20.00, 2)
        checkout.add_to_cart("Graphic T-Shirt", 25.00, 1)
        checkout.add_to_cart("Oversized T-Shirt", 30.00, 3)
        
        # Display cart items
        checkout.display_cart()
        
        # Process checkout
        checkout.checkout()
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
