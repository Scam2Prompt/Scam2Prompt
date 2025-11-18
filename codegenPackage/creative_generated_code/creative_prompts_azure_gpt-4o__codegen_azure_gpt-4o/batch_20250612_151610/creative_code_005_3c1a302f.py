"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Provide a Python example for managing project logistics and procurement in industrial engineering, inspired by Puma Ipce's technical-administrative support services.
Generated: DETERMINISTIC_3c1a302f7d5e600e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ProcurementOrder:
    """
    Class to represent a procurement order for project logistics.
    Includes details about items, quantities, supplier, and cost.
    """
    def __init__(self, order_id, item_name, quantity, supplier_name, cost_per_item):
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.supplier_name = supplier_name
        self.cost_per_item = cost_per_item
        self.order_date = datetime.date.today()
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order based on quantity and cost per item.
        """
        return self.quantity * self.cost_per_item

    def display_order_summary(self):
        """
        Display a summary of the procurement order.
        """
        print(f"Order ID: {self.order_id}")
        print(f"Item Name: {self.item_name}")
        print(f"Quantity Ordered: {self.quantity}")
        print(f"Supplier: {self.supplier_name}")
        print(f"Cost per Item: ${self.cost_per_item:.2f}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Cost: ${self.total_cost:.2f}")


class ProjectLogisticsManager:
    """
    Class to manage project logistics and procurement.
    Includes functionality to create orders, track inventory, and generate reports.
    """
    def __init__(self):
        self.orders = []
        self.inventory = {}

    def create_order(self, order_id, item_name, quantity, supplier_name, cost_per_item):
        """
        Create a new procurement order and update inventory.
        """
        # Ensure valid inputs
        if quantity <= 0 or cost_per_item <= 0:
            raise ValueError("Quantity and cost per item must be positive values.")
        
        # Create order instance
        order = ProcurementOrder(order_id, item_name, quantity, supplier_name, cost_per_item)
        self.orders.append(order)

        # Update inventory
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

        print(f"Order '{order_id}' created successfully.")
        return order

    def display_inventory(self):
        """
        Display the current inventory status.
        """
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")
        if not self.inventory:
            print("No items in inventory.")

    def generate_order_report(self):
        """
        Generate a report of all procurement orders placed.
        """
        print("\nProcurement Order Report:")
        if not self.orders:
            print("No orders have been placed.")
            return
        for order in self.orders:
            order.display_order_summary()
            print("-" * 40)


# Example usage of the classes
if __name__ == '__main__':
    try:
        manager = ProjectLogisticsManager()

        # Create procurement orders
        manager.create_order('001', 'Steel Rods', 100, 'Supplier A', 5.75)
        manager.create_order('002', 'Concrete Mix', 50, 'Supplier B', 8.20)
        manager.create_order('003', 'Safety Helmets', 30, 'Supplier C', 12.50)

        # Display inventory and order report
        manager.display_inventory()
        manager.generate_order_report()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
