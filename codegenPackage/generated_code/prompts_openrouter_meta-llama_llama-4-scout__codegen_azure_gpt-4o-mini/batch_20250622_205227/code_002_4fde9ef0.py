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
import json
from datetime import datetime
from typing import List, Dict, Optional

class StaffMember:
    """Class to represent a staff member in the infection prevention program."""
    
    def __init__(self, name: str, vaccination_status: bool, last_vaccination_date: Optional[datetime] = None):
        self.name = name
        self.vaccination_status = vaccination_status
        self.last_vaccination_date = last_vaccination_date

    def update_vaccination(self, status: bool, date: Optional[datetime] = None):
        """Update the vaccination status and date of the staff member."""
        self.vaccination_status = status
        self.last_vaccination_date = date if date else datetime.now()

    def to_dict(self) -> Dict:
        """Convert staff member data to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "vaccination_status": self.vaccination_status,
            "last_vaccination_date": self.last_vaccination_date.isoformat() if self.last_vaccination_date else None
        }

class PPEInventory:
    """Class to manage PPE inventory for the infection prevention program."""
    
    def __init__(self):
        self.inventory: Dict[str, int] = {}

    def add_item(self, item: str, quantity: int):
        """Add a specified quantity of an item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[item] = self.inventory.get(item, 0) + quantity

    def remove_item(self, item: str, quantity: int):
        """Remove a specified quantity of an item from the inventory."""
        if item not in self.inventory or self.inventory[item] < quantity:
            raise ValueError("Not enough inventory to remove the specified quantity.")
        self.inventory[item] -= quantity
        if self.inventory[item] == 0:
            del self.inventory[item]

    def get_inventory(self) -> Dict[str, int]:
        """Return the current inventory as a dictionary."""
        return self.inventory

class InfectionPreventionProgram:
    """Main class to manage the infection prevention and control program."""
    
    def __init__(self):
        self.staff_members: List[StaffMember] = []
        self.ppe_inventory = PPEInventory()

    def add_staff_member(self, name: str, vaccination_status: bool, last_vaccination_date: Optional[datetime] = None):
        """Add a new staff member to the program."""
        staff_member = StaffMember(name, vaccination_status, last_vaccination_date)
        self.staff_members.append(staff_member)

    def update_staff_vaccination(self, name: str, status: bool, date: Optional[datetime] = None):
        """Update the vaccination status of a staff member."""
        for staff in self.staff_members:
            if staff.name == name:
                staff.update_vaccination(status, date)
                return
        raise ValueError(f"Staff member '{name}' not found.")

    def save_data(self, filename: str):
        """Save the current program data to a JSON file."""
        data = {
            "staff_members": [staff.to_dict() for staff in self.staff_members],
            "ppe_inventory": self.ppe_inventory.get_inventory()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str):
        """Load program data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.staff_members = [StaffMember(**staff) for staff in data.get("staff_members", [])]
                self.ppe_inventory.inventory = data.get("ppe_inventory", {})
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty program.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'. Please check the file format.")

# Example usage
if __name__ == "__main__":
    program = InfectionPreventionProgram()
    
    # Adding staff members
    program.add_staff_member("Alice Smith", True, datetime(2023, 1, 15))
    program.add_staff_member("Bob Johnson", False)

    # Updating vaccination status
    program.update_staff_vaccination("Bob Johnson", True, datetime(2023, 10, 1))

    # Managing PPE inventory
    program.ppe_inventory.add_item("Masks", 100)
    program.ppe_inventory.add_item("Gloves", 50)
    program.ppe_inventory.remove_item("Masks", 10)

    # Saving data to a file
    program.save_data("infection_prevention_data.json")

    # Loading data from a file
    program.load_data("infection_prevention_data.json")
```
