"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Write a Python script to manage a tire and wheel inventory for a company like Poutakidis, including tracking services such as tire changes, balancing, and repairs.
Generated: DETERMINISTIC_ed8b104deaad3bba
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

class InventoryItem:
    """
    Represents an item in the inventory.
    """
    def __init__(self, item_id, name, quantity, price_per_unit):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount):
        """
        Updates the quantity of the item.
        :param amount: Positive to add, negative to subtract.
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price_per_unit:.2f}"


class ServiceRecord:
    """
    Represents a record of a service performed.
    """
    def __init__(self, service_id, customer_name, service_type, date, cost):
        self.service_id = service_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.date = date
        self.cost = cost

    def __str__(self):
        return f"Service ID: {self.service_id}, Customer: {self.customer_name}, Type: {self.service_type}, Date: {self.date}, Cost: ${self.cost:.2f}"


class TireAndWheelInventoryManager:
    """
    Manages the inventory and services for a tire and wheel company.
    """
    def __init__(self):
        self.inventory = {}
        self.service_records = []

    def add_inventory_item(self, item_id, name, quantity, price_per_unit):
        """
        Adds a new item to the inventory.
        """
        if item_id in self.inventory:
            raise ValueError("Item ID already exists in inventory.")
        self.inventory[item_id] = InventoryItem(item_id, name, quantity, price_per_unit)

    def update_inventory_item(self, item_id, quantity_change):
        """
        Updates the quantity of an existing inventory item.
        """
        if item_id not in self.inventory:
            raise ValueError("Item ID not found in inventory.")
        self.inventory[item_id].update_quantity(quantity_change)

    def list_inventory(self):
        """
        Lists all items in the inventory.
        """
        for item in self.inventory.values():
            print(item)

    def add_service_record(self, service_id, customer_name, service_type, cost):
        """
        Adds a new service record.
        """
        if any(record.service_id == service_id for record in self.service_records):
            raise ValueError("Service ID already exists.")
        service_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.service_records.append(ServiceRecord(service_id, customer_name, service_type, service_date, cost))

    def list_service_records(self):
        """
        Lists all service records.
        """
        for record in self.service_records:
            print(record)


# Example usage
if __name__ == "__main__":
    manager = TireAndWheelInventoryManager()

    # Adding inventory items
    manager.add_inventory_item("T001", "All-Season Tire", 50, 120.00)
    manager.add_inventory_item("W001", "Alloy Wheel", 20, 250.00)

    # Updating inventory
    manager.update_inventory_item("T001", -5)  # Selling 5 tires
    manager.update_inventory_item("W001", 10)  # Adding 10 wheels

    # Listing inventory
    print("Inventory:")
    manager.list_inventory()

    # Adding service records
    manager.add_service_record("S001", "John Doe", "Tire Change", 50.00)
    manager.add_service_record("S002", "Jane Smith", "Wheel Balancing", 75.00)

    # Listing service records
    print("\nService Records:")
    manager.list_service_records()
```
