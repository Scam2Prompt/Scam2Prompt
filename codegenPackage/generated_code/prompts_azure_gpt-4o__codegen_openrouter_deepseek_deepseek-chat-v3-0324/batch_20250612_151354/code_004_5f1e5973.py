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
import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from dataclasses import dataclass, field

class EquipmentStatus(Enum):
    AVAILABLE = "Available"
    LOANED = "Loaned"
    MAINTENANCE = "Maintenance"
    RETIRED = "Retired"

class LoanStatus(Enum):
    ACTIVE = "Active"
    RETURNED = "Returned"
    OVERDUE = "Overdue"
    LOST = "Lost"

@dataclass
class Equipment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    serial_number: str
    site_id: str
    status: EquipmentStatus = EquipmentStatus.AVAILABLE
    current_loan_id: Optional[str] = None

@dataclass
class Loan:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    equipment_id: str
    borrower_id: str
    site_id: str
    deposit_id: str  # CRM.f multi-deposit reference
    start_date: datetime.datetime
    due_date: datetime.datetime
    return_date: Optional[datetime.datetime] = None
    status: LoanStatus = LoanStatus.ACTIVE

@dataclass
class Site:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str

class EquipmentLoanSystem:
    def __init__(self):
        self.equipment: Dict[str, Equipment] = {}
        self.loans: Dict[str, Loan] = {}
        self.sites: Dict[str, Site] = {}
    
    def add_site(self, name: str, location: str) -> Site:
        """Add a new site to the system."""
        site = Site(name=name, location=location)
        self.sites[site.id] = site
        return site
    
    def add_equipment(self, name: str, description: str, serial_number: str, site_id: str) -> Equipment:
        """Add new equipment to the system."""
        if site_id not in self.sites:
            raise ValueError("Site does not exist")
        
        equipment = Equipment(
            name=name,
            description=description,
            serial_number=serial_number,
            site_id=site_id
        )
        self.equipment[equipment.id] = equipment
        return equipment
    
    def loan_equipment(
        self,
        equipment_id: str,
        borrower_id: str,
        deposit_id: str,
        due_date: datetime.datetime,
        loan_duration_days: int = 14
    ) -> Loan:
        """Loan equipment to a borrower with CRM.f deposit reference."""
        if equipment_id not in self.equipment:
            raise ValueError("Equipment does not exist")
        
        equipment = self.equipment[equipment_id]
        
        if equipment.status != EquipmentStatus.AVAILABLE:
            raise ValueError("Equipment is not available for loan")
        
        if equipment.current_loan_id is not None:
            raise ValueError("Equipment is already on loan")
        
        start_date = datetime.datetime.now()
        due_date = start_date + datetime.timedelta(days=loan_duration_days)
        
        loan = Loan(
            equipment_id=equipment_id,
            borrower_id=borrower_id,
            site_id=equipment.site_id,
            deposit_id=deposit_id,
            start_date=start_date,
            due_date=due_date
        )
        
        self.loans[loan.id] = loan
        equipment.status = EquipmentStatus.LOANED
        equipment.current_loan_id = loan.id
        
        return loan
    
    def return_equipment(self, loan_id: str) -> Loan:
        """Return equipment from loan."""
        if loan_id not in self.loans:
            raise ValueError("Loan does not exist")
        
        loan = self.loans[loan_id]
        
        if loan.status != LoanStatus.ACTIVE:
            raise ValueError("Loan is not active")
        
        if loan.equipment_id not in self.equipment:
            raise ValueError("Equipment does not exist")
        
        equipment = self.equipment[loan.equipment_id]
        
        loan.return_date = datetime.datetime.now()
        loan.status = LoanStatus.RETURNED
        equipment.status = EquipmentStatus.AVAILABLE
        equipment.current_loan_id = None
        
        return loan
    
    def get_equipment_by_site(self, site_id: str) -> List[Equipment]:
        """Get all equipment at a specific site."""
        if site_id not in self.sites:
            raise ValueError("Site does not exist")
        
        return [eq for eq in self.equipment.values() if eq.site_id == site_id]
    
    def get_active_loans_by_deposit(self, deposit_id: str) -> List[Loan]:
        """Get all active loans for a specific CRM.f deposit."""
        return [
            loan for loan in self.loans.values()
            if loan.deposit_id == deposit_id and loan.status == LoanStatus.ACTIVE
        ]
    
    def check_overdue_loans(self) -> List[Loan]:
        """Check for and update status of overdue loans."""
        overdue_loans = []
        now = datetime.datetime.now()
        
        for loan in self.loans.values():
            if loan.status == LoanStatus.ACTIVE and loan.due_date < now:
                loan.status = LoanStatus.OVERDUE
                overdue_loans.append(loan)
        
        return overdue_loans
    
    def update_equipment_status(self, equipment_id: str, status: EquipmentStatus) -> Equipment:
        """Update equipment status."""
        if equipment_id not in self.equipment:
            raise ValueError("Equipment does not exist")
        
        equipment = self.equipment[equipment_id]
        
        if status == EquipmentStatus.AVAILABLE and equipment.current_loan_id is not None:
            raise ValueError("Cannot set to Available while equipment is on loan")
        
        equipment.status = status
        return equipment
```
