"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cakco.com
Prompt: Generate a code snippet for a shopping cart system that includes features for selecting multiple variants of trendy bags, as described on the Cakco website.
Generated: DETERMINISTIC_7750aaeebc794778
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

# Define a custom exception for the ShoppingCart
class ShoppingCartError(Exception):
    pass

# Bag class to represent individual bag variants
class Bag:
    def __init__(self, name, variant, price):
        """
        Initialize a Bag object.

        :param name: Name of the bag
        :param variant: Variant (e.g., color, size) of the bag
        :param price: Price of the bag
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the bag
        self.name = name
        self.variant = variant
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.variant}) - ${self.price:.2f}"

# ShoppingCart class to manage the cart system
class ShoppingCart:
    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.items = []

    def add_item(self, bag, quantity=1):
        """
        Add a bag to the cart.

        :param bag: Bag object to add
        :param quantity: Quantity of the bag to add (default is 1)
        :raises ShoppingCartError: If the quantity is invalid
        """
        if quantity <= 0:
            raise ShoppingCartError("Quantity must be greater than 0.")
        
        self.items.append({"bag": bag, "quantity": quantity})

    def remove_item(self, bag_id):
        """
        Remove a bag from the cart by its unique ID.

        :param bag_id: Unique ID of the bag to remove
        :raises ShoppingCartError: If the bag is not found in the cart
        """
        for item in self.items:
            if item["bag"].id == bag_id:
                self.items.remove(item)
                return
        raise ShoppingCartError("Bag not found in the cart.")

    def view_cart(self):
        """
        View the contents of the cart.

        :return: List of items in the cart
        """
        if not self.items:
            return "Your cart is empty."
        return "\n".join(
            [f"{item['bag']} - Quantity: {item['quantity']}" for item in self.items]
        )

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.

        :return: Total cost of items in the cart
        """
        return sum(item["bag"].price * item["quantity"] for item in self.items)

# Example usage
if __name__ == "__main__":
    try:
        # Create some trendy bag variants
        bag1 = Bag("Trendy Bag", "Red", 49.99)
        bag2 = Bag("Trendy Bag", "Blue", 54.99)
        bag3 = Bag("Trendy Bag", "Green", 59.99)

        # Initialize the shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(bag1, quantity=2)
        cart.add_item(bag2, quantity=1)

        # View the cart
        print("Cart Contents:")
        print(cart.view_cart())

        # Calculate the total
        print("\nTotal Cost: $", cart.calculate_total())

        # Remove an item from the cart
        cart.remove_item(bag1.id)
        print("\nCart after removing an item:")
        print(cart.view_cart())

    except ShoppingCartError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
