"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Illustrate how to implement a discount feature in a shopping cart application, taking cues from the 5% discount offer mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_5f33b8453faf8005
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, name, price):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """Represents a shopping cart with products and discount functionality."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = []
        self.discount_rate = 0.05  # 5% discount

    def add_product(self, product):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def calculate_subtotal(self):
        """
        Calculates the subtotal of the shopping cart.

        Returns:
            float: The subtotal.
        """
        return sum(product.price for product in self.products)

    def calculate_discount(self, subtotal):
        """
        Calculates the discount amount.

        Args:
            subtotal (float): The subtotal.

        Returns:
            float: The discount amount.
        """
        return subtotal * self.discount_rate

    def calculate_total(self):
        """
        Calculates the total cost of the shopping cart with discount.

        Returns:
            float: The total cost.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        return subtotal - discount

    def checkout(self):
        """
        Performs the checkout process.

        Returns:
            dict: A dictionary containing the subtotal, discount, and total.
        """
        try:
            subtotal = self.calculate_subtotal()
            discount = self.calculate_discount(subtotal)
            total = self.calculate_total()

            return {
                "subtotal": f"R${subtotal:.2f}",
                "discount": f"-R${discount:.2f}",
                "total": f"R${total:.2f}",
            }
        except Exception as e:
            # Handle any unexpected errors during checkout
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Example usage
    cart = ShoppingCart()

    product1 = Product("Product A", 100.0)
    product2 = Product("Product B", 200.0)

    cart.add_product(product1)
    cart.add_product(product2)

    result = cart.checkout()

    if result:
        print("Checkout Result:")
        for key, value in result.items():
            print(f"{key.capitalize()}: {value}")


if __name__ == "__main__":
    main()
```
