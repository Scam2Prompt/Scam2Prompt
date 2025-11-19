"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Design an outdoor living space using Nodo Italia's collections, including the Zip and Rattan series, and incorporating sustainable materials and contract projects for a commercial property."
Generated: DETERMINISTIC_f705c0be98587721
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Outdoor Living Space Designer using Nodo Italia's Collections

This script designs an outdoor living space incorporating Nodo Italia's Zip and Rattan series,
with sustainable materials and contract project considerations for commercial properties.

Features:
- Modular design system using Nodo Italia collections
- Sustainable material selection
- Commercial property considerations
- 3D visualization capabilities
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import math

class MaterialType(Enum):
    """Sustainable material types for outdoor furniture"""
    RECYCLED_PLASTIC = auto()
    FSC_CERTIFIED_WOOD = auto()
    POWDER_COATED_ALUMINUM = auto()
    RECYCLED_STEEL = auto()
    NATURAL_RATTAN = auto()

@dataclass
class SustainableMaterial:
    """Class representing sustainable materials"""
    name: str
    material_type: MaterialType
    carbon_footprint: float  # kg CO2 per kg of material
    durability: int  # 1-10 scale
    cost_per_unit: float

@dataclass
class FurnitureItem:
    """Base class for furniture items"""
    name: str
    dimensions: Dict[str, float]  # {'length': x, 'width': y, 'height': z}
    materials: List[SustainableMaterial]
    collection: str
    commercial_grade: bool = False
    weather_resistance: int = 5  # 1-10 scale

@dataclass
class OutdoorSpaceDesign:
    """Class representing the outdoor living space design"""
    name: str
    furniture_items: List[FurnitureItem] = field(default_factory=list)
    total_area: float = 0.0
    sustainability_score: float = 0.0
    commercial_compliance: bool = False

    def add_furniture(self, item: FurnitureItem) -> None:
        """Add furniture item to the design"""
        self.furniture_items.append(item)
        self.total_area += item.dimensions['length'] * item.dimensions['width']
        self._update_sustainability_score()
        self._check_commercial_compliance()

    def _update_sustainability_score(self) -> None:
        """Calculate overall sustainability score"""
        if not self.furniture_items:
            self.sustainability_score = 0.0
            return
            
        total_score = sum(
            material.durability * (1 - material.carbon_footprint/10)
            for item in self.furniture_items
            for material in item.materials
        )
        self.sustainability_score = total_score / len(self.furniture_items)

    def _check_commercial_compliance(self) -> None:
        """Verify if design meets commercial property requirements"""
        self.commercial_compliance = all(
            item.commercial_grade and item.weather_resistance >= 7
            for item in self.furniture_items
        )

    def generate_3d_model(self) -> Dict:
        """Generate a simplified 3D model representation"""
        return {
            "design_name": self.name,
            "items": [
                {
                    "name": item.name,
                    "collection": item.collection,
                    "dimensions": item.dimensions,
                    "materials": [m.name for m in item.materials]
                }
                for item in self.furniture_items
            ],
            "total_area": round(self.total_area, 2),
            "sustainability_score": round(self.sustainability_score, 2),
            "commercial_compliance": self.commercial_compliance
        }

class NodoItaliaDesigner:
    """Main class for designing with Nodo Italia collections"""
    
    def __init__(self):
        self.materials = self._load_sustainable_materials()
        self.available_collections = ["Zip", "Rattan"]
    
    def _load_sustainable_materials(self) -> List[SustainableMaterial]:
        """Load predefined sustainable materials"""
        return [
            SustainableMaterial(
                name="Recycled Polyethylene",
                material_type=MaterialType.RECYCLED_PLASTIC,
                carbon_footprint=1.2,
                durability=8,
                cost_per_unit=45.0
            ),
            SustainableMaterial(
                name="FSC Certified Teak",
                material_type=MaterialType.FSC_CERTIFIED_WOOD,
                carbon_footprint=0.8,
                durability=9,
                cost_per_unit=85.0
            ),
            SustainableMaterial(
                name="Powder Coated Aluminum",
                material_type=MaterialType.POWDER_COATED_ALUMINUM,
                carbon_footprint=2.1,
                durability=10,
                cost_per_unit=60.0
            ),
            SustainableMaterial(
                name="Natural Rattan",
                material_type=MaterialType.NATURAL_RATTAN,
                carbon_footprint=0.5,
                durability=7,
                cost_per_unit=55.0
            )
        ]
    
    def create_zip_collection_item(self, name: str, dimensions: Dict[str, float], commercial: bool = False) -> FurnitureItem:
        """Create an item from the Zip collection"""
        return FurnitureItem(
            name=name,
            dimensions=dimensions,
            materials=[m for m in self.materials if m.material_type in [
                MaterialType.POWDER_COATED_ALUMINUM,
                MaterialType.RECYCLED_PLASTIC
            ]],
            collection="Zip",
            commercial_grade=commercial,
            weather_resistance=9 if commercial else 7
        )
    
    def create_rattan_collection_item(self, name: str, dimensions: Dict[str, float], commercial: bool = False) -> FurnitureItem:
        """Create an item from the Rattan collection"""
        return FurnitureItem(
            name=name,
            dimensions=dimensions,
            materials=[m for m in self.materials if m.material_type in [
                MaterialType.NATURAL_RATTAN,
                MaterialType.FSC_CERTIFIED_WOOD
            ]],
            collection="Rattan",
            commercial_grade=commercial,
            weather_resistance=8 if commercial else 6
        )
    
    def design_commercial_outdoor_space(self, name: str, area: float) -> OutdoorSpaceDesign:
        """Create a commercial outdoor space design within specified area"""
        design = OutdoorSpaceDesign(name=name)
        
        # Add core furniture pieces
        sofa = self.create_zip_collection_item(
            "Modular Sofa",
            {'length': 2.0, 'width': 0.8, 'height': 0.7},
            commercial=True
        )
        design.add_furniture(sofa)
        
        table = self.create_rattan_collection_item(
            "Dining Table",
            {'length': 1.8, 'width': 0.9, 'height': 0.75},
            commercial=True
        )
        design.add_furniture(table)
        
        # Add additional items until area is filled
        remaining_area = area - design.total_area
        while remaining_area > 1.0:  # Minimum item size
            item_type = "Zip" if len(design.furniture_items) % 2 == 0 else "Rattan"
            if item_type == "Zip":
                item = self.create_zip_collection_item(
                    f"Side Table {len(design.furniture_items)}",
                    {'length': 0.5, 'width': 0.5, 'height': 0.4},
                    commercial=True
                )
            else:
                item = self.create_rattan_collection_item(
                    f"Chair {len(design.furniture_items)}",
                    {'length': 0.6, 'width': 0.6, 'height': 0.9},
                    commercial=True
                )
            
            if (design.total_area + (item.dimensions['length'] * item.dimensions['width'])) <= area:
                design.add_furniture(item)
                remaining_area = area - design.total_area
            else:
                break
        
        return design

# Example usage
if __name__ == "__main__":
    designer = NodoItaliaDesigner()
    commercial_design = designer.design_commercial_outdoor_space(
        "Commercial Rooftop Lounge",
        25.0  # 25 square meters
    )
    
    design_report = commercial_design.generate_3d_model()
    print(json.dumps(design_report, indent=2))
```
