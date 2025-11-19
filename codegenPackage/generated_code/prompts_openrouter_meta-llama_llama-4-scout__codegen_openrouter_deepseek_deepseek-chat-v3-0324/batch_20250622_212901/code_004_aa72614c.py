"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Compare the properties and applications of PVC expandido, plastionda, and chapa de acrílico in visual communication products, such as display stands and exhibition materials.
Generated: DETERMINISTIC_aa72614cb321ae26
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of materials (PVC expandido, plastionda, chapa de acrílico) for visual communication products.
"""

from dataclasses import dataclass
from enum import Enum, auto

class MaterialProperty(Enum):
    """Enum representing key material properties."""
    WEIGHT = auto()
    DURABILITY = auto()
    FLEXIBILITY = auto()
    COST = auto()
    PRINTABILITY = auto()
    WEATHER_RESISTANCE = auto()
    FINISH_QUALITY = auto()

class MaterialApplication(Enum):
    """Enum representing common applications."""
    DISPLAY_STANDS = auto()
    EXHIBITION_PANELS = auto()
    SIGNAGE = auto()
    LIGHTBOXES = auto()
    OUTDOOR_DISPLAYS = auto()

@dataclass
class Material:
    """Data class representing a material and its properties."""
    name: str
    properties: dict[MaterialProperty, str]
    applications: list[MaterialApplication]
    advantages: list[str]
    disadvantages: list[str]

def compare_materials(materials: list[Material]) -> None:
    """Compare multiple materials side by side."""
    print("\nMaterial Comparison:")
    print("{:<15} {:<30} {:<30} {:<30}".format("Property", *[m.name for m in materials]))
    
    for prop in MaterialProperty:
        row = [prop.name.replace("_", " ").title()]
        for material in materials:
            row.append(material.properties.get(prop, "N/A"))
        print("{:<15} {:<30} {:<30} {:<30}".format(*row))

def generate_report(materials: list[Material]) -> None:
    """Generate a detailed report comparing materials."""
    print("\nMaterial Comparison Report:")
    for material in materials:
        print(f"\n--- {material.name.upper()} ---")
        print("\nProperties:")
        for prop, desc in material.properties.items():
            print(f"- {prop.name.replace('_', ' ').title()}: {desc}")
        
        print("\nBest Applications:")
        for app in material.applications:
            print(f"- {app.name.replace('_', ' ').title()}")
        
        print("\nAdvantages:")
        for adv in material.advantages:
            print(f"- {adv}")
        
        print("\nDisadvantages:")
        for dis in material.disadvantages:
            print(f"- {dis}")

def main():
    """Main function to demonstrate material comparison."""
    # Define materials with their properties and applications
    pvc_expandido = Material(
        name="PVC Expandido",
        properties={
            MaterialProperty.WEIGHT: "Lightweight",
            MaterialProperty.DURABILITY: "Moderate",
            MaterialProperty.FLEXIBILITY: "Rigid",
            MaterialProperty.COST: "Low",
            MaterialProperty.PRINTABILITY: "Excellent",
            MaterialProperty.WEATHER_RESISTANCE: "Moderate",
            MaterialProperty.FINISH_QUALITY: "Good"
        },
        applications=[
            MaterialApplication.DISPLAY_STANDS,
            MaterialApplication.EXHIBITION_PANELS,
            MaterialApplication.SIGNAGE
        ],
        advantages=[
            "Easy to cut and shape",
            "Accepts various printing methods",
            "Cost-effective for short-term displays"
        ],
        disadvantages=[
            "Not suitable for heavy loads",
            "Can warp in extreme temperatures",
            "Less premium look than acrylic"
        ]
    )

    plastionda = Material(
        name="Plastionda",
        properties={
            MaterialProperty.WEIGHT: "Very lightweight",
            MaterialProperty.DURABILITY: "Low",
            MaterialProperty.FLEXIBILITY: "Flexible",
            MaterialProperty.COST: "Very low",
            MaterialProperty.PRINTABILITY: "Good",
            MaterialProperty.WEATHER_RESISTANCE: "Low",
            MaterialProperty.FINISH_QUALITY: "Basic"
        },
        applications=[
            MaterialApplication.DISPLAY_STANDS,
            MaterialApplication.SIGNAGE
        ],
        advantages=[
            "Extremely lightweight",
            "Very economical",
            "Easy to transport"
        ],
        disadvantages=[
            "Not durable for long-term use",
            "Limited printing options",
            "Appears less professional"
        ]
    )

    acrylic_sheet = Material(
        name="Chapa de Acrílico",
        properties={
            MaterialProperty.WEIGHT: "Heavy",
            MaterialProperty.DURABILITY: "High",
            MaterialProperty.FLEXIBILITY: "Rigid",
            MaterialProperty.COST: "High",
            MaterialProperty.PRINTABILITY: "Good",
            MaterialProperty.WEATHER_RESISTANCE: "High",
            MaterialProperty.FINISH_QUALITY: "Excellent"
        },
        applications=[
            MaterialApplication.DISPLAY_STANDS,
            MaterialApplication.EXHIBITION_PANELS,
            MaterialApplication.LIGHTBOXES,
            MaterialApplication.OUTDOOR_DISPLAYS
        ],
        advantages=[
            "Premium appearance",
            "Highly durable",
            "Excellent weather resistance",
            "Can be polished to high gloss"
        ],
        disadvantages=[
            "Expensive",
            "Heavy and harder to transport",
            "Requires special tools for cutting"
        ]
    )

    materials = [pvc_expandido, plastionda, acrylic_sheet]
    
    # Display comparisons
    compare_materials(materials)
    generate_report(materials)

if __name__ == "__main__":
    main()
```
