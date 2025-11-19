"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Develop a script that simulates a shopping cart for homeopathic products, allowing users to add items like Pekana Granules and Syrups.
Generated: DETERMINISTIC_f35a68968551cc5f
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ShoppingCart:
    """
    A class to represent a shopping cart for homeopathic products.
    """

    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.cart = []

    def add_item(self, product_name, quantity, price):
        """
        Add an item to the shopping cart.

        :param product_name: Name of the product
        :param quantity: Quantity of the product
        :param price: Price per unit of the product
        """
        if quantity <= 0 or price <= 0:
            print("Error: Quantity and price must be positive numbers.")
            return

        item = {
            "product_name": product_name,
            "quantity": quantity,
            "price": price,
            "total_price": quantity * price
        }
        self.cart.append(item)
        print(f"Added {quantity} x {product_name} to the cart.")

    def view_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\nShopping Cart:")
        for idx, item in enumerate(self.cart, start=1):
            print(f"{idx}. {item['product_name']} - Quantity: {item['quantity']}, "
                  f"Price: ${item['price']:.2f}, Total: ${item['total_price']:.2f}")
        print(f"Total Cart Value: ${self.calculate_total():.2f}\n")

    def calculate_total(self):
        """
        Calculate the total value of the shopping cart.

        :return: Total value of the cart
        """
        return sum(item['total_price'] for item in self.cart)

    def remove_item(self, product_name):
        """
        Remove an item from the shopping cart by product name.

        :param product_name: Name of the product to remove
        """
        for item in self.cart:
            if item['product_name'].lower() == product_name.lower():
                self.cart.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"Error: {product_name} not found in the cart.")

    def clear_cart(self):
        """
        Clear all items from the shopping cart.
        """
        self.cart.clear()
        print("Shopping cart cleared.")

def main():
    """
    Main function to simulate the shopping cart functionality.
    """
    cart = ShoppingCart()

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Clear Cart")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            product_name = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: "))
            except ValueError:
                print("Error: Quantity must be an integer and price must be a number.")
                continue
            cart.add_item(product_name, quantity, price)
        elif choice == 2:
            cart.view_cart()
        elif choice == 3:
            product_name = input("Enter product name to remove: ")
            cart.remove_item(product_name)
        elif choice == 4:
            cart.clear_cart()
        elif choice == 5:
            print("Exiting the shopping cart. Goodbye!")
            sys.exit(0)
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
