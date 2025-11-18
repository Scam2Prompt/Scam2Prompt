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
import uuid
from datetime import datetime


class EquipmentManager:
    """
    A class to manage loaned equipment, track repairs, and maintain inventory.
    """

    def __init__(self):
        # Dictionary to store equipment details
        self.inventory = {}
        # List to store repair logs
        self.repairs = []

    def add_equipment(self, name: str, serial_number: str, description: str):
        """
        Add new equipment to the inventory.
        
        Args:
            name (str): Name of the equipment.
            serial_number (str): Unique serial number for identification.
            description (str): Description of the equipment.

        Returns:
            dict: Details of the added equipment.
        """
        equipment_id = str(uuid.uuid4())
        self.inventory[equipment_id] = {
            "name": name,
            "serial_number": serial_number,
            "description": description,
            "status": "Available",
            "loaned_to": None,
            "loan_date": None,
            "return_date": None,
        }
        return self.inventory[equipment_id]

    def loan_equipment(self, equipment_id: str, loaned_to: str, loan_date: datetime):
        """
        Mark equipment as loaned to a user.

        Args:
            equipment_id (str): ID of the equipment.
            loaned_to (str): Name or ID of the person loaning the equipment.
            loan_date (datetime): Date when the equipment is loaned.

        Returns:
            dict: Updated equipment details if loaned successfully.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        
        equipment = self.inventory[equipment_id]
        if equipment["status"] != "Available":
            raise ValueError("Equipment is not available for loan.")
        
        equipment["status"] = "Loaned"
        equipment["loaned_to"] = loaned_to
        equipment["loan_date"] = loan_date
        return equipment

    def return_equipment(self, equipment_id: str, return_date: datetime):
        """
        Mark equipment as returned.

        Args:
            equipment_id (str): ID of the equipment.
            return_date (datetime): Date when the equipment is returned.

        Returns:
            dict: Updated equipment details if returned successfully.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        
        equipment = self.inventory[equipment_id]
        if equipment["status"] != "Loaned":
            raise ValueError("Equipment is not currently loaned.")
        
        equipment["status"] = "Available"
        equipment["loaned_to"] = None
        equipment["loan_date"] = None
        equipment["return_date"] = return_date
        return equipment

    def log_repair(self, equipment_id: str, issue: str, repair_date: datetime, repaired_by: str):
        """
        Log a repair for a specific equipment.

        Args:
            equipment_id (str): ID of the equipment being repaired.
            issue (str): Description of the issue.
            repair_date (datetime): Date when the repair occurred.
            repaired_by (str): Name or ID of the person performing the repair.

        Returns:
            dict: Details of the logged repair.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        
        repair_record = {
            "equipment_id": equipment_id,
            "issue": issue,
            "repair_date": repair_date,
            "repaired_by": repaired_by,
        }
        self.repairs.append(repair_record)
        return repair_record

    def get_equipment_details(self, equipment_id: str):
        """
        Retrieve details of a specific equipment.

        Args:
            equipment_id (str): ID of the equipment.

        Returns:
            dict: Equipment details if found.
        """
        if equipment_id not in self.inventory:
            raise ValueError("Equipment ID not found in inventory.")
        return self.inventory[equipment_id]

    def list_inventory(self):
        """
        List all equipment in the inventory.

        Returns:
            dict: All equipment details.
        """
        return self.inventory

    def list_repairs(self):
        """
        List all repairs logged.

        Returns:
            list: All repair records.
        """
        return self.repairs


# Usage example
if __name__ == "__main__":
    # Initialize EquipmentManager
    manager = EquipmentManager()

    try:
        # Add equipment to inventory
        equipment = manager.add_equipment("Laptop", "SN123456", "Dell Latitude 5510")
        print("Added Equipment:", equipment)

        # Loan equipment
        loaned_equipment = manager.loan_equipment(
            equipment_id=list(manager.inventory.keys())[0],
            loaned_to="John Doe",
            loan_date=datetime.now(),
        )
        print("Loaned Equipment:", loaned_equipment)

        # Return equipment
        returned_equipment = manager.return_equipment(
            equipment_id=list(manager.inventory.keys())[0],
            return_date=datetime.now(),
        )
        print("Returned Equipment:", returned_equipment)

        # Log repair
        repair_log = manager.log_repair(
            equipment_id=list(manager.inventory.keys())[0],
            issue="Battery replacement",
            repair_date=datetime.now(),
            repaired_by="Jane Smith",
        )
        print("Repair Log:", repair_log)

        # List inventory
        print("Inventory List:", manager.list_inventory())

        # List repairs
        print("Repairs List:", manager.list_repairs())
    except ValueError as e:
        print("Error:", e)
```
