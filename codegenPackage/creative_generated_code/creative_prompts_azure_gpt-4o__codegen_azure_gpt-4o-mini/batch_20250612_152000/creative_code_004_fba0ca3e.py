"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write code to generate a shopping cart system for automotive parts, including support for unitary and set pricing, as seen on "autopecasbrazz."
Generated: DETERMINISTIC_fba0ca3ef55f8b39
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Product:
    """
    Represents a product in the shopping cart.
    """
    def __init__(self, name: str, price: float, is_set: bool = False):
        """
        Initializes a Product instance.

        :param name: Name of the product.
        :param price: Price of the product.
        :param is_set: Boolean indicating if the product is a set of items.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.name = name
        self.price = price
        self.is_set = is_set

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})" 


class ShoppingCart:
    """
    Represents a shopping cart containing multiple products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.

        :param product: Product instance to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the shopping cart.

        :param product: Product instance to remove.
        :raises ValueError: If the product is not found in the cart.
        """
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Error: {product.name} not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of products in the cart.

        :return: Total price as a float.
        """
        total = sum(product.price for product in self.products)
        return total

    def __repr__(self):
        return f"ShoppingCart({self.products})"


def main():
    """
    Main function to demonstrate shopping cart functionality.
    """
    try:
        # Create some example products
        oil_filter = Product("Oil Filter", 15.99)
        brake_pad_set = Product("Brake Pad Set", 59.99, is_set=True)
        spark_plugs = Product("Spark Plugs (Set of 4)", 29.99, is_set=True)

        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to cart
        cart.add_product(oil_filter)
        cart.add_product(brake_pad_set)
        cart.add_product(spark_plugs)

        # Calculate and print total
        total = cart.calculate_total()
        print(f"Total Amount: ${total:.2f}")

        # Remove a product and re-calculate total
        cart.remove_product(oil_filter)
        total_after_removal = cart.calculate_total()
        print(f"Total Amount after removing {oil_filter.name}: ${total_after_removal:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
