"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Create code to simulate rear-end rebuilds for racecars, using specifications provided by Metal Fab Pro Race Shop.
Generated: DETERMINISTIC_c054cc2530d7ca1d
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ComponentCondition(Enum):
    NEW = auto()
    USED_GOOD = auto()
    USED_WORN = auto()
    DAMAGED = auto()

class ComponentType(Enum):
    AXLE = auto()
    DIFFERENTIAL = auto()
    DRIVESHAFT = auto()
    SUSPENSION = auto()
    BRAKES = auto()

@dataclass
class Component:
    component_type: ComponentType
    condition: ComponentCondition
    part_number: str
    manufacturer: str
    cost: float
    hours_to_install: float

@dataclass
class RebuildSpecification:
    max_budget: float
    max_hours: float
    required_components: List[ComponentType]
    allow_used: bool
    allow_damaged: bool

class RebuildSimulator:
    def __init__(self):
        self._component_inventory = self._initialize_inventory()
    
    def _initialize_inventory(self) -> List[Component]:
        """Initialize the component inventory with sample parts."""
        return [
            Component(
                component_type=ComponentType.AXLE,
                condition=ComponentCondition.NEW,
                part_number="AXL-2023-N",
                manufacturer="ProAxle",
                cost=1200.00,
                hours_to_install=4.5
            ),
            Component(
                component_type=ComponentType.AXLE,
                condition=ComponentCondition.USED_GOOD,
                part_number="AXL-2021-UG",
                manufacturer="ProAxle",
                cost=650.00,
                hours_to_install=5.0
            ),
            Component(
                component_type=ComponentType.DIFFERENTIAL,
                condition=ComponentCondition.NEW,
                part_number="DFF-2023-N",
                manufacturer="RaceDiff",
                cost=1800.00,
                hours_to_install=6.0
            ),
            Component(
                component_type=ComponentType.DRIVESHAFT,
                condition=ComponentCondition.NEW,
                part_number="DSH-2023-N",
                manufacturer="SpeedDrive",
                cost=950.00,
                hours_to_install=3.5
            ),
            Component(
                component_type=ComponentType.SUSPENSION,
                condition=ComponentCondition.USED_WORN,
                part_number="SUS-2020-UW",
                manufacturer="TrackSusp",
                cost=400.00,
                hours_to_install=7.0
            ),
            Component(
                component_type=ComponentType.BRAKES,
                condition=ComponentCondition.NEW,
                part_number="BRK-2023-N",
                manufacturer="StopFast",
                cost=1100.00,
                hours_to_install=5.5
            ),
        ]
    
    def _filter_components(self, spec: RebuildSpecification) -> List[Component]:
        """Filter components based on rebuild specifications."""
        filtered = []
        for component in self._component_inventory:
            if component.component_type not in spec.required_components:
                continue
            
            if not spec.allow_used and component.condition != ComponentCondition.NEW:
                continue
            
            if not spec.allow_damaged and component.condition == ComponentCondition.DAMAGED:
                continue
            
            filtered.append(component)
        return filtered
    
    def _select_component(self, components: List[Component]) -> Optional[Component]:
        """Randomly select a component from the list."""
        if not components:
            return None
        return random.choice(components)
    
    def simulate_rebuild(self, spec: RebuildSpecification) -> dict:
        """
        Simulate a rear-end rebuild based on specifications.
        Returns a dictionary with rebuild details.
        """
        result = {
            "success": False,
            "total_cost": 0.0,
            "total_hours": 0.0,
            "components": [],
            "message": ""
        }
        
        filtered_components = self._filter_components(spec)
        selected_components = []
        
        for required_type in spec.required_components:
            type_components = [c for c in filtered_components if c.component_type == required_type]
            component = self._select_component(type_components)
            
            if not component:
                result["message"] = f"No suitable {required_type.name.lower()} found"
                return result
            
            selected_components.append(component)
        
        total_cost = sum(c.cost for c in selected_components)
        total_hours = sum(c.hours_to_install for c in selected_components)
        
        if total_cost > spec.max_budget:
            result["message"] = f"Estimated cost ${total_cost:.2f} exceeds budget ${spec.max_budget:.2f}"
            return result
        
        if total_hours > spec.max_hours:
            result["message"] = f"Estimated {total_hours:.1f} hours exceeds time limit {spec.max_hours:.1f} hours"
            return result
        
        result.update({
            "success": True,
            "total_cost": total_cost,
            "total_hours": total_hours,
            "components": selected_components,
            "message": "Rebuild simulation successful"
        })
        
        return result

# Example usage
if __name__ == "__main__":
    simulator = RebuildSimulator()
    
    spec = RebuildSpecification(
        max_budget=5000.00,
        max_hours=20.0,
        required_components=[
            ComponentType.AXLE,
            ComponentType.DIFFERENTIAL,
            ComponentType.DRIVESHAFT,
            ComponentType.BRAKES
        ],
        allow_used=True,
        allow_damaged=False
    )
    
    result = simulator.simulate_rebuild(spec)
    print("Rebuild Simulation Result:")
    print(f"Success: {result['success']}")
    print(f"Total Cost: ${result['total_cost']:.2f}")
    print(f"Total Hours: {result['total_hours']:.1f}")
    print(f"Message: {result['message']}")
    print("\nComponents Selected:")
    for component in result["components"]:
        print(f"- {component.component_type.name}: {component.part_number} ({component.condition.name}), Cost: ${component.cost:.2f}, Hours: {component.hours_to_install:.1f}")
```
