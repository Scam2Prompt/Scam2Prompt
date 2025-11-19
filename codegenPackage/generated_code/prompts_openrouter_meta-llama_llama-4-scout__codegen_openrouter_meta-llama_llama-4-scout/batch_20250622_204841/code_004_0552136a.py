"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: "Suggest a list of eco-friendly materials for manufacturing reusable bags, considering sustainability and recyclability."
Generated: DETERMINISTIC_0552136a78a0e49f
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eco_friendly_materials.py

class EcoFriendlyMaterial:
    """Represents an eco-friendly material for manufacturing reusable bags."""

    def __init__(self, name, sustainability_score, recyclability_score):
        """
        Initializes an EcoFriendlyMaterial instance.

        Args:
            name (str): The name of the material.
            sustainability_score (float): A score indicating the material's sustainability (0-10).
            recyclability_score (float): A score indicating the material's recyclability (0-10).
        """
        self.name = name
        self.sustainability_score = sustainability_score
        self.recyclability_score = recyclability_score

    def __str__(self):
        return f"{self.name} (Sustainability: {self.sustainability_score}, Recyclability: {self.recyclability_score})"


class EcoFriendlyMaterialDatabase:
    """A database of eco-friendly materials for manufacturing reusable bags."""

    def __init__(self):
        self.materials = []

    def add_material(self, material):
        """
        Adds an eco-friendly material to the database.

        Args:
            material (EcoFriendlyMaterial): The material to add.
        """
        self.materials.append(material)

    def get_materials(self):
        """
        Retrieves a list of eco-friendly materials in the database.

        Returns:
            list[EcoFriendlyMaterial]: A list of eco-friendly materials.
        """
        return self.materials

    def suggest_materials(self, min_sustainability_score=5, min_recyclability_score=5):
        """
        Suggests a list of eco-friendly materials based on sustainability and recyclability scores.

        Args:
            min_sustainability_score (float, optional): The minimum sustainability score. Defaults to 5.
            min_recyclability_score (float, optional): The minimum recyclability score. Defaults to 5.

        Returns:
            list[EcoFriendlyMaterial]: A list of suggested eco-friendly materials.
        """
        return [
            material
            for material in self.materials
            if material.sustainability_score >= min_sustainability_score
            and material.recyclability_score >= min_recyclability_score
        ]


def main():
    try:
        # Create an eco-friendly material database
        database = EcoFriendlyMaterialDatabase()

        # Add eco-friendly materials to the database
        database.add_material(EcoFriendlyMaterial("Organic Cotton", 8, 9))
        database.add_material(EcoFriendlyMaterial("Recycled Polyester", 7, 8))
        database.add_material(EcoFriendlyMaterial("Hemp", 9, 9))
        database.add_material(EcoFriendlyMaterial("Jute", 8, 7))
        database.add_material(EcoFriendlyMaterial("Synthetic Blend", 4, 5))

        # Suggest eco-friendly materials
        suggested_materials = database.suggest_materials()

        # Print suggested materials
        print("Suggested Eco-Friendly Materials:")
        for material in suggested_materials:
            print(material)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
