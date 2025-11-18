"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write Python code to generate a custom design for a laser-engraved professional plaque, incorporating options for materials like PVC, aluminum, and wood, as described on "La Graveuse Normande."
Generated: DETERMINISTIC_aeb2535df3697795
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def select_material():
    """
    Prompts the user to select a material for the plaque.
    Available materials: PVC, aluminum, wood.
    
    Returns:
        str: Chosen material.
    """
    materials = ["PVC", "aluminum", "wood"]
    print("Available materials:")
    for idx, material in enumerate(materials, start=1):
        print(f"{idx}. {material}")
    
    try:
        choice = int(input("Enter the number corresponding to your material choice: "))
        if choice < 1 or choice > len(materials):
            raise ValueError("Invalid selection. Please choose a valid option.")
        return materials[choice - 1]
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def get_plaque_details():
    """
    Prompts the user for custom details for the plaque design.
    
    Returns:
        dict: A dictionary containing plaque details like dimensions and text.
    """
    try:
        width = float(input("Enter the width of the plaque in cm: "))
        height = float(input("Enter the height of the plaque in cm: "))
        text = input("Enter the text to be engraved on the plaque: ")
        
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        
        return {"width": width, "height": height, "text": text}
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def design_plaque():
    """
    Combines user inputs for material and design details to create a plaque design.

    Returns:
        dict: Complete plaque design.
    """
    print("Welcome to La Graveuse Normande's plaque design tool!")
    material = select_material()
    details = get_plaque_details()
    
    plaque_design = {
        "material": material,
        "dimensions": {
            "width": details["width"],
            "height": details["height"]
        },
        "engraved_text": details["text"]
    }
    
    return plaque_design


def main():
    """
    Main function to execute the plaque design process.
    """
    try:
        plaque = design_plaque()
        print("\nCustom plaque design created successfully!")
        print("Design Details:")
        print(f"Material: {plaque['material']}")
        print(f"Dimensions: {plaque['dimensions']['width']} cm x {plaque['dimensions']['height']} cm")
        print(f"Engraved Text: {plaque['engraved_text']}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
