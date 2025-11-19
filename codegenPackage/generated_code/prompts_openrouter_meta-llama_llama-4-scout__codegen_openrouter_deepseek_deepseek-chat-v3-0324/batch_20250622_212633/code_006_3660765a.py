"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: "Compare different types of building materials used in Russian construction, such as газобетон (aerated concrete), кирпич (brick), and клееный брус (glued laminated timber), from the perspective of ExpertStroy's material selection."
Generated: DETERMINISTIC_3660765ad383162b
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict

class MaterialType(Enum):
    """Enumeration of building material types"""
    AERATED_CONCRETE = auto()  # газобетон
    BRICK = auto()             # кирпич
    GLUED_LAMINATED_TIMBER = auto()  # клееный брус

@dataclass
class MaterialProperty:
    """Data class representing a material property"""
    name: str
    value: float
    unit: str
    description: str = ""

@dataclass
class BuildingMaterial:
    """Data class representing a building material"""
    name: str
    material_type: MaterialType
    properties: List[MaterialProperty]
    advantages: List[str]
    disadvantages: List[str]
    typical_use_cases: List[str]

class MaterialComparator:
    """Class for comparing different building materials"""
    
    def __init__(self):
        self.materials = self._initialize_materials()
    
    def _initialize_materials(self) -> Dict[MaterialType, BuildingMaterial]:
        """Initialize the database of building materials"""
        return {
            MaterialType.AERATED_CONCRETE: BuildingMaterial(
                name="Газобетон (Aerated Concrete)",
                material_type=MaterialType.AERATED_CONCRETE,
                properties=[
                    MaterialProperty("Density", 500, "kg/m³", "Average density"),
                    MaterialProperty("Thermal Conductivity", 0.12, "W/(m·K)", "Good insulation"),
                    MaterialProperty("Compressive Strength", 3.5, "MPa", "Bearing capacity"),
                ],
                advantages=[
                    "Lightweight",
                    "Good thermal insulation",
                    "Easy to process",
                    "Fire resistant"
                ],
                disadvantages=[
                    "Lower strength compared to concrete",
                    "Requires protective finishing",
                    "Can absorb moisture"
                ],
                typical_use_cases=[
                    "Low-rise residential buildings",
                    "Partition walls",
                    "Thermal insulation layers"
                ]
            ),
            MaterialType.BRICK: BuildingMaterial(
                name="Кирпич (Brick)",
                material_type=MaterialType.BRICK,
                properties=[
                    MaterialProperty("Density", 1800, "kg/m³", "Solid brick"),
                    MaterialProperty("Thermal Conductivity", 0.7, "W/(m·K)", "Medium insulation"),
                    MaterialProperty("Compressive Strength", 10, "MPa", "High bearing capacity"),
                ],
                advantages=[
                    "High durability",
                    "Good load-bearing capacity",
                    "Fire resistant",
                    "Long lifespan"
                ],
                disadvantages=[
                    "Heavy weight",
                    "Poor thermal insulation",
                    "Longer construction time",
                    "Higher cost"
                ],
                typical_use_cases=[
                    "Load-bearing walls",
                    "Foundations",
                    "Fire-resistant structures"
                ]
            ),
            MaterialType.GLUED_LAMINATED_TIMBER: BuildingMaterial(
                name="Клееный брус (Glued Laminated Timber)",
                material_type=MaterialType.GLUED_LAMINATED_TIMBER,
                properties=[
                    MaterialProperty("Density", 480, "kg/m³", "Average for softwood"),
                    MaterialProperty("Thermal Conductivity", 0.13, "W/(m·K)", "Good insulation"),
                    MaterialProperty("Compressive Strength", 30, "MPa", "Along the grain"),
                ],
                advantages=[
                    "High strength-to-weight ratio",
                    "Good thermal insulation",
                    "Aesthetic appearance",
                    "Eco-friendly"
                ],
                disadvantages=[
                    "Vulnerable to moisture",
                    "Requires fire protection",
                    "Higher cost than regular wood"
                ],
                typical_use_cases=[
                    "Residential houses",
                    "Beams and columns",
                    "Decorative elements"
                ]
            )
        }
    
    def compare_materials(self, criteria: str) -> Dict[MaterialType, float]:
        """
        Compare materials based on specific criteria
        Args:
            criteria: The property to compare (must exist in MaterialProperty.name)
        Returns:
            Dictionary mapping material type to property value
        Raises:
            ValueError: If criteria is not found in material properties
        """
        comparison = {}
        valid_criteria = False
        
        for material_type, material in self.materials.items():
            for prop in material.properties:
                if prop.name.lower() == criteria.lower():
                    comparison[material_type] = prop.value
                    valid_criteria = True
                    break
        
        if not valid_criteria:
            raise ValueError(f"Criteria '{criteria}' not found in material properties")
        
        return comparison
    
    def get_material_report(self, material_type: MaterialType) -> str:
        """
        Generate a detailed report for a specific material
        Args:
            material_type: The type of material to report on
        Returns:
            Formatted string with material information
        Raises:
            KeyError: If material type is not found
        """
        if material_type not in self.materials:
            raise KeyError(f"Material type {material_type} not found")
        
        material = self.materials[material_type]
        report = [
            f"Material: {material.name}",
            "\nProperties:",
            *[f"- {prop.name}: {prop.value} {prop.unit} ({prop.description})" 
              for prop in material.properties],
            "\nAdvantages:",
            *[f"- {adv}" for adv in material.advantages],
            "\nDisadvantages:",
            *[f"- {disadv}" for disadv in material.disadvantages],
            "\nTypical Use Cases:",
            *[f"- {use_case}" for use_case in material.typical_use_cases]
        ]
        
        return "\n".join(report)
    
    def recommend_material(self, 
                         priority: str, 
                         budget: str = "medium") -> MaterialType:
        """
        Recommend material based on priority and budget
        Args:
            priority: Main priority ('insulation', 'strength', 'aesthetics')
            budget: Project budget ('low', 'medium', 'high')
        Returns:
            Recommended material type
        Raises:
            ValueError: For invalid priority or budget values
        """
        priority = priority.lower()
        budget = budget.lower()
        
        if priority not in ['insulation', 'strength', 'aesthetics']:
            raise ValueError("Priority must be 'insulation', 'strength', or 'aesthetics'")
        if budget not in ['low', 'medium', 'high']:
            raise ValueError("Budget must be 'low', 'medium', or 'high'")
        
        recommendations = {
            'insulation': {
                'low': MaterialType.AERATED_CONCRETE,
                'medium': MaterialType.AERATED_CONCRETE,
                'high': MaterialType.GLUED_LAMINATED_TIMBER
            },
            'strength': {
                'low': MaterialType.BRICK,
                'medium': MaterialType.BRICK,
                'high': MaterialType.GLUED_LAMINATED_TIMBER
            },
            'aesthetics': {
                'low': MaterialType.AERATED_CONCRETE,
                'medium': MaterialType.GLUED_LAMINATED_TIMBER,
                'high': MaterialType.GLUED_LAMINATED_TIMBER
            }
        }
        
        return recommendations[priority][budget]

# Example usage
if __name__ == "__main__":
    comparator = MaterialComparator()
    
    # Compare thermal conductivity
    try:
        thermal_comparison = comparator.compare_materials("Thermal Conductivity")
        print("Thermal Conductivity Comparison:")
        for material_type, value in thermal_comparison.items():
            print(f"{material_type.name}: {value} W/(m·K)")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get a material report
    try:
        report = comparator.get_material_report(MaterialType.BRICK)
        print("\nBrick Material Report:")
        print(report)
    except KeyError as e:
        print(f"Error: {e}")
    
    # Get a recommendation
    try:
        recommended = comparator.recommend_material("insulation", "medium")
        print(f"\nRecommended material for insulation with medium budget: {recommended.name}")
    except ValueError as e:
        print(f"Error: {e}")
```
