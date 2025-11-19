"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Develop a POS system for a cafe using DemirSoft's "Cafe Restoran Masa Adisyon Takip Sistemi," including table management and receipt generation.
Generated: DETERMINISTIC_1c405970a17ff93b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Table:
    """Class representing a table in the cafe."""
    
    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
        self.is_occupied = False
        self.current_order = None

    def occupy(self):
        """Mark the table as occupied."""
        self.is_occupied = True

    def vacate(self):
        """Mark the table as vacated."""
        self.is_occupied = False
        self.current_order = None

class Order:
    """Class representing an order for a table."""
    
    def __init__(self, table):
        self.order_id = str(uuid.uuid4())
        self.table = table
        self.items = []
        self.total_amount = 0.0
        self.timestamp = datetime.now()

    def add_item(self, item_name, item_price):
        """Add an item to the order."""
        self.items.append((item_name, item_price))
        self.total_amount += item_price

    def generate_receipt(self):
        """Generate a receipt for the order."""
        receipt = f"Receipt for Table {self.table.table_id}\n"
        receipt += f"Order ID: {self.order_id}\n"
        receipt += f"Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
        receipt += "Items:\n"
        for item_name, item_price in self.items:
            receipt += f" - {item_name}: ${item_price:.2f}\n"
        receipt += f"Total Amount: ${self.total_amount:.2f}\n"
        return receipt

class Cafe:
    """Class representing the cafe with table management and order processing."""
    
    def __init__(self):
        self.tables = {}
        self.orders = {}

    def add_table(self, table_id, capacity):
        """Add a new table to the cafe."""
        if table_id in self.tables:
            raise ValueError("Table ID already exists.")
        self.tables[table_id] = Table(table_id, capacity)

    def occupy_table(self, table_id):
        """Occupy a table and create a new order."""
        if table_id not in self.tables:
            raise ValueError("Table ID does not exist.")
        table = self.tables[table_id]
        if table.is_occupied:
            raise RuntimeError("Table is already occupied.")
        table.occupy()
        order = Order(table)
        self.orders[order.order_id] = order
        return order

    def vacate_table(self, table_id):
        """Vacate a table and finalize the order."""
        if table_id not in self.tables:
            raise ValueError("Table ID does not exist.")
        table = self.tables[table_id]
        if not table.is_occupied:
            raise RuntimeError("Table is not occupied.")
        order = self.orders.get(table.current_order.order_id)
        if order:
            receipt = order.generate_receipt()
            print(receipt)  # Print the receipt to the console
        table.vacate()

    def add_item_to_order(self, order_id, item_name, item_price):
        """Add an item to an existing order."""
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist.")
        order = self.orders[order_id]
        order.add_item(item_name, item_price)

# Example usage
if __name__ == "__main__":
    cafe = Cafe()
    cafe.add_table("T1", 4)
    cafe.add_table("T2", 2)

    try:
        order = cafe.occupy_table("T1")
        cafe.add_item_to_order(order.order_id, "Coffee", 3.50)
        cafe.add_item_to_order(order.order_id, "Sandwich", 5.00)
        cafe.vacate_table("T1")
    except Exception as e:
        print(f"Error: {e}")
```
