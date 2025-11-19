"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Generate a code snippet to create a shopping cart feature for an online furniture store like Tahirbrosfurniture, including functionalities for adding items, removing items, and calculating total price.
Generated: DETERMINISTIC_d875732b5e9472b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    """
    A class to represent a shopping cart for an online furniture store.
    Includes functionalities for adding items, removing items, and calculating the total price.
    """

    def __init__(self):
        """
        Initializes the shopping cart with an empty items list.
        Each item will be represented as a dictionary with 'name', 'price', and 'quantity'.
        """
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Adds an item to the shopping cart.

        :param name: Name of the furniture item
        :param price: Price of the furniture item
        :param quantity: Quantity of the item (default is 1)
        :raises ValueError: If price or quantity are invalid
        """
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        # Check if the item already exists in the cart
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return

        # If the item is not in the cart, add it as a new entry
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name: str):
        """
        Removes an item from the shopping cart by name.

        :param name: Name of the furniture item to remove
        :raises ValueError: If the item is not found in the cart
        """
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return
        raise ValueError(f"Item '{name}' not found in the cart")

    def calculate_total_price(self) -> float:
        """
        Calculates the total price of all items in the shopping cart.

        :return: The total price
        """
        return sum(item['price'] * item['quantity'] for item in self.items)

    def display_cart(self):
        """
        Displays the contents of the shopping cart in a readable format.

        :return: None
        """
        if not self.items:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item['name']} (Price: ${item['price']:.2f}, Quantity: {item['quantity']})")
        print(f"Total Price: ${self.calculate_total_price():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_item("Sofa", 599.99, 1)
        cart.add_item("Dining Table", 899.99, 1)
        cart.add_item("Chair", 199.99, 4)
        cart.display_cart()
        cart.remove_item("Chair")
        cart.display_cart()
    except ValueError as e:
        print(f"Error: {e}")
```
