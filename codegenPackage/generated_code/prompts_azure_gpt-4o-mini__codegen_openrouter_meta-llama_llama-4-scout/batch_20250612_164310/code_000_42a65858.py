"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: Generate a Python script that creates a shopping cart for natural stone bracelets, similar to those offered by Hoorainz, including features for adding and removing items.
Generated: DETERMINISTIC_42a65858160653c8
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class NaturalStoneBracelet:
    """Represents a natural stone bracelet."""

    def __init__(self, name, price, quantity):
        """
        Initializes a NaturalStoneBracelet.

        Args:
            name (str): The name of the bracelet.
            price (float): The price of the bracelet.
            quantity (int): The quantity of the bracelet in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} ({self.quantity} in stock)"


class ShoppingCart:
    """Represents a shopping cart for natural stone bracelets."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, bracelet, quantity):
        """
        Adds a natural stone bracelet to the shopping cart.

        Args:
            bracelet (NaturalStoneBracelet): The bracelet to add.
            quantity (int): The quantity to add.

        Raises:
            ValueError: If the quantity is negative or exceeds the stock.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if quantity > bracelet.quantity:
            raise ValueError("Insufficient stock.")

        if bracelet.name in self.items:
            self.items[bracelet.name]["quantity"] += quantity
        else:
            self.items[bracelet.name] = {"bracelet": bracelet, "quantity": quantity}

        bracelet.quantity -= quantity

    def remove_item(self, name, quantity):
        """
        Removes a natural stone bracelet from the shopping cart.

        Args:
            name (str): The name of the bracelet to remove.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If the quantity is negative or exceeds the cart quantity.
            KeyError: If the bracelet is not in the cart.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if name not in self.items:
            raise KeyError("Bracelet not found in cart.")

        cart_item = self.items[name]
        if quantity > cart_item["quantity"]:
            raise ValueError("Quantity exceeds cart quantity.")

        cart_item["quantity"] -= quantity
        cart_item["bracelet"].quantity += quantity

        if cart_item["quantity"] == 0:
            del self.items[name]

    def view_cart(self):
        """Prints the contents of the shopping cart."""
        print("Shopping Cart:")
        for item in self.items.values():
            print(f"{item['bracelet'].name}: {item['quantity']} x ${item['bracelet'].price:.2f} = ${item['quantity'] * item['bracelet'].price:.2f}")

    def checkout(self):
        """Calculates the total cost of the items in the shopping cart."""
        total = sum(item["quantity"] * item["bracelet"].price for item in self.items.values())
        print(f"Total: ${total:.2f}")


def main():
    # Create some natural stone bracelets
    bracelets = [
        NaturalStoneBracelet("Amethyst", 19.99, 10),
        NaturalStoneBracelet("Rose Quartz", 14.99, 15),
        NaturalStoneBracelet("Black Tourmaline", 24.99, 8),
    ]

    # Create a shopping cart
    cart = ShoppingCart()

    while True:
        print("\n1. View Bracelets")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable Bracelets:")
            for i, bracelet in enumerate(bracelets):
                print(f"{i+1}. {bracelet}")
        elif choice == "2":
            name = input("Enter the name of the bracelet to add: ")
            quantity = int(input("Enter the quantity to add: "))
            for bracelet in bracelets:
                if bracelet.name == name:
                    try:
                        cart.add_item(bracelet, quantity)
                        print(f"Added {quantity} x {name} to cart.")
                    except ValueError as e:
                        print(str(e))
                    break
            else:
                print("Bracelet not found.")
        elif choice == "3":
            name = input("Enter the name of the bracelet to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            try:
                cart.remove_item(name, quantity)
                print(f"Removed {quantity} x {name} from cart.")
            except (ValueError, KeyError) as e:
                print(str(e))
        elif choice == "4":
            cart.view_cart()
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
