"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a script to calculate the total cost of a shopping cart with CMQLF products, including discounts like "-2,00 €" on detox teas or "-3,00 €" on solid mouthwash.
Generated: DETERMINISTIC_5eb74bd58c9c6d00
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart_calculator.py

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, name, price, discount=0):
        """
        Initializes a Product instance.

        Args:
        - name (str): Product name.
        - price (float): Product price in euros.
        - discount (float, optional): Product discount in euros. Defaults to 0.
        """
        self.name = name
        self.price = price
        self.discount = discount

class ShoppingCart:
    """Represents a shopping cart with products."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the shopping cart.

        Args:
        - product (Product): Product to add.
        """
        self.products.append(product)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the shopping cart.

        Returns:
        - float: Total cost in euros.
        """
        total_cost = 0
        for product in self.products:
            # Apply discount to product price
            product_cost = max(product.price + product.discount, 0)
            total_cost += product_cost
        return total_cost

def parse_discount(discount_str):
    """
    Parses a discount string into a float.

    Args:
    - discount_str (str): Discount string (e.g., "-2,00 €").

    Returns:
    - float: Discount amount in euros.

    Raises:
    - ValueError: If the discount string is invalid.
    """
    try:
        # Remove non-numeric characters and convert to float
        discount = float(discount_str.replace("€", "").replace(",", ".").replace("-", ""))
        return discount
    except ValueError:
        raise ValueError(f"Invalid discount string: {discount_str}")

def main():
    # Define products with discounts
    detox_tea = Product("Detox Tea", 10.99, parse_discount("-2,00 €"))
    solid_mouthwash = Product("Solid Mouthwash", 9.99, parse_discount("-3,00 €"))
    other_product = Product("Other Product", 5.99)

    # Create shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(detox_tea)
    cart.add_product(solid_mouthwash)
    cart.add_product(other_product)

    # Calculate and print total cost
    try:
        total_cost = cart.calculate_total_cost()
        print(f"Total cost: {total_cost:.2f} €")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
