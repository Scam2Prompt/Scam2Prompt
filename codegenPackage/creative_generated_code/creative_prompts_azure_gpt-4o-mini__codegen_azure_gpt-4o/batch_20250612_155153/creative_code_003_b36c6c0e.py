"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Develop a script that calculates the total price of selected items from a shopping cart, including furniture like sarokkanapék and előszobafalak.
Generated: DETERMINISTIC_b36c6c0e91f84efb
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
shopping_cart.py

Script to calculate the total price of selected items from a shopping cart.
Handles furniture like 'sarokkanapék' and 'előszobafalak'.
"""

# Importing necessary modules
import sys


class ShoppingCart:
    """
    Class representing a shopping cart. Contains items and their prices.
    """

    def __init__(self):
        """
        Initialize an empty shopping cart and total price set to 0.
        """
        self.items = []
        self.total_price = 0.0

    def add_item(self, name, price):
        """
        Add an item to the shopping cart.

        Args:
            name (str): Name of the item (e.g., 'sarokkanapé', 'előszobafal').
            price (float): Price of the item.

        Raises:
            ValueError: If the price is not a positive number.
        """
        if price < 0:
            raise ValueError("Price must be a positive number.")
        self.items.append({"name": name, "price": price})
        self.total_price += price

    def calculate_total_price(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            float: Total price.
        """
        return self.total_price

    def display_cart(self):
        """
        Display the contents of the shopping cart.
        """
        print("Shopping Cart:")
        for item in self.items:
            print(f" - {item['name']}: {item['price']:.2f} EUR")
        print(f"Total Price: {self.total_price:.2f} EUR")


def main():
    """
    Main function to demonstrate the ShoppingCart functionality.
    """
    try:
        # Instantiate the ShoppingCart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("sarokkanapé", 799.99)
        cart.add_item("előszobafal", 299.99)
        cart.add_item("asztal", 149.50)

        # Display cart contents
        cart.display_cart()

        # Calculate and print the total price
        print(f"Final Total Price: {cart.calculate_total_price():.2f} EUR")

    except ValueError as ve:
        # Handle invalid prices
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected exceptions
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
