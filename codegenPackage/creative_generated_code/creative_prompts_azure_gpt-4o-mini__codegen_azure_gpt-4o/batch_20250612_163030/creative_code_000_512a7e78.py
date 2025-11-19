"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Generate a code snippet for a shopping cart feature that includes items like "rowerki," "hulajnogi," and "jeździki" from Milly Mally's product range.
Generated: DETERMINISTIC_512a7e784ab1bd36
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class ShoppingCart:
    """A class for managing a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, product_name, quantity, price_per_unit):
        """
        Add an item to the shopping cart.

        Args:
            product_name (str): Name of the product.
            quantity (int): Number of units to add.
            price_per_unit (float): Price of a single unit.

        Raises:
            ValueError: If quantity or price_per_unit is invalid.
        """
        if quantity <= 0 or price_per_unit <= 0:
            raise ValueError("Quantity and price per unit must be positive numbers.")
        
        item_id = str(uuid.uuid4())  # Generate a unique ID for each item
        self.items[item_id] = {
            'product_name': product_name,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'total_price': quantity * price_per_unit
        }

    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart.

        Args:
            item_id (str): ID of the item to remove.

        Raises:
            KeyError: If the item_id does not exist in the cart.
        """
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError(f"Item with ID {item_id} not found in the cart.")

    def calculate_total(self):
        """
        Calculate the total price of items in the cart.

        Returns:
            float: Total price of all items in the cart.
        """
        return sum(item['total_price'] for item in self.items.values())

    def list_items(self):
        """
        List all items in the shopping cart.

        Returns:
            dict: A dictionary of items in the cart.
        """
        return self.items


# Example usage:

if __name__ == "__main__":
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item("rowerki", 2, 100.0)  # Adding 2 units of "rowerki" priced at 100.0 each
        cart.add_item("hulajnogi", 1, 150.0)  # Adding 1 unit of "hulajnogi" priced at 150.0
        cart.add_item("jeździki", 3, 75.0)  # Adding 3 units of "jeździki" priced at 75.0 each

        # List items in the cart
        print("Items in the cart:")
        for item_id, item_details in cart.list_items().items():
            print(f"ID: {item_id}, Product: {item_details['product_name']}, Quantity: {item_details['quantity']}, "
                  f"Price per Unit: {item_details['price_per_unit']}, Total Price: {item_details['total_price']}")

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price: {total_price}")

        # Remove an item by ID (replace with a valid ID from the output above)
        # Uncomment the line below and provide a valid ID to test removal functionality
        # cart.remove_item("<valid_item_id_here>")

    except Exception as e:
        print(f"An error occurred: {e}")
```
