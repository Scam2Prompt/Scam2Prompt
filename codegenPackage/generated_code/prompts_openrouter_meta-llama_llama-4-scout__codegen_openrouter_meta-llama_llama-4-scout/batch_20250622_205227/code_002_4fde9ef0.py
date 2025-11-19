"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Generate a sample code for an infection prevention and control program like the one implemented by Shareth Homecare Services, including staff vaccination tracking and PPE inventory management."
Generated: DETERMINISTIC_4fde9ef089ed91ab
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# infection_prevention_control.py

from datetime import datetime
from typing import Dict, List

class StaffMember:
    """Represents a staff member with vaccination information."""

    def __init__(self, staff_id: int, name: str, vaccinated: bool = False, vaccination_date: datetime = None):
        """
        Initializes a StaffMember object.

        Args:
        - staff_id (int): Unique staff ID.
        - name (str): Staff member name.
        - vaccinated (bool): Vaccination status (default: False).
        - vaccination_date (datetime): Vaccination date (default: None).
        """
        self.staff_id = staff_id
        self.name = name
        self.vaccinated = vaccinated
        self.vaccination_date = vaccination_date

    def mark_as_vaccinated(self, vaccination_date: datetime):
        """Marks the staff member as vaccinated."""
        self.vaccinated = True
        self.vaccination_date = vaccination_date


class PPEItem:
    """Represents a PPE item with inventory information."""

    def __init__(self, item_id: int, name: str, quantity: int):
        """
        Initializes a PPEItem object.

        Args:
        - item_id (int): Unique item ID.
        - name (str): PPE item name.
        - quantity (int): Initial quantity.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def update_quantity(self, quantity: int):
        """Updates the PPE item quantity."""
        self.quantity = quantity


class InfectionPreventionControl:
    """Manages staff vaccination tracking and PPE inventory."""

    def __init__(self):
        self.staff_members: Dict[int, StaffMember] = {}
        self.ppe_inventory: Dict[int, PPEItem] = {}

    def add_staff_member(self, staff_id: int, name: str):
        """Adds a new staff member."""
        if staff_id not in self.staff_members:
            self.staff_members[staff_id] = StaffMember(staff_id, name)
        else:
            raise ValueError("Staff member already exists.")

    def mark_staff_as_vaccinated(self, staff_id: int, vaccination_date: datetime):
        """Marks a staff member as vaccinated."""
        if staff_id in self.staff_members:
            self.staff_members[staff_id].mark_as_vaccinated(vaccination_date)
        else:
            raise ValueError("Staff member not found.")

    def add_ppe_item(self, item_id: int, name: str, quantity: int):
        """Adds a new PPE item to the inventory."""
        if item_id not in self.ppe_inventory:
            self.ppe_inventory[item_id] = PPEItem(item_id, name, quantity)
        else:
            raise ValueError("PPE item already exists.")

    def update_ppe_quantity(self, item_id: int, quantity: int):
        """Updates the quantity of a PPE item."""
        if item_id in self.ppe_inventory:
            self.ppe_inventory[item_id].update_quantity(quantity)
        else:
            raise ValueError("PPE item not found.")

    def get_staff_vaccination_status(self) -> List[Dict]:
        """Returns a list of staff members with their vaccination status."""
        vaccination_status = []
        for staff_member in self.staff_members.values():
            vaccination_status.append({
                "staff_id": staff_member.staff_id,
                "name": staff_member.name,
                "vaccinated": staff_member.vaccinated,
                "vaccination_date": staff_member.vaccination_date
            })
        return vaccination_status

    def get_ppe_inventory(self) -> List[Dict]:
        """Returns the current PPE inventory."""
        ppe_inventory = []
        for ppe_item in self.ppe_inventory.values():
            ppe_inventory.append({
                "item_id": ppe_item.item_id,
                "name": ppe_item.name,
                "quantity": ppe_item.quantity
            })
        return ppe_inventory


def main():
    ipc = InfectionPreventionControl()

    # Add staff members
    ipc.add_staff_member(1, "John Doe")
    ipc.add_staff_member(2, "Jane Smith")

    # Mark staff members as vaccinated
    vaccination_date = datetime(2022, 1, 1)
    ipc.mark_staff_as_vaccinated(1, vaccination_date)

    # Add PPE items
    ipc.add_ppe_item(1, "Masks", 100)
    ipc.add_ppe_item(2, "Gloves", 500)

    # Update PPE quantity
    ipc.update_ppe_quantity(1, 80)

    # Get staff vaccination status
    vaccination_status = ipc.get_staff_vaccination_status()
    print("Staff Vaccination Status:")
    for status in vaccination_status:
        print(status)

    # Get PPE inventory
    ppe_inventory = ipc.get_ppe_inventory()
    print("\nPPE Inventory:")
    for item in ppe_inventory:
        print(item)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
