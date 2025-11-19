"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

# Import necessary modules
import sys

class ShoppingCart:
    """
    A class to represent a shopping cart for kitchen accessories.
    """

    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.items = []

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param name: Name of the item (str)
        :param price: Price of the item (float)
        :param quantity: Quantity of the item (int, default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        """
        Remove an item from the shopping cart by name.

        :param name: Name of the item to remove (str)
        """
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        raise ValueError(f"Item '{name}' not found in the cart.")

    def view_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.items:
            print("Your shopping cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item['name']} (x{item['quantity']}): ${item['price']:.2f} each")
        print(f"Total: ${self.calculate_total():.2f}")

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.

        :return: Total cost (float)
        """
        return sum(item["price"] * item["quantity"] for item in self.items)

    def checkout(self):
        """
        Simulate the checkout process.
        """
        if not self.items:
            print("Your shopping cart is empty. Add items before checking out.")
            return
        print("Proceeding to checkout...")
        print(f"Total amount due: ${self.calculate_total():.2f}")
        print("Thank you for shopping with us!")


def main():
    """
    Main function to simulate the shopping cart experience.
    """
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                cart.add_item(name, price, quantity)
                print(f"Added {quantity} x {name} to the cart.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            try:
                name = input("Enter item name to remove: ")
                cart.remove_item(name)
                print(f"Removed {name} from the cart.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 3:
            cart.view_cart()
        elif choice == 4:
            cart.checkout()
        elif choice == 5:
            print("Exiting the shopping cart. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
```
