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
class Product:
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name: str, price: float):
        """Initialize a new product with a name and price.
        
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        
        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price


class ShoppingCart:
    """Class to manage the shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product: Product):
        """Add a product to the shopping cart.
        
        Args:
            product (Product): The product to be added.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.items.append(product)

    def calculate_total(self) -> float:
        """Calculate the total price of all products in the cart.
        
        Returns:
            float: The total price of the cart.
        """
        total = sum(product.price for product in self.items)
        return total

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()


def main():
    """Main function to demonstrate adding products to the shopping cart."""
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Create some products
        product1 = Product("pain de rasage bio", 15.99)
        product2 = Product("baume à lèvres au coco et karité", 7.50)

        # Add products to the cart
        cart.add_product(product1)
        cart.add_product(product2)

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price of items in the cart: €{total_price:.2f}")

    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
