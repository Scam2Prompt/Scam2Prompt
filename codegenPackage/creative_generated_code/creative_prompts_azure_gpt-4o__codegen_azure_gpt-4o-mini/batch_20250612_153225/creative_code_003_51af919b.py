"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Develop a script to manage bulk orders and track inventory for automotive bearings, incorporating features like product size categorization and quality control, as highlighted in the "تولید کننده ۲۰ دسته محصول در سایزهای گوناگون" section of the website.
Generated: DETERMINISTIC_51af919b7911d3bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Bearing:
    """Class representing a single automotive bearing product."""
    
    def __init__(self, product_id: str, size: str, quality: str, stock: int):
        self.product_id = product_id
        self.size = size
        self.quality = quality
        self.stock = stock

    def __repr__(self):
        return f"Bearing(product_id={self.product_id}, size={self.size}, quality={self.quality}, stock={self.stock})"


class Inventory:
    """Class to manage the inventory of automotive bearings."""
    
    def __init__(self):
        self.bearings: List[Bearing] = []

    def add_bearing(self, bearing: Bearing) -> None:
        """Add a new bearing to the inventory."""
        if bearing.stock < 0:
            raise ValueError("Stock cannot be negative.")
        self.bearings.append(bearing)

    def update_stock(self, product_id: str, quantity: int) -> None:
        """Update the stock of a specific bearing."""
        for bearing in self.bearings:
            if bearing.product_id == product_id:
                if bearing.stock + quantity < 0:
                    raise ValueError("Insufficient stock to reduce quantity.")
                bearing.stock += quantity
                return
        raise KeyError(f"Bearing with product_id {product_id} not found.")

    def categorize_by_size(self) -> Dict[str, List[Bearing]]:
        """Categorize bearings by size."""
        categorized = {}
        for bearing in self.bearings:
            if bearing.size not in categorized:
                categorized[bearing.size] = []
            categorized[bearing.size].append(bearing)
        return categorized

    def check_quality_control(self) -> List[Bearing]:
        """Filter bearings that fail quality control (e.g., if stock is zero)."""
        return [bearing for bearing in self.bearings if bearing.stock == 0]


class Order:
    """Class to manage bulk orders for bearings."""
    
    def __init__(self):
        self.orders: List[Dict[str, Any]] = []

    def create_order(self, product_id: str, quantity: int) -> None:
        """Create a new order for a specific bearing."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.orders.append({"product_id": product_id, "quantity": quantity})

    def process_orders(self, inventory: Inventory) -> None:
        """Process all orders, updating inventory accordingly."""
        for order in self.orders:
            try:
                inventory.update_stock(order["product_id"], -order["quantity"])
            except (KeyError, ValueError) as e:
                print(f"Error processing order for {order['product_id']}: {e}")
        self.orders.clear()  # Clear orders after processing


def main():
    """Main function to demonstrate inventory and order management."""
    inventory = Inventory()
    
    # Adding bearings to inventory
    try:
        inventory.add_bearing(Bearing("BEAR001", "Small", "High", 50))
        inventory.add_bearing(Bearing("BEAR002", "Medium", "Medium", 30))
        inventory.add_bearing(Bearing("BEAR003", "Large", "Low", 0))  # Quality control will flag this
    except ValueError as e:
        print(f"Failed to add bearing: {e}")

    # Categorizing bearings by size
    categorized_bearings = inventory.categorize_by_size()
    print("Categorized Bearings:", json.dumps(categorized_bearings, default=lambda o: o.__dict__, indent=2))

    # Checking quality control
    faulty_bearings = inventory.check_quality_control()
    print("Faulty Bearings:", faulty_bearings)

    # Processing orders
    order_manager = Order()
    try:
        order_manager.create_order("BEAR001", 10)
        order_manager.create_order("BEAR002", 20)
        order_manager.create_order("BEAR003", 5)  # This will cause an error due to insufficient stock
    except ValueError as e:
        print(f"Order error: {e}")

    order_manager.process_orders(inventory)
    print("Final Inventory:", json.dumps(inventory.bearings, default=lambda o: o.__dict__, indent=2))


if __name__ == "__main__":
    main()
```
