"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Develop a shopping cart feature that calculates total prices based on original and current prices, reflecting the sales on Queenzie.
Generated: DETERMINISTIC_5ec350f100cae8c6
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
    Class to represent an item in the shopping cart.

    Attributes:
        name (str): The name of the item.
        original_price (float): The original price of the item.
        current_price (float): The current sale price of the item.
        quantity (int): The quantity of the item in the cart.
    """

    def __init__(self, name: str, original_price: float, current_price: float, quantity: int):
        """
        Initializes an Item with its properties.

        Args:
            name (str): The name of the item.
            original_price (float): The original price of the item.
            current_price (float): The current sale price of the item.
            quantity (int): The quantity of the item in the cart.
        """
        self.name = name
        self.original_price = original_price
        self.current_price = current_price
        self.quantity = quantity

    def total_price(self) -> float:
        """
        Calculates the total price for the item.

        Returns:
            float: Total price based on current price and quantity.
        """
        return self.current_price * self.quantity


class ShoppingCart:
    """
    Class to represent a shopping cart which contains multiple items.

    Attributes:
        items (list): A list of Item objects in the cart.
    """

    def __init__(self):
        """ Initializes an empty shopping cart. """
        self.items = []

    def add_item(self, item: Item):
        """
        Adds an item to the shopping cart.

        Args:
            item (Item): The item to add to the cart.
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item objects can be added to the cart.")
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.

        Returns:
            float: Total price of all items in the cart.
        """
        total = 0.0
        for item in self.items:
            total += item.total_price()
        return total

    def clear_cart(self):
        """ Clears all items from the shopping cart. """
        self.items = []

    def get_receipt(self) -> str:
        """
        Generates a receipt for the items in the cart.

        Returns:
            str: A receipt string listing items, their prices, and total.
        """
        receipt_lines = []
        for item in self.items:
            receipt_lines.append(f"{item.name}: ${item.current_price:.2f} x {item.quantity} = ${item.total_price():.2f}")
        total = self.calculate_total()
        receipt_lines.append(f"Total: ${total:.2f}")
        return "\n".join(receipt_lines)


# Example usage:
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        # Adding items to the cart
        cart.add_item(Item("T-shirt", 20.00, 15.00, 2))
        cart.add_item(Item("Jeans", 40.00, 30.00, 1))
        
        # Display the receipt
        print(cart.get_receipt())
        
        # Calculate total
        print(f"Total Price: ${cart.calculate_total():.2f}")

        # Clear the cart
        cart.clear_cart()
        print("Cart cleared.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
