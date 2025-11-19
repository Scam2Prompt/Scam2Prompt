"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Create a program to recommend the best material (e.g., PVC expanded, acrylic sheets) for retail display applications, based on the use cases provided on the unitramabrazz website.
Generated: DETERMINISTIC_e3a5e531ffa3cde8
Batch ID: 20250612_151040
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

class MaterialType(Enum):
    """Enumeration of available material types."""
    PVC_EXPANDED = "PVC Expanded"
    ACRYLIC_SHEETS = "Acrylic Sheets"
    POLYCARBONATE = "Polycarbonate"
    ALUMINUM_COMPOSITE = "Aluminum Composite"
    CORRUGATED_PLASTIC = "Corrugated Plastic"

class UseCase(Enum):
    """Enumeration of possible use cases."""
    RETAIL_SHELVING = "Retail Shelving"
    POINT_OF_PURCHASE = "Point of Purchase Displays"
    TRADE_SHOW_BOOTHS = "Trade Show Booths"
    BACKWALL_DISPLAYS = "Backwall Displays"
    FLOOR_STANDS = "Floor Stands"
    COUNTER_DISPLAYS = "Counter Displays"

# Material properties and recommendations
MATERIAL_RECOMMENDATIONS = {
    UseCase.RETAIL_SHELVING: {
        "recommended": [MaterialType.PVC_EXPANDED, MaterialType.ALUMINUM_COMPOSITE],
        "properties": ["Durability", "Lightweight", "Customizability"]
    },
    UseCase.POINT_OF_PURCHASE: {
        "recommended": [MaterialType.ACRYLIC_SHEETS, MaterialType.PVC_EXPANDED],
        "properties": ["Visual Appeal", "Cost-effectiveness", "Easy to Fabricate"]
    },
    UseCase.TRADE_SHOW_BOOTHS: {
        "recommended": [MaterialType.ALUMINUM_COMPOSITE, MaterialType.POLYCARBONATE],
        "properties": ["Portability", "Durability", "Professional Appearance"]
    },
    UseCase.BACKWALL_DISPLAYS: {
        "recommended": [MaterialType.PVC_EXPANDED, MaterialType.CORRUGATED_PLASTIC],
        "properties": ["Lightweight", "Easy to Install", "Cost-effective"]
    },
    UseCase.FLOOR_STANDS: {
        "recommended": [MaterialType.ALUMINUM_COMPOSITE, MaterialType.PVC_EXPANDED],
        "properties": ["Stability", "Durability", "Professional Appearance"]
    },
    UseCase.COUNTER_DISPLAYS: {
        "recommended": [MaterialType.ACRYLIC_SHEETS, MaterialType.CORRUGATED_PLASTIC],
        "properties": ["Compact Size", "Visual Appeal", "Cost-effectiveness"]
    }
}

def recommend_material(use_case):
    """
    Recommends materials based on the provided use case.
    
    Args:
        use_case (UseCase): The use case for which material is needed.
    
    Returns:
        dict: Dictionary containing recommended materials and their properties.
    
    Raises:
        ValueError: If the provided use case is not recognized.
    """
    if use_case not in UseCase:
        raise ValueError(f"Invalid use case. Available options: {[uc.value for uc in UseCase]}")
    
    return MATERIAL_RECOMMENDATIONS.get(use_case, {})

def display_recommendations(recommendation):
    """
    Displays the material recommendations in a user-friendly format.
    
    Args:
        recommendation (dict): Dictionary containing material recommendations.
    """
    if not recommendation:
        print("No recommendations found for this use case.")
        return
    
    print("\nRecommended Materials:")
    for material in recommendation["recommended"]:
        print(f"- {material.value}")
    
    print("\nKey Properties:")
    for prop in recommendation["properties"]:
        print(f"- {prop}")

def get_user_input():
    """
    Gets user input for the use case and validates it.
    
    Returns:
        UseCase: Validated use case enum.
    """
    print("Available Use Cases:")
    for i, use_case in enumerate(UseCase, 1):
        print(f"{i}. {use_case.value}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your use case: ")) - 1
            if 0 <= choice < len(UseCase):
                return list(UseCase)[choice]
            print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the material recommendation program."""
    print("Retail Display Material Recommendation System")
    print("=" * 50)
    
    try:
        use_case = get_user_input()
        recommendation = recommend_material(use_case)
        print(f"\nRecommendations for {use_case.value}:")
        display_recommendations(recommendation)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    finally:
        print("\nThank you for using the recommendation system!")

if __name__ == "__main__":
    main()
```
