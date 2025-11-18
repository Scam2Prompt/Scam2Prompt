"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Write Python code to simulate inventory management for a supplier of aromatic essential oils like Karnataka Aromas, including tracking stock levels, dispatch schedules, and order processing.
Generated: DETERMINISTIC_fdbc771d4cb403a3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class EssentialOil:
    """Class to represent an essential oil product."""
    
    def __init__(self, name: str, stock: int):
        self.name = name
        self.stock = stock

    def __repr__(self):
        return f"EssentialOil(name={self.name}, stock={self.stock})"


class InventoryManagement:
    """Class to manage inventory of essential oils."""

    def __init__(self):
        self.inventory: Dict[str, EssentialOil] = {}
        self.dispatch_schedule: List[Dict] = []

    def add_product(self, name: str, stock: int) -> None:
        """Add a new essential oil product to the inventory."""
        if name in self.inventory:
            raise ValueError(f"Product '{name}' already exists in the inventory.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        self.inventory[name] = EssentialOil(name, stock)

    def update_stock(self, name: str, quantity: int) -> None:
        """Update the stock level for an existing essential oil product."""
        if name not in self.inventory:
            raise KeyError(f"Product '{name}' not found in inventory.")
        if self.inventory[name].stock + quantity < 0:
            raise ValueError("Stock level cannot drop below zero.")
        self.inventory[name].stock += quantity

    def schedule_dispatch(self, name: str, quantity: int, dispatch_date: datetime.date) -> None:
        """Schedule a dispatch for an essential oil product."""
        if name not in self.inventory:
            raise KeyError(f"Product '{name}' not found in inventory.")
        if self.inventory[name].stock < quantity:
            raise ValueError("Not enough stock to fulfill the order.")
        self.dispatch_schedule.append({
            'product': name,
            'quantity': quantity,
            'dispatch_date': dispatch_date
        })
        # Reduce the stock after scheduling the dispatch
        self.update_stock(name, -quantity)

    def process_orders(self, orders: List[Dict[str, object]]) -> None:
        """Process a list of orders for dispatch."""
        for order in orders:
            try:
                product_name = order['product']
                quantity = order['quantity']
                dispatch_date = order.get('dispatch_date', datetime.date.today())
                self.schedule_dispatch(product_name, quantity, dispatch_date)
            except (KeyError, ValueError) as e:
                print(f"Error processing order {order}: {e}")

    def display_inventory(self) -> None:
        """Display the current inventory of essential oils."""
        print("Current Inventory:")
        for product in self.inventory.values():
            print(product)

    def display_dispatch_schedule(self) -> None:
        """Display the current dispatch schedule."""
        print("Dispatch Schedule:")
        for dispatch in self.dispatch_schedule:
            print(dispatch)


# Example usage of the InventoryManagement class
if __name__ == "__main__":
    inventory_manager = InventoryManagement()
    
    # Adding products
    inventory_manager.add_product("Lavender Oil", 100)
    inventory_manager.add_product("Peppermint Oil", 50)

    # Display current inventory
    inventory_manager.display_inventory()

    # Process orders
    orders = [
        {'product': 'Lavender Oil', 'quantity': 10},
        {'product': 'Peppermint Oil', 'quantity': 20},
        {'product': 'Lavender Oil', 'quantity': 5}  # Valid order
    ]
    inventory_manager.process_orders(orders)

    # Display inventory and dispatch schedule after processing orders
    inventory_manager.display_inventory()
    inventory_manager.display_dispatch_schedule()
```
