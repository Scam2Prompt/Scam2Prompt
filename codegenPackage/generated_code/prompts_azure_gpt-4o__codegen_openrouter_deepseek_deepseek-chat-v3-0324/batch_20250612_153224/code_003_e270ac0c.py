"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Create a script to automate the selection of facade system components, such as "کلپیس ابتدایی استیل 1.2 میلی متر رنگی," based on building dimensions and environmental conditions.
Generated: DETERMINISTIC_e270ac0cc3e407ef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple

class EnvironmentalCondition(Enum):
    """Enum representing different environmental conditions."""
    MILD = "mild"
    MODERATE = "moderate"
    HARSH = "harsh"
    EXTREME = "extreme"

class FacadeComponent:
    """Class representing a facade component with its properties."""
    
    def __init__(
        self,
        name: str,
        material: str,
        thickness_mm: float,
        color: str,
        durability: EnvironmentalCondition,
        cost_per_sqm: float
    ):
        """
        Initialize a facade component.
        
        Args:
            name: Name of the component.
            material: Material of the component.
            thickness_mm: Thickness in millimeters.
            color: Color of the component.
            durability: Environmental condition durability.
            cost_per_sqm: Cost per square meter.
        """
        self.name = name
        self.material = material
        self.thickness_mm = thickness_mm
        self.color = color
        self.durability = durability
        self.cost_per_sqm = cost_per_sqm
    
    def to_dict(self) -> Dict:
        """Convert the component to a dictionary."""
        return {
            "name": self.name,
            "material": self.material,
            "thickness_mm": self.thickness_mm,
            "color": self.color,
            "durability": self.durability.value,
            "cost_per_sqm": self.cost_per_sqm
        }

class FacadeSystemSelector:
    """Class to automate facade system component selection."""
    
    def __init__(self, components_db_path: str = "facade_components.json"):
        """
        Initialize the selector with a components database.
        
        Args:
            components_db_path: Path to the JSON file containing components data.
        """
        self.components_db_path = components_db_path
        self.components = self._load_components()
    
    def _load_components(self) -> List[FacadeComponent]:
        """Load components from the JSON database."""
        try:
            with open(self.components_db_path, "r", encoding="utf-8") as file:
                components_data = json.load(file)
                return [
                    FacadeComponent(
                        name=item["name"],
                        material=item["material"],
                        thickness_mm=item["thickness_mm"],
                        color=item["color"],
                        durability=EnvironmentalCondition(item["durability"]),
                        cost_per_sqm=item["cost_per_sqm"]
                    )
                    for item in components_data
                ]
        except FileNotFoundError:
            raise ValueError(f"Components database file not found: {self.components_db_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in components database: {self.components_db_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in components database: {e}")
    
    def select_components(
        self,
        building_width_m: float,
        building_height_m: float,
        environmental_condition: EnvironmentalCondition,
        max_cost_per_sqm: Optional[float] = None
    ) -> Tuple[List[FacadeComponent], float]:
        """
        Select suitable facade components based on building dimensions and environmental conditions.
        
        Args:
            building_width_m: Building width in meters.
            building_height_m: Building height in meters.
            environmental_condition: Environmental condition of the building location.
            max_cost_per_sqm: Optional maximum cost per square meter constraint.
        
        Returns:
            Tuple of (selected components list, total cost).
        """
        if building_width_m <= 0 or building_height_m <= 0:
            raise ValueError("Building dimensions must be positive numbers.")
        
        surface_area = building_width_m * building_height_m
        
        # Filter components by environmental condition and optional cost constraint
        suitable_components = [
            comp for comp in self.components
            if comp.durability.value >= environmental_condition.value
            and (max_cost_per_sqm is None or comp.cost_per_sqm <= max_cost_per_sqm)
        ]
        
        if not suitable_components:
            raise ValueError("No suitable components found for the given criteria.")
        
        # Sort by cost (ascending) to get the most economical options
        suitable_components.sort(key=lambda x: x.cost_per_sqm)
        
        total_cost = surface_area * suitable_components[0].cost_per_sqm
        
        return suitable_components, total_cost

# Example usage
if __name__ == "__main__":
    try:
        # Initialize selector with components database
        selector = FacadeSystemSelector()
        
        # Example building dimensions and environmental conditions
        building_width = 50.0  # meters
        building_height = 30.0  # meters
        env_condition = EnvironmentalCondition.HARSH
        max_cost = 150.0  # Optional: maximum cost per square meter
        
        # Select components
        components, total_cost = selector.select_components(
            building_width_m=building_width,
            building_height_m=building_height,
            environmental_condition=env_condition,
            max_cost_per_sqm=max_cost
        )
        
        # Print results
        print("Selected Facade Components:")
        for comp in components:
            print(f"- {comp.name}: {comp.material}, {comp.thickness_mm}mm, {comp.color}, "
                  f"Durability: {comp.durability.value}, Cost: {comp.cost_per_sqm}/sqm")
        
        print(f"\nTotal Surface Area: {building_width * building_height} sqm")
        print(f"Total Cost: {total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
