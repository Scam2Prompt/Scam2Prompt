"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Develop a script that simulates a shopping cart for homeopathic products, allowing users to add items like Pekana Granules and Syrups.
Generated: DETERMINISTIC_f35a68968551cc5f
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class to represent a product in the shopping cart."""

    def __init__(self, name: str, price: float):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param price: The price of the product.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: The product to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product_name: str):
        """
        Remove a product from the shopping cart by name.

        :param product_name: The name of the product to remove.
        :raises ValueError: If the product is not found in the cart.
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculate the total price of items in the cart.

        :return: The total price.
        """
        return sum(item.price for item in self.items)

    def view_cart(self) -> str:
        """
        Return a string representation of the current cart contents.

        :return: A string listing the items in the cart.
        """
        if not self.items:
            return "Your cart is empty."
        return "\n".join(str(item) for item in self.items)


def main():
    """Main function to simulate the shopping cart."""
    cart = ShoppingCart()
    
    # Sample products
    pekana_granules = Product("Pekana Granules", 12.99)
    pekana_syrup = Product("Pekana Syrup", 15.49)

    # Adding products to cart
    cart.add_product(pekana_granules)
    cart.add_product(pekana_syrup)

    # Viewing the cart
    print("Current items in the cart:")
    print(cart.view_cart())

    # Calculating total price
    total_price = cart.calculate_total()
    print(f"Total price: ${total_price:.2f}")

    # Removing a product
    try:
        cart.remove_product("Pekana Granules")
        print("\nAfter removing Pekana Granules:")
        print(cart.view_cart())
    except ValueError as e:
        print(e)

    # Final total
    final_total = cart.calculate_total()
    print(f"Final total price: ${final_total:.2f}")


if __name__ == "__main__":
    main()
```
