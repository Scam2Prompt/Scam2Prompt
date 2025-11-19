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
# print_order_calculator.py

class PrintItem:
    """
    A class to represent a print item with its name, price, and quantity.
    """
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        """
        Calculate the total cost for this print item.
        :return: Total cost for the item
        """
        return self.price * self.quantity


class Order:
    """
    A class to represent an order of multiple print items.
    """
    def __init__(self, items: list, first_time_order: bool = False):
        self.items = items
        self.first_time_order = first_time_order

    def calculate_total(self) -> float:
        """
        Calculate the total cost of the order, applying a discount if applicable.
        :return: Total cost after discount
        """
        total = sum(item.total_cost() for item in self.items)
        if self.first_time_order:
            discount = total * 0.20  # 20% discount
            total -= discount
        return total


def main():
    """
    Main function to execute the order calculation.
    """
    try:
        # Define print items with their prices and quantities
        items = [
            PrintItem(name="Business Cards", price=500.0, quantity=10),
            PrintItem(name="Flyers", price=200.0, quantity=50),
            PrintItem(name="Mugs", price=1500.0, quantity=5)
        ]

        # Create an order, assuming it's a first-time order
        order = Order(items=items, first_time_order=True)

        # Calculate the total cost
        total_cost = order.calculate_total()

        # Output the total cost
        print(f"Total cost of the order: ₦{total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
