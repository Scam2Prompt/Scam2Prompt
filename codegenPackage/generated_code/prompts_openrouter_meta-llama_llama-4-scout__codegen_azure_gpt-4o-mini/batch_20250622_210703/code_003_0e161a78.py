"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Develop a simple sales program for a cafe or restaurant using DemirSoft's tools, including order tracking and adisyon printing.
Generated: DETERMINISTIC_0e161a78cb4f7887
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sales_program.py

class Order:
    """Class to represent a single order in the cafe."""
    
    def __init__(self, order_id, items):
        """
        Initialize an order with an ID and a list of items.
        
        :param order_id: Unique identifier for the order
        :param items: List of items in the order
        """
        self.order_id = order_id
        self.items = items
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """Calculate the total price of the order."""
        return sum(item['price'] * item['quantity'] for item in self.items)

    def __str__(self):
        """Return a string representation of the order."""
        items_str = "\n".join(f"{item['name']} x {item['quantity']} - ${item['price'] * item['quantity']:.2f}" for item in self.items)
        return f"Order ID: {self.order_id}\nItems:\n{items_str}\nTotal: ${self.total_price:.2f}"


class Cafe:
    """Class to represent the cafe and manage orders."""
    
    def __init__(self):
        """Initialize the cafe with an empty order list."""
        self.orders = []

    def add_order(self, order):
        """
        Add a new order to the cafe's order list.
        
        :param order: An instance of the Order class
        """
        if not isinstance(order, Order):
            raise ValueError("Invalid order. Must be an instance of Order.")
        self.orders.append(order)

    def print_adisyon(self, order_id):
        """
        Print the adisyon (receipt) for a specific order.
        
        :param order_id: The ID of the order to print
        """
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if order is None:
            raise ValueError(f"Order ID {order_id} not found.")
        
        print("\n--- Adisyon ---")
        print(order)
        print("----------------")


def main():
    """Main function to run the cafe sales program."""
    cafe = Cafe()

    # Sample orders
    try:
        order1 = Order(order_id=1, items=[
            {'name': 'Coffee', 'price': 3.00, 'quantity': 2},
            {'name': 'Croissant', 'price': 2.50, 'quantity': 1}
        ])
        cafe.add_order(order1)

        order2 = Order(order_id=2, items=[
            {'name': 'Tea', 'price': 2.00, 'quantity': 3},
            {'name': 'Sandwich', 'price': 5.00, 'quantity': 2}
        ])
        cafe.add_order(order2)

        # Print adisyon for each order
        cafe.print_adisyon(order_id=1)
        cafe.print_adisyon(order_id=2)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
