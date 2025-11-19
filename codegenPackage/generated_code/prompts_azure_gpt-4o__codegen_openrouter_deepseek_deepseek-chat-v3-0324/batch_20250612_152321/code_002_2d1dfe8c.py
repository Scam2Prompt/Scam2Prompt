"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate code to simulate the ordering process for stainless steel screws and bolts from APN Hardware, including product selection, quantity input, and order confirmation.
Generated: DETERMINISTIC_2d1dfe8c65d6bca5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Product:
    """Represents a product available for purchase."""
    sku: str
    name: str
    description: str
    price: float
    stock: int

@dataclass
class OrderItem:
    """Represents an item in an order."""
    product: Product
    quantity: int

@dataclass
class Order:
    """Represents a customer order."""
    order_id: str
    items: List[OrderItem]
    total: float

class APNHardwareStore:
    """Simulates the APN Hardware store ordering system."""
    
    def __init__(self):
        """Initialize the store with sample products."""
        self.products = [
            Product("SS-101", "Stainless Steel Screw (M3x10)", "M3 diameter, 10mm length", 0.15, 500),
            Product("SS-102", "Stainless Steel Screw (M4x12)", "M4 diameter, 12mm length", 0.20, 400),
            Product("SS-201", "Stainless Steel Bolt (M5x20)", "M5 diameter, 20mm length", 0.35, 300),
            Product("SS-202", "Stainless Steel Bolt (M6x25)", "M6 diameter, 25mm length", 0.45, 250),
            Product("SS-301", "Stainless Steel Nut (M3)", "M3 size", 0.10, 600),
            Product("SS-302", "Stainless Steel Nut (M4)", "M4 size", 0.12, 550)
        ]
        self.orders: Dict[str, Order] = {}
        self.next_order_id = 1000
    
    def display_products(self) -> None:
        """Display available products to the user."""
        print("\nAvailable Products:")
        print("------------------")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product.name} ({product.sku})")
            print(f"   Description: {product.description}")
            print(f"   Price: ${product.price:.2f} | Stock: {product.stock}")
            print("")
    
    def get_product_choice(self) -> Optional[Product]:
        """Get user's product selection."""
        try:
            choice = int(input("Enter product number (0 to finish): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(self.products):
                return self.products[choice - 1]
            print("Invalid product number. Please try again.")
            return self.get_product_choice()
        except ValueError:
            print("Please enter a valid number.")
            return self.get_product_choice()
    
    def get_quantity(self, product: Product) -> int:
        """Get quantity from user with stock validation."""
        try:
            quantity = int(input(f"Enter quantity for {product.name} (max {product.stock}): "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return self.get_quantity(product)
            if quantity > product.stock:
                print(f"Only {product.stock} available in stock.")
                return self.get_quantity(product)
            return quantity
        except ValueError:
            print("Please enter a valid number.")
            return self.get_quantity(product)
    
    def create_order(self) -> Order:
        """Create a new order with selected items."""
        order_items: List[OrderItem] = []
        
        print("\nAPN Hardware - Stainless Steel Screws & Bolts Ordering")
        print("-----------------------------------------------------")
        
        while True:
            self.display_products()
            product = self.get_product_choice()
            if product is None:
                break
            
            quantity = self.get_quantity(product)
            order_items.append(OrderItem(product, quantity))
            product.stock -= quantity  # Update stock
            print(f"Added {quantity} x {product.name} to your order.\n")
        
        if not order_items:
            print("No items selected. Order cancelled.")
            raise ValueError("No items in order")
        
        order_id = f"APN-{self.next_order_id}"
        self.next_order_id += 1
        
        total = sum(item.product.price * item.quantity for item in order_items)
        order = Order(order_id, order_items, total)
        self.orders[order_id] = order
        
        return order
    
    def display_order_confirmation(self, order: Order) -> None:
        """Display order confirmation to the user."""
        print("\nOrder Confirmation")
        print("------------------")
        print(f"Order ID: {order.order_id}")
        print("\nItems:")
        for item in order.items:
            print(f" - {item.quantity} x {item.product.name} @ ${item.product.price:.2f} each")
        print(f"\nTotal: ${order.total:.2f}")
        print("\nThank you for your order with APN Hardware!")
    
    def save_order_to_file(self, order: Order, filename: str = "orders.json") -> None:
        """Save order details to a JSON file."""
        order_data = {
            "order_id": order.order_id,
            "items": [
                {
                    "sku": item.product.sku,
                    "name": item.product.name,
                    "quantity": item.quantity,
                    "price": item.product.price
                } for item in order.items
            ],
            "total": order.total
        }
        
        try:
            with open(filename, "a") as f:
                json.dump(order_data, f, indent=2)
                f.write("\n")
        except IOError as e:
            print(f"Error saving order: {e}")

def main():
    """Main function to run the ordering simulation."""
    store = APNHardwareStore()
    
    try:
        print("Welcome to APN Hardware Stainless Steel Screws & Bolts Ordering System")
        order = store.create_order()
        store.display_order_confirmation(order)
        store.save_order_to_file(order)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nOrder process completed.")

if __name__ == "__main__":
    main()
```
