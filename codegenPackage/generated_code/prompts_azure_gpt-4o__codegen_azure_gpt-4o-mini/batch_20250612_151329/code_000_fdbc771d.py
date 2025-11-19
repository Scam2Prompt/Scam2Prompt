"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Write Python code to simulate inventory management for a supplier of aromatic essential oils like Karnataka Aromas, including tracking stock levels, dispatch schedules, and order processing.
Generated: DETERMINISTIC_fdbc771d4cb403a3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class EssentialOil:
    """Class to represent an essential oil product."""
    
    def __init__(self, name: str, stock: int, reorder_level: int):
        """
        Initialize an essential oil product.

        :param name: Name of the essential oil.
        :param stock: Current stock level.
        :param reorder_level: Stock level at which to reorder.
        """
        self.name = name
        self.stock = stock
        self.reorder_level = reorder_level

    def update_stock(self, quantity: int):
        """Update the stock level of the essential oil."""
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock += quantity

    def needs_reorder(self) -> bool:
        """Check if the product needs to be reordered."""
        return self.stock <= self.reorder_level


class Order:
    """Class to represent an order for essential oils."""
    
    def __init__(self, oil: EssentialOil, quantity: int):
        """
        Initialize an order.

        :param oil: The essential oil being ordered.
        :param quantity: Quantity of the essential oil.
        """
        self.oil = oil
        self.quantity = quantity
        self.order_date = datetime.datetime.now()

    def process_order(self) -> bool:
        """Process the order and update stock if possible."""
        if self.oil.stock >= self.quantity:
            self.oil.update_stock(-self.quantity)
            return True
        else:
            raise ValueError("Insufficient stock to fulfill the order.")


class InventoryManager:
    """Class to manage the inventory of essential oils."""
    
    def __init__(self):
        """Initialize the inventory manager with an empty inventory."""
        self.inventory: Dict[str, EssentialOil] = {}

    def add_oil(self, oil: EssentialOil):
        """Add a new essential oil to the inventory."""
        if oil.name in self.inventory:
            raise ValueError("Essential oil already exists in inventory.")
        self.inventory[oil.name] = oil

    def get_oil(self, name: str) -> Optional[EssentialOil]:
        """Retrieve an essential oil by name."""
        return self.inventory.get(name)

    def check_inventory(self) -> List[str]:
        """Check the inventory and return a list of oils that need reordering."""
        return [oil.name for oil in self.inventory.values() if oil.needs_reorder()]

    def process_order(self, name: str, quantity: int) -> bool:
        """Process an order for a specific essential oil."""
        oil = self.get_oil(name)
        if oil is None:
            raise ValueError("Essential oil not found in inventory.")
        order = Order(oil, quantity)
        return order.process_order()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize inventory manager
        inventory_manager = InventoryManager()

        # Add essential oils to inventory
        lavender = EssentialOil("Lavender", stock=50, reorder_level=20)
        peppermint = EssentialOil("Peppermint", stock=30, reorder_level=10)

        inventory_manager.add_oil(lavender)
        inventory_manager.add_oil(peppermint)

        # Check inventory for reorder needs
        oils_needing_reorder = inventory_manager.check_inventory()
        print("Oils needing reorder:", oils_needing_reorder)

        # Process an order
        order_success = inventory_manager.process_order("Lavender", 10)
        print("Order processed successfully:", order_success)

        # Check inventory after order
        oils_needing_reorder = inventory_manager.check_inventory()
        print("Oils needing reorder after order:", oils_needing_reorder)

    except ValueError as e:
        print(f"Error: {e}")
```
