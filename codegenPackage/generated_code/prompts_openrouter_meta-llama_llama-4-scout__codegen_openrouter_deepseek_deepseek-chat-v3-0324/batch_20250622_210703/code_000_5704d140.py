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
import os
from typing import Dict, List, Optional

class InventoryItem:
    """Represents an item in the inventory."""
    def __init__(self, name: str, quantity: int, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def to_dict(self) -> Dict:
        """Convert inventory item to dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit
        }

class ComboMeal:
    """Represents a combo meal."""
    def __init__(self, name: str, items: Dict[str, int], price: float):
        self.name = name
        self.items = items  # {item_name: quantity}
        self.price = price

    def to_dict(self) -> Dict:
        """Convert combo meal to dictionary."""
        return {
            'name': self.name,
            'items': self.items,
            'price': self.price
        }

class OrderItem:
    """Represents an item in an order."""
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert order item to dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Order:
    """Represents a customer order."""
    def __init__(self, order_id: int, customer_name: str, items: List[OrderItem], 
                 delivery_address: Optional[str] = None, is_delivery: bool = False):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.delivery_address = delivery_address
        self.is_delivery = is_delivery
        self.total_price = sum(item.price * item.quantity for item in items)

    def to_dict(self) -> Dict:
        """Convert order to dictionary."""
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'items': [item.to_dict() for item in self.items],
            'delivery_address': self.delivery_address,
            'is_delivery': self.is_delivery,
            'total_price': self.total_price
        }

class TakeawayService:
    """Manages food orders and inventory for a takeaway service."""
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}
        self.combo_meals: Dict[str, ComboMeal] = {}
        self.orders: Dict[int, Order] = {}
        self.next_order_id = 1
        self.load_data()

    def load_data(self):
        """Load data from JSON files if they exist."""
        try:
            if os.path.exists('inventory.json'):
                with open('inventory.json', 'r') as f:
                    inventory_data = json.load(f)
                    for item in inventory_data:
                        self.inventory[item['name']] = InventoryItem(
                            item['name'], item['quantity'], item['unit'])
            
            if os.path.exists('combo_meals.json'):
                with open('combo_meals.json', 'r') as f:
                    combo_data = json.load(f)
                    for combo in combo_data:
                        self.combo_meals[combo['name']] = ComboMeal(
                            combo['name'], combo['items'], combo['price'])
            
            if os.path.exists('orders.json'):
                with open('orders.json', 'r') as f:
                    orders_data = json.load(f)
                    for order in orders_data:
                        items = [OrderItem(item['name'], item['quantity'], item['price']) 
                                for item in order['items']]
                        self.orders[order['order_id']] = Order(
                            order['order_id'], order['customer_name'], items,
                            order['delivery_address'], order['is_delivery'])
                        if order['order_id'] >= self.next_order_id:
                            self.next_order_id = order['order_id'] + 1
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        """Save data to JSON files."""
        try:
            with open('inventory.json', 'w') as f:
                json.dump([item.to_dict() for item in self.inventory.values()], f, indent=2)
            
            with open('combo_meals.json', 'w') as f:
                json.dump([combo.to_dict() for combo in self.combo_meals.values()], f, indent=2)
            
            with open('orders.json', 'w') as f:
                json.dump([order.to_dict() for order in self.orders.values()], f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_inventory_item(self, name: str, quantity: int, unit: str):
        """Add or update an inventory item."""
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = InventoryItem(name, quantity, unit)
        self.save_data()

    def remove_inventory_item(self, name: str, quantity: int):
        """Remove quantity from inventory item."""
        if name not in self.inventory:
            raise ValueError(f"Inventory item '{name}' not found")
        if self.inventory[name].quantity < quantity:
            raise ValueError(f"Not enough {name} in inventory")
        self.inventory[name].quantity -= quantity
        if self.inventory[name].quantity == 0:
            del self.inventory[name]
        self.save_data()

    def add_combo_meal(self, name: str, items: Dict[str, int], price: float):
        """Add a new combo meal."""
        if name in self.combo_meals:
            raise ValueError(f"Combo meal '{name}' already exists")
        self.combo_meals[name] = ComboMeal(name, items, price)
        self.save_data()

    def update_combo_meal(self, name: str, items: Dict[str, int], price: float):
        """Update an existing combo meal."""
        if name not in self.combo_meals:
            raise ValueError(f"Combo meal '{name}' not found")
        self.combo_meals[name] = ComboMeal(name, items, price)
        self.save_data()

    def remove_combo_meal(self, name: str):
        """Remove a combo meal."""
        if name not in self.combo_meals:
            raise ValueError(f"Combo meal '{name}' not found")
        del self.combo_meals[name]
        self.save_data()

    def place_order(self, customer_name: str, items: List[Dict], 
                   delivery_address: Optional[str] = None) -> Order:
        """
        Place a new order.
        items format: [{'name': 'item_name', 'quantity': 1}, ...]
        """
        order_items = []
        
        # Process each item in the order
        for item in items:
            item_name = item['name']
            quantity = item['quantity']
            
            # Check if it's a combo meal
            if item_name in self.combo_meals:
                combo = self.combo_meals[item_name]
                order_items.append(OrderItem(item_name, quantity, combo.price))
                
                # Check inventory for each component
                for component, comp_quantity in combo.items.items():
                    if component not in self.inventory:
                        raise ValueError(f"Component '{component}' not in inventory")
                    if self.inventory[component].quantity < comp_quantity * quantity:
                        raise ValueError(f"Not enough '{component}' in inventory for this order")
                    
                    # Reserve the components
                    self.inventory[component].quantity -= comp_quantity * quantity
            else:
                # Regular menu item
                if item_name not in self.inventory:
                    raise ValueError(f"Item '{item_name}' not in inventory")
                if self.inventory[item_name].quantity < quantity:
                    raise ValueError(f"Not enough '{item_name}' in inventory")
                
                # Assume price is 1.0 for simplicity (should be from menu in real app)
                order_items.append(OrderItem(item_name, quantity, 1.0))
                self.inventory[item_name].quantity -= quantity
        
        # Create the order
        is_delivery = delivery_address is not None
        order = Order(self.next_order_id, customer_name, order_items, delivery_address, is_delivery)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        self.save_data()
        
        return order

    def cancel_order(self, order_id: int):
        """Cancel an order and return items to inventory."""
        if order_id not in self.orders:
            raise ValueError(f"Order {order_id} not found")
        
        order = self.orders[order_id]
        
        # Return items to inventory
        for item in order.items:
            if item.name in self.combo_meals:
                # Return components of combo meal
