"""
Generated Code Metadata:
========================
Original URL: https://lggraphics.com.br
Prompt: Compare and contrast the features of adhesive vinyl and couché paper for printing projects, as discussed on the L&G Graphics blog.
Generated: DETERMINISTIC_72a9a73c63c30b42
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for material types
class MaterialType(str, Enum):
    ADHESIVE_VINYL = "adhesive_vinyl"
    COUCHE_PAPER = "couche_paper"

# Define a data class for material features
@dataclass
class MaterialFeatures:
    durability: str
    finish: str
    thickness: str
    cost: str
    application: str

# Define a class for printing materials
class PrintingMaterial:
    def __init__(self, material_type: MaterialType, features: MaterialFeatures):
        self.material_type = material_type
        self.features = features

    def __str__(self):
        return f"Material Type: {self.material_type.value}\nFeatures:\n{self.features}"

# Define a class for comparing printing materials
class PrintingMaterialComparator:
    def __init__(self):
        self.materials = []

    def add_material(self, material: PrintingMaterial):
        self.materials.append(material)

    def compare_features(self):
        if len(self.materials) < 2:
            raise ValueError("At least two materials are required for comparison")

        # Compare features of materials
        for i in range(len(self.materials)):
            for j in range(i + 1, len(self.materials)):
                material1 = self.materials[i]
                material2 = self.materials[j]

                print(f"Comparing {material1.material_type.value} and {material2.material_type.value}:")
                self._compare_material_features(material1.features, material2.features)
                print()

    @staticmethod
    def _compare_material_features(features1: MaterialFeatures, features2: MaterialFeatures):
        features = ["durability", "finish", "thickness", "cost", "application"]
        for feature in features:
            value1 = getattr(features1, feature)
            value2 = getattr(features2, feature)

            if value1 == value2:
                print(f"{feature.capitalize()}: Both materials have {value1}")
            else:
                print(f"{feature.capitalize()}: {material1.material_type.value} has {value1}, while {material2.material_type.value} has {value2}")

def main():
    try:
        # Define features for adhesive vinyl
        adhesive_vinyl_features = MaterialFeatures(
            durability="High",
            finish="Glossy or Matte",
            thickness="Medium",
            cost="Moderate",
            application="Indoor and Outdoor"
        )

        # Define features for couché paper
        couche_paper_features = MaterialFeatures(
            durability="Medium",
            finish="Glossy or Matte",
            thickness="Thin",
            cost="Low",
            application="Indoor"
        )

        # Create printing materials
        adhesive_vinyl = PrintingMaterial(MaterialType.ADHESIVE_VINYL, adhesive_vinyl_features)
        couche_paper = PrintingMaterial(MaterialType.COUCHE_PAPER, couche_paper_features)

        # Compare printing materials
        comparator = PrintingMaterialComparator()
        comparator.add_material(adhesive_vinyl)
        comparator.add_material(couche_paper)
        comparator.compare_features()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
