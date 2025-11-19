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
import datetime
import json
import os
from enum import Enum
from typing import Dict, List, Optional


class VaccinationStatus(Enum):
    """Enum representing vaccination status options."""
    NOT_VACCINATED = "Not Vaccinated"
    PARTIALLY_VACCINATED = "Partially Vaccinated"
    FULLY_VACCINATED = "Fully Vaccinated"


class PPEItemType(Enum):
    """Enum representing types of PPE items."""
    MASK = "Mask"
    GLOVES = "Gloves"
    GOWN = "Gown"
    FACE_SHIELD = "Face Shield"
    GOGGLES = "Goggles"


class StaffMember:
    """Class representing a staff member with vaccination tracking."""
    
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.employee_id = employee_id
        self.vaccination_records: List[Dict] = []
        self.vaccination_status = VaccinationStatus.NOT_VACCINATED
    
    def add_vaccination_record(self, vaccine_name: str, date_administered: datetime.date, dose_number: int):
        """Add a vaccination record for the staff member."""
        record = {
            "vaccine_name": vaccine_name,
            "date_administered": date_administered.isoformat(),
            "dose_number": dose_number
        }
        self.vaccination_records.append(record)
        self._update_vaccination_status()
    
    def _update_vaccination_status(self):
        """Update vaccination status based on records."""
        doses = [r["dose_number"] for r in self.vaccination_records]
        if not doses:
            self.vaccination_status = VaccinationStatus.NOT_VACCINATED
        elif max(doses) >= 2:
            self.vaccination_status = VaccinationStatus.FULLY_VACCINATED
        else:
            self.vaccination_status = VaccinationStatus.PARTIALLY_VACCINATED
    
    def to_dict(self) -> Dict:
        """Convert staff member data to dictionary for serialization."""
        return {
            "name": self.name,
            "employee_id": self.employee_id,
            "vaccination_records": self.vaccination_records,
            "vaccination_status": self.vaccination_status.value
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'StaffMember':
        """Create StaffMember from dictionary."""
        staff = cls(data["name"], data["employee_id"])
        staff.vaccination_records = data["vaccination_records"]
        staff.vaccination_status = VaccinationStatus(data["vaccination_status"])
        return staff


class PPEInventory:
    """Class representing PPE inventory management."""
    
    def __init__(self):
        self.inventory: Dict[PPEItemType, Dict] = {
            item_type: {"quantity": 0, "threshold": 10} 
            for item_type in PPEItemType
        }
    
    def add_item(self, item_type: PPEItemType, quantity: int):
        """Add items to inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.inventory[item_type]["quantity"] += quantity
    
    def use_item(self, item_type: PPEItemType, quantity: int):
        """Use items from inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.inventory[item_type]["quantity"] < quantity:
            raise ValueError("Insufficient inventory")
        self.inventory[item_type]["quantity"] -= quantity
    
    def check_low_stock(self) -> List[PPEItemType]:
        """Check for items below threshold."""
        return [
            item_type 
            for item_type, data in self.inventory.items() 
            if data["quantity"] < data["threshold"]
        ]
    
    def set_threshold(self, item_type: PPEItemType, threshold: int):
        """Set threshold for low stock alert."""
        if threshold < 0:
            raise ValueError("Threshold cannot be negative")
        self.inventory[item_type]["threshold"] = threshold
    
    def to_dict(self) -> Dict:
        """Convert inventory data to dictionary for serialization."""
        return {
            item_type.value: {
                "quantity": data["quantity"],
                "threshold": data["threshold"]
            }
            for item_type, data in self.inventory.items()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PPEInventory':
        """Create PPEInventory from dictionary."""
        inventory = cls()
        for item_type_str, item_data in data.items():
            item_type = PPEItemType(item_type_str)
            inventory.inventory[item_type] = {
                "quantity": item_data["quantity"],
                "threshold": item_data["threshold"]
            }
        return inventory


class InfectionControlProgram:
    """Main class for infection prevention and control program."""
    
    def __init__(self):
        self.staff_members: Dict[str, StaffMember] = {}
        self.ppe_inventory = PPEInventory()
        self.data_file = "infection_control_data.json"
    
    def add_staff_member(self, name: str, employee_id: str):
        """Add a new staff member."""
        if employee_id in self.staff_members:
            raise ValueError("Employee ID already exists")
        self.staff_members[employee_id] = StaffMember(name, employee_id)
    
    def record_vaccination(self, employee_id: str, vaccine_name: str, date_administered: datetime.date, dose_number: int):
        """Record a vaccination for a staff member."""
        if employee_id not in self.staff_members:
            raise ValueError("Employee ID not found")
        self.staff_members[employee_id].add_vaccination_record(vaccine_name, date_administered, dose_number)
    
    def get_vaccination_status(self, employee_id: str) -> VaccinationStatus:
        """Get vaccination status of a staff member."""
        if employee_id not in self.staff_members:
            raise ValueError("Employee ID not found")
        return self.staff_members[employee_id].vaccination_status
    
    def save_data(self):
        """Save program data to file."""
        data = {
            "staff_members": {
                emp_id: staff.to_dict() 
                for emp_id, staff in self.staff_members.items()
            },
            "ppe_inventory": self.ppe_inventory.to_dict()
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load program data from file."""
        if not os.path.exists(self.data_file):
            return
        
        with open(self.data_file, "r") as f:
            data = json.load(f)
        
        self.staff_members = {
            emp_id: StaffMember.from_dict(staff_data) 
            for emp_id, staff_data in data["staff_members"].items()
        }
        self.ppe_inventory = PPEInventory.from_dict(data["ppe_inventory"])
    
    def generate_vaccination_report(self) -> Dict[str, Dict]:
        """Generate vaccination status report."""
        report = {
            "total_staff": len(self.staff_members),
            "vaccination_status": {
                status.value: 0 
                for status in VaccinationStatus
            }
        }
        
        for staff in self.staff_members.values():
            report["vaccination_status"][staff.vaccination_status.value] += 1
        
        return report
    
    def generate_inventory_report(self) -> Dict:
        """Generate inventory status report."""
        return {
            "inventory": self.ppe_inventory.to_dict(),
            "low_stock_items": [
                item.value 
                for item in self.ppe_inventory.check_low_stock()
            ]
        }


# Example usage
if __name__ == "__main__":
    program = InfectionControlProgram()
    program.load_data()
    
    # Add sample staff
    try:
        program.add_staff_member("John Doe", "EMP001")
        program.add_staff_member("Jane Smith", "EMP002")
    except ValueError as e:
        print(f"Error adding staff: {e}")
    
    # Record vaccinations
    today = datetime.date.today()
    try:
        program.record_vaccination("EMP001", "COVID-19 Vaccine", today, 1)
        program.record_vaccination("EMP002", "COVID-19 Vaccine", today, 2)
    except ValueError as e:
        print(f"Error recording vaccination: {e}")
    
    # Manage PPE inventory
    try:
        program.ppe_inventory.add_item(PPEItemType.MASK, 100)
        program.ppe_inventory.add_item(PPEItemType.GLOVES, 50)
        program.ppe_inventory.use_item(PPEItemType.MASK, 10)
    except ValueError as e:
        print(f"Error managing inventory: {e}")
    
    # Generate reports
    print("Vaccination Report:")
    print(json.dumps(program.generate_vaccination_report(), indent=2))
    
    print("\nInventory Report:")
    print(json.dumps(program.generate_inventory_report(), indent=2))
    
    # Save data
    program.save_data()
```
