"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Illustrate how to use Fortic's technical services in a project management tool, including steps for calculating structures and logistics for material delivery.
Generated: DETERMINISTIC_3724f69c1f7d8b0e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Fortic's Technical Services

This module integrates Fortic's technical services into a project management tool,
including structural calculations and logistics for material delivery.
"""

import math
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto


class MaterialType(Enum):
    """Enumeration of material types for structural components."""
    STEEL = auto()
    CONCRETE = auto()
    WOOD = auto()
    COMPOSITE = auto()


@dataclass
class Material:
    """Data class representing a construction material."""
    type: MaterialType
    density: float  # kg/m³
    strength: float  # MPa
    cost_per_unit: float  # USD per unit
    unit: str = "kg"  # Default unit


@dataclass
class StructuralComponent:
    """Data class representing a structural component."""
    name: str
    material: Material
    quantity: int
    dimensions: Dict[str, float]  # e.g., {'length': 5.0, 'width': 0.5, 'height': 0.3}


@dataclass
class DeliveryVehicle:
    """Data class representing a delivery vehicle."""
    name: str
    capacity: float  # kg
    cost_per_km: float  # USD per kilometer
    max_speed: float  # km/h


class ProjectManager:
    """Main class for managing projects using Fortic's technical services."""

    def __init__(self):
        self.components: List[StructuralComponent] = []
        self.vehicles: List[DeliveryVehicle] = []

    def add_component(self, component: StructuralComponent) -> None:
        """Add a structural component to the project."""
        self.components.append(component)

    def add_vehicle(self, vehicle: DeliveryVehicle) -> None:
        """Add a delivery vehicle to the project."""
        self.vehicles.append(vehicle)

    def calculate_total_weight(self) -> float:
        """Calculate the total weight of all structural components."""
        total_weight = 0.0
        for component in self.components:
            volume = 1.0
            for dim in component.dimensions.values():
                volume *= dim
            weight = volume * component.material.density * component.quantity
            total_weight += weight
        return total_weight

    def calculate_total_cost(self) -> float:
        """Calculate the total material cost of all components."""
        return sum(
            component.quantity * component.material.cost_per_unit
            for component in self.components
        )

    def estimate_delivery(
        self,
        distance: float,
        vehicle_name: Optional[str] = None
    ) -> Dict[str, float]:
        """
        Estimate delivery logistics for material transport.
        
        Args:
            distance: Distance to construction site in km.
            vehicle_name: Optional specific vehicle to use.
        
        Returns:
            Dictionary containing:
            - 'vehicle': Vehicle name
            - 'trips': Number of trips needed
            - 'cost': Total delivery cost
            - 'time': Total delivery time in hours
        """
        total_weight = self.calculate_total_weight()
        
        if vehicle_name:
            vehicle = next(v for v in self.vehicles if v.name == vehicle_name)
        else:
            # Select vehicle with sufficient capacity or smallest possible
            suitable_vehicles = [v for v in self.vehicles if v.capacity >= total_weight]
            if suitable_vehicles:
                vehicle = min(suitable_vehicles, key=lambda v: v.cost_per_km)
            else:
                vehicle = max(self.vehicles, key=lambda v: v.capacity)

        trips = math.ceil(total_weight / vehicle.capacity)
        cost = trips * distance * vehicle.cost_per_km * 2  # Round trip
        time = (distance * 2 * trips) / vehicle.max_speed  # Total hours

        return {
            'vehicle': vehicle.name,
            'trips': trips,
            'cost': cost,
            'time': time
        }

    def generate_report(self) -> str:
        """Generate a comprehensive project report."""
        total_weight = self.calculate_total_weight()
        total_cost = self.calculate_total_cost()
        
        report = [
            "Fortic Technical Services Project Report",
            "=======================================",
            f"Total Components: {len(self.components)}",
            f"Total Weight: {total_weight:.2f} kg",
            f"Total Material Cost: ${total_cost:.2f}",
            "\nComponents:"
        ]
        
        for component in self.components:
            report.append(
                f"- {component.name}: {component.quantity}x {component.material.type.name}, "
                f"Dimensions: {component.dimensions}"
            )
        
        report.append("\nAvailable Delivery Vehicles:")
        for vehicle in self.vehicles:
            report.append(
                f"- {vehicle.name}: Capacity {vehicle.capacity} kg, "
                f"Cost ${vehicle.cost_per_km}/km, Max Speed {vehicle.max_speed} km/h"
            )
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Initialize project manager
    pm = ProjectManager()

    # Define materials
    steel = Material(
        type=MaterialType.STEEL,
        density=7850,
        strength=400,
        cost_per_unit=0.8
    )
    concrete = Material(
        type=MaterialType.CONCRETE,
        density=2400,
        strength=30,
        cost_per_unit=0.1
    )

    # Add structural components
    pm.add_component(StructuralComponent(
        name="Main Beam",
        material=steel,
        quantity=4,
        dimensions={'length': 6.0, 'width': 0.3, 'height': 0.4}
    ))
    pm.add_component(StructuralComponent(
        name="Foundation Slab",
        material=concrete,
        quantity=1,
        dimensions={'length': 10.0, 'width': 10.0, 'height': 0.5}
    ))

    # Add delivery vehicles
    pm.add_vehicle(DeliveryVehicle(
        name="Small Truck",
        capacity=5000,
        cost_per_km=1.5,
        max_speed=80
    ))
    pm.add_vehicle(DeliveryVehicle(
        name="Large Truck",
        capacity=20000,
        cost_per_km=2.5,
        max_speed=70
    ))

    # Generate report
    print(pm.generate_report())

    # Calculate delivery estimate
    distance = 50  # km
    delivery = pm.estimate_delivery(distance)
    print("\nDelivery Estimate:")
    print(f"Vehicle: {delivery['vehicle']}")
    print(f"Trips: {delivery['trips']}")
    print(f"Cost: ${delivery['cost']:.2f}")
    print(f"Time: {delivery['time']:.2f} hours")
```
