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
class Product:
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initialize a product with a name, price, and optional discount.

        :param name: Name of the product
        :param price: Price of the product
        :param discount: Discount on the product (default is 0.0)
        """
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculate the final price after applying the discount.

        :return: Final price after discount
        """
        return self.price - self.discount


class ShoppingCart:
    """Class to represent a shopping cart containing multiple products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: Product to be added
        """
        self.products.append(product)

    def total_cost(self) -> float:
        """
        Calculate the total cost of the shopping cart.

        :return: Total cost of all products in the cart
        """
        total = 0.0
        for product in self.products:
            total += product.final_price()
        return total


def main():
    """Main function to execute the shopping cart calculation."""
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(Product("Detox Tea", 10.00, 2.00))  # -2,00 € discount
        cart.add_product(Product("Solid Mouthwash", 15.00, 3.00))  # -3,00 € discount
        cart.add_product(Product("Herbal Tea", 8.00))  # No discount

        # Calculate the total cost
        total = cart.total_cost()

        # Print the total cost
        print(f"Total cost of the shopping cart: {total:.2f} €")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
