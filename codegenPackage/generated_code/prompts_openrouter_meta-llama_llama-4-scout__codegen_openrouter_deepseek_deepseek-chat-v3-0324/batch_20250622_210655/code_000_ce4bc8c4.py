"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Write a Python script to manage food orders and inventory for a cloud kitchen like Perfect Food Corner, considering gluten-free and vegetarian options.
Generated: DETERMINISTIC_ce4bc8c43de46409
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum, auto
import datetime


class FoodCategory(Enum):
    VEGETARIAN = auto()
    NON_VEGETARIAN = auto()
    GLUTEN_FREE = auto()


@dataclass
class FoodItem:
    id: int
    name: str
    price: float
    category: FoodCategory
    ingredients: List[str]
    quantity_available: int = 0

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'FoodItem':
        return cls(
            id=data['id'],
            name=data['name'],
            price=data['price'],
            category=FoodCategory[data['category']],
            ingredients=data['ingredients'],
            quantity_available=data['quantity_available']
        )


@dataclass
class OrderItem:
    food_item_id: int
    quantity: int
    special_instructions: Optional[str] = None


@dataclass
class Order:
    id: int
    customer_name: str
    items: List[OrderItem]
    order_time: datetime.datetime
    status: str = "pending"

    def to_dict(self) -> Dict:
        return {
            **asdict(self),
            'order_time': self.order_time.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        return cls(
            id=data['id'],
            customer_name=data['customer_name'],
            items=[OrderItem(**item) for item in data['items']],
            order_time=datetime.datetime.fromisoformat(data['order_time']),
            status=data['status']
        )


class KitchenManager:
    def __init__(self):
        self.menu: Dict[int, FoodItem] = {}
        self.orders: Dict[int, Order] = {}
        self.next_food_id = 1
        self.next_order_id = 1

    def add_food_item(self, name: str, price: float, category: FoodCategory, 
                      ingredients: List[str], quantity: int = 0) -> FoodItem:
        """Add a new food item to the menu."""
        food_item = FoodItem(
            id=self.next_food_id,
            name=name,
            price=price,
            category=category,
            ingredients=ingredients,
            quantity_available=quantity
        )
        self.menu[self.next_food_id] = food_item
        self.next_food_id += 1
        return food_item

    def update_food_item(self, food_id: int, **kwargs) -> Optional[FoodItem]:
        """Update an existing food item."""
        if food_id not in self.menu:
            return None
        
        food_item = self.menu[food_id]
        for key, value in kwargs.items():
            if hasattr(food_item, key):
                setattr(food_item, key, value)
        return food_item

    def remove_food_item(self, food_id: int) -> bool:
        """Remove a food item from the menu."""
        if food_id in self.menu:
            del self.menu[food_id]
            return True
        return False

    def place_order(self, customer_name: str, items: List[OrderItem]) -> Optional[Order]:
        """Place a new order after checking inventory."""
        # Check if all items are available
        for item in items:
            food_item = self.menu.get(item.food_item_id)
            if not food_item:
                return None
            if food_item.quantity_available < item.quantity:
                return None

        # Deduct quantities from inventory
        for item in items:
            food_item = self.menu[item.food_item_id]
            food_item.quantity_available -= item.quantity

        # Create the order
        order = Order(
            id=self.next_order_id,
            customer_name=customer_name,
            items=items,
            order_time=datetime.datetime.now()
        )
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order

    def update_order_status(self, order_id: int, status: str) -> Optional[Order]:
        """Update the status of an existing order."""
        if order_id not in self.orders:
            return None
        self.orders[order_id].status = status
        return self.orders[order_id]

    def get_menu(self, category: Optional[FoodCategory] = None) -> List[FoodItem]:
        """Get the menu, optionally filtered by category."""
        if category:
            return [item for item in self.menu.values() if item.category == category]
        return list(self.menu.values())

    def restock_inventory(self, food_id: int, quantity: int) -> Optional[FoodItem]:
        """Add quantity to existing inventory."""
        if food_id not in self.menu:
            return None
        self.menu[food_id].quantity_available += quantity
        return self.menu[food_id]

    def save_to_file(self, filename: str) -> bool:
        """Save current state to a JSON file."""
        try:
            data = {
                'menu': {k: v.to_dict() for k, v in self.menu.items()},
                'orders': {k: v.to_dict() for k, v in self.orders.items()},
                'next_food_id': self.next_food_id,
                'next_order_id': self.next_order_id
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.menu = {
                int(k): FoodItem.from_dict(v) 
                for k, v in data.get('menu', {}).items()
            }
            self.orders = {
                int(k): Order.from_dict(v) 
                for k, v in data.get('orders', {}).items()
            }
            self.next_food_id = data.get('next_food_id', 1)
            self.next_order_id = data.get('next_order_id', 1)
            return True
        except Exception:
            return False


# Example usage
if __name__ == "__main__":
    manager = KitchenManager()
    
    # Add some food items
    manager.add_food_item(
        "Vegetable Pasta", 12.99, FoodCategory.VEGETARIAN,
        ["pasta", "vegetables", "tomato sauce"], 10
    )
    manager.add_food_item(
        "Gluten-Free Pizza", 15.99, FoodCategory.GLUTEN_FREE,
        ["gluten-free dough", "cheese", "tomatoes"], 5
    )
    manager.add_food_item(
        "Chicken Curry", 14.99, FoodCategory.NON_VEGETARIAN,
        ["chicken", "curry sauce", "spices"], 8
    )
    
    # Place an order
    order_items = [
        OrderItem(food_item_id=1, quantity=2),
        OrderItem(food_item_id=2, quantity=1, special_instructions="Extra cheese")
    ]
    order = manager.place_order("John Doe", order_items)
    
    if order:
        print(f"Order placed successfully. Order ID: {order.id}")
    else:
        print("Failed to place order. Items may be out of stock.")
    
    # Save to file
    manager.save_to_file("kitchen_data.json")
```
