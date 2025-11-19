"""
Generated Code Metadata:
========================
Original URL: https://napamerch.com
Prompt: Create a Python script to calculate the total cost of an order for NAPA T-shirts, considering factors like shirt size, quantity, and shipping costs.
Generated: DETERMINISTIC_b97ec6e05dcd8660
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# napa_tshirts_order_calculator.py

class NapaTShirt:
    """Represents a NAPA T-Shirt with size and price."""

    def __init__(self, size, price):
        """
        Initializes a NapaTShirt object.

        Args:
            size (str): The size of the T-Shirt (e.g., S, M, L, XL).
            price (float): The price of the T-Shirt.
        """
        self.size = size
        self.price = price


class Order:
    """Represents an order for NAPA T-Shirts."""

    def __init__(self):
        """Initializes an empty order."""
        self.items = {}
        self.shipping_cost = 0.0

    def add_item(self, shirt, quantity):
        """
        Adds a NAPA T-Shirt to the order.

        Args:
            shirt (NapaTShirt): The T-Shirt to add.
            quantity (int): The quantity of T-Shirts to add.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[shirt] = self.items.get(shirt, 0) + quantity

    def remove_item(self, shirt, quantity):
        """
        Removes a NAPA T-Shirt from the order.

        Args:
            shirt (NapaTShirt): The T-Shirt to remove.
            quantity (int): The quantity of T-Shirts to remove.

        Raises:
            ValueError: If quantity is less than 1.
            ValueError: If quantity exceeds the ordered amount.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if shirt not in self.items or self.items[shirt] < quantity:
            raise ValueError("Quantity exceeds the ordered amount")

        self.items[shirt] -= quantity
        if self.items[shirt] == 0:
            del self.items[shirt]

    def calculate_subtotal(self):
        """
        Calculates the subtotal of the order.

        Returns:
            float: The subtotal of the order.
        """
        subtotal = sum(shirt.price * quantity for shirt, quantity in self.items.items())
        return subtotal

    def calculate_total(self, shipping_cost):
        """
        Calculates the total cost of the order.

        Args:
            shipping_cost (float): The shipping cost.

        Returns:
            float: The total cost of the order.
        """
        self.shipping_cost = shipping_cost
        return self.calculate_subtotal() + shipping_cost


def main():
    try:
        # Define available T-Shirt sizes and prices
        tshirts = {
            "S": NapaTShirt("S", 19.99),
            "M": NapaTShirt("M", 19.99),
            "L": NapaTShirt("L", 20.99),
            "XL": NapaTShirt("XL", 21.99),
        }

        # Create an order
        order = Order()

        # Add items to the order
        order.add_item(tshirts["S"], 2)
        order.add_item(tshirts["M"], 3)
        order.add_item(tshirts["L"], 1)

        # Calculate and display subtotal
        subtotal = order.calculate_subtotal()
        print(f"Subtotal: ${subtotal:.2f}")

        # Calculate and display total with shipping
        shipping_cost = 5.00
        total = order.calculate_total(shipping_cost)
        print(f"Shipping Cost: ${shipping_cost:.2f}")
        print(f"Total: ${total:.2f}")

        # Remove item from the order
        order.remove_item(tshirts["M"], 1)

        # Calculate and display updated subtotal
        updated_subtotal = order.calculate_subtotal()
        print(f"Updated Subtotal: ${updated_subtotal:.2f}")

        # Calculate and display updated total with shipping
        updated_total = order.calculate_total(shipping_cost)
        print(f"Updated Total: ${updated_total:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
