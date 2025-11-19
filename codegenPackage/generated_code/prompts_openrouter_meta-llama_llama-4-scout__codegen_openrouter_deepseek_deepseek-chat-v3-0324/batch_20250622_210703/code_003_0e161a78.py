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
import datetime
import json
import os
from typing import List, Dict, Optional

class MenuItem:
    """Represents a menu item with name and price."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class OrderItem:
    """Represents an item in an order with quantity."""
    def __init__(self, menu_item: MenuItem, quantity: int = 1):
        self.menu_item = menu_item
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.menu_item.price * self.quantity

class Order:
    """Represents a customer order with multiple items."""
    def __init__(self, table_number: int):
        self.table_number = table_number
        self.items: List[OrderItem] = []
        self.order_time = datetime.datetime.now()
        self.is_paid = False

    def add_item(self, menu_item: MenuItem, quantity: int = 1) -> None:
        """Add an item to the order."""
        for item in self.items:
            if item.menu_item.name == menu_item.name:
                item.quantity += quantity
                return
        self.items.append(OrderItem(menu_item, quantity))

    def remove_item(self, menu_item_name: str) -> None:
        """Remove an item from the order."""
        self.items = [item for item in self.items if item.menu_item.name != menu_item_name]

    def update_item_quantity(self, menu_item_name: str, quantity: int) -> None:
        """Update the quantity of an item in the order."""
        for item in self.items:
            if item.menu_item.name == menu_item_name:
                item.quantity = quantity
                return
        raise ValueError(f"Item {menu_item_name} not found in order")

    @property
    def total_price(self) -> float:
        """Calculate the total price of the order."""
        return sum(item.total_price for item in self.items)

    def mark_as_paid(self) -> None:
        """Mark the order as paid."""
        self.is_paid = True

class CafeSystem:
    """Main cafe management system."""
    def __init__(self):
        self.menu: Dict[str, MenuItem] = {}
        self.orders: Dict[int, Order] = {}
        self.load_menu()

    def load_menu(self) -> None:
        """Load menu from a JSON file."""
        try:
            if os.path.exists("menu.json"):
                with open("menu.json", "r") as f:
                    menu_data = json.load(f)
                    for item_name, price in menu_data.items():
                        self.menu[item_name] = MenuItem(item_name, price)
            else:
                # Default menu if file doesn't exist
                default_menu = {
                    "Coffee": 12.50,
                    "Tea": 8.00,
                    "Sandwich": 15.00,
                    "Cake": 10.00
                }
                self.menu = {name: MenuItem(name, price) for name, price in default_menu.items()}
        except Exception as e:
            print(f"Error loading menu: {e}")
            self.menu = {}

    def save_menu(self) -> None:
        """Save menu to a JSON file."""
        try:
            menu_data = {item.name: item.price for item in self.menu.values()}
            with open("menu.json", "w") as f:
                json.dump(menu_data, f, indent=4)
        except Exception as e:
            print(f"Error saving menu: {e}")

    def add_menu_item(self, name: str, price: float) -> None:
        """Add a new item to the menu."""
        if name in self.menu:
            raise ValueError("Item already exists in menu")
        self.menu[name] = MenuItem(name, price)
        self.save_menu()

    def update_menu_item(self, name: str, new_price: float) -> None:
        """Update the price of a menu item."""
        if name not in self.menu:
            raise ValueError("Item not found in menu")
        self.menu[name].price = new_price
        self.save_menu()

    def remove_menu_item(self, name: str) -> None:
        """Remove an item from the menu."""
        if name not in self.menu:
            raise ValueError("Item not found in menu")
        del self.menu[name]
        self.save_menu()

    def create_order(self, table_number: int) -> Order:
        """Create a new order for a table."""
        if table_number in self.orders and not self.orders[table_number].is_paid:
            raise ValueError(f"Table {table_number} already has an active order")
        self.orders[table_number] = Order(table_number)
        return self.orders[table_number]

    def get_order(self, table_number: int) -> Optional[Order]:
        """Get an order by table number."""
        return self.orders.get(table_number)

    def close_order(self, table_number: int) -> None:
        """Close and mark an order as paid."""
        if table_number not in self.orders:
            raise ValueError(f"No order found for table {table_number}")
        self.orders[table_number].mark_as_paid()

    def print_bill(self, table_number: int) -> str:
        """Generate a bill for the order."""
        order = self.get_order(table_number)
        if not order:
            raise ValueError(f"No order found for table {table_number}")

        bill_lines = [
            f"Bill for Table {table_number}",
            f"Time: {order.order_time.strftime('%Y-%m-%d %H:%M:%S')}",
            "---------------------------------",
        ]

        for item in order.items:
            bill_lines.append(f"{item.menu_item.name} x{item.quantity}: ${item.total_price:.2f}")

        bill_lines.extend([
            "---------------------------------",
            f"Total: ${order.total_price:.2f}",
            "Thank you for your visit!"
        ])

        return "\n".join(bill_lines)

    def print_all_bills(self) -> List[str]:
        """Generate bills for all active orders."""
        return [self.print_bill(table) for table, order in self.orders.items() if not order.is_paid]

def main():
    """Main function to demonstrate the cafe system."""
    cafe = CafeSystem()

    # Example usage
    try:
        # Create an order
        order = cafe.create_order(1)
        
        # Add items to order
        order.add_item(cafe.menu["Coffee"], 2)
        order.add_item(cafe.menu["Sandwich"])
        
        # Print the bill
        print(cafe.print_bill(1))
        
        # Close the order
        cafe.close_order(1)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
