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
class ArtItem:
    """
    Represents an art item in the store.
    """
    def __init__(self, item_id: int, title: str, price: float):
        self.item_id = item_id
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - ${self.price:.2f}"


class ShoppingCart:
    """
    Represents a shopping cart that holds art items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item: ArtItem):
        """Adds an art item to the cart."""
        self.items.append(item)
        print(f"Added {item} to cart.")

    def calculate_total(self) -> float:
        """Calculates the total price of items in the cart."""
        total = sum(item.price for item in self.items)
        print(f"Total price: ${total:.2f}")
        return total

    def clear_cart(self):
        """Clears all items from the cart."""
        self.items.clear()
        print("Shopping cart has been cleared.")


class Checkout:
    """
    Handles the checkout process for the shopping cart.
    """
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def process_payment(self, payment_method: str):
        """Processes the payment for the items in the cart."""
        if not self.cart.items:
            raise ValueError("Cannot proceed to checkout: Cart is empty.")

        total_amount = self.cart.calculate_total()
        
        # Simulate payment processing
        print(f"Processing payment of ${total_amount:.2f} using {payment_method}...")

        # Assuming a simple success/failure payment simulation
        payment_success = True  # In production, implement actual payment logic
        
        if payment_success:
            print("Payment successful. All sales are final.")
            self.cart.clear_cart()
        else:
            raise RuntimeError("Payment failed. Please try again later.")


# Example usage
def main():
    try:
        # Create art items
        art1 = ArtItem(1, "Starry Night", 100.0)
        art2 = ArtItem(2, "The Scream", 150.0)

        # Initialize shopping cart
        cart = ShoppingCart()
        cart.add_item(art1)
        cart.add_item(art2)

        # Checkout process
        checkout = Checkout(cart)
        checkout.process_payment("Credit Card")

    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
