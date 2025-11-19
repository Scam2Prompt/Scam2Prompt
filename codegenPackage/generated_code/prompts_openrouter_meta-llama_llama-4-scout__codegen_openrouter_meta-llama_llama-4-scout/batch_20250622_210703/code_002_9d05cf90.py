"""
Generated Code Metadata:
========================
Original URL: https://chedanthe.dk
Prompt: "Write a Python script to calculate the total cost of a furniture shopping cart, considering discounts and taxes, for an online store like Chedanthe."
Generated: DETERMINISTIC_9d05cf906a16f18b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_shopping_cart.py

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, name, price, discount=0):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            price (float): Product price.
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_price(self):
        """Calculates the price after discount."""
        return self.price * (1 - self.discount / 100)


class ShoppingCart:
    """Represents a shopping cart."""
    
    def __init__(self, tax_rate):
        """
        Initializes a ShoppingCart.

        Args:
            tax_rate (float): Tax rate percentage.
        """
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        """Adds a product to the cart."""
        self.products.append(product)

    def calculate_subtotal(self):
        """Calculates the subtotal of the cart."""
        return sum(product.calculate_price() for product in self.products)

    def calculate_tax(self):
        """Calculates the tax amount."""
        return self.calculate_subtotal() * (self.tax_rate / 100)

    def calculate_total(self):
        """Calculates the total cost of the cart."""
        return self.calculate_subtotal() + self.calculate_tax()


def main():
    try:
        # Create products
        product1 = Product("Chair", 100, discount=10)
        product2 = Product("Table", 200)

        # Create shopping cart with 8% tax rate
        cart = ShoppingCart(tax_rate=8)
        cart.add_product(product1)
        cart.add_product(product2)

        # Calculate and print total cost
        print("Shopping Cart:")
        for i, product in enumerate(cart.products, start=1):
            print(f"{i}. {product.name} - ${product.calculate_price():.2f}")
        print(f"Subtotal: ${cart.calculate_subtotal():.2f}")
        print(f"Tax ({cart.tax_rate}%): ${cart.calculate_tax():.2f}")
        print(f"Total: ${cart.calculate_total():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
