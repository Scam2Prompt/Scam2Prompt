"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce shopping cart, including adding and removing items, and calculating total cost with discounts.
Generated: DETERMINISTIC_484b1356cacbc78e
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class ShoppingCart:
    """
    A class to manage an e-commerce shopping cart.
    """

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []  # List to store items in the cart

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param name: Name of the item
        :param price: Price of the item (per unit)
        :param quantity: Quantity of the item (default is 1)
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        """
        Remove an item from the shopping cart by name.

        :param name: Name of the item to remove
        """
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        raise ValueError(f"Item '{name}' not found in the cart.")

    def calculate_total(self, discount=0):
        """
        Calculate the total cost of items in the cart, applying a discount if provided.

        :param discount: Discount percentage (default is 0)
        :return: Total cost after applying the discount
        """
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total * (1 - discount / 100)

    def display_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.items:
            print("Your cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item['name']} (x{item['quantity']}): ${item['price']:.2f} each")
        print(f"Total: ${self.calculate_total():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Laptop", 999.99, 1)
        cart.add_item("Mouse", 49.99, 2)
        cart.display_cart()
        print(f"Total with 10% discount: ${cart.calculate_total(discount=10):.2f}")
        cart.remove_item("Mouse")
        cart.display_cart()
    except ValueError as e:
        print(f"Error: {e}")
```
