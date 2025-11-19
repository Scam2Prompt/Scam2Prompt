"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: Generate a script that calculates the total cost of ordering multiple print items (e.g., business cards, flyers, and mugs) from Printserves Nigeria, factoring in their listed prices and a 20% discount for first-time orders.
Generated: DETERMINISTIC_d7577f7f30f85ed5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# printserves_order_calculator.py

class PrintItem:
    """Represents a print item with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a PrintItem.

        Args:
            name (str): The name of the print item.
            price (float): The price of the print item.
        """
        self.name = name
        self.price = price


class Order:
    """Represents an order with a list of print items and a discount."""

    def __init__(self, is_first_time_order: bool):
        """
        Initializes an Order.

        Args:
            is_first_time_order (bool): Whether this is the customer's first order.
        """
        self.print_items = []
        self.is_first_time_order = is_first_time_order

    def add_print_item(self, print_item: PrintItem, quantity: int):
        """
        Adds a print item to the order.

        Args:
            print_item (PrintItem): The print item to add.
            quantity (int): The quantity of the print item.
        """
        self.print_items.append((print_item, quantity))

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the order.

        Returns:
            float: The total cost of the order.
        """
        subtotal = sum(print_item.price * quantity for print_item, quantity in self.print_items)

        discount_percentage = 0.20 if self.is_first_time_order else 0.0
        discount_amount = subtotal * discount_percentage

        total_cost = subtotal - discount_amount

        return total_cost


def main():
    try:
        # Define print items and their prices
        business_cards = PrintItem("Business Cards", 5000.0)
        flyers = PrintItem("Flyers", 2000.0)
        mugs = PrintItem("Mugs", 1500.0)

        # Create an order
        is_first_time_order = True
        order = Order(is_first_time_order)

        # Add print items to the order
        order.add_print_item(business_cards, 2)
        order.add_print_item(flyers, 5)
        order.add_print_item(mugs, 1)

        # Calculate and print the total cost
        total_cost = order.calculate_total_cost()
        print(f"Total cost: ₦{total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
