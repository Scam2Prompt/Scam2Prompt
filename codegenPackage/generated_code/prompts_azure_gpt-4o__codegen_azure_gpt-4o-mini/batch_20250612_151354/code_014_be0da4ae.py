"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Develop a feature for tracking repairs and inventory management of loaned equipment, inspired by CRM.f's equipment management capabilities.
Generated: DETERMINISTIC_be0da4aeee991afd
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Equipment:
    """Class representing a piece of equipment."""
    
    def __init__(self, equipment_id: str, name: str, description: str):
        """
        Initialize an Equipment instance.

        :param equipment_id: Unique identifier for the equipment
        :param name: Name of the equipment
        :param description: Description of the equipment
        """
        self.equipment_id = equipment_id
        self.name = name
        self.description = description
        self.is_loaned = False
        self.loaned_to = None
        self.loan_date = None

    def loan(self, borrower: str):
        """Loan the equipment to a borrower."""
        if self.is_loaned:
            raise Exception(f"Equipment {self.name} is already loaned out.")
        self.is_loaned = True
        self.loaned_to = borrower
        self.loan_date = datetime.datetime.now()

    def return_equipment(self):
        """Return the loaned equipment."""
        if not self.is_loaned:
            raise Exception(f"Equipment {self.name} is not currently loaned out.")
        self.is_loaned = False
        self.loaned_to = None
        self.loan_date = None


class Repair:
    """Class representing a repair record for equipment."""
    
    def __init__(self, equipment_id: str, repair_date: datetime.datetime, description: str):
        """
        Initialize a Repair instance.

        :param equipment_id: Unique identifier for the equipment being repaired
        :param repair_date: Date when the repair was made
        :param description: Description of the repair
        """
        self.equipment_id = equipment_id
        self.repair_date = repair_date
        self.description = description


class Inventory:
    """Class for managing equipment inventory and repairs."""
    
    def __init__(self):
        """Initialize the inventory with empty lists for equipment and repairs."""
        self.equipment_list: List[Equipment] = []
        self.repair_records: List[Repair] = []

    def add_equipment(self, equipment: Equipment):
        """Add a new piece of equipment to the inventory."""
        self.equipment_list.append(equipment)

    def loan_equipment(self, equipment_id: str, borrower: str):
        """Loan equipment to a borrower."""
        equipment = self._find_equipment(equipment_id)
        equipment.loan(borrower)

    def return_equipment(self, equipment_id: str):
        """Return loaned equipment."""
        equipment = self._find_equipment(equipment_id)
        equipment.return_equipment()

    def record_repair(self, equipment_id: str, description: str):
        """Record a repair for a piece of equipment."""
        equipment = self._find_equipment(equipment_id)
        repair = Repair(equipment_id, datetime.datetime.now(), description)
        self.repair_records.append(repair)

    def _find_equipment(self, equipment_id: str) -> Equipment:
        """Find equipment by its ID.

        :param equipment_id: Unique identifier for the equipment
        :return: Equipment instance
        :raises Exception: If equipment is not found
        """
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment
        raise Exception(f"Equipment with ID {equipment_id} not found.")

    def get_loaned_equipment(self) -> List[Equipment]:
        """Get a list of currently loaned equipment."""
        return [equipment for equipment in self.equipment_list if equipment.is_loaned]

    def get_repair_history(self, equipment_id: str) -> List[Repair]:
        """Get the repair history for a specific piece of equipment.

        :param equipment_id: Unique identifier for the equipment
        :return: List of repair records
        """
        return [repair for repair in self.repair_records if repair.equipment_id == equipment_id]


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding equipment
    equipment1 = Equipment("001", "Laptop", "Dell XPS 13")
    inventory.add_equipment(equipment1)

    # Loaning equipment
    try:
        inventory.loan_equipment("001", "John Doe")
    except Exception as e:
        print(e)

    # Recording a repair
    try:
        inventory.record_repair("001", "Replaced battery")
    except Exception as e:
        print(e)

    # Returning equipment
    try:
        inventory.return_equipment("001")
    except Exception as e:
        print(e)

    # Display loaned equipment
    loaned_equipment = inventory.get_loaned_equipment()
    print(f"Loaned Equipment: {[eq.name for eq in loaned_equipment]}")
```
