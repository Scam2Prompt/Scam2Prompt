"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Write code to simulate the hybrid design of the Settled Collection fireplaces, combining furniture and fireplace elements in a single piece.
Generated: DETERMINISTIC_0c73fef2b40cd0a4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of the Settled Collection fireplaces hybrid design combining furniture and fireplace elements.
This code models the design, materials, and functionality of the hybrid piece.
"""

from enum import Enum
from typing import List, Optional, Dict

class MaterialType(Enum):
    """Enumeration of possible materials used in the hybrid design."""
    WOOD = "Wood"
    METAL = "Metal"
    GLASS = "Glass"
    STONE = "Stone"
    CERAMIC = "Ceramic"

class FireplaceType(Enum):
    """Types of fireplace mechanisms."""
    ELECTRIC = "Electric"
    ETHANOL = "Ethanol"
    GAS = "Gas"
    WOOD_BURNING = "Wood Burning"

class FurnitureComponent:
    """Base class for furniture components in the hybrid design."""
    def __init__(self, name: str, material: MaterialType, dimensions: Dict[str, float]):
        """
        Initialize a furniture component.
        
        Args:
            name: Name of the component
            material: Material used
            dimensions: Dictionary with 'length', 'width', 'height' keys in meters
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def get_volume(self) -> float:
        """Calculate volume of the component in cubic meters."""
        return self.dimensions['length'] * self.dimensions['width'] * self.dimensions['height']

class FireplaceComponent:
    """Base class for fireplace components in the hybrid design."""
    def __init__(self, fireplace_type: FireplaceType, heat_output: float, fuel_source: str):
        """
        Initialize a fireplace component.
        
        Args:
            fireplace_type: Type of fireplace
            heat_output: Heat output in BTUs
            fuel_source: Description of fuel source
        """
        self.fireplace_type = fireplace_type
        self.heat_output = heat_output
        self.fuel_source = fuel_source
        self.is_on = False

    def toggle_power(self) -> None:
        """Toggle the fireplace power state."""
        self.is_on = not self.is_on

class SettledCollectionHybrid:
    """Main class representing the hybrid furniture-fireplace design."""
    def __init__(self, name: str, furniture_components: List[FurnitureComponent], fireplace: FireplaceComponent):
        """
        Initialize the hybrid design.
        
        Args:
            name: Name of the hybrid piece
            furniture_components: List of furniture components
            fireplace: Fireplace component
        """
        self.name = name
        self.furniture_components = furniture_components
        self.fireplace = fireplace
        self._validate_design()

    def _validate_design(self) -> None:
        """Validate that the design meets safety and aesthetic requirements."""
        if not self.furniture_components:
            raise ValueError("At least one furniture component is required")
        
        # Safety check for fireplace proximity to flammable materials
        if self.fireplace.fireplace_type != FireplaceType.ELECTRIC:
            for component in self.furniture_components:
                if component.material == MaterialType.WOOD and component.dimensions['height'] < 1.0:
                    raise ValueError("Wood components must be at least 1m tall near non-electric fireplaces")

    def get_total_volume(self) -> float:
        """Calculate total volume of all furniture components."""
        return sum(comp.get_volume() for comp in self.furniture_components)

    def get_materials_used(self) -> List[MaterialType]:
        """Get list of unique materials used in the design."""
        materials = set(comp.material for comp in self.furniture_components)
        return list(materials)

    def activate_fireplace(self) -> str:
        """Activate the fireplace with safety checks."""
        if self.fireplace.is_on:
            return "Fireplace is already on"
        
        self.fireplace.toggle_power()
        return f"Fireplace activated. Heat output: {self.fireplace.heat_output} BTUs"

    def deactivate_fireplace(self) -> str:
        """Deactivate the fireplace."""
        if not self.fireplace.is_on:
            return "Fireplace is already off"
        
        self.fireplace.toggle_power()
        return "Fireplace deactivated"

# Example usage
if __name__ == "__main__":
    # Create furniture components
    cabinet = FurnitureComponent(
        name="Storage Cabinet",
        material=MaterialType.WOOD,
        dimensions={'length': 1.2, 'width': 0.6, 'height': 1.8}
    )
    
    shelf = FurnitureComponent(
        name="Display Shelf",
        material=MaterialType.METAL,
        dimensions={'length': 1.5, 'width': 0.3, 'height': 0.5}
    )
    
    # Create fireplace component
    fireplace = FireplaceComponent(
        fireplace_type=FireplaceType.ELECTRIC,
        heat_output=5000,
        fuel_source="Electricity"
    )
    
    # Create hybrid design
    hybrid_design = SettledCollectionHybrid(
        name="Modern Lounge Hybrid",
        furniture_components=[cabinet, shelf],
        fireplace=fireplace
    )
    
    # Demonstrate functionality
    print(f"Design Name: {hybrid_design.name}")
    print(f"Total Volume: {hybrid_design.get_total_volume():.2f} m³")
    print(f"Materials Used: {[mat.value for mat in hybrid_design.get_materials_used()]}")
    print(hybrid_design.activate_fireplace())
    print(hybrid_design.deactivate_fireplace())
```
