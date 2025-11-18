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
# Import necessary libraries
from datetime import datetime, timedelta
from typing import List, Optional

class Equipment:
    """Class representing the interpretation equipment available for rent or sale."""
    
    def __init__(self, equipment_id: int, name: str, quantity: int, price: float):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def is_available(self, requested_quantity: int) -> bool:
        """Check if the requested quantity is available."""
        return self.quantity >= requested_quantity

    def rent_equipment(self, quantity: int):
        """Rent out a specified quantity of equipment."""
        if self.is_available(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Requested quantity exceeds available stock.")

    def return_equipment(self, quantity: int):
        """Return rented equipment, increasing available stock."""
        self.quantity += quantity

class Rental:
    """Class to handle rental transactions of equipment."""
    
    def __init__(self, equipment: Equipment, rental_days: int):
        self.equipment = equipment
        self.rental_days = rental_days
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=rental_days)
        self.total_cost = self.calculate_cost()

    def calculate_cost(self) -> float:
        """Calculate total rental cost based on rental days and equipment price."""
        return self.equipment.price * self.rental_days

class EquipmentManager:
    """Manager class to handle the inventory and transactions for equipment."""
    
    def __init__(self):
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment):
        """Add equipment to the inventory."""
        self.equipment_list.append(equipment)

    def rent_equipment(self, equipment_id: int, quantity: int, rental_days: int) -> Optional[Rental]:
        """Process a rental request for the specified equipment."""
        equipment = self.get_equipment_by_id(equipment_id)
        if equipment and equipment.is_available(quantity):
            equipment.rent_equipment(quantity)
            return Rental(equipment, rental_days)
        raise ValueError("Requested equipment is not available for rent.")

    def return_equipment(self, equipment_id: int, quantity: int):
        """Return rented equipment to inventory."""
        equipment = self.get_equipment_by_id(equipment_id)
        if equipment:
            equipment.return_equipment(quantity)
        else:
            raise ValueError("Equipment ID not found.")

    def get_equipment_by_id(self, equipment_id: int) -> Optional[Equipment]:
        """Retrieve equipment by ID."""
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment
        return None

# Example usage
if __name__ == "__main__":
    manager = EquipmentManager()
    
    # Adding equipment to the inventory
    manager.add_equipment(Equipment(1, "Wireless Headset", 10, 15.0))
    manager.add_equipment(Equipment(2, "Portable Interpreter Device", 5, 50.0))

    try:
        # Renting equipment
        rental = manager.rent_equipment(1, 2, 3)  # Rent 2 Wireless Headsets for 3 days
        print(f"Rental successful! Total cost: ${rental.total_cost:.2f}")
        
        # Returning equipment
        manager.return_equipment(1, 2)
        print("Equipment returned successfully.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
