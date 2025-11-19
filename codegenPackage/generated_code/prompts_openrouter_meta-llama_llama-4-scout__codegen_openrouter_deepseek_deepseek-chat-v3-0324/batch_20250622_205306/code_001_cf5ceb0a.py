"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: "What are the different types of industrial belts used in food processing, as offered by KOVE INDUSTRIAL S.A.C.?"
Generated: DETERMINISTIC_cf5ceb0a7170f48b
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from enum import Enum
from typing import List, Dict

class BeltType(Enum):
    """
    Enum representing different types of industrial belts used in food processing.
    These are the types offered by KOVE INDUSTRIAL S.A.C.
    """
    MODULAR_PLASTIC = "Modular Plastic Belts"
    CONVEYOR = "Conveyor Belts"
    TIMING = "Timing Belts"
    FLAT = "Flat Belts"
    V_BELTS = "V-Belts"
    ROUND = "Round Belts"
    FOOD_GRADE = "Food Grade Belts"
    STAINLESS_STEEL = "Stainless Steel Belts"
    PU = "Polyurethane Belts"
    PVC = "PVC Belts"

class BeltMaterial(Enum):
    """
    Enum representing materials used in food processing belts.
    """
    PLASTIC = "Plastic"
    RUBBER = "Rubber"
    STAINLESS_STEEL = "Stainless Steel"
    POLYURETHANE = "Polyurethane"
    PVC = "PVC"

class BeltFeature(Enum):
    """
    Enum representing special features of food processing belts.
    """
    HEAT_RESISTANT = "Heat Resistant"
    OIL_RESISTANT = "Oil Resistant"
    CHEMICAL_RESISTANT = "Chemical Resistant"
    ANTISTATIC = "Antistatic"
    ANTIMICROBIAL = "Antimicrobial"
    FDA_APPROVED = "FDA Approved"
    EASY_CLEAN = "Easy to Clean"

class FoodProcessingBelt:
    """
    Class representing a food processing belt with its properties.
    """
    def __init__(
        self,
        belt_type: BeltType,
        material: BeltMaterial,
        features: List[BeltFeature],
        description: str = "",
        temperature_range: str = "",
        width_options: List[str] = None,
        length_options: List[str] = None
    ):
        self.belt_type = belt_type
        self.material = material
        self.features = features
        self.description = description
        self.temperature_range = temperature_range
        self.width_options = width_options if width_options else []
        self.length_options = length_options if length_options else []

    def __str__(self) -> str:
        return f"{self.belt_type.value} ({self.material.value})"

def get_kove_industrial_belts() -> List[FoodProcessingBelt]:
    """
    Returns a list of food processing belts offered by KOVE INDUSTRIAL S.A.C.
    """
    return [
        FoodProcessingBelt(
            belt_type=BeltType.MODULAR_PLASTIC,
            material=BeltMaterial.PLASTIC,
            features=[BeltFeature.FDA_APPROVED, BeltFeature.ANTIMICROBIAL, BeltFeature.EASY_CLEAN],
            description="Hygienic modular belts for food processing",
            temperature_range="-10°C to 80°C",
            width_options=["100mm", "200mm", "300mm"],
            length_options=["1m", "2m", "3m"]
        ),
        FoodProcessingBelt(
            belt_type=BeltType.FOOD_GRADE,
            material=BeltMaterial.POLYURETHANE,
            features=[BeltFeature.FDA_APPROVED, BeltFeature.CHEMICAL_RESISTANT],
            description="General purpose food grade belts",
            temperature_range="-20°C to 90°C"
        ),
        FoodProcessingBelt(
            belt_type=BeltType.STAINLESS_STEEL,
            material=BeltMaterial.STAINLESS_STEEL,
            features=[BeltFeature.HEAT_RESISTANT, BeltFeature.CHEMICAL_RESISTANT],
            description="High temperature stainless steel belts",
            temperature_range="-50°C to 500°C"
        ),
        FoodProcessingBelt(
            belt_type=BeltType.PU,
            material=BeltMaterial.POLYURETHANE,
            features=[BeltFeature.OIL_RESISTANT, BeltFeature.ANTISTATIC],
            description="Polyurethane belts for oily food processing",
            temperature_range="-30°C to 100°C"
        ),
        FoodProcessingBelt(
            belt_type=BeltType.PVC,
            material=BeltMaterial.PVC,
            features=[BeltFeature.FDA_APPROVED, BeltFeature.EASY_CLEAN],
            description="PVC belts for general food handling",
            temperature_range="-10°C to 70°C"
        )
    ]

def display_belt_types() -> None:
    """
    Displays all available belt types from KOVE INDUSTRIAL S.A.C.
    """
    belts = get_kove_industrial_belts()
    print("Food Processing Belts Offered by KOVE INDUSTRIAL S.A.C.:")
    print("--------------------------------------------------------")
    for belt in belts:
        print(f"- {belt}")
        print(f"  Features: {', '.join([f.value for f in belt.features])}")
        if belt.description:
            print(f"  Description: {belt.description}")
        if belt.temperature_range:
            print(f"  Temperature Range: {belt.temperature_range}")
        if belt.width_options:
            print(f"  Available Widths: {', '.join(belt.width_options)}")
        if belt.length_options:
            print(f"  Available Lengths: {', '.join(belt.length_options)}")
        print()

if __name__ == "__main__":
    display_belt_types()
```
