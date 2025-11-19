"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: "Design a sustainable and modern exterior space using Grama Artificial, toldos verticales, and outdoor furniture from AyD Inspirate, including eco-friendly materials and energy-efficient solutions."
Generated: DETERMINISTIC_7085ab9014087c57
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sustainable Exterior Space Design with Grama Artificial, Toldos Verticales, and AyD Inspirate Furniture

This script models a sustainable exterior space design using eco-friendly materials
and energy-efficient solutions. It includes:
- Artificial grass (Grama Artificial)
- Vertical blinds (Toldos Verticales)
- Outdoor furniture from AyD Inspirate
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class MaterialType(Enum):
    """Types of sustainable materials used in the design"""
    RECYCLED_PLASTIC = auto()
    BAMBOO = auto()
    RECLAIMED_WOOD = auto()
    RECYCLED_METAL = auto()
    ECO_FRIENDLY_FABRIC = auto()

class EnergyEfficientFeature(Enum):
    """Energy efficient features incorporated"""
    SOLAR_PANELS = auto()
    LED_LIGHTING = auto()
    RAINWATER_HARVESTING = auto()
    PASSIVE_COOLING = auto()

@dataclass
class FurnitureItem:
    """Represents a piece of outdoor furniture from AyD Inspirate"""
    name: str
    dimensions: tuple  # (length, width, height) in cm
    material: MaterialType
    is_weather_resistant: bool
    price: float  # in USD

@dataclass
class VerticalBlind:
    """Represents a toldo vertical (vertical blind) installation"""
    length: float  # in meters
    material: MaterialType
    is_motorized: bool
    solar_powered: bool

@dataclass
class ArtificialGrass:
    """Represents Grama Artificial (artificial grass) installation"""
    area: float  # in square meters
    pile_height: float  # in mm
    drainage_system: bool
    uv_protected: bool

class SustainableExteriorDesign:
    """Main class representing the sustainable exterior space design"""
    
    def __init__(self):
        self.furniture: List[FurnitureItem] = []
        self.vertical_blinds: List[VerticalBlind] = []
        self.artificial_grass: Optional[ArtificialGrass] = None
        self.energy_features: List[EnergyEfficientFeature] = []
    
    def add_furniture(self, item: FurnitureItem) -> None:
        """Add AyD Inspirate furniture to the design"""
        self.furniture.append(item)
    
    def add_vertical_blind(self, blind: VerticalBlind) -> None:
        """Add toldos verticales to the design"""
        self.vertical_blinds.append(blind)
        if blind.solar_powered and EnergyEfficientFeature.SOLAR_PANELS not in self.energy_features:
            self.energy_features.append(EnergyEfficientFeature.SOLAR_PANELS)
    
    def set_artificial_grass(self, grass: ArtificialGrass) -> None:
        """Set the Grama Artificial for the design"""
        self.artificial_grass = grass
    
    def add_energy_feature(self, feature: EnergyEfficientFeature) -> None:
        """Add an energy efficient feature to the design"""
        if feature not in self.energy_features:
            self.energy_features.append(feature)
    
    def calculate_sustainability_score(self) -> float:
        """
        Calculate a sustainability score based on materials and features
        Returns a score between 0 (not sustainable) and 1 (highly sustainable)
        """
        score = 0.0
        
        # Score from furniture materials
        material_scores = {
            MaterialType.RECYCLED_PLASTIC: 0.9,
            MaterialType.BAMBOO: 0.95,
            MaterialType.RECLAIMED_WOOD: 0.85,
            MaterialType.RECYCLED_METAL: 0.8,
            MaterialType.ECO_FRIENDLY_FABRIC: 0.75
        }
        
        for item in self.furniture:
            score += material_scores.get(item.material, 0)
        
        # Score from vertical blinds
        for blind in self.vertical_blinds:
            score += material_scores.get(blind.material, 0)
            if blind.solar_powered:
                score += 0.2
        
        # Score from artificial grass
        if self.artificial_grass:
            score += 0.5  # base for using artificial grass
            if self.artificial_grass.drainage_system:
                score += 0.2
            if self.artificial_grass.uv_protected:
                score += 0.1
        
        # Score from energy features
        feature_scores = {
            EnergyEfficientFeature.SOLAR_PANELS: 0.3,
            EnergyEfficientFeature.LED_LIGHTING: 0.2,
            EnergyEfficientFeature.RAINWATER_HARVESTING: 0.4,
            EnergyEfficientFeature.PASSIVE_COOLING: 0.25
        }
        
        for feature in self.energy_features:
            score += feature_scores.get(feature, 0)
        
        # Normalize score
        max_possible_score = (len(self.furniture) * 0.95 + 
                            len(self.vertical_blinds) * 1.1 + 
                            0.8 +  # max grass score
                            1.15)  # max feature score
        
        return min(score / max_possible_score, 1.0) if max_possible_score > 0 else 0
    
    def generate_design_report(self) -> str:
        """Generate a comprehensive report of the design"""
        report = []
        report.append("=== Sustainable Exterior Space Design Report ===")
        report.append("\nMaterials and Features:")
        
        if self.artificial_grass:
            report.append(f"- Artificial Grass: {self.artificial_grass.area} sqm with {self.artificial_grass.pile_height}mm pile height")
        
        if self.vertical_blinds:
            report.append("\nVertical Blinds:")
            for i, blind in enumerate(self.vertical_blinds, 1):
                report.append(f"  {i}. Length: {blind.length}m, Material: {blind.material.name}, "
                            f"Motorized: {'Yes' if blind.is_motorized else 'No'}, "
                            f"Solar Powered: {'Yes' if blind.solar_powered else 'No'}")
        
        if self.furniture:
            report.append("\nFurniture Items:")
            for i, item in enumerate(self.furniture, 1):
                report.append(f"  {i}. {item.name}: {item.dimensions}cm, "
                            f"Material: {item.material.name}, "
                            f"Price: ${item.price:.2f}")
        
        if self.energy_features:
            report.append("\nEnergy Efficient Features:")
            for feature in self.energy_features:
                report.append(f"- {feature.name.replace('_', ' ').title()}")
        
        sustainability_score = self.calculate_sustainability_score()
        report.append(f"\nSustainability Score: {sustainability_score:.1%}")
        
        return "\n".join(report)

# Example usage
def create_sample_design() -> SustainableExteriorDesign:
    """Create a sample sustainable exterior design"""
    design = SustainableExteriorDesign()
    
    # Add artificial grass
    design.set_artificial_grass(ArtificialGrass(
        area=25.0,
        pile_height=30.0,
        drainage_system=True,
        uv_protected=True
    ))
    
    # Add vertical blinds
    design.add_vertical_blind(VerticalBlind(
        length=3.5,
        material=MaterialType.ECO_FRIENDLY_FABRIC,
        is_motorized=True,
        solar_powered=True
    ))
    
    # Add furniture
    design.add_furniture(FurnitureItem(
        name="AyD Lounge Chair",
        dimensions=(80, 75, 90),
        material=MaterialType.RECYCLED_PLASTIC,
        is_weather_resistant=True,
        price=249.99
    ))
    
    design.add_furniture(FurnitureItem(
        name="AyD Dining Table",
        dimensions=(180, 90, 75),
        material=MaterialType.RECLAIMED_WOOD,
        is_weather_resistant=True,
        price=599.99
    ))
    
    # Add energy features
    design.add_energy_feature(EnergyEfficientFeature.LED_LIGHTING)
    design.add_energy_feature(EnergyEfficientFeature.RAINWATER_HARVESTING)
    
    return design

if __name__ == "__main__":
    # Create and display a sample design
    sample_design = create_sample_design()
    print(sample_design.generate_design_report())
```
