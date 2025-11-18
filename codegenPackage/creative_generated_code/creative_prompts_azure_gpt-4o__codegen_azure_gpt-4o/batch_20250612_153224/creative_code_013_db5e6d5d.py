"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write a function to manage inventory for schools, including stock tracking and purchase records, inspired by Him Saral's Inventory module.
Generated: DETERMINISTIC_db5e6d5d66b30156
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InventoryManager:
    """
    A class to manage inventory for schools, including stock tracking and purchase records.
    """

    def __init__(self):
        # Initialize empty inventory and purchase records
        self.inventory = {}
        self.purchase_records = []

    def add_item(self, item_name, quantity, price_per_unit):
        """
        Add a new item or update the quantity of an existing item in the inventory.

        :param item_name: Name of the item.
        :param quantity: Quantity to add to inventory.
        :param price_per_unit: Price per unit of the item.
        """
        if quantity <= 0 or price_per_unit <= 0:
            raise ValueError("Quantity and price per unit must be positive numbers.")
        
        if item_name in self.inventory:
            # Update existing item quantity
            self.inventory[item_name]['quantity'] += quantity
        else:
            # Add new item to inventory
            self.inventory[item_name] = {
                'quantity': quantity,
                'price_per_unit': price_per_unit
            }

    def remove_item(self, item_name, quantity):
        """
        Remove items from inventory.

        :param item_name: Name of the item to remove.
        :param quantity: Quantity to remove from inventory.
        """
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        
        if quantity <= 0:
            raise ValueError("Quantity to remove must be a positive number.")
        
        if self.inventory[item_name]['quantity'] < quantity:
            raise ValueError("Insufficient stock to remove the requested quantity.")
        
        # Reduce the quantity of the item
        self.inventory[item_name]['quantity'] -= quantity

        # If the quantity becomes zero, remove the item from inventory
        if self.inventory[item_name]['quantity'] == 0:
            del self.inventory[item_name]

    def record_purchase(self, item_name, quantity, buyer_name):
        """
        Record the purchase of an item.

        :param item_name: Name of the item purchased.
        :param quantity: Quantity purchased.
        :param buyer_name: Name of the person or organization purchasing the item.
        """
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        
        if quantity <= 0:
            raise ValueError("Quantity purchased must be a positive number.")
        
        if self.inventory[item_name]['quantity'] < quantity:
            raise ValueError("Insufficient stock to complete the purchase.")
        
        # Reduce the quantity of the item in inventory
        self.remove_item(item_name, quantity)

        # Record the purchase
        purchase_record = {
            'item_name': item_name,
            'quantity': quantity,
            'buyer_name': buyer_name,
            'purchase_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'price_per_unit': self.inventory[item_name]['price_per_unit'] if item_name in self.inventory else None,
            'total_price': quantity * self.inventory[item_name]['price_per_unit']
        }
        self.purchase_records.append(purchase_record)

    def view_inventory(self):
        """
        View the current inventory.

        :return: Dictionary representing the current inventory.
        """
        return self.inventory

    def view_purchase_records(self):
        """
        View all purchase records.

        :return: List of dictionaries representing purchase records.
        """
        return self.purchase_records


# Example usage:
if __name__ == "__main__":
    try:
        inventory_manager = InventoryManager()

        # Adding items to inventory
        inventory_manager.add_item("Notebooks", 100, 2.5)
        inventory_manager.add_item("Pens", 50, 1.2)

        # Viewing inventory
        print("Current Inventory:")
        print(inventory_manager.view_inventory())

        # Recording a purchase
        inventory_manager.record_purchase("Notebooks", 10, "Student A")

        # Viewing purchase records
        print("\nPurchase Records:")
        print(inventory_manager.view_purchase_records())

        # Viewing updated inventory
        print("\nUpdated Inventory:")
        print(inventory_manager.view_inventory())

    except Exception as e:
        print(f"Error: {e}")
```
