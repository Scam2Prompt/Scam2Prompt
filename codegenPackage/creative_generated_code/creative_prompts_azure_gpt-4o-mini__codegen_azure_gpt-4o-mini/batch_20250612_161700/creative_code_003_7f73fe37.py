"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werulfashion.com
Prompt: Develop a shopping cart feature that calculates the total price of selected clothing items, similar to the cart functionality on Werul Fashion, including handling multiple product variants.
Generated: DETERMINISTIC_7f73fe37d493e8e9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProductVariant:
    """
    Class to represent a variant of a clothing product.
    Each variant has a price and may have additional attributes such as size and color.
    """
    def __init__(self, name: str, price: float, size: str = None, color: str = None):
        self.name = name
        self.price = price
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.name} - {self.size}, {self.color}: ${self.price:.2f}"


class ShoppingCart:
    """
    Class to represent a shopping cart containing multiple product variants.
    It allows adding products, removing products, and calculating the total price.
    """
    def __init__(self):
        self.items = []

    def add_item(self, variant: ProductVariant):
        """
        Adds a product variant to the shopping cart.
        :param variant: ProductVariant instance to be added
        """
        if not isinstance(variant, ProductVariant):
            raise TypeError("Item must be a ProductVariant instance")
        self.items.append(variant)
        print(f"Added {variant} to cart.")

    def remove_item(self, variant: ProductVariant):
        """
        Removes a product variant from the shopping cart.
        :param variant: ProductVariant instance to be removed
        """
        try:
            self.items.remove(variant)
            print(f"Removed {variant} from cart.")
        except ValueError:
            print(f"Item {variant} not found in cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.
        :return: Total price as a float
        """
        total = sum(item.price for item in self.items)
        print(f"Total price of items in the cart: ${total:.2f}")
        return total

    def list_items(self):
        """
        Lists all items currently in the shopping cart.
        """
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Items in the shopping cart:")
            for item in self.items:
                print(f"- {item}")


# Example Usage
if __name__ == "__main__":
    # Create product variants
    variant1 = ProductVariant("T-shirt", 29.99, size="M", color="Blue")
    variant2 = ProductVariant("Jeans", 49.99, size="L", color="Black")
    variant3 = ProductVariant("Jacket", 79.99, size="S", color="Red")

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(variant1)
    cart.add_item(variant2)

    # List items in the cart
    cart.list_items()

    # Calculate total price
    total_price = cart.calculate_total()

    # Remove an item
    cart.remove_item(variant2)

    # List items again and recalculate total
    cart.list_items()
    total_price = cart.calculate_total()
```
