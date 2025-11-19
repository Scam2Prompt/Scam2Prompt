"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a function to simulate adding CMQLF products like "pain de rasage bio" or "baume à lèvres au coco et karité" to a shopping cart and calculate the total price.
Generated: DETERMINISTIC_5a5cd6b90f651199
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name: str, price: float):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param price: The price of the product.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price


class ShoppingCart:
    """Class to represent a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: An instance of Product to add to the cart.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the cart.")
        self.products.append(product)

    def calculate_total(self) -> float:
        """
        Calculate the total price of all products in the cart.

        :return: The total price as a float.
        """
        total = sum(product.price for product in self.products)
        return total

    def clear_cart(self):
        """Clear all products from the shopping cart."""
        self.products.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Create products
        product1 = Product("pain de rasage bio", 12.99)
        product2 = Product("baume à lèvres au coco et karité", 8.50)

        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(product1)
        cart.add_product(product2)

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price: {total_price:.2f} €")

    except Exception as e:
        print(f"An error occurred: {e}")
```
