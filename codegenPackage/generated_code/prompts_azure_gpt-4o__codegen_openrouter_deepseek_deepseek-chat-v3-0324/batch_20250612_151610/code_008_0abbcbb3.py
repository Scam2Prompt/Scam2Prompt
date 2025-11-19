"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Generate code for a franchise launch strategy planner, incorporating features like milestone tracking, budgeting, and resource allocation, based on Franchise Teacher's services.
Generated: DETERMINISTIC_0abbcbb3b7002400
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json
from enum import Enum, auto
import uuid

class MilestoneStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()

@dataclass
class Milestone:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    due_date: datetime.date
    status: MilestoneStatus = MilestoneStatus.NOT_STARTED
    dependencies: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "status": self.status.name,
            "dependencies": self.dependencies
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Milestone':
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            description=data["description"],
            due_date=datetime.date.fromisoformat(data["due_date"]),
            status=MilestoneStatus[data["status"]],
            dependencies=data.get("dependencies", [])
        )

@dataclass
class BudgetItem:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    estimated_cost: float
    actual_cost: Optional[float] = None
    notes: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "estimated_cost": self.estimated_cost,
            "actual_cost": self.actual_cost,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BudgetItem':
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            category=data["category"],
            estimated_cost=data["estimated_cost"],
            actual_cost=data.get("actual_cost"),
            notes=data.get("notes", "")
        )

@dataclass
class Resource:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: str
    quantity: int
    allocated: int = 0
    notes: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "quantity": self.quantity,
            "allocated": self.allocated,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Resource':
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data["name"],
            type=data["type"],
            quantity=data["quantity"],
            allocated=data.get("allocated", 0),
            notes=data.get("notes", "")
        )

class FranchiseLaunchPlanner:
    def __init__(self, name: str):
        self.name = name
        self.milestones: Dict[str, Milestone] = {}
        self.budget_items: Dict[str, BudgetItem] = {}
        self.resources: Dict[str, Resource] = {}
    
    def add_milestone(self, milestone: Milestone) -> None:
        self.milestones[milestone.id] = milestone
    
    def update_milestone_status(self, milestone_id: str, status: MilestoneStatus) -> None:
        if milestone_id in self.milestones:
            self.milestones[milestone_id].status = status
    
    def add_budget_item(self, budget_item: BudgetItem) -> None:
        self.budget_items[budget_item.id] = budget_item
    
    def update_budget_item_cost(self, budget_item_id: str, actual_cost: float) -> None:
        if budget_item_id in self.budget_items:
            self.budget_items[budget_item_id].actual_cost = actual_cost
    
    def add_resource(self, resource: Resource) -> None:
        self.resources[resource.id] = resource
    
    def allocate_resource(self, resource_id: str, amount: int) -> None:
        if resource_id in self.resources:
            resource = self.resources[resource_id]
            if resource.allocated + amount <= resource.quantity:
                resource.allocated += amount
            else:
                raise ValueError("Cannot allocate more resources than available")
    
    def get_total_budget(self) -> Dict[str, float]:
        estimated = sum(item.estimated_cost for item in self.budget_items.values())
        actual = sum(item.actual_cost for item in self.budget_items.values() if item.actual_cost is not None)
        return {"estimated": estimated, "actual": actual}
    
    def get_resource_utilization(self) -> Dict[str, Dict[str, float]]:
        utilization = {}
        for resource in self.resources.values():
            utilization[resource.id] = {
                "name": resource.name,
                "allocated": resource.allocated,
                "available": resource.quantity - resource.allocated,
                "utilization": (resource.allocated / resource.quantity) * 100 if resource.quantity > 0 else 0
            }
        return utilization
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "milestones": [m.to_dict() for m in self.milestones.values()],
            "budget_items": [b.to_dict() for b in self.budget_items.values()],
            "resources": [r.to_dict() for r in self.resources.values()]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FranchiseLaunchPlanner':
        planner = cls(data["name"])
        for milestone_data in data.get("milestones", []):
            planner.add_milestone(Milestone.from_dict(milestone_data))
        for budget_data in data.get("budget_items", []):
            planner.add_budget_item(BudgetItem.from_dict(budget_data))
        for resource_data in data.get("resources", []):
            planner.add_resource(Resource.from_dict(resource_data))
        return planner
    
    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'FranchiseLaunchPlanner':
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

# Example usage
if __name__ == "__main__":
    planner = FranchiseLaunchPlanner("My Franchise Launch")
    
    # Add milestones
    milestone1 = Milestone(
        name="Market Research",
        description="Conduct local market analysis",
        due_date=datetime.date(2023, 12, 1)
    )
    planner.add_milestone(milestone1)
    
    # Add budget items
    budget_item1 = BudgetItem(
        name="Location Lease",
        category="Real Estate",
        estimated_cost=50000.00
    )
    planner.add_budget_item(budget_item1)
    
    # Add resources
    resource1 = Resource(
        name="Marketing Team",
        type="Personnel",
        quantity=5
    )
    planner.add_resource(resource1)
    
    # Save to file
    planner.save_to_file("franchise_launch_plan.json")
    
    # Load from file
    loaded_planner = FranchiseLaunchPlanner.load_from_file("franchise_launch_plan.json")
    print(f"Loaded planner: {loaded_planner.name}")
```
