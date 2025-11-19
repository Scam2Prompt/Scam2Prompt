"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write Python code to generate a custom design for a laser-engraved professional plaque, incorporating options for materials like PVC, aluminum, and wood, as described on "La Graveuse Normande."
Generated: DETERMINISTIC_aeb2535df3697795
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Optional

class Material(Enum):
    """Available materials for the plaque"""
    PVC = "PVC"
    ALUMINUM = "Aluminum"
    WOOD = "Wood"

class PlaqueDesign:
    """Class representing a custom plaque design"""

    def __init__(self, 
                 text: str, 
                 material: Material, 
                 font_size: int = 24, 
                 font_style: str = "Arial", 
                 plaque_size: tuple = (10, 5)):
        """
        Initialize a PlaqueDesign object.

        Args:
        - text (str): The text to be engraved on the plaque.
        - material (Material): The material of the plaque.
        - font_size (int, optional): The font size of the text. Defaults to 24.
        - font_style (str, optional): The font style of the text. Defaults to "Arial".
        - plaque_size (tuple, optional): The size of the plaque in inches. Defaults to (10, 5).
        """
        self.text = text
        self.material = material
        self.font_size = font_size
        self.font_style = font_style
        self.plaque_size = plaque_size

    def get_material_properties(self) -> dict:
        """Get properties of the selected material"""
        material_properties = {
            Material.PVC: {"color": "White", "thickness": 0.25},
            Material.ALUMINUM: {"color": "Silver", "thickness": 0.125},
            Material.WOOD: {"color": "Brown", "thickness": 0.375}
        }
        return material_properties.get(self.material, {})

    def generate_design(self) -> str:
        """Generate a string representing the plaque design"""
        material_properties = self.get_material_properties()
        design = f"Plaque Design:\n"
        design += f"Material: {self.material.value}\n"
        design += f"Color: {material_properties.get('color', 'Unknown')}\n"
        design += f"Thickness: {material_properties.get('thickness', 0)} inches\n"
        design += f"Text: {self.text}\n"
        design += f"Font Size: {self.font_size}\n"
        design += f"Font Style: {self.font_style}\n"
        design += f"Plaque Size: {self.plaque_size[0]} x {self.plaque_size[1]} inches\n"
        return design

    def __str__(self) -> str:
        return self.generate_design()

def main():
    try:
        text = input("Enter the text for the plaque: ")
        material_choice = input("Enter the material (PVC, Aluminum, Wood): ")
        material = Material(material_choice.upper())
        font_size = int(input("Enter the font size (default=24): ") or 24)
        font_style = input("Enter the font style (default=Arial): ") or "Arial"
        plaque_size = tuple(map(float, input("Enter the plaque size (width height) in inches (default=10 5): ").split())) or (10, 5)

        plaque = PlaqueDesign(text, material, font_size, font_style, plaque_size)
        print(plaque)

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
