"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Generate a list of sustainable materials for construction projects with a focus on thermal insulation and aesthetic design."
Generated: DETERMINISTIC_6bae117efb04e418
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sustainable_materials.py
"""
A module for listing sustainable construction materials with thermal insulation properties
and aesthetic design considerations.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SustainableMaterial:
    """Data class representing a sustainable construction material."""
    name: str
    thermal_conductivity: float  # W/m·K (lower is better for insulation)
    embodied_carbon: float  # kgCO2/kg (lower is better)
    aesthetic_qualities: List[str]
    typical_applications: List[str]
    source: Optional[str] = None

def get_sustainable_materials() -> List[SustainableMaterial]:
    """
    Returns a list of sustainable construction materials with thermal insulation properties
    and aesthetic design considerations.
    
    Returns:
        List[SustainableMaterial]: List of sustainable materials
    """
    materials = [
        SustainableMaterial(
            name="Hempcrete",
            thermal_conductivity=0.12,
            embodied_carbon=0.2,
            aesthetic_qualities=["Natural texture", "Breathable surface"],
            typical_applications=["Walls", "Insulation"],
            source="Renewable plant material"
        ),
        SustainableMaterial(
            name="Cork",
            thermal_conductivity=0.04,
            embodied_carbon=0.15,
            aesthetic_qualities=["Warm appearance", "Textured surface"],
            typical_applications=["Flooring", "Wall panels", "Insulation"],
            source="Renewable bark harvesting"
        ),
        SustainableMaterial(
            name="Straw Bale",
            thermal_conductivity=0.05,
            embodied_carbon=0.1,
            aesthetic_qualities=["Rustic appearance", "Thick walls"],
            typical_applications=["Wall systems", "Insulation"],
            source="Agricultural byproduct"
        ),
        SustainableMaterial(
            name="Recycled Denim",
            thermal_conductivity=0.04,
            embodied_carbon=0.3,
            aesthetic_qualities=["Soft appearance", "Color variations"],
            typical_applications=["Wall insulation", "Soundproofing"],
            source="Post-consumer waste"
        ),
        SustainableMaterial(
            name="Mycelium",
            thermal_conductivity=0.08,
            embodied_carbon=0.05,
            aesthetic_qualities=["Organic shapes", "Customizable"],
            typical_applications=["Insulation panels", "Decorative elements"],
            source="Fungal growth"
        ),
        SustainableMaterial(
            name="Sheep's Wool",
            thermal_conductivity=0.04,
            embodied_carbon=0.25,
            aesthetic_qualities=["Natural fiber look", "Soft texture"],
            typical_applications=["Wall insulation", "Acoustic panels"],
            source="Renewable animal product"
        ),
        SustainableMaterial(
            name="Bamboo",
            thermal_conductivity=0.15,
            embodied_carbon=0.3,
            aesthetic_qualities=["Modern appearance", "Grain patterns"],
            typical_applications=["Flooring", "Wall cladding", "Structural elements"],
            source="Fast-growing renewable"
        ),
        SustainableMaterial(
            name="Recycled Glass",
            thermal_conductivity=0.8,
            embodied_carbon=0.4,
            aesthetic_qualities=["Translucent options", "Color variety"],
            typical_applications=["Countertops", "Decorative tiles"],
            source="Post-consumer waste"
        )
    ]
    
    return materials

def filter_materials_by_thermal_performance(
    materials: List[SustainableMaterial], 
    max_conductivity: float = 0.1
) -> List[SustainableMaterial]:
    """
    Filters materials by thermal conductivity threshold.
    
    Args:
        materials: List of materials to filter
        max_conductivity: Maximum thermal conductivity value (W/m·K)
        
    Returns:
        List of materials with thermal conductivity <= max_conductivity
    """
    return [m for m in materials if m.thermal_conductivity <= max_conductivity]

def filter_materials_by_aesthetic(
    materials: List[SustainableMaterial], 
    aesthetic_keywords: List[str]
) -> List[SustainableMaterial]:
    """
    Filters materials containing any of the specified aesthetic keywords.
    
    Args:
        materials: List of materials to filter
        aesthetic_keywords: List of keywords to search for
        
    Returns:
        List of materials matching any aesthetic keyword
    """
    return [
        m for m in materials 
        if any(keyword.lower() in q.lower() 
               for q in m.aesthetic_qualities 
               for keyword in aesthetic_keywords)
    ]

def print_material_details(material: SustainableMaterial):
    """Prints formatted details of a material."""
    print(f"\nMaterial: {material.name}")
    print(f"Thermal Conductivity: {material.thermal_conductivity} W/m·K")
    print(f"Embodied Carbon: {material.embodied_carbon} kgCO2/kg")
    print("Aesthetic Qualities:", ", ".join(material.aesthetic_qualities))
    print("Typical Applications:", ", ".join(material.typical_applications))
    if material.source:
        print(f"Source: {material.source}")

if __name__ == "__main__":
    try:
        materials = get_sustainable_materials()
        
        print("=== All Sustainable Materials ===")
        for material in materials:
            print_material_details(material)
            
        print("\n=== Best Thermal Insulators ===")
        best_insulators = filter_materials_by_thermal_performance(materials)
        for material in best_insulators:
            print_material_details(material)
            
        print("\n=== Materials with Natural Aesthetics ===")
        natural_aesthetics = filter_materials_by_aesthetic(materials, ["natural", "organic"])
        for material in natural_aesthetics:
            print_material_details(material)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
