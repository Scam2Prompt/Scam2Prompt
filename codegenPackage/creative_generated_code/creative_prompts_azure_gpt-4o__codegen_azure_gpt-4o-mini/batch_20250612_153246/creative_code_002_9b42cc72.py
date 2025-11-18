"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idgfiber.com
Prompt: Create a function that simulates a shopping cart calculation for IDG Fiber products, ensuring it supports multiple variants and dynamically updates the total cost based on selected options.
Generated: DETERMINISTIC_9b42cc72eb70ad0c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FiberProduct:
    """
    Class representing a fiber product with its variants.
    """

    def __init__(self, name, base_price):
        """
        Initialize a new FiberProduct.

        :param name: str - The name of the fiber product.
        :param base_price: float - The base price of the product.
        """
        self.name = name
        self.base_price = base_price
        self.variants = {}

    def add_variant(self, variant_name, price):
        """
        Add a variant to the fiber product.

        :param variant_name: str - The name of the variant.
        :param price: float - The price of the variant.
        """
        self.variants[variant_name] = price

    def get_variant_price(self, variant_name):
        """
        Get the price of a specific variant.

        :param variant_name: str - The name of the variant.
        :return: float - The price of the variant, or raises KeyError if not found.
        """
        if variant_name in self.variants:
            return self.variants[variant_name]
        else:
            raise KeyError(f"Variant '{variant_name}' not found.")


class ShoppingCart:
    """
    Class representing a shopping cart for fiber products.
    """

    def __init__(self):
        """
        Initialize a new ShoppingCart.
        """
        self.items = []

    def add_product(self, product, variant_name):
        """
        Add a fiber product and its variant to the cart.

        :param product: FiberProduct - The fiber product to add.
        :param variant_name: str - The name of the variant to add.
        :raises KeyError: If the variant does not exist.
        """
        try:
            variant_price = product.get_variant_price(variant_name)
            self.items.append((product, variant_name, variant_price))
        except KeyError as e:
            print(e)

    def calculate_total(self):
        """
        Calculate the total cost of all items in the cart.

        :return: float - The total cost of the shopping cart.
        """
        total = sum(price for _, _, price in self.items)
        return total

    def clear_cart(self):
        """
        Clear all items from the cart.
        """
        self.items.clear()


# Example usage
if __name__ == "__main__":
    # Create fiber products
    fiber1 = FiberProduct("Basic Fiber", 50.00)
    fiber1.add_variant("100Mbps", 10.00)
    fiber1.add_variant("1Gbps", 20.00)

    fiber2 = FiberProduct("Premium Fiber", 75.00)
    fiber2.add_variant("200Mbps", 15.00)
    fiber2.add_variant("2Gbps", 30.00)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(fiber1, "100Mbps")
    cart.add_product(fiber1, "1Gbps")
    cart.add_product(fiber2, "200Mbps")

    # Display total cost
    print(f"Total cost: ${cart.calculate_total():.2f}")

    # Clear the cart
    cart.clear_cart()
```
