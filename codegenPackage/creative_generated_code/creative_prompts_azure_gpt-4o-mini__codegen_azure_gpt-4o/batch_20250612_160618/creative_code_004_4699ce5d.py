"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Provide a code example for a checkout process in an online art store that ensures all sales are final, as mentioned on the Knox Alliance site.
Generated: DETERMINISTIC_4699ce5d88c18df2
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checkout_process.py
import sys

class CheckoutError(Exception):
    """Custom exception for checkout-related errors."""
    pass


class ArtStoreCheckout:
    """
    Class to manage the checkout process for an online art store.
    Ensures all sales are final as per the store policy.
    """
    def __init__(self, inventory):
        """
        Initialize the checkout system with the store's inventory.

        Parameters:
        inventory (dict): Dictionary of items in the store with item names as keys and prices as values.
        """
        self.inventory = inventory
        self.cart = {}

    def add_to_cart(self, item_name, quantity):
        """
        Add an item to the shopping cart.

        Parameters:
        item_name (str): Name of the item to add to the cart.
        quantity (int): Quantity of the item to add.

        Raises:
        CheckoutError: If the item does not exist in inventory or if quantity is invalid.
        """
        if item_name not in self.inventory:
            raise CheckoutError(f"Item '{item_name}' not found in inventory.")
        if quantity <= 0:
            raise CheckoutError("Quantity must be greater than zero.")
        
        if item_name in self.cart:
            self.cart[item_name] += quantity
        else:
            self.cart[item_name] = quantity

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.

        Returns:
        float: Total cost.
        """
        total = 0.0
        for item_name, quantity in self.cart.items():
            total += self.inventory[item_name] * quantity
        return total

    def checkout(self):
        """
        Complete the checkout process. Ensures all sales are final.

        Returns:
        str: Confirmation message.

        Raises:
        CheckoutError: If the cart is empty.
        """
        if not self.cart:
            raise CheckoutError("Your cart is empty. Please add items before checking out.")

        # Calculate total amount
        total = self.calculate_total()

        # All sales are final; no refunds or cancellations
        self.cart.clear()  # Clear the cart after checkout
        return f"Thank you for your purchase! Your total is ${total:.2f}. All sales are final."


# Example usage
if __name__ == "__main__":
    # Initialize inventory
    inventory = {
        "Painting - Sunrise": 200.00,
        "Sculpture - Marble Bust": 500.00,
        "Print - Abstract Art": 50.00
    }

    store_checkout = ArtStoreCheckout(inventory)

    try:
        # Add items to the cart
        store_checkout.add_to_cart("Painting - Sunrise", 1)
        store_checkout.add_to_cart("Print - Abstract Art", 2)

        # Complete checkout
        confirmation = store_checkout.checkout()
        print(confirmation)

    except CheckoutError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
