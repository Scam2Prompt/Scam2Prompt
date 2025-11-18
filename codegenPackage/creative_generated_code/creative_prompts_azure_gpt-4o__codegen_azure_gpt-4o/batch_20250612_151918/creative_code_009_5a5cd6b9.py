"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a function to simulate adding CMQLF products like "pain de rasage bio" or "baume à lèvres au coco et karité" to a shopping cart and calculate the total price.
Generated: DETERMINISTIC_5a5cd6b90f651199
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Shopping Cart Simulation

# Define a product class to represent each product
class Product:
    def __init__(self, name, price):
        """
        Initialize a Product instance.

        :param name: Name of the product (string)
        :param price: Price of the product (float)
        """
        self.name = name
        self.price = price


# Define a shopping cart class to manage products
class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        :param product: Product instance to be added
        """
        if not isinstance(product, Product):
            raise TypeError("Invalid product type. Must be an instance of Product.")
        self.products.append(product)

    def calculate_total(self):
        """
        Calculate the total price of all products in the cart.

        :return: Total price (float)
        """
        return sum(product.price for product in self.products)

    def show_cart(self):
        """
        Display the contents of the shopping cart.

        :return: None
        """
        if not self.products:
            print("Your shopping cart is empty.")
        else:
            print("Products in your cart:")
            for product in self.products:
                print(f"- {product.name}: €{product.price:.2f}")
            print(f"Total: €{self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create products
        product1 = Product("Pain de rasage bio", 12.99)
        product2 = Product("Baume à lèvres au coco et karité", 8.50)

        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(product1)
        cart.add_product(product2)

        # Show cart contents and total price
        cart.show_cart()

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
