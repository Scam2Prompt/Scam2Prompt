"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a script to calculate the total cost of a shopping cart with CMQLF products, including discounts like "-2,00 €" on detox teas or "-3,00 €" on solid mouthwash.
Generated: DETERMINISTIC_5eb74bd58c9c6d00
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initializes a new product with a name, price, and optional discount.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            discount (float): The discount applied to the product (default is 0.0).
        """
        if price < 0 or discount < 0:
            raise ValueError("Price and discount must be non-negative values.")
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """Calculates the final price after applying the discount."""
        return self.price - self.discount


class ShoppingCart:
    """Class representing a shopping cart to manage products and calculate total cost."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = []

    def add_product(self, product: Product):
        """Adds a product to the shopping cart.

        Args:
            product (Product): The product to add to the cart.
        """
        self.products.append(product)

    def total_cost(self) -> float:
        """Calculates the total cost of products in the cart, including discounts.

        Returns:
            float: The total cost of the shopping cart.
        """
        total = sum(product.final_price() for product in self.products)
        return round(total, 2)  # Round to 2 decimal places for currency


if __name__ == "__main__":
    # Create a shopping cart
    cart = ShoppingCart()

    # Create some products with their respective prices and discounts
    detox_tea = Product(name="Detox Tea", price=10.00, discount=2.00)
    mouthwash = Product(name="Solid Mouthwash", price=15.00, discount=3.00)
    
    # Add products to the cart
    cart.add_product(detox_tea)
    cart.add_product(mouthwash)

    # Calculate and print the total cost
    try:
        total = cart.total_cost()
        print(f"Total cost of the shopping cart: {total} €")
    except Exception as e:
        print(f"An error occurred while calculating the total cost: {e}")
```
