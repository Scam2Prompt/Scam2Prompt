"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Write a program to generate invoices for bulk uniform orders, incorporating Real Garment's pricing structure and accessory options.
Generated: DETERMINISTIC_a42f354bcbf24070
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class UniformItem:
    """Represents a uniform item with its details and pricing."""
    
    def __init__(self, name: str, base_price: float, sizes: List[str], colors: List[str]):
        """
        Initialize a uniform item.
        
        Args:
            name: Name of the uniform item
            base_price: Base price per unit
            sizes: Available sizes
            colors: Available colors
        """
        self.name = name
        self.base_price = base_price
        self.sizes = sizes
        self.colors = colors

class Accessory:
    """Represents an accessory item with its details and pricing."""
    
    def __init__(self, name: str, price: float):
        """
        Initialize an accessory item.
        
        Args:
            name: Name of the accessory
            price: Price per unit
        """
        self.name = name
        self.price = price

class OrderItem:
    """Represents an item in an order with quantity and customization."""
    
    def __init__(self, item: UniformItem, quantity: int, size: str, color: str):
        """
        Initialize an order item.
        
        Args:
            item: UniformItem object
            quantity: Quantity ordered
            size: Selected size
            color: Selected color
        """
        self.item = item
        self.quantity = quantity
        self.size = size
        self.color = color
        
    def calculate_price(self) -> float:
        """Calculate total price for this order item."""
        return self.item.base_price * self.quantity

class Order:
    """Represents a complete order with items and accessories."""
    
    def __init__(self, customer_name: str, order_date: Optional[datetime] = None):
        """
        Initialize an order.
        
        Args:
            customer_name: Name of the customer
            order_date: Date of the order (defaults to current date)
        """
        self.customer_name = customer_name
        self.order_date = order_date if order_date else datetime.now()
        self.items: List[OrderItem] = []
        self.accessories: List[Accessory] = []
        
    def add_item(self, item: OrderItem) -> None:
        """Add an order item to the order."""
        self.items.append(item)
        
    def add_accessory(self, accessory: Accessory) -> None:
        """Add an accessory to the order."""
        self.accessories.append(accessory)
        
    def calculate_subtotal(self) -> float:
        """Calculate subtotal for all items and accessories."""
        items_total = sum(item.calculate_price() for item in self.items)
        accessories_total = sum(accessory.price for accessory in self.accessories)
        return items_total + accessories_total
        
    def calculate_total(self, tax_rate: float = 0.08) -> float:
        """Calculate total with tax."""
        subtotal = self.calculate_subtotal()
        return subtotal * (1 + tax_rate)

class InvoiceGenerator:
    """Generates invoices for uniform orders."""
    
    def __init__(self):
        """Initialize with default uniform items and accessories."""
        self.uniform_items = [
            UniformItem("Polo Shirt", 15.99, ["S", "M", "L", "XL"], ["Red", "Blue", "Black"]),
            UniformItem("T-Shirt", 12.99, ["S", "M", "L", "XL"], ["White", "Black", "Gray"]),
            UniformItem("Jacket", 45.99, ["S", "M", "L", "XL", "XXL"], ["Black", "Navy", "Gray"])
        ]
        
        self.accessories = [
            Accessory("Logo Embroidery", 5.99),
            Accessory("Name Tag", 3.50),
            Accessory("Custom Packaging", 2.00)
        ]
    
    def generate_invoice(self, order: Order, filename: str) -> None:
        """
        Generate an invoice CSV file for the order.
        
        Args:
            order: Order object
            filename: Output filename
        """
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header
                writer.writerow(["Real Garment - Bulk Uniform Order Invoice"])
                writer.writerow([])
                writer.writerow(["Customer:", order.customer_name])
                writer.writerow(["Order Date:", order.order_date.strftime("%Y-%m-%d")])
                writer.writerow([])
                
                # Write items header
                writer.writerow(["Item", "Size", "Color", "Quantity", "Unit Price", "Total"])
                
                # Write items
                for item in order.items:
                    writer.writerow([
                        item.item.name,
                        item.size,
                        item.color,
                        item.quantity,
                        f"${item.item.base_price:.2f}",
                        f"${item.calculate_price():.2f}"
                    ])
                
                # Write accessories if any
                if order.accessories:
                    writer.writerow([])
                    writer.writerow(["Accessories", "", "", "", "Price", ""])
                    for accessory in order.accessories:
                        writer.writerow([
                            accessory.name,
                            "", "", "",
                            f"${accessory.price:.2f}",
                            ""
                        ])
                
                # Write totals
                writer.writerow([])
                writer.writerow(["Subtotal:", "", "", "", "", f"${order.calculate_subtotal():.2f}"])
                writer.writerow(["Tax (8%):", "", "", "", "", f"${order.calculate_subtotal() * 0.08:.2f}"])
                writer.writerow(["Total:", "", "", "", "", f"${order.calculate_total():.2f}"])
                
        except IOError as e:
            print(f"Error writing invoice file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    generator = InvoiceGenerator()
    
    # Create an order
    order = Order("ABC Corporation")
    
    # Add items to order
    polo = next(item for item in generator.uniform_items if item.name == "Polo Shirt")
    order.add_item(OrderItem(polo, 10, "M", "Blue"))
    
    jacket = next(item for item in generator.uniform_items if item.name == "Jacket")
    order.add_item(OrderItem(jacket, 5, "L", "Black"))
    
    # Add accessories
    embroidery = next(acc for acc in generator.accessories if acc.name == "Logo Embroidery")
    order.add_accessory(embroidery)
    
    # Generate invoice
    generator.generate_invoice(order, "abc_corporation_invoice.csv")
```
