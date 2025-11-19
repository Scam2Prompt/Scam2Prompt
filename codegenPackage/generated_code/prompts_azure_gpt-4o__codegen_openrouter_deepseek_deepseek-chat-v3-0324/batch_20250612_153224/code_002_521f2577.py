"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Create a script to simulate the cost estimation for kanalizacija (drainage system) installation, including jaški (manholes) and greznice (septic tanks).
Generated: DETERMINISTIC_521f2577189656db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


class MaterialType(Enum):
    CONCRETE = auto()
    PLASTIC = auto()
    BRICK = auto()


class ComponentType(Enum):
    MANHOLE = auto()
    SEPTIC_TANK = auto()
    PIPE = auto()


@dataclass
class Component:
    component_type: ComponentType
    material: MaterialType
    dimensions: tuple  # (length, width, depth) in meters
    unit_cost: float  # cost per unit (per m³ for tanks, per m for pipes)
    quantity: int = 1

    def calculate_cost(self) -> float:
        if self.component_type == ComponentType.PIPE:
            # Cost for pipes is per meter
            return self.dimensions[0] * self.unit_cost * self.quantity
        else:
            # Cost for manholes and septic tanks is per volume
            volume = self.dimensions[0] * self.dimensions[1] * self.dimensions[2]
            return volume * self.unit_cost * self.quantity


@dataclass
class DrainageProject:
    components: List[Component]
    labor_cost_per_hour: float = 50.0
    estimated_hours: float = 0.0

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def calculate_total_material_cost(self) -> float:
        return sum(comp.calculate_cost() for comp in self.components)

    def calculate_labor_cost(self) -> float:
        return self.estimated_hours * self.labor_cost_per_hour

    def calculate_total_cost(self) -> float:
        return self.calculate_total_material_cost() + self.calculate_labor_cost()

    def generate_estimate(self) -> dict:
        return {
            "total_material_cost": self.calculate_total_material_cost(),
            "labor_cost": self.calculate_labor_cost(),
            "total_cost": self.calculate_total_cost(),
            "components": [
                {
                    "type": comp.component_type.name,
                    "material": comp.material.name,
                    "dimensions": comp.dimensions,
                    "quantity": comp.quantity,
                    "cost": comp.calculate_cost()
                }
                for comp in self.components
            ]
        }


def main():
    # Example usage
    project = DrainageProject([], estimated_hours=40)

    # Add manholes
    project.add_component(Component(
        component_type=ComponentType.MANHOLE,
        material=MaterialType.CONCRETE,
        dimensions=(1.2, 1.2, 2.0),
        unit_cost=300.0,
        quantity=3
    ))

    # Add septic tank
    project.add_component(Component(
        component_type=ComponentType.SEPTIC_TANK,
        material=MaterialType.PLASTIC,
        dimensions=(2.0, 1.5, 1.8),
        unit_cost=250.0
    ))

    # Add pipes
    project.add_component(Component(
        component_type=ComponentType.PIPE,
        material=MaterialType.PLASTIC,
        dimensions=(50.0, 0.2, 0.2),  # 50m length, 20cm diameter
        unit_cost=15.0
    ))

    # Generate and print estimate
    estimate = project.generate_estimate()
    print("Drainage System Cost Estimate")
    print("=" * 30)
    print(f"Total Material Cost: €{estimate['total_material_cost']:.2f}")
    print(f"Labor Cost: €{estimate['labor_cost']:.2f}")
    print(f"Total Project Cost: €{estimate['total_cost']:.2f}")
    print("\nComponent Breakdown:")
    for comp in estimate["components"]:
        print(f"- {comp['type']} ({comp['material']}): {comp['quantity']} x €{comp['cost']:.2f}")


if __name__ == "__main__":
    main()
```
