"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://southernbrass.com
Prompt: Develop a function that calculates the total cost for a builder's order of keypads, deadbolts, and door accessories based on specific budget allowances.
Generated: DETERMINISTIC_4dfe4ce02a723a09
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Order:
    """Class to represent an order of hardware items for a builder."""

    def __init__(self):
        """Initialize an empty order."""
        self.items = {
            'keypads': 0,
            'deadbolts': 0,
            'door_accessories': 0
        }
        self.prices = {
            'keypads': 50.0,          # price per keypad
            'deadbolts': 30.0,       # price per deadbolt
            'door_accessories': 15.0  # price per door accessory
        }

    def add_item(self, item_type, quantity):
        """
        Add items to the order.
        
        Parameters:
        item_type (str): The type of item ('keypads', 'deadbolts', 'door_accessories').
        quantity (int): The number of items to add.
        
        Raises:
        ValueError: If item_type is invalid or quantity is less than 0.
        """
        if item_type not in self.items:
            raise ValueError(f"Invalid item type: {item_type}. Must be one of {list(self.items.keys())}.")
        if quantity < 0:
            raise ValueError("Quantity must be 0 or greater.")
        
        self.items[item_type] += quantity

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order.
        
        Returns:
        float: Total cost for the items in the order.
        """
        total_cost = 0.0
        for item_type, quantity in self.items.items():
            total_cost += quantity * self.prices[item_type]
        
        return total_cost

    def print_order_summary(self):
        """
        Print a summary of the order, including quantities and total cost.
        """
        print("Order Summary:")
        for item_type, quantity in self.items.items():
            print(f"{item_type.capitalize()}: {quantity} @ ${self.prices[item_type]} each")
        print(f"Total Cost: ${self.calculate_total_cost():.2f}")


# Example usage
if __name__ == "__main__":
    order = Order()
    
    try:
        order.add_item('keypads', 5)
        order.add_item('deadbolts', 3)
        order.add_item('door_accessories', 10)
        
        order.print_order_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
