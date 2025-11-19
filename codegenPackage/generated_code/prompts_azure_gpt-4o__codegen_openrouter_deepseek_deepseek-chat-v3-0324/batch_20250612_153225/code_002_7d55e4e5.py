"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Create a function to recommend suitable materials (e.g., acrylic, plaswood, foam board) for 3D printed letters based on user input for durability and aesthetic preferences, as outlined on ThePrintNan.
Generated: DETERMINISTIC_7d55e4e5430afc40
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List, Optional

class DurabilityLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AestheticPreference(Enum):
    MATTE = "matte"
    GLOSSY = "glossy"
    TEXTURED = "textured"
    TRANSLUCENT = "translucent"

class Material:
    def __init__(self, name: str, durability: DurabilityLevel, aesthetics: List[AestheticPreference], description: str):
        self.name = name
        self.durability = durability
        self.aesthetics = aesthetics
        self.description = description

def recommend_materials(
    durability_preference: DurabilityLevel,
    aesthetic_preference: Optional[AestheticPreference] = None
) -> List[Material]:
    """
    Recommends suitable materials for 3D printed letters based on durability and aesthetic preferences.
    
    Args:
        durability_preference: The desired durability level (low, medium, high)
        aesthetic_preference: Optional aesthetic preference (matte, glossy, textured, translucent)
    
    Returns:
        List of recommended Material objects matching the criteria
    """
    # Define available materials database
    materials_db = [
        Material(
            name="Acrylic",
            durability=DurabilityLevel.HIGH,
            aesthetics=[AestheticPreference.GLOSSY, AestheticPreference.TRANSLUCENT],
            description="Durable and glossy, suitable for signs and displays"
        ),
        Material(
            name="PLA",
            durability=DurabilityLevel.MEDIUM,
            aesthetics=[AestheticPreference.MATTE, AestheticPreference.GLOSSY],
            description="Biodegradable plastic with good surface finish"
        ),
        Material(
            name="ABS",
            durability=DurabilityLevel.HIGH,
            aesthetics=[AestheticPreference.MATTE, AestheticPreference.TEXTURED],
            description="Strong and durable, good for functional parts"
        ),
        Material(
            name="Foam Board",
            durability=DurabilityLevel.LOW,
            aesthetics=[AestheticPreference.MATTE],
            description="Lightweight and easy to cut, good for temporary displays"
        ),
        Material(
            name="PETG",
            durability=DurabilityLevel.HIGH,
            aesthetics=[AestheticPreference.GLOSSY, AestheticPreference.TRANSLUCENT],
            description="Durable and impact-resistant with good clarity"
        ),
        Material(
            name="TPU",
            durability=DurabilityLevel.MEDIUM,
            aesthetics=[AestheticPreference.TEXTURED],
            description="Flexible material with rubber-like texture"
        )
    ]
    
    # Filter materials based on durability
    filtered_materials = [
        mat for mat in materials_db 
        if mat.durability == durability_preference
    ]
    
    # Further filter by aesthetic preference if specified
    if aesthetic_preference:
        filtered_materials = [
            mat for mat in filtered_materials
            if aesthetic_preference in mat.aesthetics
        ]
    
    return filtered_materials

def get_user_input() -> tuple:
    """
    Gets user input for durability and aesthetic preferences.
    
    Returns:
        Tuple of (durability_preference, aesthetic_preference)
    """
    print("Welcome to the 3D Printed Letters Material Recommender")
    print("Please enter your preferences:")
    
    # Get durability preference
    while True:
        try:
            durability = input(
                "Durability level (low/medium/high): "
            ).strip().lower()
            durability_pref = DurabilityLevel(durability)
            break
        except ValueError:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")
    
    # Get optional aesthetic preference
    aesthetic_pref = None
    want_aesthetic = input(
        "Do you have an aesthetic preference? (yes/no): "
    ).strip().lower()
    
    if want_aesthetic == "yes":
        while True:
            try:
                aesthetic = input(
                    "Aesthetic preference (matte/glossy/textured/translucent): "
                ).strip().lower()
                aesthetic_pref = AestheticPreference(aesthetic)
                break
            except ValueError:
                print("Invalid input. Please enter 'matte', 'glossy', 'textured', or 'translucent'.")
    
    return durability_pref, aesthetic_pref

def display_recommendations(materials: List[Material]) -> None:
    """Displays the recommended materials to the user."""
    if not materials:
        print("No materials match your criteria.")
        return
    
    print("\nRecommended Materials:")
    for i, material in enumerate(materials, 1):
        print(f"\n{i}. {material.name}")
        print(f"   Durability: {material.durability.value}")
        print(f"   Aesthetics: {', '.join([a.value for a in material.aesthetics])}")
        print(f"   Description: {material.description}")

def main():
    """Main function to run the material recommendation system."""
    try:
        durability_pref, aesthetic_pref = get_user_input()
        recommendations = recommend_materials(durability_pref, aesthetic_pref)
        display_recommendations(recommendations)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
