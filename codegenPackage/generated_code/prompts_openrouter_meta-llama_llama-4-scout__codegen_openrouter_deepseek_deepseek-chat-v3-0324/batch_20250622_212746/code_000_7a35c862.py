"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: What are the different types of electric flat cars offered by EVO视讯, and what are their applications?
Generated: DETERMINISTIC_7a35c862ea7aea66
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EVO视讯 Electric Flat Cars Catalog and Applications

This module provides information about the different types of electric flat cars
offered by EVO视讯 along with their typical applications.
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ElectricFlatCar:
    """Base class representing an electric flat car model."""
    model: str
    description: str
    load_capacity: float  # in tons
    dimensions: Dict[str, float]  # length, width, height in meters
    power_source: str
    applications: List[str]
    
    def get_specifications(self) -> Dict:
        """Returns a dictionary of the car's specifications."""
        return {
            "model": self.model,
            "description": self.description,
            "load_capacity": self.load_capacity,
            "dimensions": self.dimensions,
            "power_source": self.power_source,
            "applications": self.applications
        }

def get_evo_electric_flat_cars() -> List[ElectricFlatCar]:
    """
    Returns a list of electric flat car models offered by EVO视讯
    with their specifications and applications.
    """
    return [
        ElectricFlatCar(
            model="EFC-100",
            description="Compact electric flat car for light-duty transport",
            load_capacity=5.0,
            dimensions={"length": 3.2, "width": 1.5, "height": 0.8},
            power_source="Lithium-ion battery",
            applications=[
                "Warehouse material handling",
                "Small factory transport",
                "Light assembly line operations"
            ]
        ),
        ElectricFlatCar(
            model="EFC-200",
            description="Medium-duty electric flat car with extended range",
            load_capacity=10.0,
            dimensions={"length": 4.5, "width": 1.8, "height": 1.0},
            power_source="Dual lithium-ion battery",
            applications=[
                "Manufacturing plant transport",
                "Construction material handling",
                "Port operations"
            ]
        ),
        ElectricFlatCar(
            model="EFC-300",
            description="Heavy-duty electric flat car for industrial use",
            load_capacity=20.0,
            dimensions={"length": 6.0, "width": 2.2, "height": 1.2},
            power_source="High-capacity lithium battery",
            applications=[
                "Steel plant operations",
                "Mining transport",
                "Heavy machinery movement"
            ]
        ),
        ElectricFlatCar(
            model="EFC-400X",
            description="Specialized electric flat car with extra features",
            load_capacity=15.0,
            dimensions={"length": 5.5, "width": 2.0, "height": 1.1},
            power_source="Fast-charging battery system",
            applications=[
                "Automotive assembly lines",
                "Aerospace component transport",
                "Precision equipment handling"
            ]
        )
    ]

def display_catalog() -> None:
    """Displays the EVO视讯 electric flat car catalog in a formatted way."""
    cars = get_evo_electric_flat_cars()
    
    print("EVO视讯 Electric Flat Cars Catalog")
    print("=" * 40)
    
    for car in cars:
        print(f"\nModel: {car.model}")
        print(f"Description: {car.description}")
        print(f"Load Capacity: {car.load_capacity} tons")
        print(f"Dimensions (LxWxH): {car.dimensions['length']}m x {car.dimensions['width']}m x {car.dimensions['height']}m")
        print(f"Power Source: {car.power_source}")
        print("Applications:")
        for app in car.applications:
            print(f" - {app}")
        print("-" * 40)

if __name__ == "__main__":
    display_catalog()
```
