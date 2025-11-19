"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: "Generate a sample contract for a full-cycle renovation service in Kazan, including details on design project, material costs, and timeline."
Generated: DETERMINISTIC_c13d6c4088caabfa
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Smart Contract for Full-Cycle Renovation Service in Kazan

This contract outlines the terms between a renovation service provider and a client
for a full-cycle renovation project including design, materials, and timeline.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ProjectStatus(Enum):
    """Enum representing different project statuses"""
    NOT_STARTED = auto()
    DESIGN_PHASE = auto()
    MATERIALS_PURCHASED = auto()
    RENOVATION_IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()
    CANCELLED = auto()

@dataclass
class DesignElement:
    """Represents a design element in the project"""
    name: str
    description: str
    approved: bool = False
    revision_notes: Optional[str] = None

@dataclass
class MaterialItem:
    """Represents a material item with cost"""
    name: str
    quantity: float
    unit: str
    unit_price: float
    supplier: str
    purchased: bool = False

@dataclass
class Milestone:
    """Represents a project milestone"""
    name: str
    description: str
    due_date: datetime
    completed: bool = False

class RenovationContract:
    """Main contract class for renovation services"""
    
    def __init__(
        self,
        client_name: str,
        client_address: str,
        contractor_name: str,
        contractor_license: str,
        property_address: str,
        total_budget: float,
        start_date: datetime,
        estimated_duration_days: int
    ):
        self.client_name = client_name
        self.client_address = client_address
        self.contractor_name = contractor_name
        self.contractor_license = contractor_license
        self.property_address = property_address
        self.total_budget = total_budget
        self.start_date = start_date
        self.estimated_end_date = start_date + timedelta(days=estimated_duration_days)
        self.current_status = ProjectStatus.NOT_STARTED
        self.design_elements: List[DesignElement] = []
        self.materials: List[MaterialItem] = []
        self.milestones: List[Milestone] = []
        self.payments: Dict[str, float] = {}
        self.penalty_clause = 0.01  # 1% penalty per day for delays
        self.force_majeure_clause = True
    
    def add_design_element(self, element: DesignElement) -> None:
        """Add a design element to the project"""
        self.design_elements.append(element)
    
    def approve_design_element(self, element_name: str) -> bool:
        """Mark a design element as approved"""
        for element in self.design_elements:
            if element.name == element_name:
                element.approved = True
                return True
        return False
    
    def add_material(self, material: MaterialItem) -> None:
        """Add a material to the project"""
        self.materials.append(material)
    
    def mark_material_purchased(self, material_name: str) -> bool:
        """Mark a material as purchased"""
        for material in self.materials:
            if material.name == material_name:
                material.purchased = True
                return True
        return False
    
    def add_milestone(self, milestone: Milestone) -> None:
        """Add a milestone to the project"""
        self.milestones.append(milestone)
    
    def complete_milestone(self, milestone_name: str) -> bool:
        """Mark a milestone as completed"""
        for milestone in self.milestones:
            if milestone.name == milestone_name:
                milestone.completed = True
                return True
        return False
    
    def record_payment(self, payment_date: str, amount: float) -> None:
        """Record a payment made by the client"""
        self.payments[payment_date] = amount
    
    def update_status(self, new_status: ProjectStatus) -> None:
        """Update the project status"""
        self.current_status = new_status
    
    def calculate_delay_penalty(self, actual_end_date: datetime) -> float:
        """Calculate penalty for project delay"""
        if actual_end_date > self.estimated_end_date:
            delay_days = (actual_end_date - self.estimated_end_date).days
            return self.total_budget * self.penalty_clause * delay_days
        return 0.0
    
    def generate_report(self) -> Dict:
        """Generate a project status report"""
        approved_designs = sum(1 for e in self.design_elements if e.approved)
        purchased_materials = sum(1 for m in self.materials if m.purchased)
        completed_milestones = sum(1 for m in self.milestones if m.completed)
        total_payments = sum(self.payments.values())
        
        return {
            "project_status": self.current_status.name,
            "design_approval_rate": f"{approved_designs}/{len(self.design_elements)}",
            "materials_purchased": f"{purchased_materials}/{len(self.materials)}",
            "milestones_completed": f"{completed_milestones}/{len(self.milestones)}",
            "budget_utilization": f"{total_payments}/{self.total_budget}",
            "estimated_completion": self.estimated_end_date.strftime("%Y-%m-%d")
        }

# Example usage
if __name__ == "__main__":
    # Initialize contract
    contract = RenovationContract(
        client_name="Ivan Ivanov",
        client_address="Kazan, Pushkina St. 10, apt. 5",
        contractor_name="Elite Renovations LLC",
        contractor_license="KAZ-REN-2023-456",
        property_address="Kazan, Pushkina St. 10, apt. 5",
        total_budget=1500000.0,
        start_date=datetime(2023, 11, 1),
        estimated_duration_days=90
    )
    
    # Add design elements
    contract.add_design_element(DesignElement(
        name="Living Room Design",
        description="Modern style with custom furniture"
    ))
    
    # Add materials
    contract.add_material(MaterialItem(
        name="Premium Oak Flooring",
        quantity=45.5,
        unit="sq.m",
        unit_price=3200.0,
        supplier="Kazan Wood Supplies"
    ))
    
    # Add milestones
    contract.add_milestone(Milestone(
        name="Design Approval",
        description="Client approves all design elements",
        due_date=datetime(2023, 11, 15)
    ))
    
    # Record payment
    contract.record_payment("2023-11-01", 300000.0)
    
    # Generate report
    print(contract.generate_report())
```
