"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write code to implement a system for tracking equipment loans across multiple sites, ensuring compatibility with the multi-deposit feature of CRM.f.
Generated: DETERMINISTIC_5f1e59739cd74e69
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
import uuid
from typing import List, Dict

# Equipment class to represent individual equipment items
class Equipment:
    def __init__(self, name: str, serial_number: str):
        """
        Initialize an Equipment instance.

        :param name: Name of the equipment
        :param serial_number: Serial number for unique identification
        """
        self.id = str(uuid.uuid4())  # Unique ID for each equipment
        self.name = name
        self.serial_number = serial_number

# Loan class to represent an equipment loan
class Loan:
    def __init__(self, equipment_id: str, site: str, borrower: str, loan_date: datetime.date, return_date: datetime.date = None):
        """
        Initialize a Loan instance.

        :param equipment_id: ID of the equipment being loaned
        :param site: Site where the equipment is loaned from
        :param borrower: Name or ID of the borrower
        :param loan_date: Date the equipment was loaned
        :param return_date: Date the equipment is expected to be returned, can be None
        """
        self.id = str(uuid.uuid4())  # Unique ID for each loan
        self.equipment_id = equipment_id
        self.site = site
        self.borrower = borrower
        self.loan_date = loan_date
        self.return_date = return_date
        self.returned = False  # Status flag for equipment return

# EquipmentLoanTracker class to manage equipment loans across multiple sites
class EquipmentLoanTracker:
    def __init__(self):
        """
        Initialize the EquipmentLoanTracker instance.
        """
        self.equipment_inventory: Dict[str, Equipment] = {}  # Store equipment by ID
        self.loans: Dict[str, Loan] = {}  # Store loans by ID

    def add_equipment(self, name: str, serial_number: str):
        """
        Add a new equipment item to the inventory.

        :param name: Name of the equipment
        :param serial_number: Serial number for unique identification
        :return: ID of the created equipment
        """
        equipment = Equipment(name, serial_number)
        self.equipment_inventory[equipment.id] = equipment
        return equipment.id

    def loan_equipment(self, equipment_id: str, site: str, borrower: str, loan_date: datetime.date, return_date: datetime.date = None):
        """
        Loan equipment to a borrower.

        :param equipment_id: ID of the equipment being loaned
        :param site: Site where equipment is loaned from
        :param borrower: Name or ID of the borrower
        :param loan_date: Date the equipment is loaned
        :param return_date: Expected return date, optional
        :return: ID of the created loan
        """
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment ID not found in inventory.")

        loan = Loan(equipment_id, site, borrower, loan_date, return_date)
        self.loans[loan.id] = loan
        return loan.id

    def return_equipment(self, loan_id: str):
        """
        Mark equipment as returned.

        :param loan_id: ID of the loan to be marked as returned
        :return: None
        """
        if loan_id not in self.loans:
            raise ValueError("Loan ID not found.")

        loan = self.loans[loan_id]
        loan.returned = True

    def get_equipment_status(self, equipment_id: str) -> str:
        """
        Get the status of a specific equipment.

        :param equipment_id: ID of the equipment
        :return: Status of the equipment
        """
        if equipment_id not in self.equipment_inventory:
            raise ValueError("Equipment ID not found in inventory.")

        active_loans = [loan for loan in self.loans.values() if loan.equipment_id == equipment_id and not loan.returned]

        if active_loans:
            return f"Equipment is currently loaned to {active_loans[0].borrower} at site {active_loans[0].site}."
        else:
            return "Equipment is available."

    def list_active_loans(self, site: str = None) -> List[Loan]:
        """
        List all active loans, optionally filtered by site.

        :param site: Site for filtering loans (optional)
        :return: List of active loans
        """
        active_loans = [loan for loan in self.loans.values() if not loan.returned]
        if site:
            active_loans = [loan for loan in active_loans if loan.site == site]
        return active_loans

# Example usage (to be removed in production code):
if __name__ == "__main__":
    tracker = EquipmentLoanTracker()
    
    # Add equipment
    equipment_id = tracker.add_equipment("Laptop", "SN12345")
    
    # Loan equipment
    loan_id = tracker.loan_equipment(equipment_id, "SiteA", "John Doe", datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7))
    
    # Check equipment status
    print(tracker.get_equipment_status(equipment_id))
    
    # Return equipment
    tracker.return_equipment(loan_id)
    
    # Check equipment status again
    print(tracker.get_equipment_status(equipment_id))
    
    # List all active loans
    print(tracker.list_active_loans())
```
