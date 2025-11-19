"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Generate a code snippet for an e-commerce website that applies a discount coupon for free shipping, similar to the "GRATISONGKIR" offer on Queenzie.
Generated: DETERMINISTIC_2b3e2097e2378948
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        # Initialize an empty shopping cart
        self.items = []
        self.shipping_cost = 5.00  # Default shipping cost
        self.discount_coupon = None

    def add_item(self, item_name, item_price):
        """
        Add an item to the shopping cart.

        :param item_name: Name of the item being added
        :param item_price: Price of the item being added
        """
        self.items.append({'name': item_name, 'price': item_price})

    def apply_discount_coupon(self, coupon_code):
        """
        Apply a discount coupon for free shipping.

        :param coupon_code: The coupon code to apply
        :raises ValueError: If the coupon code is invalid
        """
        if coupon_code == "GRATISONGKIR":
            self.discount_coupon = coupon_code
            self.shipping_cost = 0.00  # Set shipping cost to free
            print("Discount coupon applied successfully: Free shipping!")
        else:
            raise ValueError("Invalid coupon code. Please try again.")

    def calculate_total(self):
        """
        Calculate the total cost of the shopping cart including shipping.

        :return: Total cost of items plus shipping
        """
        total_item_cost = sum(item['price'] for item in self.items)
        total_cost = total_item_cost + self.shipping_cost
        return total_cost

    def display_cart(self):
        """
        Display the current items in the shopping cart and total cost.

        :return: None
        """
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']:.2f}")
        print(f"Shipping Cost: ${self.shipping_cost:.2f}")
        print(f"Total Cost: ${self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("T-Shirt", 20.00)
    cart.add_item("Jeans", 40.00)

    try:
        cart.apply_discount_coupon("GRATISONGKIR")  # Apply free shipping coupon
    except ValueError as e:
        print(e)

    cart.display_cart()  # Display the cart contents and total
```
