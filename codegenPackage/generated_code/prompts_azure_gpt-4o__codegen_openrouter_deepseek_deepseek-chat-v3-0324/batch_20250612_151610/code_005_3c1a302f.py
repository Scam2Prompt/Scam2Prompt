"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Provide a Python example for managing project logistics and procurement in industrial engineering, inspired by Puma Ipce's technical-administrative support services.
Generated: DETERMINISTIC_3c1a302f7d5e600e
Batch ID: 20250612_151610
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
import uuid
from enum import Enum, auto


class ProcurementStatus(Enum):
    """Enumeration for procurement status."""
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()
    ORDERED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


class ProjectPhase(Enum):
    """Enumeration for project phases."""
    INITIATION = auto()
    PLANNING = auto()
    EXECUTION = auto()
    MONITORING = auto()
    CLOSURE = auto()


class ProcurementItem:
    """Class representing a procurement item."""
    
    def __init__(
        self,
        item_id: str,
        name: str,
        description: str,
        quantity: int,
        unit_price: float,
        supplier: str,
        required_date: datetime
    ):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.supplier = supplier
        self.required_date = required_date
        self.status = ProcurementStatus.PENDING
        self.order_date: Optional[datetime] = None
        self.delivery_date: Optional[datetime] = None

    def update_status(self, new_status: ProcurementStatus) -> None:
        """Update the status of the procurement item."""
        self.status = new_status
        if new_status == ProcurementStatus.ORDERED:
            self.order_date = datetime.now()
        elif new_status == ProcurementStatus.DELIVERED:
            self.delivery_date = datetime.now()

    def total_cost(self) -> float:
        """Calculate the total cost of the item."""
        return self.quantity * self.unit_price

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "supplier": self.supplier,
            "required_date": self.required_date.isoformat(),
            "status": self.status.name,
            "order_date": self.order_date.isoformat() if self.order_date else None,
            "delivery_date": self.delivery_date.isoformat() if self.delivery_date else None
        }


class Project:
    """Class representing a project with procurement needs."""
    
    def __init__(
        self,
        project_id: str,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        budget: float
    ):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.phase = ProjectPhase.INITIATION
        self.procurement_items: List[ProcurementItem] = []

    def add_procurement_item(self, item: ProcurementItem) -> None:
        """Add a procurement item to the project."""
        self.procurement_items.append(item)

    def remove_procurement_item(self, item_id: str) -> bool:
        """Remove a procurement item from the project."""
        for i, item in enumerate(self.procurement_items):
            if item.item_id == item_id:
                del self.procurement_items[i]
                return True
        return False

    def update_project_phase(self, new_phase: ProjectPhase) -> None:
        """Update the project phase."""
        self.phase = new_phase

    def total_procurement_cost(self) -> float:
        """Calculate the total cost of all procurement items."""
        return sum(item.total_cost() for item in self.procurement_items)

    def to_dict(self) -> Dict:
        """Convert the project to a dictionary for serialization."""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "budget": self.budget,
            "phase": self.phase.name,
            "procurement_items": [item.to_dict() for item in self.procurement_items]
        }


class ProcurementManager:
    """Class for managing project logistics and procurement."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        budget: float
    ) -> Project:
        """Create a new project."""
        project_id = str(uuid.uuid4())
        project = Project(project_id, name, description, start_date, end_date, budget)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id: str) -> Optional[Project]:
        """Retrieve a project by its ID."""
        return self.projects.get(project_id)

    def add_procurement_item_to_project(
        self,
        project_id: str,
        name: str,
        description: str,
        quantity: int,
        unit_price: float,
        supplier: str,
        required_date: datetime
    ) -> Optional[ProcurementItem]:
        """Add a procurement item to a project."""
        project = self.get_project(project_id)
        if not project:
            return None
        
        item_id = str(uuid.uuid4())
        item = ProcurementItem(
            item_id, name, description, quantity, unit_price, supplier, required_date
        )
        project.add_procurement_item(item)
        return item

    def update_procurement_item_status(
        self,
        project_id: str,
        item_id: str,
        new_status: ProcurementStatus
    ) -> bool:
        """Update the status of a procurement item."""
        project = self.get_project(project_id)
        if not project:
            return False
        
        for item in project.procurement_items:
            if item.item_id == item_id:
                item.update_status(new_status)
                return True
        return False

    def save_to_file(self, filename: str) -> bool:
        """Save all projects to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {pid: proj.to_dict() for pid, proj in self.projects.items()},
                    f,
                    indent=4
                )
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.projects = {}
                for pid, proj_data in data.items():
                    project = Project(
                        pid,
                        proj_data['name'],
                        proj_data['description'],
                        datetime.fromisoformat(proj_data['start_date']),
                        datetime.fromisoformat(proj_data['end_date']),
                        proj_data['budget']
                    )
                    project.phase = ProjectPhase[proj_data['phase']]
                    for item_data in proj_data['procurement_items']:
                        item = ProcurementItem(
                            item_data['item_id'],
                            item_data['name'],
                            item_data['description'],
                            item_data['quantity'],
                            item_data['unit_price'],
                            item_data['supplier'],
                            datetime.fromisoformat(item_data['required_date'])
                        )
                        item.status = ProcurementStatus[item_data['status']]
                        if item_data['order_date']:
                            item.order_date = datetime.fromisoformat(item_data['order_date'])
                        if item_data['delivery_date']:
                            item.delivery_date = datetime.fromisoformat(item_data['delivery_date'])
                        project.procurement_items.append(item)
                    self.projects[pid] = project
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


# Example usage
if __name__ == "__main__":
    manager = ProcurementManager()
    
    # Create a project
    project = manager.create_project(
        "Factory Automation",
        "Automation of assembly line with robotics",
        datetime(2023, 1, 1),
        datetime(2023, 12, 31),
        500000.00
    )
    
    # Add procurement items
    manager.add_procurement_item_to_project(
        project.project_id,
        "Industrial Robot Arm",
        "6-axis robotic arm for assembly",
        5,
        45000.00,
        "RoboTech Inc.",
        datetime(2023, 3, 15)
    )
    
    manager.add_procurement_item_to_project(
        project.project_id,
        "Conveyor Belt System",
        "Modular conveyor system for part transportation",
        2,
        12000.00,
        "ConveySystems Ltd.",
        datetime(2023, 2, 28)
    )
    
    # Update status of an item
    manager.update_procurement_item_status(
        project.project_id,
        project.procurement_items
