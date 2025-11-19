"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplife.life
Prompt: Generate a code snippet for a shopping cart that includes a feature for free shipping on orders over $40, similar to the policy on simplife.life.
Generated: DETERMINISTIC_c820509c24d25cbe
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class ShoppingCart:
    """
    A shopping cart class that supports adding items, calculating total cost,
    and applying free shipping for orders over $40.
    """
    FREE_SHIPPING_THRESHOLD = 40.0  # Free shipping threshold in dollars

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []  # List to store items in the cart

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.
        
        :param name: Name of the item (string)
        :param price: Price of the item (float)
        :param quantity: Quantity of the item (int, default is 1)
        """
        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity must be positive.")
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.
        
        :return: Total cost (float)
        """
        return sum(item['price'] * item['quantity'] for item in self.items)

    def apply_free_shipping(self):
        """
        Check if the order qualifies for free shipping based on the total cost.
        
        :return: True if eligible for free shipping, False otherwise.
        """
        total = self.calculate_total()
        return total >= self.FREE_SHIPPING_THRESHOLD

    def checkout_summary(self):
        """
        Generate a summary of the cart including items, total, and shipping status.
        
        :return: Dictionary containing the cart summary.
        """
        total = self.calculate_total()
        free_shipping = self.apply_free_shipping()

        return {
            'items': self.items,
            'total': total,
            'free_shipping': free_shipping
        }


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()

        # Adding items to the cart
        cart.add_item(name="Reusable Water Bottle", price=15.0, quantity=2)
        cart.add_item(name="Eco-friendly Notebook", price=12.5, quantity=1)

        # Print checkout summary
        summary = cart.checkout_summary()
        print("Cart Summary:")
        print(f"Items: {summary['items']}")
        print(f"Total: ${summary['total']:.2f}")
        print(f"Free Shipping Eligible: {'Yes' if summary['free_shipping'] else 'No'}")
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
