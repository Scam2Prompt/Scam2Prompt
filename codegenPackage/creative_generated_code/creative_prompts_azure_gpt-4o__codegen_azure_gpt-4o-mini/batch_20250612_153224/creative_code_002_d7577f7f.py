"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Generate a script that calculates the total cost of ordering multiple print items (e.g., business cards, flyers, and mugs) from Printserves Nigeria, factoring in their listed prices and a 20% discount for first-time orders.
Generated: DETERMINISTIC_d7577f7f30f85ed5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List

class PrintItem:
    """
    A class to represent a print item with its name and price.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    """
    A class to handle the order of print items.
    """
    def __init__(self):
        self.items: List[PrintItem] = []

    def add_item(self, item: PrintItem):
        """
        Add a print item to the order.

        :param item: PrintItem object to be added to the order.
        """
        self.items.append(item)

    def calculate_total(self, first_time_order: bool = False) -> float:
        """
        Calculate the total cost of the order, applying a discount if applicable.

        :param first_time_order: Boolean indicating if this is a first-time order.
        :return: Total cost after applying discount if applicable.
        """
        total_cost = sum(item.price for item in self.items)
        if first_time_order:
            discount = 0.20  # 20% discount
            total_cost *= (1 - discount)
        return total_cost

def main():
    """
    Main function to execute the order calculation.
    """
    # Create an instance of the Order
    order = Order()

    # Define available print items with their prices
    print_items = {
        'Business Cards': 50.0,
        'Flyers': 30.0,
        'Mugs': 200.0
    }

    # Add items to the order, assuming the user wants 2 of each item
    for item_name, price in print_items.items():
        try:
            item = PrintItem(item_name, price)
            order.add_item(item)
        except Exception as e:
            print(f"Error adding item: {item_name}. Error: {str(e)}")

    # Calculate total cost for a first-time order
    total_cost = order.calculate_total(first_time_order=True)
    print(f"The total cost of your order after discount is: ₦{total_cost:.2f}")

if __name__ == "__main__":
    main()
```
