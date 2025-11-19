"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgmaybest.top
Prompt: Develop a script that calculates the total cost of items in a cart for a track cycling shop, including discounts for clearance items.
Generated: DETERMINISTIC_4319830046d73f91
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CartItem:
    """Class representing an item in the cart."""
    
    def __init__(self, name: str, price: float, quantity: int, is_clearance: bool = False):
        """
        Initialize a CartItem instance.

        :param name: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item being purchased.
        :param is_clearance: Boolean indicating if the item is on clearance.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_clearance = is_clearance

    def get_total_price(self) -> float:
        """
        Calculate the total price for this item.

        :return: Total price for this item (price * quantity).
        """
        return self.price * self.quantity

    def get_discounted_price(self) -> float:
        """
        Calculate the discounted price if the item is on clearance.

        :return: Discounted price if on clearance; otherwise the original price.
        """
        if self.is_clearance:
            # Apply a 20% discount for clearance items
            return self.price * 0.8
        return self.price


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item: CartItem):
        """
        Add an item to the shopping cart.

        :param item: CartItem to be added to the cart.
        """
        if not isinstance(item, CartItem):
            raise ValueError("Item must be an instance of CartItem.")
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculate the total cost of items in the cart.

        :return: Total cost of the shopping cart.
        """
        total = 0.0
        for item in self.items:
            total += item.get_discounted_price() * item.quantity
        return total


def main():
    """Main function to run the shopping cart calculation."""
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(CartItem("Track Bike", 1200.00, 1))
        cart.add_item(CartItem("Helmet", 99.99, 2))
        cart.add_item(CartItem("Cycling Shoes", 150.00, 1, is_clearance=True))  # Clearance item

        # Calculate the total cost of items in the cart
        total_cost = cart.calculate_total()

        # Output the total cost
        print(f"Total cost of items in the cart: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
