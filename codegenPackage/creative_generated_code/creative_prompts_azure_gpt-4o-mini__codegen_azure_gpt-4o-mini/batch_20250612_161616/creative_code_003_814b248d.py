"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Develop a script that calculates the total price for a shopping cart containing multiple items, including jackets and accessories from KAMBOZ.
Generated: DETERMINISTIC_814b248d96dd8fcc
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """
    A class to represent an item in the shopping cart.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes an instance of Item.

        :param name: str: The name of the item.
        :param price: float: The price of a single unit of the item.
        :param quantity: int: The quantity of the item.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """
        Calculates the total price for the item based on its quantity.

        :return: float: Total price for the item.
        """
        return self.price * self.quantity


class ShoppingCart:
    """
    A class to represent a shopping cart.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the shopping cart.

        :param item: Item: An instance of Item to be added to the cart.
        """
        if not isinstance(item, Item):
            raise ValueError("Item must be an instance of Item class.")
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total price for all items in the shopping cart.

        :return: float: The total price for the shopping cart.
        """
        total = 0.0
        for item in self.items:
            total += item.total_price()
        return total


def main():
    """
    Main function to demonstrate the shopping cart functionality.
    """
    cart = ShoppingCart()

    # Add some sample items to the cart
    try:
        cart.add_item(Item("KAMBOZ Jacket", 99.99, 1))
        cart.add_item(Item("KAMBOZ Accessory", 19.99, 2))
        cart.add_item(Item("KAMBOZ Jacket", 89.99, 1))
        
        # Calculate the total price
        total_price = cart.calculate_total()
        print(f"Total price for the shopping cart is: ${total_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
