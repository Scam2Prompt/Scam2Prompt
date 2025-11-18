"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Write a program to manage renting and selling of simultaneous interpretation equipment, incorporating features mentioned on Parrotrans's website.
Generated: DETERMINISTIC_1d058cd4e3b3a6ec
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to manage renting and selling simultaneous interpretation equipment.
Features:
- Manage equipment inventory.
- Allow renting and selling of equipment.
- Track rented and sold equipment.
- Provide error handling for invalid operations.
"""

import datetime


class Equipment:
    """
    Class representing a piece of interpretation equipment.
    """
    def __init__(self, equipment_id, name, quantity, price):
        """
        Initialize equipment with ID, name, quantity, and price.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.price = price


class RentalManagementSystem:
    """
    Class representing the rental and sales management system for equipment.
    """
    def __init__(self):
        """
        Initialize the system with an empty inventory, rented items, and sales records.
        """
        self.inventory = {}
        self.rented_items = {}
        self.sales_records = []

    def add_equipment(self, equipment_id, name, quantity, price):
        """
        Add new equipment to the inventory.
        """
        if equipment_id in self.inventory:
            raise ValueError("Equipment ID already exists in the inventory.")
        self.inventory[equipment_id] = Equipment(equipment_id, name, quantity, price)

    def rent_equipment(self, equipment_id, quantity, renter_name):
        """
        Rent equipment to a renter.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        
        equipment = self.inventory[equipment_id]
        if quantity > equipment.quantity:
            raise ValueError("Not enough equipment available for rent.")

        # Update inventory and rental records
        equipment.quantity -= quantity
        rental_record = {
            'equipment_id': equipment_id,
            'name': equipment.name,
            'quantity': quantity,
            'renter_name': renter_name,
            'rent_date': datetime.date.today()
        }
        self.rented_items[equipment_id] = rental_record
        print(f"Equipment '{equipment.name}' rented successfully.")

    def sell_equipment(self, equipment_id, quantity):
        """
        Sell equipment from the inventory.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        
        equipment = self.inventory[equipment_id]
        if quantity > equipment.quantity:
            raise ValueError("Not enough equipment available for sale.")

        # Update inventory and sales records
        equipment.quantity -= quantity
        sales_record = {
            'equipment_id': equipment_id,
            'name': equipment.name,
            'quantity': quantity,
            'sale_date': datetime.date.today(),
            'total_price': quantity * equipment.price
        }
        self.sales_records.append(sales_record)
        print(f"Equipment '{equipment.name}' sold successfully.")

    def display_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for equipment in self.inventory.values():
            print(f"ID: {equipment.equipment_id}, Name: {equipment.name}, Quantity: {equipment.quantity}, Price: ${equipment.price}")

    def display_rented_items(self):
        """
        Display the current rented items.
        """
        print("Rented Items:")
        for rental in self.rented_items.values():
            print(rental)

    def display_sales_records(self):
        """
        Display the sales records.
        """
        print("Sales Records:")
        for sale in self.sales_records:
            print(sale)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rental management system
        rms = RentalManagementSystem()

        # Add equipment to inventory
        rms.add_equipment(equipment_id=1, name="Headset", quantity=50, price=75)
        rms.add_equipment(equipment_id=2, name="Microphone", quantity=30, price=120)
        rms.add_equipment(equipment_id=3, name="Receiver", quantity=100, price=50)

        # Display inventory
        rms.display_inventory()

        # Rent equipment
        rms.rent_equipment(equipment_id=1, quantity=5, renter_name="John Doe")
        rms.display_rented_items()

        # Sell equipment
        rms.sell_equipment(equipment_id=2, quantity=10)
        rms.display_sales_records()

        # Display inventory after updates
        rms.display_inventory()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
