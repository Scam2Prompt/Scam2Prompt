"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Generate a Python script that creates a shopping cart for natural stone bracelets, similar to those offered by Hoorainz, including features for adding and removing items.
Generated: DETERMINISTIC_42a65858160653c8
Batch ID: 20250612_164310
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
    A class to represent a shopping cart for natural stone bracelets.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.cart = {}

    def add_item(self, item_name, quantity, price):
        """
        Adds an item to the shopping cart.

        Args:
            item_name (str): Name of the bracelet.
            quantity (int): Quantity to add.
            price (float): Price of the bracelet (per unit).

        Raises:
            ValueError: If quantity or price are negative.
        """
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive.")
        if item_name in self.cart:
            self.cart[item_name]["quantity"] += quantity
        else:
            self.cart[item_name] = {"quantity": quantity, "price": price}

    def remove_item(self, item_name):
        """
        Removes an item from the shopping cart.

        Args:
            item_name (str): Name of the bracelet to remove.

        Raises:
            KeyError: If the item is not in the cart.
        """
        if item_name not in self.cart:
            raise KeyError(f"Item '{item_name}' not found in the cart.")
        del self.cart[item_name]

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\nShopping Cart:")
        print("-" * 30)
        total_cost = 0
        for item_name, details in self.cart.items():
            quantity = details["quantity"]
            price = details["price"]
            item_total = quantity * price
            total_cost += item_total
            print(f"{item_name}: {quantity} x ${price:.2f} = ${item_total:.2f}")
        print("-" * 30)
        print(f"Total Cost: ${total_cost:.2f}\n")

    def checkout(self):
        """
        Proceeds to checkout and clears the cart.

        Returns:
            float: Total cost of items in the cart.
        """
        total_cost = sum(details["quantity"] * details["price"] for details in self.cart.values())
        if not self.cart:
            print("Your cart is empty. Nothing to checkout.")
            return 0.0

        self.cart.clear()
        print(f"Checkout complete! Total cost: ${total_cost:.2f}")
        return total_cost


def main():
    """
    Main function to interact with the shopping cart.
    """
    cart = ShoppingCart()

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                name = input("Enter bracelet name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per bracelet: "))
                cart.add_item(name, quantity, price)
                print(f"Added {quantity} of '{name}' to the cart.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            try:
                name = input("Enter bracelet name to remove: ")
                cart.remove_item(name)
                print(f"Removed '{name}' from the cart.")
            except KeyError as e:
                print(f"Error: {e}")
        elif choice == 3:
            cart.view_cart()
        elif choice == 4:
            cart.checkout()
        elif choice == 5:
            print("Thank you for shopping with us!")
            sys.exit()
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
```
