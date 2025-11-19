"""
Generated Code Metadata:
========================
Original URL: https://pollossukaoalcarbon.com
Prompt: "Generate a Python script to manage food orders and inventory for a takeaway service like Pollos Sukao al Carbón, including combo meals and delivery options."
Generated: DETERMINISTIC_5704d1407af3cf34
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class FoodItem:
    """Class representing a food item in the inventory."""
    
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Stock: {self.stock})"

class ComboMeal:
    """Class representing a combo meal consisting of multiple food items."""
    
    def __init__(self, name: str, items: List[FoodItem], combo_price: float):
        self.name = name
        self.items = items
        self.combo_price = combo_price

    def __str__(self):
        items_str = ', '.join(item.name for item in self.items)
        return f"{self.name} Combo: {items_str} for ${self.combo_price:.2f}"

class Inventory:
    """Class to manage the inventory of food items."""
    
    def __init__(self):
        self.items: Dict[str, FoodItem] = {}

    def add_item(self, item: FoodItem):
        """Add a food item to the inventory."""
        self.items[item.name] = item

    def update_stock(self, item_name: str, quantity: int):
        """Update the stock of a food item."""
        if item_name in self.items:
            self.items[item_name].stock += quantity
        else:
            raise ValueError(f"Item '{item_name}' not found in inventory.")

    def get_item(self, item_name: str) -> Optional[FoodItem]:
        """Retrieve a food item by name."""
        return self.items.get(item_name)

    def list_items(self) -> List[str]:
        """List all food items in the inventory."""
        return [str(item) for item in self.items.values()]

class Order:
    """Class to manage a food order."""
    
    def __init__(self):
        self.items: List[FoodItem] = []
        self.total_price: float = 0.0

    def add_item(self, item: FoodItem, quantity: int):
        """Add a food item to the order."""
        if item.stock >= quantity:
            self.items.append(item)
            self.total_price += item.price * quantity
            item.stock -= quantity
        else:
            raise ValueError(f"Not enough stock for '{item.name}'. Available: {item.stock}, Requested: {quantity}")

    def __str__(self):
        items_str = ', '.join(f"{item.name}" for item in self.items)
        return f"Order: {items_str} | Total: ${self.total_price:.2f}"

class TakeawayService:
    """Class to manage the takeaway service, including inventory and orders."""
    
    def __init__(self):
        self.inventory = Inventory()
        self.orders: List[Order] = []

    def add_food_item(self, name: str, price: float, stock: int):
        """Add a new food item to the inventory."""
        item = FoodItem(name, price, stock)
        self.inventory.add_item(item)

    def create_order(self) -> Order:
        """Create a new order."""
        order = Order()
        self.orders.append(order)
        return order

    def list_inventory(self) -> List[str]:
        """List all items in the inventory."""
        return self.inventory.list_items()

    def save_inventory(self, filename: str):
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as f:
            json.dump({name: vars(item) for name, item in self.inventory.items.items()}, f)

    def load_inventory(self, filename: str):
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as f:
                items = json.load(f)
                for name, data in items.items():
                    item = FoodItem(name, data['price'], data['stock'])
                    self.inventory.add_item(item)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'.")

# Example usage
if __name__ == "__main__":
    service = TakeawayService()
    
    # Load inventory from a file
    service.load_inventory('inventory.json')
    
    # Add some food items
    service.add_food_item("Pollo al Carbón", 10.99, 50)
    service.add_food_item("Fries", 2.99, 100)
    
    # Create an order
    order = service.create_order()
    try:
        pollo = service.inventory.get_item("Pollo al Carbón")
        fries = service.inventory.get_item("Fries")
        order.add_item(pollo, 2)
        order.add_item(fries, 3)
    except ValueError as e:
        print(e)

    print(order)
    
    # Save inventory back to the file
    service.save_inventory('inventory.json')
```
