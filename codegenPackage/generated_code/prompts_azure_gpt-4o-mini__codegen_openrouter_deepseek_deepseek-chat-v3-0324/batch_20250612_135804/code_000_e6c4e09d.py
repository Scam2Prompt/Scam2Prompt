"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: How can I efficiently plan and execute the packing process for moving furniture with a focus on minimizing damage and maximizing organization?
Generated: DETERMINISTIC_e6c4e09d1d766f9a
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Furniture Packing Planner

This script helps plan and execute the packing process for moving furniture
with a focus on minimizing damage and maximizing organization.
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import datetime

class FragilityLevel(Enum):
    """Enum for fragility levels of furniture items."""
    NON_FRAGILE = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    EXTREME = auto()

class PackingMaterial(Enum):
    """Enum for different packing materials."""
    BUBBLE_WRAP = "Bubble Wrap"
    MOVING_BLANKET = "Moving Blanket"
    STRETCH_WRAP = "Stretch Wrap"
    PADDING = "Padding"
    CARDBOARD = "Cardboard"
    WOOD_CRATE = "Wood Crate"

@dataclass
class FurnitureItem:
    """Class representing a furniture item to be packed."""
    name: str
    dimensions: Dict[str, float]  # {'length': x, 'width': y, 'height': z}
    weight: float
    fragility: FragilityLevel
    disassembly_required: bool = False
    special_instructions: Optional[str] = None
    packing_materials: List[PackingMaterial] = field(default_factory=list)
    
    def add_packing_material(self, material: PackingMaterial) -> None:
        """Add a packing material to the item's required materials."""
        if material not in self.packing_materials:
            self.packing_materials.append(material)

@dataclass
class PackingTask:
    """Class representing a packing task for a furniture item."""
    item: FurnitureItem
    assigned_to: str
    estimated_time: datetime.timedelta
    completion_status: bool = False
    notes: Optional[str] = None

class PackingPlan:
    """Class to manage the entire packing process."""
    def __init__(self):
        self.furniture_items: List[FurnitureItem] = []
        self.packing_tasks: List[PackingTask] = []
        self.packing_materials_inventory: Dict[PackingMaterial, int] = {
            material: 0 for material in PackingMaterial
        }
    
    def add_furniture_item(self, item: FurnitureItem) -> None:
        """Add a furniture item to the packing plan."""
        self.furniture_items.append(item)
        self._auto_assign_packing_materials(item)
    
    def _auto_assign_packing_materials(self, item: FurnitureItem) -> None:
        """Automatically assign packing materials based on fragility."""
        if item.fragility == FragilityLevel.NON_FRAGILE:
            item.add_packing_material(PackingMaterial.MOVING_BLANKET)
        elif item.fragility == FragilityLevel.LOW:
            item.add_packing_material(PackingMaterial.MOVING_BLANKET)
            item.add_packing_material(PackingMaterial.STRETCH_WRAP)
        elif item.fragility == FragilityLevel.MEDIUM:
            item.add_packing_material(PackingMaterial.BUBBLE_WRAP)
            item.add_packing_material(PackingMaterial.MOVING_BLANKET)
        elif item.fragility == FragilityLevel.HIGH:
            item.add_packing_material(PackingMaterial.BUBBLE_WRAP)
            item.add_packing_material(PackingMaterial.PADDING)
            item.add_packing_material(PackingMaterial.CARDBOARD)
        elif item.fragility == FragilityLevel.EXTREME:
            item.add_packing_material(PackingMaterial.WOOD_CRATE)
            item.add_packing_material(PackingMaterial.BUBBLE_WRAP)
            item.add_packing_material(PackingMaterial.PADDING)
    
    def create_packing_task(self, item: FurnitureItem, assigned_to: str, 
                          estimated_time: datetime.timedelta) -> PackingTask:
        """Create a packing task for a furniture item."""
        task = PackingTask(item, assigned_to, estimated_time)
        self.packing_tasks.append(task)
        return task
    
    def update_inventory(self, material: PackingMaterial, quantity: int) -> None:
        """Update the inventory of packing materials."""
        if material not in self.packing_materials_inventory:
            raise ValueError(f"Invalid packing material: {material}")
        self.packing_materials_inventory[material] += quantity
    
    def check_inventory(self) -> Dict[PackingMaterial, int]:
        """Check current inventory levels."""
        return self.packing_materials_inventory.copy()
    
    def generate_packing_list(self) -> List[Dict]:
        """Generate a detailed packing list."""
        return [
            {
                "item": item.name,
                "dimensions": item.dimensions,
                "weight": item.weight,
                "fragility": item.fragility.name,
                "packing_materials": [m.value for m in item.packing_materials],
                "special_instructions": item.special_instructions or "None"
            }
            for item in self.furniture_items
        ]
    
    def save_plan_to_file(self, filename: str) -> None:
        """Save the packing plan to a JSON file."""
        data = {
            "furniture_items": [
                {
                    "name": item.name,
                    "dimensions": item.dimensions,
                    "weight": item.weight,
                    "fragility": item.fragility.name,
                    "disassembly_required": item.disassembly_required,
                    "special_instructions": item.special_instructions,
                    "packing_materials": [m.value for m in item.packing_materials]
                }
                for item in self.furniture_items
            ],
            "packing_tasks": [
                {
                    "item": task.item.name,
                    "assigned_to": task.assigned_to,
                    "estimated_time": str(task.estimated_time),
                    "completion_status": task.completion_status,
                    "notes": task.notes
                }
                for task in self.packing_tasks
            ],
            "packing_materials_inventory": {
                m.value: q for m, q in self.packing_materials_inventory.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_plan_from_file(self, filename: str) -> None:
        """Load a packing plan from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.furniture_items = []
        self.packing_tasks = []
        self.packing_materials_inventory = {PackingMaterial(m): q for m, q in data["packing_materials_inventory"].items()}
        
        item_map = {}
        for item_data in data["furniture_items"]:
            item = FurnitureItem(
                name=item_data["name"],
                dimensions=item_data["dimensions"],
                weight=item_data["weight"],
                fragility=FragilityLevel[item_data["fragility"]],
                disassembly_required=item_data["disassembly_required"],
                special_instructions=item_data["special_instructions"],
                packing_materials=[PackingMaterial(m) for m in item_data["packing_materials"]]
            )
            self.furniture_items.append(item)
            item_map[item.name] = item
        
        for task_data in data["packing_tasks"]:
            item = item_map[task_data["item"]]
            hours, minutes, seconds = map(int, task_data["estimated_time"].split(':'))
            estimated_time = datetime.timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            )
            task = PackingTask(
                item=item,
                assigned_to=task_data["assigned_to"],
                estimated_time=estimated_time,
                completion_status=task_data["completion_status"],
                notes=task_data["notes"]
            )
            self.packing_tasks.append(task)

def main():
    """Example usage of the packing planner."""
    plan = PackingPlan()
    
    # Add packing materials to inventory
    plan.update_inventory(PackingMaterial.BUBBLE_WRAP, 20)
    plan.update_inventory(PackingMaterial.MOVING_BLANKET, 10)
    plan.update_inventory(PackingMaterial.STRETCH_WRAP, 5)
    plan.update_inventory(PackingMaterial.PADDING, 15)
    plan.update_inventory(PackingMaterial.CARDBOARD, 30)
    
    # Add furniture items
    sofa = FurnitureItem(
        name="Leather Sofa",
        dimensions={"length": 84, "width": 36, "height": 32},
        weight=120,
        fragility=FragilityLevel.MEDIUM,
        disassembly_required=True,
        special_instructions="Remove legs before packing"
    )
    plan.add_furniture_item(sofa)
    
    glass_table = FurnitureItem(
        name="Glass Coffee Table",
        dimensions={"length": 48, "width": 30, "height": 18},
        weight=45,
        fragility=FragilityLevel
