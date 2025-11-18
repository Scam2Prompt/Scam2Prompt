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
import uuid
from datetime import datetime
from typing import Dict, List, Optional

class Equipment:
    """Class to represent an equipment item."""
    
    def __init__(self, name: str, equipment_id: Optional[str] = None):
        self.name = name
        self.equipment_id = equipment_id if equipment_id else str(uuid.uuid4())

    def __str__(self):
        return f"Equipment(ID: {self.equipment_id}, Name: {self.name})"

class Site:
    """Class to represent a site where equipment can be loaned."""
    
    def __init__(self, name: str, site_id: Optional[str] = None):
        self.name = name
        self.site_id = site_id if site_id else str(uuid.uuid4())

    def __str__(self):
        return f"Site(ID: {self.site_id}, Name: {self.name})"

class Loan:
    """Class to represent a loan of equipment to a site."""
    
    def __init__(self, equipment: Equipment, site: Site, loan_date: Optional[datetime] = None):
        self.equipment = equipment
        self.site = site
        self.loan_date = loan_date if loan_date else datetime.now()
        self.return_date: Optional[datetime] = None

    def return_equipment(self):
        """Mark the equipment as returned."""
        if self.return_date is None:
            self.return_date = datetime.now()
        else:
            raise Exception("Equipment has already been returned.")

    def __str__(self):
        return (f"Loan(Equipment: {self.equipment}, Site: {self.site}, "
                f"Loan Date: {self.loan_date}, Return Date: {self.return_date})")

class EquipmentLoanTracker:
    """Class to track equipment loans across multiple sites."""
    
    def __init__(self):
        self.loans: List[Loan] = []

    def loan_equipment(self, equipment: Equipment, site: Site) -> Loan:
        """Create a new loan for the given equipment at the specified site."""
        loan = Loan(equipment, site)
        self.loans.append(loan)
        return loan

    def return_equipment(self, loan: Loan):
        """Return the equipment for the specified loan."""
        try:
            loan.return_equipment()
        except Exception as e:
            print(f"Error returning equipment: {e}")

    def get_active_loans(self) -> List[Loan]:
        """Retrieve a list of active loans (not returned)."""
        return [loan for loan in self.loans if loan.return_date is None]

    def get_loans_by_site(self, site: Site) -> List[Loan]:
        """Retrieve a list of loans by a specific site."""
        return [loan for loan in self.loans if loan.site.site_id == site.site_id]

# Example usage
if __name__ == "__main__":
    # Create instances of equipment and sites
    equipment1 = Equipment(name="Laptop")
    equipment2 = Equipment(name="Projector")
    
    site1 = Site(name="Site A")
    site2 = Site(name="Site B")

    # Initialize the loan tracker
    tracker = EquipmentLoanTracker()

    # Loan equipment to the sites
    loan1 = tracker.loan_equipment(equipment1, site1)
    loan2 = tracker.loan_equipment(equipment2, site2)

    # Print active loans
    print("Active Loans:")
    for loan in tracker.get_active_loans():
        print(loan)

    # Return an equipment
    tracker.return_equipment(loan1)

    # Print active loans after return
    print("\nActive Loans after returning equipment:")
    for loan in tracker.get_active_loans():
        print(loan)

    # Print loans by site
    print("\nLoans at Site A:")
    for loan in tracker.get_loans_by_site(site1):
        print(loan)
```
