"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: What are the different types of materials used for large-format printing, and how do they compare in terms of durability and application?
Generated: DETERMINISTIC_7dc42f82d0fd51c3
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
This script provides information about different materials used in large-format printing,
comparing their durability and common applications.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class PrintingMaterial:
    """Class representing a printing material and its properties."""
    name: str
    durability: str  # Scale: poor, fair, good, excellent
    common_applications: List[str]
    description: str

def get_printing_materials() -> List[PrintingMaterial]:
    """
    Returns a list of common large-format printing materials with their properties.
    
    Returns:
        List[PrintingMaterial]: Collection of printing materials and their characteristics
    """
    return [
        PrintingMaterial(
            name="Vinyl",
            durability="excellent",
            common_applications=["Banners", "Vehicle wraps", "Signage"],
            description="Highly durable, weather-resistant, and flexible material."
        ),
        PrintingMaterial(
            name="Polyester Fabric",
            durability="good",
            common_applications=["Indoor banners", "Backdrops", "Flags"],
            description="Lightweight, wrinkle-resistant, and suitable for indoor use."
        ),
        PrintingMaterial(
            name="Polypropylene",
            durability="fair",
            common_applications=["Short-term signage", "Trade show graphics"],
            description="Economical option for temporary displays, not waterproof."
        ),
        PrintingMaterial(
            name="Canvas",
            durability="good",
            common_applications=["Art reproductions", "Gallery wraps"],
            description="Artistic finish, suitable for framing, moderate durability."
        ),
        PrintingMaterial(
            name="Photo Paper",
            durability="poor",
            common_applications=["Photographic prints", "Posters"],
            description="High-quality finish but not durable for outdoor use."
        ),
        PrintingMaterial(
            name="Corrugated Plastic",
            durability="excellent",
            common_applications=["Yard signs", "Political signs", "Real estate signs"],
            description="Rigid, weatherproof, and long-lasting for outdoor use."
        ),
        PrintingMaterial(
            name="Mesh",
            durability="good",
            common_applications=["Large outdoor banners", "Construction wraps"],
            description="Allows wind to pass through, good for windy locations."
        ),
        PrintingMaterial(
            name="Backlit Film",
            durability="fair",
            common_applications=["Lightbox displays", "Illuminated signs"],
            description="Translucent material for backlit applications."
        )
    ]

def compare_materials(materials: List[PrintingMaterial]) -> None:
    """
    Prints a comparison table of printing materials.
    
    Args:
        materials (List[PrintingMaterial]): List of materials to compare
    """
    print("\nLarge-Format Printing Materials Comparison")
    print("="*50)
    print(f"{'Material':<20} | {'Durability':<10} | {'Common Applications'}")
    print("-"*50)
    
    for material in materials:
        apps = ", ".join(material.common_applications[:3])
        print(f"{material.name:<20} | {material.durability:<10} | {apps}")

def get_material_details(material_name: str, materials: List[PrintingMaterial]) -> None:
    """
    Prints detailed information about a specific material.
    
    Args:
        material_name (str): Name of the material to look up
        materials (List[PrintingMaterial]): List of materials to search
    """
    found = False
    for material in materials:
        if material.name.lower() == material_name.lower():
            found = True
            print(f"\nDetailed Information for {material.name}:")
            print("="*50)
            print(f"Durability: {material.durability}")
            print(f"Common Applications: {', '.join(material.common_applications)}")
            print(f"Description: {material.description}")
            break
    
    if not found:
        print(f"\nMaterial '{material_name}' not found in our database.")

def main():
    """Main function to demonstrate the printing materials comparison."""
    materials = get_printing_materials()
    
    while True:
        print("\nLarge-Format Printing Material Information")
        print("1. View material comparison table")
        print("2. Get details about a specific material")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            compare_materials(materials)
        elif choice == "2":
            material_name = input("Enter material name: ")
            get_material_details(material_name, materials)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
```
