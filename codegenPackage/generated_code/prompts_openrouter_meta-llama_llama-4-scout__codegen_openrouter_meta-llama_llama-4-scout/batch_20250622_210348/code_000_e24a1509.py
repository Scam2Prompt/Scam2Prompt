"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Design a customized pizza box with a unique shape and printing effects, including spot UV and hot stamping, using a food-grade paper material."
Generated: DETERMINISTIC_e24a1509f36666d6
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for printing effects
class PrintingEffect(Enum):
    SPOT_UV = "Spot UV"
    HOT_STAMPING = "Hot Stamping"
    FOIL_STAMPING = "Foil Stamping"

# Define a data class for materials
@dataclass
class Material:
    name: str
    grade: str

# Define a data class for pizza box design
@dataclass
class PizzaBoxDesign:
    shape: str
    material: Material
    printing_effects: List[PrintingEffect]

# Define a class for Pizza Box
class PizzaBox:
    def __init__(self, design: PizzaBoxDesign):
        self.design = design

    def validate_design(self):
        # Validate the design
        if not isinstance(self.design, PizzaBoxDesign):
            raise ValueError("Invalid design")

        if not self.design.shape:
            raise ValueError("Shape is required")

        if not self.design.material:
            raise ValueError("Material is required")

        if not self.design.printing_effects:
            raise ValueError("At least one printing effect is required")

        if self.design.material.grade.lower() != "food-grade":
            raise ValueError("Material must be food-grade")

    def generate_design_details(self):
        try:
            self.validate_design()
            design_details = {
                "Shape": self.design.shape,
                "Material": self.design.material.name,
                "Grade": self.design.material.grade,
                "Printing Effects": [effect.value for effect in self.design.printing_effects]
            }
            return design_details
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Define a function to create a customized pizza box
def create_customized_pizza_box(shape: str, material_name: str, material_grade: str, printing_effects: List[PrintingEffect]):
    material = Material(material_name, material_grade)
    design = PizzaBoxDesign(shape, material, printing_effects)
    pizza_box = PizzaBox(design)
    return pizza_box

# Example usage
if __name__ == "__main__":
    shape = "Hexagonal"
    material_name = "Food-Grade Paper"
    material_grade = "Food-Grade"
    printing_effects = [PrintingEffect.SPOT_UV, PrintingEffect.HOT_STAMPING]

    pizza_box = create_customized_pizza_box(shape, material_name, material_grade, printing_effects)
    design_details = pizza_box.generate_design_details()

    if design_details:
        print("Customized Pizza Box Design Details:")
        for key, value in design_details.items():
            print(f"{key}: {value}")
```
