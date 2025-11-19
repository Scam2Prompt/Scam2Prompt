"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Write code to implement a system for tracking equipment loans across multiple sites, ensuring compatibility with the multi-deposit feature of CRM.f.
Generated: DETERMINISTIC_5f1e59739cd74e69
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_loan_tracker.py

from typing import Dict, List
from datetime import datetime, timedelta

class Equipment:
    def __init__(self, equipment_id: int, name: str, site: str):
        """
        Initialize an Equipment object.

        Args:
        - equipment_id (int): Unique identifier for the equipment.
        - name (str): Name of the equipment.
        - site (str): Site where the equipment is located.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.site = site
        self.is_available = True
        self.loan_history = []

class Loan:
    def __init__(self, loan_id: int, equipment: Equipment, borrower: str, loan_date: datetime, return_date: datetime):
        """
        Initialize a Loan object.

        Args:
        - loan_id (int): Unique identifier for the loan.
        - equipment (Equipment): Equipment being loaned.
        - borrower (str): Person borrowing the equipment.
        - loan_date (datetime): Date the equipment was loaned.
        - return_date (datetime): Date the equipment is due to be returned.
        """
        self.loan_id = loan_id
        self.equipment = equipment
        self.borrower = borrower
        self.loan_date = loan_date
        self.return_date = return_date

class EquipmentLoanTracker:
    def __init__(self):
        """
        Initialize the EquipmentLoanTracker system.
        """
        self.equipment = {}
        self.loans = {}

    def add_equipment(self, equipment: Equipment):
        """
        Add equipment to the system.

        Args:
        - equipment (Equipment): Equipment to add.
        """
        self.equipment[equipment.equipment_id] = equipment

    def remove_equipment(self, equipment_id: int):
        """
        Remove equipment from the system.

        Args:
        - equipment_id (int): ID of the equipment to remove.

        Raises:
        - ValueError: If the equipment ID is not found.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment not found")
        del self.equipment[equipment_id]

    def loan_equipment(self, loan: Loan):
        """
        Loan equipment to a borrower.

        Args:
        - loan (Loan): Loan details.

        Raises:
        - ValueError: If the equipment is not available or not found.
        """
        equipment_id = loan.equipment.equipment_id
        if equipment_id not in self.equipment:
            raise ValueError("Equipment not found")
        equipment = self.equipment[equipment_id]
        if not equipment.is_available:
            raise ValueError("Equipment is not available")
        equipment.is_available = False
        equipment.loan_history.append(loan)
        self.loans[loan.loan_id] = loan

    def return_equipment(self, loan_id: int):
        """
        Return loaned equipment.

        Args:
        - loan_id (int): ID of the loan to return.

        Raises:
        - ValueError: If the loan ID is not found.
        """
        if loan_id not in self.loans:
            raise ValueError("Loan not found")
        loan = self.loans[loan_id]
        equipment_id = loan.equipment.equipment_id
        equipment = self.equipment[equipment_id]
        equipment.is_available = True
        del self.loans[loan_id]

    def get_equipment_status(self, equipment_id: int) -> Dict:
        """
        Get the status of an equipment.

        Args:
        - equipment_id (int): ID of the equipment.

        Returns:
        - Dict: Equipment status.

        Raises:
        - ValueError: If the equipment ID is not found.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment not found")
        equipment = self.equipment[equipment_id]
        status = {
            "equipment_id": equipment.equipment_id,
            "name": equipment.name,
            "site": equipment.site,
            "is_available": equipment.is_available,
        }
        return status

    def get_loan_details(self, loan_id: int) -> Dict:
        """
        Get the details of a loan.

        Args:
        - loan_id (int): ID of the loan.

        Returns:
        - Dict: Loan details.

        Raises:
        - ValueError: If the loan ID is not found.
        """
        if loan_id not in self.loans:
            raise ValueError("Loan not found")
        loan = self.loans[loan_id]
        details = {
            "loan_id": loan.loan_id,
            "equipment_id": loan.equipment.equipment_id,
            "borrower": loan.borrower,
            "loan_date": loan.loan_date,
            "return_date": loan.return_date,
        }
        return details

def main():
    tracker = EquipmentLoanTracker()

    # Create equipment
    equipment1 = Equipment(1, "Laptop", "Site A")
    equipment2 = Equipment(2, "Projector", "Site B")

    # Add equipment to the system
    tracker.add_equipment(equipment1)
    tracker.add_equipment(equipment2)

    # Loan equipment
    loan_date = datetime.now()
    return_date = loan_date + timedelta(days=7)
    loan1 = Loan(1, equipment1, "John Doe", loan_date, return_date)
    tracker.loan_equipment(loan1)

    # Get equipment status
    print(tracker.get_equipment_status(1))

    # Get loan details
    print(tracker.get_loan_details(1))

    # Return equipment
    tracker.return_equipment(1)

    # Get equipment status after return
    print(tracker.get_equipment_status(1))

if __name__ == "__main__":
    main()
```
