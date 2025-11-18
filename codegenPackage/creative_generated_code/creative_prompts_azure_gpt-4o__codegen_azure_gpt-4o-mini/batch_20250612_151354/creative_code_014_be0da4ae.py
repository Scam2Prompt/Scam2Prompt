"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Develop a feature for tracking repairs and inventory management of loaned equipment, inspired by CRM.f's equipment management capabilities.
Generated: DETERMINISTIC_be0da4aeee991afd
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional, Dict

class Equipment:
    """Class to represent equipment and track its status."""
    
    def __init__(self, equipment_id: str, name: str, description: str):
        """
        Initialize the equipment with an ID, name, and description.
        
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
        self.repair_history: List[Dict[str, str]] = []

    def loan_equipment(self, borrower: str):
        """Loan the equipment to a borrower."""
        if self.is_loaned:
            raise Exception(f"Equipment '{self.name}' is already loaned out.")
        
        self.is_loaned = True
        self.loaned_to = borrower
        self.loan_date = datetime.datetime.now()
        print(f"Equipment '{self.name}' loaned to {borrower} on {self.loan_date}.")

    def return_equipment(self):
        """Return the loaned equipment."""
        if not self.is_loaned:
            raise Exception(f"Equipment '{self.name}' is not currently loaned out.")
        
        self.is_loaned = False
        borrower = self.loaned_to
        self.loaned_to = None
        self.loan_date = None
        print(f"Equipment '{self.name}' returned from {borrower}.")

    def record_repair(self, repair_description: str):
        """Record a repair made to the equipment."""
        repair_entry = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": repair_description
        }
        self.repair_history.append(repair_entry)
        print(f"Repair recorded for '{self.name}': {repair_description}")

    def get_repair_history(self) -> List[Dict[str, str]]:
        """Get the repair history of the equipment."""
        return self.repair_history

class Inventory:
    """Class to manage the inventory of equipment."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment):
        """Add new equipment to the inventory."""
        self.equipment_list.append(equipment)
        print(f"Added equipment '{equipment.name}' to inventory.")

    def find_equipment(self, equipment_id: str) -> Optional[Equipment]:
        """Find equipment by its ID."""
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment
        print(f"Equipment with ID '{equipment_id}' not found.")
        return None

    def loan_equipment(self, equipment_id: str, borrower: str):
        """Loan equipment to a borrower."""
        equipment = self.find_equipment(equipment_id)
        if equipment:
            try:
                equipment.loan_equipment(borrower)
            except Exception as e:
                print(e)

    def return_equipment(self, equipment_id: str):
        """Return loaned equipment."""
        equipment = self.find_equipment(equipment_id)
        if equipment:
            try:
                equipment.return_equipment()
            except Exception as e:
                print(e)

    def record_repair(self, equipment_id: str, repair_description: str):
        """Record a repair for specific equipment."""
        equipment = self.find_equipment(equipment_id)
        if equipment:
            equipment.record_repair(repair_description)

    def get_equipment_report(self) -> None:
        """Print a summary report of current inventory and loan status."""
        for equipment in self.equipment_list:
            status = "Loaned" if equipment.is_loaned else "Available"
            print(f"ID: {equipment.equipment_id}, Name: {equipment.name}, Status: {status}")

# Example usage:
if __name__ == "__main__":
    inventory = Inventory()
    
    # Creating equipment instances
    equipment1 = Equipment("001", "Laptop", "Dell XPS 15")
    equipment2 = Equipment("002", "Projector", "Epson PowerLite")

    # Adding equipment to inventory
    inventory.add_equipment(equipment1)
    inventory.add_equipment(equipment2)

    # Loaning equipment
    inventory.loan_equipment("001", "John Doe")

    # Returning equipment
    inventory.return_equipment("001")

    # Recording a repair
    inventory.record_repair("002", "Replaced lamp.")

    # Getting equipment report
    inventory.get_equipment_report()
```
