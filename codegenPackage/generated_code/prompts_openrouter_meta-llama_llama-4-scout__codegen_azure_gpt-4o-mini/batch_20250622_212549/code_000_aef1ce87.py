"""
Generated Code Metadata:
========================
Original URL: https://www.lattechocolate.com.ar
Prompt: Write a Python code snippet to implement a simple e-commerce shopping cart system with product categories and shipping calculations, similar to lattechocolate.com.ar.
Generated: DETERMINISTIC_aef1ce875ad36a8b
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class representing a product in the e-commerce system."""
    
    def __init__(self, name, price, category):
        """
        Initialize a new product.

        :param name: str - The name of the product.
        :param price: float - The price of the product.
        :param category: str - The category of the product.
        """
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        :param product: Product - The product to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product):
        """
        Remove a product from the shopping cart.

        :param product: Product - The product to remove.
        """
        try:
            self.items.remove(product)
        except ValueError:
            print(f"Product {product.name} not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        return sum(product.price for product in self.items)

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

    def __repr__(self):
        return f"ShoppingCart({self.items})"


class ShippingCalculator:
    """Class to calculate shipping costs based on weight and distance."""
    
    def __init__(self, base_rate=5.0):
        """
        Initialize the shipping calculator.

        :param base_rate: float - The base shipping rate.
        """
        self.base_rate = base_rate

    def calculate_shipping(self, weight, distance):
        """
        Calculate shipping cost based on weight and distance.

        :param weight: float - The weight of the package.
        :param distance: float - The distance to ship.
        :return: float - The calculated shipping cost.
        """
        if weight <= 0 or distance <= 0:
            raise ValueError("Weight and distance must be positive values.")
        return self.base_rate + (0.5 * weight) + (0.1 * distance)


# Example usage
if __name__ == "__main__":
    # Create some products
    chocolate = Product("Chocolate Bar", 2.50, "Snacks")
    coffee = Product("Coffee Beans", 10.00, "Beverages")
    
    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(chocolate)
    cart.add_product(coffee)
    
    # Calculate total price
    total_price = cart.calculate_total()
    print(f"Total price: ${total_price:.2f}")
    
    # Calculate shipping cost
    shipping_calculator = ShippingCalculator()
    shipping_cost = shipping_calculator.calculate_shipping(weight=2.0, distance=10.0)
    print(f"Shipping cost: ${shipping_cost:.2f}")
    
    # Clear the cart
    cart.clear_cart()
    print(f"Cart after clearing: {cart}")
```
