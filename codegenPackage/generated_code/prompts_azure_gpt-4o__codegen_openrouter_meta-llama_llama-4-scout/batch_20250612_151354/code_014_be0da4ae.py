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
# equipment_tracker.py

from datetime import datetime, timedelta
from typing import Dict, List

class Equipment:
    def __init__(self, id: int, name: str, description: str, status: str = "available"):
        """
        Initialize an Equipment object.

        Args:
        id (int): Unique identifier for the equipment.
        name (str): Name of the equipment.
        description (str): Description of the equipment.
        status (str): Status of the equipment (default: "available").
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.loaned_to = None
        self.loan_date = None
        self.due_date = None

    def loan(self, to: str, due_date: datetime):
        """
        Loan the equipment to someone.

        Args:
        to (str): Person or organization the equipment is loaned to.
        due_date (datetime): Date the equipment is due back.
        """
        if self.status != "available":
            raise ValueError("Equipment is not available for loan")

        self.status = "loaned"
        self.loaned_to = to
        self.loan_date = datetime.now()
        self.due_date = due_date

    def return_equipment(self):
        """
        Return the equipment from loan.
        """
        if self.status != "loaned":
            raise ValueError("Equipment is not on loan")

        self.status = "available"
        self.loaned_to = None
        self.loan_date = None
        self.due_date = None

    def __str__(self):
        return f"Equipment {self.id}: {self.name} - {self.status}"


class Repair:
    def __init__(self, id: int, equipment: Equipment, description: str, status: str = "open"):
        """
        Initialize a Repair object.

        Args:
        id (int): Unique identifier for the repair.
        equipment (Equipment): Equipment being repaired.
        description (str): Description of the repair.
        status (str): Status of the repair (default: "open").
        """
        self.id = id
        self.equipment = equipment
        self.description = description
        self.status = status

    def update_status(self, status: str):
        """
        Update the status of the repair.

        Args:
        status (str): New status of the repair.
        """
        self.status = status

    def __str__(self):
        return f"Repair {self.id}: {self.equipment.name} - {self.status}"


class EquipmentTracker:
    def __init__(self):
        """
        Initialize an EquipmentTracker object.
        """
        self.equipment: Dict[int, Equipment] = {}
        self.repairs: Dict[int, Repair] = {}
        self.equipment_id_counter = 1
        self.repair_id_counter = 1

    def add_equipment(self, name: str, description: str) -> Equipment:
        """
        Add new equipment to the tracker.

        Args:
        name (str): Name of the equipment.
        description (str): Description of the equipment.

        Returns:
        Equipment: The added equipment.
        """
        equipment = Equipment(self.equipment_id_counter, name, description)
        self.equipment[self.equipment_id_counter] = equipment
        self.equipment_id_counter += 1
        return equipment

    def get_equipment(self, id: int) -> Equipment:
        """
        Get equipment by ID.

        Args:
        id (int): ID of the equipment.

        Returns:
        Equipment: The equipment with the given ID.

        Raises:
        ValueError: If equipment with the given ID does not exist.
        """
        try:
            return self.equipment[id]
        except KeyError:
            raise ValueError("Equipment not found")

    def add_repair(self, equipment: Equipment, description: str) -> Repair:
        """
        Add a new repair to the tracker.

        Args:
        equipment (Equipment): Equipment being repaired.
        description (str): Description of the repair.

        Returns:
        Repair: The added repair.
        """
        repair = Repair(self.repair_id_counter, equipment, description)
        self.repairs[self.repair_id_counter] = repair
        self.repair_id_counter += 1
        return repair

    def get_repair(self, id: int) -> Repair:
        """
        Get a repair by ID.

        Args:
        id (int): ID of the repair.

        Returns:
        Repair: The repair with the given ID.

        Raises:
        ValueError: If repair with the given ID does not exist.
        """
        try:
            return self.repairs[id]
        except KeyError:
            raise ValueError("Repair not found")

    def list_equipment(self) -> List[Equipment]:
        """
        List all equipment.

        Returns:
        List[Equipment]: A list of all equipment.
        """
        return list(self.equipment.values())

    def list_repairs(self) -> List[Repair]:
        """
        List all repairs.

        Returns:
        List[Repair]: A list of all repairs.
        """
        return list(self.repairs.values())


def main():
    tracker = EquipmentTracker()

    # Add equipment
    equipment1 = tracker.add_equipment("Laptop", "Company laptop")
    equipment2 = tracker.add_equipment("Projector", "Company projector")

    # Loan equipment
    equipment1.loan("John Doe", datetime.now() + timedelta(days=14))

    # Add repairs
    repair1 = tracker.add_repair(equipment1, "Screen damage")
    repair2 = tracker.add_repair(equipment2, "Lamp replacement")

    # List equipment and repairs
    print("Equipment:")
    for equipment in tracker.list_equipment():
        print(equipment)

    print("\nRepairs:")
    for repair in tracker.list_repairs():
        print(repair)

    # Update repair status
    repair1.update_status("in_progress")

    # Return equipment
    equipment1.return_equipment()

if __name__ == "__main__":
    main()
```
