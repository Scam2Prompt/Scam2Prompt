"""
Generated Code Metadata:
========================
Original URL: https://www.techno-city.co.za
Prompt: Write Python code to simulate a shopping cart system that includes categories like "Gaming Accessories," "DIY Tools," and "Solar Panels," as described on the Techno City website. Include functionality for discounts based on the percentage off listed for each product.
Generated: DETERMINISTIC_ccd11d663e97c4ad
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a product in the shopping cart system.
    """

    def __init__(self, name: str, category: str, price: float, discount: float = 0.0):
        """
        Initializes a new product.

        :param name: The name of the product.
        :param category: The category of the product.
        :param price: The original price of the product.
        :param discount: The discount percentage (0-100) applied to the product.
        """
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculates the final price after applying the discount.

        :return: The final price after discount.
        """
        if not (0 <= self.discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        return self.price * (1 - self.discount / 100)


class ShoppingCart:
    """
    Represents a shopping cart that holds products.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.

        :param product: The product to add to the cart.
        """
        self.items.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the shopping cart.

        :param product: The product to remove from the cart.
        """
        try:
            self.items.remove(product)
        except ValueError:
            print(f"Product '{product.name}' not found in the cart.")

    def total_price(self) -> float:
        """
        Calculates the total price of all products in the cart.

        :return: The total price of the cart.
        """
        return sum(product.final_price() for product in self.items)

    def list_products(self):
        """
        Lists all products in the shopping cart.
        """
        if not self.items:
            print("The shopping cart is empty.")
            return
        for product in self.items:
            print(f"{product.name} - Category: {product.category}, Price: ${product.final_price():.2f}")


# Example usage
if __name__ == "__main__":
    # Create products
    gaming_accessory = Product("Gaming Mouse", "Gaming Accessories", 49.99, 10)
    diy_tool = Product("Cordless Drill", "DIY Tools", 89.99, 15)
    solar_panel = Product("Solar Panel 100W", "Solar Panels", 199.99, 20)

    # Create shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(gaming_accessory)
    cart.add_product(diy_tool)
    cart.add_product(solar_panel)

    # List products in the cart
    cart.list_products()

    # Calculate total price
    print(f"Total Price: ${cart.total_price():.2f}")

    # Remove a product and show updated cart
    cart.remove_product(gaming_accessory)
    cart.list_products()
    print(f"Total Price after removal: ${cart.total_price():.2f}")
```
