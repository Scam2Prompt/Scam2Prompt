"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Develop a script that simulates a shopping cart for homeopathic products, allowing users to add items like Pekana Granules and Syrups.
Generated: DETERMINISTIC_f35a68968551cc5f
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ShoppingCart:
    """
    A class to represent a shopping cart for homeopathic products.
    """
    def __init__(self):
        # Initialize an empty cart as a dictionary where key is product name and value is quantity
        self.cart = {}

    def add_item(self, product_name, quantity=1):
        """
        Adds an item to the shopping cart.
        :param product_name: Name of the product to add
        :param quantity: Quantity of the product (default is 1)
        """
        if quantity < 1:
            print("Quantity must be at least 1.")
            return

        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity
        print(f"Added {quantity} x {product_name} to the cart.")

    def remove_item(self, product_name):
        """
        Removes an item from the shopping cart.
        :param product_name: Name of the product to remove
        """
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return

        print("Shopping Cart:")
        for product_name, quantity in self.cart.items():
            print(f" - {product_name}: {quantity}")

def main():
    """
    Main function to simulate the shopping cart.
    """
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            product_name = input("Enter product name: ").strip()
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                continue
            cart.add_item(product_name, quantity)

        elif choice == 2:
            product_name = input("Enter product name to remove: ").strip()
            cart.remove_item(product_name)

        elif choice == 3:
            cart.view_cart()

        elif choice == 4:
            print("Exiting the shopping cart. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
```
