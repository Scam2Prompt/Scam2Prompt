"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: How can I implement a logistics management system that incorporates the features of PLM's high-tech distribution centers in Costa Rica?
Generated: DETERMINISTIC_65f86a40766f6ac1
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Logistics Management System
This program simulates a logistics management system that incorporates the features of a high-tech distribution center.
It includes inventory tracking, shipment scheduling, and error handling.
"""

import sys

# Constants for the system
COSTA_RICA_CENTER = "Costa Rica Distribution Center"
MAX_INVENTORY_LIMIT = 10000
MAX_SHIPMENT_LIMIT = 500

class LogisticsManagementSystem:
    def __init__(self):
        """
        Initialize the logistics system with inventory and shipment records.
        """
        self.inventory = {}
        self.shipments = []
    
    def add_inventory(self, item, quantity):
        """
        Add items to inventory.
        :param item: str - Item name
        :param quantity: int - Quantity to add
        :raises ValueError: If the quantity exceeds the max inventory limit
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        current_total = sum(self.inventory.values()) + quantity
        if current_total > MAX_INVENTORY_LIMIT:
            raise ValueError(f"Exceeding max inventory limit of {MAX_INVENTORY_LIMIT}. Current total: {current_total}")
        
        self.inventory[item] = self.inventory.get(item, 0) + quantity
        print(f"Added {quantity} units of {item} to inventory.")

    def schedule_shipment(self, destination, items):
        """
        Schedule a shipment to a destination.
        :param destination: str - Destination of the shipment
        :param items: dict - Dictionary with item names as keys and quantities as values
        :raises ValueError: If any item is unavailable in the inventory or shipment exceeds limits
        """
        total_quantity = sum(items.values())
        if total_quantity > MAX_SHIPMENT_LIMIT:
            raise ValueError(f"Shipment exceeds max limit of {MAX_SHIPMENT_LIMIT}. Total items: {total_quantity}")

        for item, quantity in items.items():
            if item not in self.inventory or self.inventory[item] < quantity:
                raise ValueError(f"Insufficient stock for item '{item}'. Requested: {quantity}, Available: {self.inventory.get(item, 0)}")
        
        # Update inventory
        for item, quantity in items.items():
            self.inventory[item] -= quantity
        
        # Record shipment
        shipment = {
            "destination": destination,
            "items": items
        }
        self.shipments.append(shipment)
        print(f"Shipment scheduled to {destination} with items: {items}.")
    
    def display_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")
    
    def display_shipments(self):
        """
        Display the scheduled shipments.
        """
        print("Scheduled Shipments:")
        for shipment in self.shipments:
            print(f"Destination: {shipment['destination']}, Items: {shipment['items']}")

def main():
    """
    Main function to run the logistics management system.
    """
    try:
        # Initialize the system
        system = LogisticsManagementSystem()
        
        # Add inventory
        system.add_inventory("Laptop", 500)
        system.add_inventory("Phone", 300)
        
        # Display inventory
        system.display_inventory()
        
        # Schedule a shipment
        shipment_items = {"Laptop": 50, "Phone": 20}
        system.schedule_shipment("San Jose", shipment_items)
        
        # Display inventory and shipments
        system.display_inventory()
        system.display_shipments()
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Run the program
    main()
```
